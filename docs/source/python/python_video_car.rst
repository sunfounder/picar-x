.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

.. _video_car:

11. ビデオカー
==========================================

このプログラムはPiCar-Xからの一人称視点を提供します！
キーボードのWSADキーを使用して移動方向を制御し、
OとPで速度を調整します。

**コードの実行**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 11.video_car.py

コードが実行されると、PiCar-Xが撮影しているものを見て、次のキーを押すことで制御できます。

* O: 速度アップ
* P: 速度ダウン
* W: 前進  
* S: 後進
* A: 左折
* D: 右折
* F: 停止
* T: 写真を撮る
* Ctrl+C: 終了

**画像の表示**

コードを実行すると、ターミナルに次のプロンプトが表示されます：

.. code-block::

    No desktop !
    * Serving Flask app "vilib.vilib" (lazy loading)
    * Environment: production
    WARNING: Do not use the development server in a production environment.
    Use a production WSGI server instead.
    * Debug mode: off
    * Running on http://0.0.0.0:9000/ (Press CTRL+C to quit)

次に、ブラウザで ``http://<your IP>:9000/mjpg`` にアクセスして、ビデオ画面を表示できます。例えば： ``https://192.168.18.113:9000/mjpg``

.. image:: img/display.png


**コード**

.. code-block:: python
    
    #!/usr/bin/env python3

    from robot_hat.utils import reset_mcu
    from picarx import Picarx
    from vilib import Vilib
    from time import sleep, time, strftime, localtime
    import readchar

    import os
    user = os.getlogin()
    user_home = os.path.expanduser(f'~{user}')

    reset_mcu()
    sleep(0.2)

    manual = '''
    Press key to call the function(non-case sensitive):

        O: speed up
        P: speed down
        W: forward  
        S: backward
        A: turn left
        D: turn right
        F: stop
        T: take photo

        ctrl + c: Press twice to exit the program
    '''


    px = Picarx()

    def take_photo():
        _time = strftime('%Y-%m-%d-%H-%M-%S',localtime(time()))
        name = 'photo_%s'%_time
        path = f"{user_home}/Pictures/picar-x/"
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
            elif key == readchar.key.CTRL_C:
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


