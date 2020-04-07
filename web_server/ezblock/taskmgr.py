import subprocess, os
import RPi.GPIO as GPIO
import time
# import shlex
# import paramiko
# import pymysql

class Taskmgr(object):
    # def __init__(self):
    #     pass

    def cpu_temperature(self):          # 检测CPU温度
        raw_cpu_temperature = subprocess.getoutput("cat /sys/class/thermal/thermal_zone0/temp")
        cpu_temperature = float(raw_cpu_temperature)/1000               # 换算成摄氏温度
        #cpu_temperature = 'Cpu temperature : ' + str(cpu_temperature)
        return cpu_temperature

    def gpu_temperature(self):          # 检测GPU温度===GPU---用于图形处理
        raw_gpu_temperature = subprocess.getoutput( '/opt/vc/bin/vcgencmd measure_temp' )
        gpu_temperature = float(raw_gpu_temperature.replace( 'temp=', '' ).replace( '\'C', '' ))
        #gpu_temperature = 'Gpu temperature : ' + str(gpu_temperature)
        return gpu_temperature

    def cpu_usage(self):                # CPU占用率
        result = str(os.popen("top -n1 | awk '/Cpu\(s\):/ {print($2)}'").readline().strip())
        # args = "top -n1 | awk '/Cpu\(s\):/ {print($2)}'"
        # result = subprocess.Popen(args,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        return result

        # cpu = "vmstat 1 3|sed  '1d'|sed  '1d'|awk '{print $15}'"
        # stdin, stdout, stderr = ssh.exec_command(cpu)
        # cpu = stdout.readlines()
        # result = str(round((100 - (int(cpu[0]) + int(cpu[1]) + int(cpu[2])) / 3), 2)) + '%'
        # return result

    def disk_space(self):               # 磁盘占有率
        p = os.popen("df -h /")
        i = 0
        while 1:
            i = i +1
            line = p.readline()         # readline一次读取p中的一行内容， 占用内存小；read--一次性读取p中的所有内容，占用内存大
            if i==2:
                return line.split()[1:5]    # 以第二个到第五个（空格、换行(\n)、制表符(\t)）等为分隔符，将line字符串分成4段

    def disk_used(self):
        disk_used = float(self.disk_space()[1][:-1])
        return disk_used

    def ram_info(self):
        p = os.popen('free')
        i = 0
        while 1:
            i = i + 1
            line = p.readline()
            if i==2:
                return line.split()[1:4]    # 以第二个到第四个（空格、换行(\n)、制表符(\t)）等为分隔符，将line字符串分成4段

    def ram_used(self):
        ram_used = round(int(self.ram_info()[1]) / 1000,1)  # round---返回浮点数，四舍五入保留一位小数
        return ram_used

    def read(self):
        result = {
            "cpu_temperature": self.cpu_temperature(), 
            "gpu_temperature": self.gpu_temperature(),
            "cpu_usage": self.cpu_usage(), 
            "disk_used": self.disk_used(), 
            "ram_used": self.ram_used(), 
        }
        
        return result

def test():
    
    print(Taskmgr().cpu_temperature())
    print ("")
    print(Taskmgr().gpu_temperature())
    print ("")
    print(Taskmgr().cpu_usage())
    print ("")
    print(Taskmgr().disk_used())
    print ("")
    print(Taskmgr().ram_used())
    print ("")
    print (Taskmgr().read())

if __name__ == '__main__':
    test()