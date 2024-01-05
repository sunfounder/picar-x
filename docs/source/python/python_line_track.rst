.. _py_line_tracking:

5. ライン追跡
====================================

このプロジェクトではグレースケールモジュールを使用して、PiCar-Xを線に沿って前進させます。
できるだけまっすぐで、あまり曲がっていない暗色のテープを使って線を作ります。
PiCar-Xが脱線した場合は、いくつかの実験が必要になるかもしれません。

**コードの実行**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 5.minecart_plus.py
    
コードを実行すると、PiCar-Xは線に沿って前進します。

**コード**

.. note::
    以下のコードは **変更/リセット/コピー/実行/停止** することができます。しかし、それをする前に、 ``picar-x/example`` のようなソースコードのパスに移動する必要があります。コードを変更した後、直接実行して効果を確認できます。


.. raw:: html

    <run></run>

.. code-block:: python

    from picarx import Picarx
    from time import sleep

    px = Picarx()
    # px = Picarx(grayscale_pins=['A0', 'A1', 'A2'])

    # Please run ./calibration/grayscale_calibration.py to Auto calibrate grayscale values
    # or manual modify reference value by follow code
    # px.set_line_reference([1400, 1400, 1400])

    current_state = None
    px_power = 10
    offset = 20
    last_state = "stop"

    def outHandle():
        global last_state, current_state
        if last_state == 'left':
            px.set_dir_servo_angle(-30)
            px.backward(10)
        elif last_state == 'right':
            px.set_dir_servo_angle(30)
            px.backward(10)
        while True:
            gm_val_list = px.get_grayscale_data()
            gm_state = get_status(gm_val_list)
            print("outHandle gm_val_list: %s, %s"%(gm_val_list, gm_state))
            currentSta = gm_state
            if currentSta != last_state:
                break
        sleep(0.001)

    def get_status(val_list):
        _state = px.get_line_status(val_list)  # [bool, bool, bool], 0 means line, 1 means background
        if _state == [0, 0, 0]:
            return 'stop'
        elif _state[1] == 1:
            return 'forward'
        elif _state[0] == 1:
            return 'right'
        elif _state[2] == 1:
            return 'left'

    if __name__=='__main__':
        try:
            while True:
                gm_val_list = px.get_grayscale_data()
                gm_state = get_status(gm_val_list)
                print("gm_val_list: %s, %s"%(gm_val_list, gm_state))

                if gm_state != "stop":
                    last_state = gm_state

                if gm_state == 'forward':
                    px.set_dir_servo_angle(0)
                    px.forward(px_power) 
                elif gm_state == 'left':
                    px.set_dir_servo_angle(offset)
                    px.forward(px_power) 
                elif gm_state == 'right':
                    px.set_dir_servo_angle(-offset)
                    px.forward(px_power) 
                else:
                    outHandle()
        finally:
            px.stop()
            print("stop and exit")
            sleep(0.1)

                
**どのように動作するのか？**

このPythonスクリプトは、グレースケールセンサーを使用してPicarxロボットカーをナビゲーションします。主なコンポーネントは以下の通りです：

* インポートと初期化：

    このスクリプトは、ロボットカーを制御するための ``Picarx`` クラスと、遅延を追加するためのtimeモジュールの ``sleep`` 関数をインポートします。

    ``Picarx`` のインスタンスが作成され、特定のグレースケールセンサーピンでの代替初期化を示すコメント付きの行があります。

    .. code-block:: python

        from picarx import Picarx
        from time import sleep

        px = Picarx()

* 設定とグローバル変数：

    ``current_state``、 ``px_power``、 ``offset``、 ``last_state`` は、車の動きを追跡および制御するために使用されるグローバル変数です。 ``px_power`` はモーターのパワーを設定し、 ``offset`` はステアリング角度を調整するために使用されます。

    .. code-block:: python

        current_state = None
        px_power = 10
        offset = 20
        last_state = "stop"

* ``outHandle`` 関数：

    この関数は、車が「ラインアウト」のシナリオを処理する必要がある場合に呼び出されます。

    それは ``last_state`` に基づいて車の方向を調整し、新しい状態を決定するためにグレースケールセンサーの値をチェックします。

    .. code-block:: python

        def outHandle():
            global last_state, current_state
            if last_state == 'left':
                px.set_dir_servo_angle(-30)
                px.backward(10)
            elif last_state == 'right':
                px.set_dir_servo_angle(30)
                px.backward(10)
            while True:
                gm_val_list = px.get_grayscale_data()
                gm_state = get_status(gm_val_list)
                print("outHandle gm_val_list: %s, %s"%(gm_val_list, gm_state))
                currentSta = gm_state
                if currentSta != last_state:
                    break
            sleep(0.001)

* ``get_status`` 関数：

    この関数はグレースケールセンサーデータ（ ``val_list`` ）を解釈し、車のナビゲーション状態を決定します。

    車の状態は、どのセンサーがラインを検出するかに基づいて、 ``forward`` 、 ``left`` 、 ``right`` または ``stop`` になります。

    .. code-block:: python

        def get_status(val_list):
            _state = px.get_line_status(val_list)  # [bool, bool, bool], 0はライン、1は背景を意味します
            if _state == [0, 0, 0]:
                return 'stop'
            elif _state[1] == 1:
                return 'forward'
            elif _state[0] == 1:
                return 'right'
            elif _state[2] == 1:
                return 'left'
    
* Main Loop: 

    * ``while True`` ループは継続的にグレースケールデータをチェックし、それに応じて車の動きを調整します。

    * ``gm_state`` に応じて、ステアリング角度と動きの方向を設定します。

    .. code-block:: python

        if __name__=='__main__':
            try:
                while True:
                    gm_val_list = px.get_grayscale_data()
                    gm_state = get_status(gm_val_list)
                    print("gm_val_list: %s, %s"%(gm_val_list, gm_state))

                    if gm_state != "stop":
                        last_state = gm_state

                    if gm_state == 'forward':
                        px.set_dir_servo_angle(0)
                        px.forward(px_power) 
                    elif gm_state == 'left':
                        px.set_dir_servo_angle(offset)
                        px.forward(px_power) 
                    elif gm_state == 'right':
                        px.set_dir_servo_angle(-offset)
                        px.forward(px_power) 
                    else:
                        outHandle()

* 安全性とクリーンアップ：

    ``try...finally`` ブロックは、スクリプトが中断または終了したときに車が停止することを保証します。

    .. code-block:: python

        finally:
        px.stop()
        print("stop and exit")
        sleep(0.1)

要約すると、このスクリプトはグレースケールセンサーを使用してPicarxロボットカーをナビゲートします。センサーデータを継続的に読み取り、方向を決定し、それに応じて車の動きとステアリングを調整します。outHandle関数は、車が大きくパスを調整する必要がある場合の追加ロジックを提供します。