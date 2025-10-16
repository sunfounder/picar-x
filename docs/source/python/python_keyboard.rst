.. _py_keyboard_control:

3. 键盘控制
================================


在本项目中，我们将学习如何使用键盘远程控制 PiCar-X。您可以通过键盘控制 PiCar-X 
前进、后退、左转和右转。

**运行代码**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 3.keyboard_control.py

使用键盘按键控制 PiCar-X！ 

    * w: 前进 
    * a: 左转 
    * s: 后退 
    * d: 右转
    * i: 抬头
    * k: 低头
    * j: 左转头
    * l: 右转头     
    * ctrl + c: 按两次退出程序

**代码**

.. code-block:: python

    from picarx import Picarx
    from time import sleep
    import readchar

    manual = '''
    Press keys on keyboard to control PiCar-X!
        w: Forward
        a: Turn left
        s: Backward
        d: Turn right
        i: Head up
        k: Head down
        j: Turn head left
        l: Turn head right
        ctrl+c: Quit
    '''

    def show_info():
        print("\033[H\033[J",end='')  # clear terminal windows
        print(manual)


    if __name__ == "__main__":
        try:
            pan_angle = 0
            tilt_angle = 0
            px = Picarx()
            show_info()
            while True:
                key = readchar.readkey()
                key = key.lower()
                if key in('wsadikjl'): 
                    if 'w' == key:
                        px.set_dir_servo_angle(0)
                        px.forward(80)
                    elif 's' == key:
                        px.set_dir_servo_angle(0)
                        px.backward(80)
                    elif 'a' == key:
                        px.set_dir_servo_angle(-35)
                        px.forward(80)
                    elif 'd' == key:
                        px.set_dir_servo_angle(35)
                        px.forward(80)
                    elif 'i' == key:
                        tilt_angle+=5
                        if tilt_angle>35:
                            tilt_angle=35
                    elif 'k' == key:
                        tilt_angle-=5
                        if tilt_angle<-35:
                            tilt_angle=-35
                    elif 'l' == key:
                        pan_angle+=5
                        if pan_angle>35:
                            pan_angle=35
                    elif 'j' == key:
                        pan_angle-=5
                        if pan_angle<-35:
                            pan_angle=-35                 

                    px.set_cam_tilt_angle(tilt_angle)
                    px.set_cam_pan_angle(pan_angle)      
                    show_info()                     
                    sleep(0.5)
                    px.forward(0)
            
                elif key == readchar.key.CTRL_C:
                    print("\n Quit")
                    break

        finally:
            px.set_cam_tilt_angle(0)
            px.set_cam_pan_angle(0)  
            px.set_dir_servo_angle(0)  
            px.stop()
            sleep(.2)

**工作原理**

PiCar-X 会根据读取的键盘输入采取相应动作。 
``lower()`` 函数将大写字母转换为小写字母，以确保无论输入大小写字母都能正确识别。

.. code-block:: python

    while True:
        key = readchar.readkey()
        key = key.lower()
        if key in('wsadikjl'): 
            if 'w' == key:
                pass
            elif 's' == key:
                pass
            elif 'a' == key:
                pass
            elif 'd' == key:
                pass
            elif 'i' == key:
                pass
            elif 'k' == key:
                pass
            elif 'l' == key:
                pass
            elif 'j' == key:
                pass             
    
        elif key == readchar.key.CTRL_C:
            print("\n Quit")
            break
