import pyaudio
import wave
import os  # 新增os模块导入
from vosk import Model, KaldiRecognizer
import time
import numpy as np
import collections
import threading
from threading import Lock

class STT:
    def __init__(self, 
                 device_index=1, 
                 rate=44100, 
                 chunk=1024,
                 threshold=100,  # 初始音量检测阈值
                 noise_buffer_size=50, 
                 threshold_multiplier=1.2,  # 动态阈值=环境噪声均值*该系数
                 min_voice_duration=0.1,  # 有效语音最小持续时长（秒）
                 model_path="C:/vosk-models/vosk-model-small-en-us-0.15",  # Windows路径格式
                 output_file="translate.wav"):
        """
        STT 语音识别库初始化
        
        :param device_index: 音频设备索引
        :param rate: 采样率
        :param chunk: 音频块大小
        :param threshold: 音量检测阈值
        :param model_path: Vosk模型路径（Windows建议使用绝对路径）
        :param output_file: 录音保存文件名
        """
        self.pa = pyaudio.PyAudio()
        self.stream = None
        self.is_recording = False  # 录音状态（用户主动触发）
        self.is_listening = False  # 监听状态（后台线程）
        
        # 配置参数
        self.device_index = device_index
        self.rate = rate
        self.chunk = chunk
        self.threshold = threshold
        self.model_path = model_path
        self.output_file = output_file
        
        # 状态变量（线程安全）
        self.voice_detected = False  # 当前是否检测到声音（供主程序轮询）
        self.frames = []
        self.silent_chunks = 0
        self.pre_record_buffer = collections.deque(maxlen=int(rate / chunk * 2))  # 2秒预录缓冲
        self.model = Model(model_path)  # 加载模型
        
        # 静音检测参数
        # 增大静音超时时间（原2秒，可改为3秒）
        self.silence_timeout = 3  # 秒
        # 或增大 max_silent_chunks（根据采样率和chunk计算）
        self.max_silent_chunks = int(self.silence_timeout * self.rate / self.chunk)
        
        # 线程与锁
        self.listen_thread = None
        self.record_thread = None
        self.lock = Lock()

        # 新增动态阈值相关参数
        self.noise_buffer_size = noise_buffer_size
        self.threshold_multiplier = threshold_multiplier
        self.min_voice_duration = min_voice_duration
        self.min_voice_chunks = int(min_voice_duration * rate / chunk)  # 转换为音频块数量
        
        # 环境噪声统计缓冲区（保存最近N个音频块的音量）
        self.noise_volume_buffer = collections.deque(maxlen=noise_buffer_size)
        self.current_noise_avg = 0  # 当前环境噪声均值（动态更新）
        
        # 新增：连续超过阈值的音频块计数器
        self.consecutive_above_threshold = 0


    def start(self):
        """启动后台监听（不阻塞主程序）"""
        if self.is_listening:
            print("已在监听中...")
            return
        
        # 打开音频流
        self.stream = self.pa.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=self.rate,
            input=True,
            input_device_index=self.device_index,
            frames_per_buffer=self.chunk
        )
        self.is_listening = True
        
        # 启动后台监听线程（非阻塞）
        self.listen_thread = threading.Thread(target=self._listen_loop)
        self.listen_thread.start()
        print("开始后台监听...")

    def _listen_loop(self):
        """后台监听循环（持续检测声音，更新voice_detected状态）"""
        while self.is_listening:
            try:
                data = self.stream.read(self.chunk, exception_on_overflow=False)
                with self.lock:
                    self.pre_record_buffer.append(data)
                
                # 1. 计算当前音频块的音量
                current_volume = self._get_volume(data)
                
                # 2. 更新环境噪声缓冲区（仅统计非语音状态下的音量）
                # 3. 动态计算阈值（环境噪声均值*系数，最低不低于初始阈值）
                dynamic_threshold = max(self.threshold, self.current_noise_avg * self.threshold_multiplier)
                
                # 打印调试信息：当前音量、动态阈值、voice_detected状态
                # print(f"[调试] 当前音量: {current_volume}, 动态阈值: {dynamic_threshold}, voice_detected: {self.voice_detected}")
                
                # 仅当未检测到语音时更新环境噪声（避免语音期间调整阈值）
                if not self.voice_detected:
                    self.noise_volume_buffer.append(current_volume)
                    self.current_noise_avg = np.mean(self.noise_volume_buffer) if self.noise_volume_buffer else 0
                    # print(f"[调试] 环境噪声均值更新为: {self.current_noise_avg}")
                
                # 3. 动态计算阈值（环境噪声均值*系数，最低不低于初始阈值）
                dynamic_threshold = max(self.threshold, self.current_noise_avg * self.threshold_multiplier)
                
                # 4. 判断是否连续超过阈值（持续时长）
                if current_volume > dynamic_threshold:
                    self.consecutive_above_threshold += 1
                    # 达到最小持续时长时，标记为检测到语音
                    if self.consecutive_above_threshold >= self.min_voice_chunks:
                        self.voice_detected = True
                else:
                    self.consecutive_above_threshold = 0  # 重置计数器
                    self.voice_detected = False  # 未持续超过阈值，取消语音标记
            except Exception as e:
                print(f"监听异常: {str(e)}")
                break

    def is_voice_detected(self):
        """主程序轮询：当前是否检测到声音"""
        with self.lock:
            return self.voice_detected

    def start_recording(self):
        """主程序手动触发：开始录音（阻塞运行，直到检测到静音停止）"""
        if self.is_recording:
            print("已在录音中...")
            return
        
        self.is_recording = True
        print("开始录音...")
        self._record_loop()  # 直接调用循环（阻塞运行）

    def _record_loop(self):
        """内部录音循环（带静音检测，阻塞运行）"""
        self.silent_chunks = 0
        # 清空旧数据，加入预录缓冲
        self.frames = list(self.pre_record_buffer)
        
        while self.is_recording:
            try:
                data = self.stream.read(self.chunk, exception_on_overflow=False)
                self.frames.append(data)
                
                # 检测静音
                if not self.is_hearing_voice(data):
                    self.silent_chunks += 1
                    if self.silent_chunks >= self.max_silent_chunks:
                        print("检测到静音，停止录音...")
                        self.stop_recording()
                        break
                else:
                    self.silent_chunks = 0  # 重置静音计数器
            except Exception as e:
                print(f"录音异常: {str(e)}")
                self.stop_recording()
                break

    def is_hearing_voice(self, data):
        """检测当前音频数据是否为语音（计算音量与阈值比较）"""
        current_volume = self._get_volume(data)
        dynamic_threshold = max(self.threshold, self.current_noise_avg * self.threshold_multiplier)
        return current_volume > dynamic_threshold

    def stop_recording(self):
        """停止录音并保存文件"""
        if not self.is_recording:
            return
        
        self.is_recording = False
        with self.lock:
            # 保存录音文件
            with wave.open(self.output_file, "wb") as wf:
                wf.setnchannels(1)
                wf.setsampwidth(self.pa.get_sample_size(pyaudio.paInt16))
                wf.setframerate(self.rate)
                wf.writeframes(b"".join(self.frames))
            
            # # 播放录音（需安装sounddevice: pip install sounddevice）
            # import sounddevice as sd
            # from scipy.io import wavfile
            # sample_rate, data = wavfile.read(self.output_file)
            # sd.play(data, sample_rate)
            # sd.wait()  # 等待播放完成
            
            # 重置状态
            # self.frames = []
            # self.pre_record_buffer.clear()
            # print(f"录音已保存至 {self.output_file}，已播放验证")

    def _get_volume(self, audio_chunk):
        """计算音频块的音量（内部方法）"""
        try:
            audio_data = np.frombuffer(audio_chunk, dtype=np.int16)
            return np.abs(audio_data).max()
        except ValueError:
            return 0

    def transcribe(self):
        """将已保存的录音文件转换为纯文本"""
        try:
            wf = self._open_audio_file()
            recognizer = KaldiRecognizer(self.model, wf.getframerate())
            return self._process_audio_data(wf, recognizer)
        except Exception as e:
            return self._handle_recognition_error(e)

    def _open_audio_file(self):
        """打开并验证音频文件"""
        if not os.path.exists(self.output_file):
            raise FileNotFoundError(f"未找到录音文件 {self.output_file}")
        return wave.open(self.output_file, "rb")

    def _process_audio_data(self, wf, recognizer):
        """处理音频数据识别循环"""
        text_chunks = []
        while True:
            data = wf.readframes(4000)
            if not data:
                break
            text_chunks.append(self._process_waveform(data, recognizer))
        return self._extract_final_result(recognizer, text_chunks)

    def _process_waveform(self, data, recognizer):
        """处理单个波形数据块"""
        if recognizer.AcceptWaveform(data):
            result = eval(recognizer.Result())
            return result.get("text", "")
        return ""

    def _extract_final_result(self, recognizer, text_chunks):
        """提取并合并最终识别结果"""
        final_result = eval(recognizer.FinalResult())
        text_chunks.append(final_result.get("text", ""))
        return ' '.join(filter(None, text_chunks)).strip()

    def _handle_recognition_error(self, error):
        """处理识别过程中出现的异常"""
        print(f"语音识别失败: {str(error)}")
        if isinstance(error, FileNotFoundError):
            return ""
        return ""

    def stop(self):
        """停止所有线程和资源释放"""
        self.is_listening = False
        self.is_recording = False
        
        if self.listen_thread:
            self.listen_thread.join()
        if self.record_thread:
            self.record_thread.join()
        
        if self.stream:
            self.stream.close()  # 修复streamlose拼写错误
        self.pa.terminate()
        p__main__":
    stt = STT(
        device_index=1,
        model_path="/opt/vosk-models/vosk-model-small-en-us-0.15",  # 替换为你的模型路径
    )

    try:
        stt.start()  # 启动后台监听（非阻塞）
        
        # 主程序轮询检测声音
        while True:
            if stt.is_voice_detected():
                print("主程序检测到声音，开始录音...")
                stt.start_recording()  # 手动触发录音
                break
            time.sleep(0.1)  # 降低CPU占用
        
        # 等待录音自动停止（由静音检测触发）
        while stt.is_recording:
            time.sleep(0.1)
        
        # 转换并输出纯文本
        result = stt.transcribe()
        print("识别结果（纯文本）：", result)
    finally:
        stt.stop()  # 确保资源释放
