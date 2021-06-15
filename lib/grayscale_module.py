from adc import ADC

class Grayscale_Module(object):
    def __init__(self,ref = 1000):
        self.chn_0 = ADC("A0")
        self.chn_1 = ADC("A1")
        self.chn_2 = ADC("A2")
        self.ref = ref


    def get_line_status(self,fl_list):

        if fl_list[0] > self.ref and fl_list[1] > self.ref and fl_list[2] > self.ref:
            return 'stop'
            
        elif fl_list[1] <= self.ref:
            return 'forward'
        
        elif fl_list[0] <= self.ref:
            return 'right'

        elif fl_list[2] <= self.ref:
            return 'left'

    def get_grayscale_data(self):
        adc_value_list = []
        adc_value_list.append(self.chn_0.read())
        adc_value_list.append(self.chn_1.read())
        adc_value_list.append(self.chn_2.read())
        return adc_value_list

if __name__ == "__main__":
    import time
    GM = Grayscale_Module(950)
    while True:
        print(GM.get_grayscale_data())
        time.sleep(1)
