import time
from ezblock.i2c import I2C
from ezblock.color import Color
from ezblock.rgb_font import Alphabet, Icons

class RGB_Matrix():

    
    CONFIGURE_CMD_PAGE = 0XFD
    FRAME1_PAGE = 0x00
    FRAME2_PAGE = 0x01
    FUNCTION_PAGE = 0X0B
    LED_VAF_PAGE = 0X0D

    CONFIGURATION_REG = 0X00
    PICTURE_DISPLAY_REG = 0X01
    DISPLAY_OPTION_REG = 0X05
    BREATH_CTL_REG = 0X08
    BREATH_CTL_REG2 = 0X09
    SW_SHUT_DOWN_REG = 0X0A

    AUDIO_GAIN_CTL_REG = 0X0B
    STAGGERED_DELAY_REG = 0X0D
    SLEW_RATE_CTL_REG = 0X0E
    CURRENT_CTL_REG = 0X0F
    VAF_CTL_REG = 0X14
    VAF_CTL_REG2 = 0X15

    MSKSTD1 = (0x3<<0)	
    MSKSTD2 = (0x3<<2)
    MSKSTD3 = (0x3<<4)	
    MSKSTD4 = (0x3<<6)
    CONST_STD_GROUP1 = 0x00		
    CONST_STD_GROUP2 = 0x55	
    CONST_STD_GROUP3 = 0xAA		
    CONST_STD_GROUP4 = 0xFF

    MSKVAF1 = (0x4<<0) 
    MSKVAF2 = (0x4<<4)
    MSKVAF3 = (0x4<<0)
    MSKFORCEVAFTIME_CONST= (0x0<<3)
    MSKFORCEVAFCTL_ALWAYSON = (0x0<<6)
    MSKFORCEVAFCTL_DISABLE = (0x2<<6)
    MSKCURRENT_CTL_EN = (0x1<<7)
    CONST_CURRENT_STEP_20mA = (0x19<<0)
    mskBLINK_FRAME_300 = (0x0<<6)
    mskBLINK_EN = (0x1<<3)
    mskBLINK_DIS = (0x0<<3)
    mskBLINK_PERIOD_TIME_CONST = (0x7<<0)
    Type3Vaf = [
    #Frame 1
	0x50, 0x55, 0x55, 0x55, #C1-A ~ C1-P
	0x00, 0x00, 0x00, 0x00, #C2-A ~ C2-P
	0x00, 0x00, 0x00, 0x00, #C3-A ~ C3-P  
	0x15, 0x54, 0x55, 0x55, #C4-A ~ C4-P 
	0x00, 0x00, 0x00, 0x00, #C5-A ~ C5-P  
	0x00, 0x00, 0x00, 0x00, #C6-A ~ C6-P 
	0x55, 0x05, 0x55, 0x55, #C7-A ~ C7-P  
	0x00, 0x00, 0x00, 0x00, #C8-A ~ C8-P
	#Frame 2
	0x00, 0x00, 0x00, 0x00, #C9-A ~ C9-P 
	0x55, 0x55, 0x41, 0x55, #C10-A ~ C10-P 
	0x00, 0x00, 0x00, 0x00, #C11-A ~ C11-P  
	0x00, 0x00, 0x00, 0x00, #C12-A ~ C12-P 
	0x55, 0x55, 0x55, 0x50, #C13-A ~ C13-P  
	0x00, 0x00, 0x00, 0x00, #C14-A ~ C14-P 
	0x00, 0x00, 0x00, 0x00, #C15-A ~ C15-P 
	0x00, 0x00, 0x00, 0x00, #C16-A ~ C16-P 
    ]
    Type3PWMCTLAnodeRed = [
    #Reference SLED1735 Datasheet Type3 Map
	0x22, 0x23, 0x24, 0x25, 0x26, 0x27, 0x28, 0x29, 0x2A, 0x2B, 0x2C, 0x2D, 0x2E, 0x2F, # Red D1~D14 PWM CTL Mapping address
	0x50, 0x51, 0x52, 0x55, 0x56, 0x57, 0x58, 0x59, 0x5A, 0x5B, 0x5C, 0x5D, 0x5E, 0x5F,	# Red D15~D28 PWM CTL Mapping address
	0x80, 0x81, 0x82, 0x83, 0x84, 0x85, 0x88, 0x89, 0x8A, 0x8B, 0x8C, 0x8D, 0x8E, 0x8F, # Red D29~D42 PWM CTL Mapping address
	0x30, 0x31, 0x32, 0x33, 0x34, 0x35, 0x36, 0x37, 0x38, 0x3B, 0x3C, 0x3D, 0x3E, 0x3F, # Red D43~D56 PWM CTL Mapping address
	0x60, 0x61, 0x62, 0x63,	0x64, 0x65, 0x66, 0x67, 0x68, 0x69, 0x6A, 0x6B, 0x6E, 0x6F, # Red D57~D70 PWM CTL Mapping address
    ]
    Type3PWMCTLAnodeGreen = [
    0x32, 0x33, 0x34, 0x35,	0x36, 0x37, 0x38, 0x39, 0x3A, 0x3B, 0x3C, 0x3D, 0x3E, 0x3F,	# Green D1~D14 PWM CTL Mapping address
	0x60, 0x61, 0x62, 0x65, 0x66, 0x67,	0x68, 0x69, 0x6A, 0x6B, 0x6C, 0x6D, 0x6E, 0x6F,	# Green D15~D28 PWM CTL Mapping address
	0x90, 0x91, 0x92, 0x93, 0x94, 0x95, 0x98, 0x99, 0x9A, 0x9B, 0x9C, 0x9D,	0x9E, 0x9F, # Green D29~D42 PWM CTL Mapping address
	0x40, 0x41,	0x42, 0x43, 0x44, 0x45, 0x46, 0x47, 0x48, 0x4B, 0x4C, 0x4D, 0x4E, 0x4F, # Green D43~D56 PWM CTL Mapping address
	0x70, 0x71, 0x72, 0x73,	0x74, 0x75, 0x76, 0x77, 0x78, 0x79, 0x7A, 0x7B, 0x7E, 0x7F, # Green D57~D70 PWM CTL Mapping address
    ]
    Type3PWMCTLAnodeBlue = [
    0x42, 0x43, 0x44, 0x45, 0x46, 0x47,	0x48, 0x49, 0x4A, 0x4B, 0x4C, 0x4D, 0x4E, 0x4F, # Blue D1~D14 PWM CTL Mapping address
	0x70, 0x71, 0x72, 0x75, 0x76, 0x77,	0x78, 0x79, 0x7A, 0x7B, 0x7C, 0x7D, 0x7E, 0x7F,	# Blue D15~D28 PWM CTL Mapping address
	0x20, 0x21, 0x22, 0x23, 0x24, 0x25, 0x28, 0x29, 0x2A, 0x2B, 0x2C, 0x2D,	0x2E, 0x2F, # Blue D29~D42 PWM CTL Mapping address
	0x50, 0x51,	0x52, 0x53, 0x54, 0x55, 0x56, 0x57, 0x58, 0x5B, 0x5C, 0x5D, 0x5E, 0x5F, # Blue D43~D56 PWM CTL Mapping address
	0x80, 0x81, 0x82, 0x83,	0x84, 0x85, 0x86, 0x87, 0x88, 0x89, 0x8A, 0x8B, 0x8E, 0x8F, # Blue D57~D70 PWM CTL Mapping address
    ]


    def __init__(self, addr):
        self.bus = I2C()
        self.addr = addr
        self.alphabet = Alphabet()
        self.icons = Icons()

        self.write_cmd(self.CONFIGURE_CMD_PAGE, self.FUNCTION_PAGE)  #Setting SLED1735 Ram Page to Function Page
        self.write_cmd(self.SW_SHUT_DOWN_REG, 0x0)  #System must go to SW shutdowm mode when initialization
        self.write_cmd(self.PICTURE_DISPLAY_REG, 0x10)  #Setting Matrix Type = Type3
        self.write_cmd(self.STAGGERED_DELAY_REG, ((self.MSKSTD4 & self.CONST_STD_GROUP4)|(self.MSKSTD3 & self.CONST_STD_GROUP3)|(self.MSKSTD2 & self.CONST_STD_GROUP2)|(self.MSKSTD1 & self.CONST_STD_GROUP1)))  #Setting Staggered Delay
        self.write_cmd(self.SLEW_RATE_CTL_REG, 0x1)  #Enable Slew Rate control
        self.write_cmd(self.VAF_CTL_REG, (self.MSKVAF2 | self.MSKVAF1))  #VAF Control settings base on the LED type.
        self.write_cmd(self.VAF_CTL_REG2, (self.MSKFORCEVAFCTL_DISABLE | self.MSKFORCEVAFTIME_CONST | self.MSKVAF3))
        self.write_cmd(self.CURRENT_CTL_REG, (self.MSKCURRENT_CTL_EN | self.CONST_CURRENT_STEP_20mA))  #Setting LED driving current = 20mA and Enable current control
        self.write_cmd(self.CONFIGURE_CMD_PAGE, self.FRAME1_PAGE)  #Init Frame1Page(Clear all Ram) Setting SLED1735 Ram Page to Frame 1 Page
        self.write_Ndata(0x00, 0X00, 0XB3)  #send 0xB3 bytes length Data From address 0x00
        self.write_cmd(self.CONFIGURE_CMD_PAGE, self.FRAME2_PAGE)  #Clear Type3 Frame 2 Page 
        self.write_Ndata(0x00, 0X00, 0XB3)  #send 0xB3 bytes length Data From address 0x00
        self.write_cmd(self.CONFIGURE_CMD_PAGE, self.LED_VAF_PAGE)
        self.write_Ndata(0X00, self.Type3Vaf, 0X40)
        self.write_cmd(self.CONFIGURE_CMD_PAGE, self.FUNCTION_PAGE)
        self.write_cmd(self.SW_SHUT_DOWN_REG, 0x1)  #After initialization , system back to SW Normal mode.
        self.write_cmd(self.CONFIGURE_CMD_PAGE, self.FRAME1_PAGE)
        self.write_Ndata(0X00, 0XFF, 0X10)  #Clear LED CTL Registers (Frame1Page)
        self.write_Ndata(0x20, 0x00, 0X80)
        self.write_cmd(self.CONFIGURE_CMD_PAGE, self.FRAME2_PAGE)
        self.write_Ndata(0X00, 0XFF, 0X10)  #Clear LED CTL Registers (Frame1Page)
        self.write_Ndata(0x20, 0x00, 0X80)



    def write_cmd(self, reg, cmd):
        self.bus._i2c_write_byte_data(self.addr, reg, cmd)

    def write_Ndata(self, startaddr, data, length):
        addr = startaddr
        if isinstance(data, int):
            for i in range(length):
                self.write_cmd(addr, data)
                addr += 1
        elif isinstance(data, list):
            for i in range(length):
                self.write_cmd(addr, data[i])
                addr += 1
    

    def image(self, image):
        reds = list(map(lambda x: x[0], image))
        greens = list(map(lambda x: x[1], image))
        blues = list(map(lambda x: x[2], image))
        revert_image = [reds, greens, blues]
        reg = 0x20  #一页的寄存器起始地址
        empty = 0  #寄存器地址空缺的位置（写入的数据需要补0）
        pos = 0  #数据列表需要写入的数据所对应的索引
        # print("r: %s, g: %s, b: %s"%(len(reds), len(greens), len(blues)))
        for i in range(15):
            if i == 0:
                # print("Write Page 1")
                self.write_cmd(self.CONFIGURE_CMD_PAGE, self.FRAME1_PAGE)  #设置写入的页
            elif reg == 0x20:
                # print("Write Page 2")
                self.write_cmd(self.CONFIGURE_CMD_PAGE, self.FRAME2_PAGE)

            color = i % 3
            data = revert_image[color][pos*14:(pos+1)*14]
            data.insert(empty,0)  #写入的数据补0
            data.insert(empty + 1, 0)
            self.bus._i2c_write_i2c_block_data(self.addr, reg, data)
            if color == 2:
                empty += 3
                pos += 1
            reg += 0x10
            if reg == 0xA0:
                reg = 0x20
        
    
    def display_char(self, data, color):
        image = []
        c = Color()
        c.color(color)
        red = c.get_from("red", color)
        green = c.get_from("green", color)
        blue = c.get_from("blue", color)
        for i in data:
            for j in range(8):
                if i & 0x1:
                    image.append([red, green, blue])
                else:
                    image.append([0, 0, 0])
                i >>= 1
        self.image(image)

    def string_to_string_bits(self, string):
        smap = []
        for i in range(8):
            bits = ''
            for letter in string:
                try:
                    bits += self.alphabet.normal(letter)[-i-1]
                except:
                    for j in range(len(self.alphabet.normal(letter)[0])):
                        bits += '0'
                bits += '0'
            smap.append(bits)
        smap.reverse()
        return smap

    def string_to_bytes(self, s, pos=0):
        smap = self.string_to_string_bits(s)
        bits_list = []
        pos = -pos
        for i in range(8):
            temp = ''
            if pos <= 0:
                for j in range(-pos,8-pos):
                    try:
                        temp += smap[i][j]
                    except:
                        temp += '0'
            else:
            # add 0 at front
                for j in range(pos):
                    temp += '0'
                for j in range(8-pos):
                    try:
                        temp += smap[i][j]
                    except:
                        temp += '0'
            bits_list.append(temp)
        return self.string_bits_to_bytes(bits_list)

    def string_bits_to_bytes(self, _bits_list):
        _bytes = []
        if len(_bits_list) != 8:
            raise ValueError("arguement should be list of 8 lines of strings")
        for _bits in _bits_list:
            _bits = _bits.replace(',', '').replace(' ', '')
            if len(_bits) != 8:
                raise ValueError('every item in the list should be string with exact 8 "0" and "1" representing "off" and "on"')
            temp = _bits
            temp = list(temp)
            temp.reverse()
            temp = "".join(temp)
            temp = int(temp, base=2)
            _bytes.append(temp)
        return _bytes

    def show_string(self, string, color, pos=0):
        _bytes = self.string_to_bytes(string, pos)
        self.display_char(_bytes, color)
    
    def show_icon(self, icon, color):
        _bytes = self.string_bits_to_bytes(self.icons(icon))
        self.display_char(_bytes, color)
    
    
    
def test():
    rr = RGB_Matrix(0X74)
    # image = [ [20] * 3 ] * 64
    # t = time.time()
    # rr.image(image)
    # print("finished in %s"%(time.time()-t))
    for pos in range(40):
        rr.show_string("helloworld", "#842154", pos=pos)
        time.sleep(0.5)
    # TIME_DELAY = 0.2
    # while True:
    #     rr.show_icon("butterfly", "#F0F00F")
    #     time.sleep(TIME_DELAY)
    #     rr.show_icon("umbrella", "#00F00F")
    #     time.sleep(TIME_DELAY)
    #     rr.show_icon("skull", "#FF00F0")
    #     time.sleep(TIME_DELAY)
    #     rr.show_icon("house", "#F00F0F")
    #     time.sleep(TIME_DELAY)


# test()