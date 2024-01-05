.. _py_treasure:

12. 宝探し
============================

部屋に迷路を用意し、6つの角に6色の異なるカードを配置してください。次に、PiCar-Xをコントロールして、これらの色カードを一つずつ探索しましょう！

.. note:: 色検出用に :download:`PDFカラーカード <https://github.com/sunfounder/sf-pdf/raw/master/prop_card/object_detection/color-cards.pdf>` をダウンロードして印刷することができます。


**コードの実行**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 12.treasure_hunt.py

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

次に、ブラウザで ``http://<your IP>:9000/mjpg`` にアクセスして、ビデオ画面を表示できます。例えば： ``http://192.168.18.113:9000/mjpg``

.. image:: img/display.png

**コード**

.. code-block:: python

    from picarx import Picarx
    from time import sleep
    from robot_hat import Music,TTS
    from vilib import Vilib
    import readchar
    import random
    import threading
    
    px = Picarx()
    
    music = Music()
    tts = TTS()
    
    manual = '''
    Press keys on keyboard to control Picar-X!
        w: Forward
        a: Turn left
        s: Backward
        d: Turn right
        space: Say the target again
        ctrl+c: Quit
    '''
    
    color = "red"
    color_list=["red","orange","yellow","green","blue","purple"]
    
    def renew_color_detect():
        global color
        color = random.choice(color_list)
        Vilib.color_detect(color)
        tts.say("Look for " + color)
    
    key = None
    lock = threading.Lock()
    def key_scan_thread():
        global key
        while True:
            key_temp = readchar.readkey()
            print('\r',end='')
            with lock:
                key = key_temp.lower()
                if key == readchar.key.SPACE:
                    key = 'space'
                elif key == readchar.key.CTRL_C:
                    key = 'quit'
                    break
            sleep(0.01)
    
    def car_move(key):
        if 'w' == key:
            px.set_dir_servo_angle(0)
            px.forward(80)
        elif 's' == key:
            px.set_dir_servo_angle(0)
            px.backward(80)
        elif 'a' == key:
            px.set_dir_servo_angle(-30)
            px.forward(80)
        elif 'd' == key:
            px.set_dir_servo_angle(30)
            px.forward(80)
    
    
    def main():
        global key
        Vilib.camera_start(vflip=False,hflip=False)
        Vilib.display(local=False,web=True)
        sleep(0.8)
        print(manual)
    
        sleep(1)
        _key_t = threading.Thread(target=key_scan_thread)
        _key_t.setDaemon(True)
        _key_t.start()
    
        tts.say("game start")
        sleep(0.05)
        renew_color_detect()
        while True:
    
            if Vilib.detect_obj_parameter['color_n']!=0 and Vilib.detect_obj_parameter['color_w']>100:
                tts.say("will done")
                sleep(0.05)
                renew_color_detect()
    
            with lock:
                if key != None and key in ('wsad'):
                    car_move(key)
                    sleep(0.5)
                    px.stop()
                    key =  None
                elif key == 'space':
                    tts.say("Look for " + color)
                    key =  None
                elif key == 'quit':
                    _key_t.join()
                    print("\n\rQuit")
                    break
    
            sleep(0.05)
    
    if __name__ == "__main__":
        try:
            main()
        except KeyboardInterrupt:
            pass
        except Exception as e:
            print(f"ERROR: {e}")
        finally:
            Vilib.camera_close()
            px.stop()
            sleep(.2)


**どのように動作するのか？**

このコードの基本的なロジックを理解するために、以下の重要な部分に注目してください：

1. **初期化とインポート：**
   コードの最初にあるインポート文で使用されているライブラリを理解します。

2. **グローバル変数：**
   ターゲットの色とキーボード入力を追跡するためにコード全体で使用されるグローバル変数の定義。例えば ``color`` と ``key`` など。

3. ``renew_color_detect()`` :
   この関数はリストからランダムに色を選び、検出のターゲット色として設定します。また、選択された色をテキスト・トゥ・スピーチでアナウンスします。

4. ``key_scan_thread()`` :
   この関数は別のスレッドで実行され、継続的にキーボード入力をスキャンし、押されたキーで ``key`` 変数を更新します。スレッドセーフなアクセスのためにロックを使用します。

5. ``car_move(key)`` :
   この関数はキーボード入力（ ``key`` ）に基づいてPiCar-Xの動きを制御します。ロボットの移動方向と速度を設定します。

6. ``main()`` :コードの全体的なロジックを統合する主要な機能です。以下を行います：

    * カメラを初期化し、カメラフィードを表示します。
    * キーボード入力をスキャンするための別のスレッドを作成します。
    * テキスト・トゥ・スピーチを使用してゲームの開始をアナウンスします。
    * 継続的なループに入ります：

        * 検出された色のオブジェクトをチェックし、有効なオブジェクトが検出された場合にはアクションをトリガーします。
        * キーボード入力を処理して、ロボットを制御し、ゲームと対話します。
    * ゲームの終了と、キーボード割り込みなどの例外を処理します。
    * カメラを閉じ、PiCar-Xを停止することを確認します。

これらのコードの重要な部分を理解することで、PiCar-Xロボットがキーボード入力に応答し、
カメラとオーディオ出力機能を使用して特定の色のオブジェクトを検出し、
それと対話する基本的なロジックを把握できます。
