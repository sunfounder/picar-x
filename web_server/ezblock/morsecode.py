from ezblock.utils import delay

class MorseCode():
    PAUSE = 500
    MORSECODE = {
        'A':'01', 'B':'1000', 'C':'1010', 'D':'100', 'E':'0', 'F':'0010', 'G':'110',
        'H':'0000', 'I':'00', 'J':'0111', 'K':'101', 'L':'0100', 'M':'11', 'N':'10',
        'O':'111', 'P':'0110', 'Q':'1101', 'R':'010', 'S':'000', 'T':'1',
        'U':'001', 'V':'0001', 'W':'011', 'X':'1001', 'Y':'1011', 'Z':'1100',
        '1':'01111', '2':'00111', '3':'00011', '4':'00001', '5':'00000',
        '6':'10000', '7':'11000', '8':'11100', '9':'11110', '0':'11111',
        '?':'001100', '/':'10010', ',':'110011', '.':'010101', ';':'101010',
        '!':'101011', '@':'011010', ':':'111000',
        }

    def setup(self, on, off):
        self.on = on
        self.off = off

    def unit(self, dt):
        self.on()
        delay(dt)
        self.off()
        delay(dt)

    def dot(self):
        self.unit(self.PAUSE/2)
    
    def dash(self):
        self.unit(self.PAUSE)

    def play_char(self, s):
        s = s.upper()
        for tap in self.MORSECODE[s]:
            if tap == '0':
                self.dot()
            if tap == '1':
                self.dash()
        delay(self.PAUSE)

    def play(self, msg):
        if isinstance(msg, str):
            for s in msg:
                self.play_char(s)
