from serial import Serial
class Serial_Servo():
    DATA_HEAD = [0xFF, 0xFF]
    RECEIVE_HEAD = [0xFF, 0xF5]

    PING = 0x01  # 查询舵机/快速查询舵机状态
    READ_DATA = 0x02  # 查询指定地址的数据
    WRITE_DATA = 0x03  # 向指定地址写数据
    REG_WRITE = 0x04  # (异步写) 向指定地址预写数据，等收到 ACTION 指令后才执行，主要用于控制多个舵机 时能让舵机同时启动
    ACTION = 0x05  # (执行异步写) 触发执行 REG WRITE 指令
    RESET = 0x06  # 把寄存器恢复为出厂设定值
    SYNC_WRITE = 0x83  #(同步写)

    VERSION = 0x03  # 2 byte 记录舵机软件版本信息, 格式为 vA.B 如 v1.28 =0x011C
    SERVO_ID = 0x05  # 舵机自身 ID 号，有效范围:1~250 注: 254 为广播 ID Uint8 default: 1
    PROTECT_TIME = 0x06  # 单位:/S 舵机堵转一段时间后保护 Uint8 default: 3
    MIN_ANGLE = 0x09  # 2 byte 最小角度限制 Uint16 default: 0
    MAX_ANGLE = 0x0B  # 2 byte 最大角度限制 Uint16 default: 4095
    MAX_TORQUE = 0x10  # 2 byte 最大扭矩 Uint16 default: 800
    SPEED = 0x12  # 速度调整 Uint8 default: 30
    UNLOAD = 0x13  # 卸载条件 Uint8 default: 0
    MID_POS = 0x14  # 2 byte 位置调整偏移量，正数往 4095 方向调整， 负数往 0 方向调整 Int16 default: 0
    SET_POS_1 = 0x16  # 设定目标位置一
    SET_POS_2 = 0x18
    SET_POS_3 = 0x1A
    MODE = 0x3F # 舵机/电机模式
    MOTOR_DIR = 0x40 # 电机模式方向
    TORQUE_SWITCH = 0x28 # 扭矩开关 0:扭矩关闭 非 0:扭矩打开
    TARGET_POS = 0x2A # 目标位置
    TIME_RUN = 0x2C # 2 byte 运行时间
    CURRENT = 0x2E # 2 byte 当前电流
    LOCK = 0x30 # 锁标志(急 停)
    CURRENT_POS = 0x38 # 当前位置
    SPEED_RUN = 0x3A # 运行速度
    RUN_POS_1 = 0x3C # 运行目标位置一
    RUN_POS_2 = 0x3D # 运行目标位置二
    RUN_POS_3 = 0x3E # 运行目标位置三
    #CURRENT_TEMP = 0x3F # 当前温度 单位:°C
    #REG_WRITE_FLAG =  0x40 # REG WRITE 标志
    SPEED_ADJ = 0x41 # 2 byte 速度调整

    BROADCAST_ID = 0xFE

    MOTOR = 0x00
    SERVO = 0x01

    def __init__(self, port='/dev/ttyS0'):
        self.ser = Serial(port,115200, timeout=1)

    def print_hex_list(self, li):
        msg = ""
        for val in li:
            msg += "{:02X} ".format(val)
        print(msg.strip())

    def to_hex_list(self, h):
        str_h = '{:X}'.format(h)
        if len(str_h) % 2 == 1:
            str_h = "0" + str_h
        length = len(str_h)
        li = []
        for i in range(0, length, 2):
            temp = int(str_h[i:i+2], 16)
            li.append(temp)
        return li
        
    def flat_list(self, li):
        if not isinstance(li, list):
            li = [li]
        result = []
        for i in li:
            if isinstance(i, list):
                result += self.flat_list(i)
            else:
                result.append(i)
        return result
        

    def write(self, id, cmd_type, data=[]):
        print("Write:")
        length = len(data) + 2
        checksum = (~(id+length+cmd_type+sum(data))) & 0xFF
        msg = self.DATA_HEAD + [id] + [length] + [cmd_type] + data + [checksum]
        msg = bytearray(msg)
        print("  ", end="")
        self.print_hex_list(msg)
        self.ser.write(msg)
        self.ser.read(len(msg))

    def read(self):
        print("Read:")
        value = self.ser.read(5)
        # print(value)
        rh = list(value[0:2])
        if rh != self.RECEIVE_HEAD:
            return False
        id = value[2]
        length = value[3]
        status = value[4]
        value = self.ser.read(length-1)
        data = value[0:-1]
        checksum = value[-1]
        cs = (~(id+length+status+sum(data))) & 0xFF
        if cs != checksum:
            print("Checksum Error")
            return False
        data = list(data)
        print(id, status, data)
        return id, status, data

    def ping(self, id):
        print("ping 0x{:02X}:".format(id))
        self.write(id, self.PING)
        self.read()
    
    def read_data(self, id, cmd, num):
        self.write(id, self.READ_DATA, [cmd, num])
        self.read()

    def write_data(self, id, cmd, value):
        values = self.flat_list(value)
        data = [cmd] + values
        self.write(id, self.WRITE_DATA, data)

    def reg_write(self, id, cmd, value):
        values = self.flat_list(value)
        data = [cmd] + values
        self.write(id, self.REG_WRITE, data)

    def action(self):
        self.write(0xFE, self.ACTION)

    def sync_write(self, id, cmd=[], *value):
        values = self.flat_list(list(value))
        data = cmd + values
        self.write(id, self.SYNC_WRITE, data)

    def reset(self, id):
        self.write(id, self.RESET)

    def write_id(self, id):
        print("write_id 0x{:02X}:".format(id))
        self.write_data(self.BROADCAST_ID, self.SERVO_ID, id)
    
    def write_angle_value(self, id, angle_value, time_run):
        cmd = self.TARGET_POS
        angle_value = [angle_value>>8&0xFF, angle_value&0xFF]
        time_run = [time_run>>8&0xFF, time_run&0xFF]
        value = angle_value + time_run
        self.reg_write(id, cmd, value)

    def convert_angle_time(self, angle, time_run):
        angle_value = angle * 4096/270
        angle_value = int(angle_value)
        angle_value = [angle_value>>8&0xFF, angle_value&0xFF]
        time_run = [time_run>>8&0xFF, time_run&0xFF]
        value = angle_value + time_run
        return value

    def write_angle(self, id, angle, time_run):
        value = self.convert_angle_time(angle, time_run)
        value = [self.TARGET_POS] + value
        self.write(id, self.WRITE_DATA, value)

    def write_more_angle(self,*buff):
        cmd = [self.TARGET_POS,0X04]
        angle_value = []
        length = len(buff)
        for i in range(0, length, 3):
            id = buff[i]
            angle = buff[i+1]
            angle = int(angle*15.17)
            angle = [angle>>8&0xFF, angle&0xFF]
            time = buff[i+2]
            time = [time>>8&0xFF, time&0xFF]
            angle_value.append(id)
            angle_value +=angle
            angle_value +=time
        #print(angle_value)
        self.sync_write(0XFE,cmd,angle_value)

    # write_all_angle([id, angle, time], [id, angle, time])
    # write_all_angle(servo1, servo2)
    def write_all_angle(self,*servos):  
        cmd = [self.TARGET_POS,0X04]
        data = []
        for servo in servos:
            id = servo.id()
            value = self.convert_angle_time(servo.angle(), servo.time())
            data.append(id)
            data += value
        #print(data)
        self.sync_write(0XFE,cmd,data)

    def set_mode(self,id,num):
        self.write_data(id,self.MODE,num)

    def set_motor_dir(self,id,num):
        self.write_data(id,self.MOTOR_DIR,num)

    def set_motor_speed(self,id,num):
        # if isinstance(num, (float, int)):
        #     num = int(num)
        # else:
        #     raise ValueError("Arguement must be int or float, not {}".format(type(num).__name__))
        # num = max(0, min(100, num))
        self.write_data(id,self.SPEED_ADJ,num)

    def run(self, *servos):
        cmd = [self.TARGET_POS,0X04]
        data = []
        for servo in servos:
            if servo.mode() == 0:
                self.set_mode(servo.id(), servo.mode())
                self.set_motor_speed(servo.id(), servo.speed())
                self.set_motor_dir(servo.id(), servo._dir)
            else:
                #self.set_mode(servo.id(), servo.mode())
                value = self.convert_angle_time(servo.angle(), servo.time())
                data.append(servo.id())
                data += value
        self.sync_write(0XFE,cmd,data)
        

