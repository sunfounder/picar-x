from serial import Serial
class Serial_Sound():
    CMD_HEAD = 0XAA
    QUERY_PALYSTATUS = 0X01 #查询播放状态
    PLAY = 0X02 #播放
    SUSPEND = 0X03 #暂停
    STOP = 0X04 #停止
    LAST = 0X05 #上一曲
    NEXT = 0X06 #下一曲
    APPOINT_SONG = 0X07 #指定曲目
    APPOINT_ROUTE = 0X08 #指定盘符指定路径
    QUERY_ONLINEROUTE = 0X09 #查询在线盘符
    QUERY_PALYROUTE = 0X0A #查询播放盘符
    ROUTE = 0X0B #设置路径
    QUERY_ALLSONG = 0X0C #查询总曲目
    QUERY_PALYSONG = 0X0D #查询当前曲目
    LAST_DIR = 0X0E #上一个目录
    NEXT_DIR = 0X0F #下一个目录
    END_PALY = 0X10 #结束播放
    QUERY_DIRFIR = 0X11 #查询目录首曲目
    QUERY_DIRALL = 0X12 #查询目录总曲目
    SET_VOLUME = 0X13 #设置音量
    ADD_VOLUME = 0X14 #音量加
    REDUCE_VOLUME = 0X15 #音量减
    APPOINT_SONG_INSERT = 0X16 #指定曲目插播
    MODE = 0X18
    SET_LOOP_TIME = 0X19 #设置循环次数
    QUERY_SONG_NAME = 0X1E #查询歌曲短名称
    APPOINT_REW = 0X22 #指定时间快退
    APPOINT_FAST = 0X23 #指定时间快进
    GET_SONG_TIME = 0X24 #获取当前曲目总时间

    ROUTE_U = 0X00   #盘符
    ROUTE_SD = 0X01
    ROUTE_FLASH = 0X02
    MODULE_ALL_LOOP = 0X00 #模式
    MODULE_SINGLE_LOOP = 0X01
    MODULE_SINGLE_STOP = 0X02
    MODULE_ALL_RANDOM = 0X03
    MODULE_DIR_LOOP = 0X04
    MODULE_DIR_RANDOM = 0X05
    MODULE_DIR_ORDER = 0X06
    MODELE_ORDER = 0X07

    def __init__(self, port='/dev/ttyS0'):
        self.ser = Serial(port, 9600, timeout=10)
    
    # def write(self, cmd, data=[]):
    def write(self, *data):
        data = list(data)
        if len(data) < 0:
            raise ValueError("write expect 1 positional argument, 0 givin")
        cmd = data.pop(0)
        length = len(data)
        checksum = (self.CMD_HEAD+cmd+length+sum(data)) & 0XFF
        msg = [self.CMD_HEAD, cmd, length, *data, checksum]
        self.ser.write(msg)
   
    def read(self):
        print("Read:")
        value = self.ser.read(3)
        # print(value)
        code = value[0]
        mold = value[1]
        len = value[2]
        value = self.ser.read(len+1)
        data = value[0:-1]
        checksum = value[-1]
        cs = (code+mold+len+sum(data)) & 0xFF
        if cs != checksum:
            print("Checksum Error")
            return False
        data = list(data)
        print(data)
        return data

    def read_data(self,cmd):
        self.write(cmd)
        self.read()

    def play(self, *num):  #名称分高8位 低8位
        self.write(self.APPOINT_SONG, *num)

    def set_route(self,num):  # 0X00为U盘 0X01为SD卡 0X02为FLASH
        self.write(self.ROUTE, num)

    def set_mode(self,num): #全盘循环(00)单曲循环(01)单曲停止(02)全盘随机(03)目录循环(04)目录随机(05)目录顺序播放(06)顺序播放(07)
        self.write(self.MODE, num)

    def set_loop_time(self, *num): #次数为高8位 低8位 
        self.write(self.SET_LOOP_TIME, *num)

    def set_volume(self,num):
        self.write(self.SET_VOLUME, num)

    def play_route(self,num,str):
        data = list(str.encode("gb2312"))
        #print(data)
        self.write(self.APPOINT_ROUTE, num, data)





def main():
    import time
    ss = Serial_Sound()
    ss.set_route(ss.ROUTE_SD)
    ss.read_data(ss.QUERY_ALLSONG)
    ss.read_data(ss.QUERY_PALYROUTE)
    #ss.set_mode(MODULE_SINGLE_STOP)
    #ss.set_loop_time(0X00,0X04)
    #ss.set_volume(0X08)
    #ss.play(0X00, 0X08)
    ss.read_data(ss.QUERY_PALYSONG)
    #ss.play_route(0X01,"/广告*/小米*???")



# main()




