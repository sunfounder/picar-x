from ezblock.basic import _Basic_class
from ezblock.utils import mapping, is_installed
from distutils.spawn import find_executable

class TTS(_Basic_class):
    _class_name = 'TTS'
    SUPPORTED_LANGUAUE = [
        'en-US', #英语(美国)English-United States
        'en-GB', # 英语(英国)English-United Kingdom
        'de-DE', # 德语(德国)Germany-Deutsch
        'es-ES', # 西班牙语(西班牙)España-Español
        'fr-FR', #  法语(法国)France-Le français
        'it-IT', # 意大利语(意大利)Italia-lingua italiana
    ]

    def __init__(self, engine='espeak'):
        super().__init__()
        self._lang = "en-US"            # 默认输入的语言为英语
        self._amp   = 100 
        self._speed = 175
        self._gap   = 5
        self._pitch = 50
        if not is_installed("espeak"):
            raise Exception("TTS engine: espeak in not installed.")
    
    # def engine(self, value= 'espeak'):
    #     self._engine = value
    #     if self._engine == 'espeak':
    #         self._amp   = 100 
    #         self._speed = 175
    #         self._gap   = 5
    #         self._pitch = 50

    def _check_executable(self, executable):
        executable_path = find_executable(executable)
        found = executable_path is not None
        return found

    def say(self, words):           # 输入的文字
        self.write(words)

    def write(self, words):
        self._debug('Say:\n [%s]' % (words))
        # if self._check_executable('pico2wave') and self._check_executable('aplay'):
        #     cmd = 'pico2wave -l %s -w /tmp/pico.wav "%s" && aplay /tmp/pico.wav' % (self._lang, words)  # 传入语言，和需要转换成语言的文字
        #     self.run_command(cmd)
        #     self._debug('command: %s' %cmd)
        # else:
        #     self._debug('pico is busy. Pass')

        if self._check_executable('espeak'):
                cmd = 'espeak -a%d -s%d -g%d -p%d \"%s\" --stdout | aplay 2>/dev/null & ' % (self._amp, self._speed, self._gap, self._pitch, words)
                self.run_command(cmd)
                self._debug('command: %s' %cmd)
        else:
            self._debug('espeak is busy. Pass')

    def lang(self, *value):     # 切换语言，可识别5种语言
        if len(value) == 0:
            return self._lang
        elif len(value) == 1:
            v = value[0]
            if v in self.SUPPORTED_LANGUAUE:
                self._lang = v
                return self._lang
        raise ValueError("Arguement \"%s\" is not supported. run tts.supported_lang to get supported language type."%value)

    def supported_lang(self):           # 返回支持的语言类型
        return self.SUPPORTED_LANGUAUE

    def espeak_params(self, amp=None, speed=None, gap=None, pitch=None):
        if amp == None: 
            amp=self._amp
        if speed == None:
            speed=self._speed
        if gap == None:
            gap=self._gap
        if pitch == None:
            pitch=self._pitch

        if amp not in range(0, 200):
            raise ValueError('Amp should be in 0 to 200, not "{0}"'.format(amp))
        if speed not in range(80, 260):
            raise ValueError('speed should be in 80 to 260, not "{0}"'.format(speed))
        if pitch not in range(0, 99):
            raise ValueError('pitch should be in 0 to 99, not "{0}"'.format(pitch)) 
        self._amp   = amp
        self._speed = speed
        self._gap   = gap
        self._pitch = pitch

def test():
    tts = TTS()
    # tts.lang("de-DE")
    tts.speaker_volume(100)
    tts.espeak_params(amp=50, speed=80, gap=0, pitch=10)


if __name__ == "__main__":
    test()