class Servo1():
    MOTOR = 0
    SERVO = 1
    def __init__(self, id, angle=0, time=500, mode=1, speed=50, dir=0):
        self._id = id
        self._angle = angle
        self._time = time
        self._mode = mode
        self._speed = speed
        self._dir = dir
    
    def id(self, *value):
        if len(value) == 0:
            return self._id
        elif len(value) == 1:
            v = value[0]
            if isinstance(v, int):
                self._id = v
            else:
                raise ValueError("argument must be int, not {}".format(type(v).__name__))
        else:
            raise ValueError("function takes one arguement, {} is given".format(len(value)))

    def angle(self, *value):
        if len(value) == 0:
            return self._angle
        elif len(value) == 1:
            v = value[0]
            if isinstance(v, int):
                v = max(0, min(270, v))
                self._angle = v
            else:
                raise ValueError("argument must be int, not {}".format(type(v).__name__))
        else:
            raise ValueError("function takes one arguement, {} is given".format(len(value)))

    def time(self, *value):
        if len(value) == 0:
            return self._time
        elif len(value) == 1:
            v = value[0]
            if isinstance(v, int):
                self._time = v
            else:
                raise ValueError("argument must be int, not {}".format(type(v)))
        else:
            raise ValueError("function takes one arguement, {} is given".format(len(value)))
    
    def mode(self, *value):
        if len(value) == 0:
            return self._mode
        elif len(value) == 1:
            v = value[0]
            if isinstance(v, int):
                self._mode = v
            else:
                raise ValueError("argument must be int, not {}".format(type(v).__name__))
        else:
            raise ValueError("function takes one arguement, {} is given".format(len(value)))
    
    def speed(self, *value):
        if len(value) == 0:
            return self._speed
        elif len(value) == 1:
            v = value[0]
            if isinstance(v, int):
                if v > 0:
                    self._dir = 1
                else:
                    self._dir = 0
                v = max(0, min(100, abs(v)))
                self._speed = v
            else:
                raise ValueError("argument must be int, not {}".format(type(v).__name__))
        else:
            raise ValueError("function takes one arguement, {} is given".format(len(value)))

    

