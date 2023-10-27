ビデオ・カー
==========================================

このプログラムはPiCar-X からの一人称のビュー（カメラ画像）を表示します! キーボードの W、S、A、D の各キーを使用して移動方向を制御し、O と P を使用して速度を調整します。


**コードの実行**


.. note::

    * このプロジェクトでは、カメラ モジュールで撮影した映像を表示するためにRaspberry Piデスクトップにアクセスする必要があります。
    * モニター（またはTV）をPiCar-Xに接続するか、 :ref:`remote_desktop` を参照して VNC または XRDP でアクセスできます。
    * Raspberry Piのデスクトップに入ったらターミナルを開き次のコマンドを入力して実行するか、Pythonエディターで開いて実行します。



.. code-block::

    cd /home/pi/picar-x/example
    sudo python3 video_car.py

コードが実行されると、PiCar-X が何を見ているかを確認しながら次のキーを押して運転できます。

* O: スピードアップ
* P: スピードダウン
* W: 前進  
* S: 後退
* A: 左折
* D: 右折
* F: 停止
* T: 静止画の撮影
* ESC / Ctrl+C: 終了

**コード**

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

