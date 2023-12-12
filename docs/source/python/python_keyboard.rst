.. _py_keyboard_control:

2. キーボード制御
================================

このプロジェクトでは、キーボードを使ってPiCar-Xをリモートで制御する方法を学びます。
PiCar-Xを前進、後退、左、右に動かすことができます。

**コードの実行**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 2.keyboard_control.py

キーボードのキーを押してPiCar-Xを制御しましょう！

    * w: 前進
    * a: 左に曲がる
    * s: 後退
    * d: 右に曲がる
    * i: 頭を上げる
    * k: 頭を下げる
    * j: 頭を左に向ける
    * l: 頭を右に向ける     
    * ctrl + c: 終了

**コード**

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


**どのように動作するのか？**

PiCar-Xは、読み取ったキーボードの文字に基づいて適切なアクションを行うべきです。
``lower()`` 関数は大文字を小文字に変換するため、文字の大文字・小文字に関わらず有効です。

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
