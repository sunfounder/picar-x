from ezblock.basic import _Basic_class

class Music(_Basic_class):
    MUSIC_BEAT = 500

    NOTES = {
        "Low C": 261.63,
        "Low C#": 277.18,
        "Low D": 293.66,
        "Low D#": 311.13,
        "Low E": 329.63,
        "Low F": 349.23,
        "Low F#": 369.99,
        "Low G": 392.00,
        "Low G#": 415.30,
        "Low A": 440.00,
        "Low A#": 466.16,
        "Low B": 493.88,
        "Middle C": 523.25,
        "Middle C#": 554.37,
        "Middle D": 587.33,
        "Middle D#": 622.25,
        "Middle E": 659.25,
        "Middle F": 698.46,
        "Middle F#": 739.99,
        "Middle G": 783.99,
        "Middle G#": 830.61,
        "Middle A": 880.00,
        "Middle A#": 932.33,
        "Middle B": 987.77,
        "High C": 1046.50,
        "High C#": 1108.73,
        "High D": 1174.66,
        "High D#": 1244.51,
        "High E": 1318.51,
        "High F": 1396.91,
        "High F#": 1479.98,
        "High G": 1567.98,
        "High G#": 1661.22,
        "High A": 1760.00,
        "High A#": 1864.66,
        "High B": 1975.53,
    }
    def note(self, n):
        try:
            n = self.NOTES[n]
            return n
        except:
            raise ValueError("{} is not a note".format(n))
    
    def beat(self, b):
        b = float(b)
        b = b * self.MUSIC_BEAT
        return b
    
    def tempo(self, *args):
        if len(args) == 0:
            return int(60.0 / (self.MUSIC_BEAT / 1000.0))
        else:
            try:
                tempo = int(args[0])
                self.MUSIC_BEAT = int((60.0 / tempo) * 1000.0)
                return tempo
            except:
                raise ValueError("tempo must be int not {}".format(args[0]))