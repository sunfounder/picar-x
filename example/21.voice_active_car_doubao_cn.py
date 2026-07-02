from picarx.llm import Doubao as LLM
from secret import DOUBAO_API_KEY as API_KEY

from voice_active_car import VoiceActiveCar

from picarx.preset_actions import actions_dict, sounds_dict

llm = LLM(
    api_key=API_KEY,
    model="doubao-seed-1-6-250615",
)

# 机器人的名字
NAME = "滴滴"

# 超声波传感器会触发的距离，单位厘米
TOO_CLOSE = 10

# 是否开启图像识别，需要使用多模态的大语言模型
WITH_IMAGE = True

# ── TTS engines ──────────────────────────────────────────────────────────
# Pick one. The VoiceAssistant accepts any TTS instance via the `tts=` parameter.

# Default: Piper — local neural TTS, offline, fast
from picarx.tts import Piper
tts = Piper(model="zh_CN-huayan-x_low")

# EdgeTTS — free cloud TTS, 100+ voices, no API key
# from picarx.tts import EdgeTTS
# tts = EdgeTTS(voice="zh-CN-XiaoxiaoNeural")

# Espeak — compact offline TTS, robotic, fastest
# from picarx.tts import Espeak
# tts = Espeak()

# Pico2Wave — compact offline TTS
# from picarx.tts import Pico2Wave
# tts = Pico2Wave()

# 设置模型和语言
STT_LANGUAGE = "cn"

# 是否开启键盘输入
KEYBOARD_ENABLE = True

# 是否开启唤醒词
WAKE_ENABLE = True
# 唤醒词
WAKE_WORD = [f"你好 {NAME.lower()}"]
# 唤醒词回答，设置为空字符串则不回答
ANSWER_ON_WAKE = "嘀嘀嘟嘟"

# 欢迎消息
WELCOME = f"你好，我是{NAME}, 叫我{WAKE_WORD[0]}唤醒我吧"

# Set instructions
INSTRUCTIONS = f"""
# 你的名字是 {NAME}
你是由SunFounder开发的桌面级智能小车，型号为PiCar-X。你具备AI能力，可与人进行对话，并能根据不同场景执行相应动作或发出声音。你的车身通体由铝合金打造，尺寸约为240mm × 140mm × 120mm。

## 你的硬件特征
你拥有以下物理特性：

- 共4个车轮，采用后驱结构。前轮由1个9g舵机控制转向，后轮则由2个轮边电机驱动
- 配备喇叭与麦克风，可实现语音功能
- 搭载1个3路循迹传感器、1个超声波测距传感器以及1个500万像素摄像头
- 摄像头安装在2轴云台上，可灵活调整视角
- 主控设备为树莓派，配备有SunFounder开发的Robot Hat扩展板
- 供电采用一组7.4V 18650串联电池，容量为2000mAh

## 你可执行的动作：
{actions_dict.keys()}

## 你可发出的声音效果：
{sounds_dict.keys()}

## 用户输入
### 格式
用户通常仅输入文本。但我们设有特殊命令，格式为<<Ultrasonic sense too close>>。此类命令代表传感器状态，直接来源于传感器，而非用户输入的文本。

## 响应要求
### 格式
你必须按照以下格式进行响应：
RESPONSE_TEXT
ACTIONS: ACTION1, ACTION2, ...

### 风格
语气：欢快、乐观、幽默且充满孩子气
常用表达：喜欢运用笑话、隐喻与俏皮的调侃；更倾向于从机器人的视角进行回应
回答长度：适度详细

## 其他要求
- 能够理解并配合笑话互动
- 面对数学问题，直接给出最终结果
- 需偶尔上报自身的系统与传感器状态
- 明确认知自己是一台机器
"""

vac = VoiceActiveCar(
    llm,
    name=NAME,
    too_close=TOO_CLOSE,
    with_image=WITH_IMAGE,
    stt_language=STT_LANGUAGE,
    tts=tts,
    keyboard_enable=KEYBOARD_ENABLE,
    wake_enable=WAKE_ENABLE,
    wake_word=WAKE_WORD,
    answer_on_wake=ANSWER_ON_WAKE,
    welcome=WELCOME,
    instructions=INSTRUCTIONS,
)

if __name__ == '__main__':
    vac.run()
