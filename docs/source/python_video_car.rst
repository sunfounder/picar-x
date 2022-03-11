视频车
==========================================

该程序将提供帕克的第一人称视角！ 使用键盘 WSAD 键控制移动方向，使用 O 和 P 调整速度。


**运行代码**


.. note::

    * 这个项目需要访问树莓派的桌面来查看相机模块拍摄的画面。
    * 你可以将屏幕连接到PiCar-X上，或者参考教程 :ref:`remote_desktop`，用VNC或XRDP访问它。
    * 一旦进入树莓派的桌面，打开Terminal并输入以下命令来运行它，或者直接用Python编辑器打开并运行它。



.. code-block::

    cd /home/pi/picar-x/example
    sudo python3 video_car.py

代码运行后，您可以看到 PiCar-X 正在拍摄画面，并通过按以下键来控制它。

* O：加速
* P：减速
* W：前锋
* S：向后
* A：左转
* D：右转
* F：停止
* T：拍照
* ESC / Ctrl+C：退出

**代码**

.. code-block:: python
    
    # #!/usr/bin/env python3

    print('Please run under desktop environment (eg: vnc) to display the image window')

    from utils import reset_mcu
    reset_mcu()
    from picarx import Picarx
    from vilib import Vilib
    from time import sleep, time, strftime, localtime
    import readchar

    manual = '''
    Press key to call the function(non-case sensitive)：
        O: speed up
        P: speed down
        W: forward  
        S: backward
        A: turn left
        D：turn right
        F: stop
        T: take photo
        ESC / Ctrl+C: quit
    '''


    px = Picarx()

    def take_photo():
        _time = strftime('%Y-%m-%d-%H-%M-%S',localtime(time()))
        name = 'photo_%s'%_time
        path = "/home/pi/Pictures/picar-x/"
        Vilib.take_photo(name, path)
        print('\nphoto save as %s%s.jpg'%(path,name))


    def move(operate:str, speed):

        if operate == 'stop':
            px.stop()  
        else:
            if operate == 'forward':
                px.set_dir_servo_angle(0)
                px.forward(speed)
            elif operate == 'backward':
                px.set_dir_servo_angle(0)
                px.backward(speed)
            elif operate == 'turn left':
                px.set_dir_servo_angle(-30)
                px.forward(speed)
            elif operate == 'turn right':
                px.set_dir_servo_angle(30)
                px.forward(speed)
            


    def main():
        speed = 0
        status = 'stop'

        Vilib.camera_start(vflip=False,hflip=False)
        Vilib.display(local=True,web=True)
        sleep(2)  # wait for startup
        print(manual)
        
        while True:
            print("\rstatus: %s , speed: %s    "%(status, speed), end='', flush=True)
            # readkey
            key = readchar.readkey().lower()
            # operation 
            if key in ('wsadfop'):
                # throttle
                if key == 'o':
                    if speed <=90:
                        speed += 10           
                elif key == 'p':
                    if speed >=10:
                        speed -= 10
                    if speed == 0:
                        status = 'stop'
                # direction
                elif key in ('wsad'):
                    if speed == 0:
                        speed = 10
                    if key == 'w':
                        # Speed limit when reversing,avoid instantaneous current too large
                        if status != 'forward' and speed > 60:  
                            speed = 60
                        status = 'forward'
                    elif key == 'a':
                        status = 'turn left'
                    elif key == 's':
                        if status != 'backward' and speed > 60: # Speed limit when reversing
                            speed = 60
                        status = 'backward'
                    elif key == 'd':
                        status = 'turn right' 
                # stop
                elif key == 'f':
                    status = 'stop'
                # move 
                move(status, speed)  
            # take photo
            elif key == 't':
                take_photo()
            # quit
            elif key == readchar.key.CTRL_C or key in readchar.key.ESCAPE_SEQUENCES:
                print('\nquit ...')
                px.stop()
                Vilib.camera_close()
                break 

            sleep(0.1)


    if __name__ == "__main__":
        try:
            main()
        except Exception as e:
            print("error:%s"%e)
        finally:
            px.stop()
            Vilib.camera_close()
