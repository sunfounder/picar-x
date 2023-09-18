Video Car
==========================================

このプログラムでは、PiCar-Xからの第一人称視点が提供されます！キーボードのWSADキーを使用して動きの方向を制御し、OとPキーでスピードを調整してください。

**コードの実行**

.. note::

    * このプロジェクトは、カメラモジュールで撮影した映像を見るためにRaspberry Piのデスクトップへのアクセスが必要です。
    * PiCar-Xにスクリーンを接続するか、 :ref:`remote_desktop` のチュートリアルを参照してVNCやXRDPでアクセスしてください。
    * Raspberry Piのデスクトップに入ったら、ターミナルを開いて以下のコマンドを入力するか、Pythonエディタで開いて実行してください。

.. code-block::

    cd ~/picar-x/example
    sudo python3 video_car.py

コードが実行されると、PiCar-Xが撮影している内容を確認し、以下のキーを押して制御することができます。

* O: スピードアップ
* P: スピードダウン
* W: 前進
* S: 後進
* A: 左へ旋回
* D: 右へ旋回
* F: 停止
* T: 写真を撮る
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
        path = "~/Pictures/picar-x/"
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