def test_sync():
    import time
    servo1 = Servo1(1)
    servo2 = Servo1(2)
    ss = Serial_Servo1()
    ss.write_all_angle(servo1,servo2)
    time.sleep(1)
    servo1.angle(90)
    servo2.angle(90)
    ss.write_all_angle(servo1,servo2)


def test1():
    ss = Serial_Servo1()
    ss.set_mode(0XFE,ss.MOTOR)
    ss.set_motor_dir(0XFE,0)
    ss.set_motor_speed(0XFE,50)

def test2():
    import time
    ss = Serial_Servo1()
    #ss.write_id(0x02)
    #time.sleep(1)
    #ss.ping(0x02)
    #while True:
    ss.write_angle(0XFE,0,500)
    time.sleep(1)
        # ss.write_angle(0XFE,45,500)
        # time.sleep(1)
    ss.write_angle(0XFE,90,500)
    time.sleep(1)
    ss.write_angle(0XFE,180,500)
        #time.sleep(1)
        #ss.write_angle(0XFE,270,500)
        #time.sleep(1)
        #ss.write_angle(0XFE,180,500)
        #time.sleep(1)
        #ss.write_angle(0XFE,90,500)
        #time.sleep(1)
    #time.sleep(1)
    #ss.write_angle(0X02,280,500)
    #ss.read_data(0X02,ss.MAX_TORQUE,0x02)
    ss.read_data(0X02,ss.MAX_ANGLE,0X02)

def main():
    import time
    #ss = Serial_Servo1()
    #servo1 = Servo1(1)
    #ss.run(servo1)
    #servo2 = Servo1(2)
    # ss.run(servo1,servo2)
    #time.sleep(1)
    #servo1.angle(90)
    # servo2.angle(90)
    #ss.run(servo1)
    #servo1.mode(ss.MOTOR)
    #servo1.speed(0)
    #ss.run(servo1,servo2)
    #time.sleep(1)
    #servo2.angle(180)
    #ss.run(servo1,servo2)
    ss = Serial_Servo()     #create an servo object from serial port and defaults to "/dev/ttyS0"
    servo1 = Servo1(1)       #create an parameter object and ID is 1
    servo2 = Servo1(2)       #create an parameter object and ID is 2
    servo1.mode(ss.MOTOR)   #set servo1 model to motor
    servo2.mode(ss.MOTOR)   #set servo2 model to motor
    servo1.speed(50)        #set servo1 speed to 50 max is 100 and dir is Clockwise
    servo2.speed(-50)       #set servo2 speed to 50 and dir is Anti-clockwise
    ss.run(servo1,servo2)   #run all servo



# main()
#test2()
#test_sync()