import random
from ezblock.utils import constrain

class Color():
    def color(self, value):
        if self.iscolor(value):
            return value
        else:
            self.raise_not_color(value)
    def led_color(self, value):
        if self.iscolor(value):
            return value
        else:
            self.raise_not_color(value)

    def iscolor(self, value):
        if isinstance(value, str):
            if value.startswith("#"):
                color = value[1:]
                if len(color) == 6:
                    try:
                        int(color,16)
                        return True
                    except:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

    def raise_not_color(self, value):
        raise ValueError('Color must be in form of "#ff45b6", not {}({})'.format(value, type(value)))

    def get_from(self, rgb, c):
        if not self.iscolor(c):
            self.raise_not_color(c)
        rgb = rgb.lower()
        if rgb == 'red':
            return int(c[1:3], 16)
        elif rgb == 'green':
            return int(c[3:5], 16)
        elif rgb == 'blue':
            return int(c[5:7], 16)
        else:
            raise ValueError('RGB value must be "red", "green" or "blue", not {}({})'.format(rgb, type(rgb)))

    def random(self):
        return '#{:06X}'.format(random.randint(0, 2**24 - 1))
    
    def rgb(self, r,g,b):
        r = int(constrain(r, 0, 255))
        g = int(constrain(g, 0, 255))
        b = int(constrain(b, 0, 255))
        return '#{:02X}{:02X}{:02X}'.format(r, g, b)

    def blend(self, colour1, colour2, ratio):
        if not self.iscolor(colour1):
            self.raise_not_color(colour1)
        if not self.iscolor(colour2):
            self.raise_not_color(colour1)
        r1, r2 = int(colour1[1:3], 16), int(colour2[1:3], 16)
        g1, g2 = int(colour1[3:5], 16), int(colour2[3:5], 16)
        b1, b2 = int(colour1[5:7], 16), int(colour2[5:7], 16)
        ratio = min(1, max(0, ratio))
        r = round(r1 * (1 - ratio) + r2 * ratio)
        g = round(g1 * (1 - ratio) + g2 * ratio)
        b = round(b1 * (1 - ratio) + b2 * ratio)
        return '#{:02X}{:02X}{:02X}'.format(r, g, b)