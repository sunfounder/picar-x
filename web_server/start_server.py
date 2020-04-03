from os import system
from ezblock import getIP
import time
import os
dirs = './records' 


def start_http_server():
    system("cd /home/pi/picar-x-web-control/web_client && sudo python3 -m http.server 80 2>&1 1>/dev/null &")#开启服务器

def close_http_server():
    system("sudo kill $(ps aux | grep 'http.server' | awk '{ print $2 }') 2>&1 1>/dev/null")
    
def start_websocket():
    # print("start_websocket")
    # if not os.path.exists(dirs):
    #     os.makedirs(dirs)
    # system("python3 file_server.py &")
    system("python3 web_server.py 2>&1 1>/dev/null&")

def close_websocket():
    # print("close_websocket")
    system("kill $(ps aux | grep 'web_server.py' | awk '{ print $2 }') 2>&1 1>/dev/null")
    # system("kill $(ps aux | grep 'file_server.py' | awk '{ print $2 }') 2>&1 1>/dev/null")



if __name__ == '__main__':
    try:
        for _ in range(10):
            ip = getIP()
            if ip:
                break
            time.sleep(1)
        start_websocket()
        print("Web example starts at %s" % (ip)) 
        print("Open http://%s in your web browser to control the car!" % (ip))
        # print("Press Ctrl + C to exit")
        while 1:
            
            pass 
    except KeyboardInterrupt:
        print('KeyboardInterrupt')
    finally:
        print("Finished")
        close_websocket()
        close_http_server()