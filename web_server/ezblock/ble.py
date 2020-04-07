from ezblock.basic import _Basic_class
from ezblock.uart import UART
from time import sleep

class BLE(_Basic_class):
    # Delay between every 20 Byte
    SEND_DELAY = 100
    # Length of every package bluetooth sent
    DATA_LENGTH = 19
    def __init__(self, port='/dev/serial0', baudrate=115200, debug=False):
        super().__init__()
        self.uart = UART(port, baudrate)
        #self.uart = UART(1)
        #self.uart.init(9600)

    def read(self, num):
        result = self.uart.read(num)
        return result

    def writechar(self, data):
        self.uart.writechar(data)

    def write(self, data):
        data = data.encode('utf-8')
        for i in range(0, len(data), self.DATA_LENGTH):
            temp = data[i:i+self.DATA_LENGTH]
            self._debug("Raspberrypi.Ble.write.temp: %s"%temp)
            sleep(self.SEND_DELAY/1000.0)
            self.uart.write(temp)

    def verify(self, raw_data):
        self._debug("Flash.verify")
        import re
        self._debug("raw_data: %s" % raw_data)
        data_type = None
        data = None
        data_head = re.search('[*][$][A-Z]+[#][H][#]\d+[$][*]', raw_data)
        data_tail = re.search('[*][$][A-Z]+[#][T][#]\d+[$][*]', raw_data)
        ble = BLE()
        if data_head and data_tail:
            self._debug("Tansfer finished!")
            data_head = data_head.group(0)
            data_tail = data_tail.group(0)
            data_head_info = data_head.strip('*').strip('$').split('#')
            data_head_type = data_head_info[0]
            data_tail_info = data_tail.strip('*').strip('$').split('#')
            data_tail_type = data_tail_info[0]
            if data_head_type == data_tail_type:
                data_type = data_head_type
                self._debug("Tranfer type: %s" % data_type)
                expect_data_length = int(data_head_info[2])
                data = raw_data.split(data_head)[1].split(data_tail)[0]
                data_length = len(data)
                if expect_data_length == data_length:
                    self._debug("Verified!")
                    ble.write("1")
                    return [data_type, data, True]
                else:
                    self._debug("Verified error, expecting %s, received %s" %
                        (expect_data_length, data_length))
                    ble.write("0")
            else:
                self._debug("Verified error, data head type is %s, while data tail type is %s" % (
                    data_head_type, data_tail_type))
        else:
            self._debug("Verified error, head or tail not found")
        return [None, None, False]

class Remote(BLE):
    def __init__(self):
        super().__init__()
        self._value = {}

    def read(self):
        buf = bytearray()
        while self.uart.inWaiting():
            buf = buf + super().read(self.uart.inWaiting())

        buf = buf.decode()
        for i in range(0, len(buf), 20):
            _ = buf[i: i+20]
            if _:
                _ = _.strip()
                _ = _.split("#")
                if len(_) == 4:
                    _device, _id, _name, _value = _
                    _device_id = "{}_{}".format(_device, _id)
                    self._value[_device_id] = {_name: _value}

    def get_value(self, ctrl, id, name):
        _device_id = "{}_{}".format(ctrl, id)
        _result = self._value.get(_device_id, {}).get(name, 0)
        return _result

    def get_joystick_value(self, id, coord):
        try:
            _values = (self.get_value('JS', id, 'V')).split('+')
            if coord == 'X':
                return int(_values[0])
            elif coord == 'Y':
                return int(_values[1])
            else:
                return 0
        except:
            return 0
    
    def get_slider_value(self, id):
        try:
            _value = int(self.get_value('SL', id, 'V',))
            return _value
        except:
            return 0
    
    def get_dpad_value(self, id, direction):
        try:
            _value = int(self.get_value('DP', id, direction,))
            return _value
        except:
            return 0
            
    def get_button_value(self, id):
        try:
            _value = int(self.get_value('BT', id, 'V',))
            return _value
        except:
            return 0
            
    def get_switch_value(self, id):
        try:
            _value = int(self.get_value('SW', id, 'V',))
            return _value
        except:
            return 0