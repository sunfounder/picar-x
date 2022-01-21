from typing import List
from adc import ADC

class IRSensors(object):
    def __init__(self) -> None:
        # Initialize IR sensor pins
        self.S0 = ADC('A0')
        self.S1 = ADC('A1')
        self.S2 = ADC('A2')

    def read(self)->List[int]:
        """ Read IR sensor array
        """
        adc_value_list = []
        adc_value_list.append(self.S0.read())
        adc_value_list.append(self.S1.read())
        adc_value_list.append(self.S2.read())
        return adc_value_list
