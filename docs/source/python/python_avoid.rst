.. _py_avoid:

4. 障害物回避
=============================

このプロジェクトでは、PiCar-Xが前進しながら前方の障害物を検出し、
障害物が近すぎる場合には前進の方向を変えます。

**コードの実行**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 4.avoiding_obstacles.py
    
コードを実行すると、PiCar-Xは前進します。

前方の障害物の距離が20cm以下であると検出すると、後退します。

20cmから40cmの範囲内に障害物がある場合は、左に曲がります。

左に曲がった後の方向に障害物がないか、障害物の距離が25cm以上である場合は、
引き続き前進します。

**コード**

.. note::
    以下のコードを **変更/リセット/コピー/実行/停止** することができます。しかし、それをする前に、 ``picar-x/example`` のようなソースコードのパスに移動する必要があります。コードを変更した後、直接実行して効果を確認できます。

.. raw:: html

    <run></run>

.. code-block:: python

    from picarx import Picarx
    import time
    
    POWER = 50
    SafeDistance = 40   # > 40 safe
    DangerDistance = 20 # > 20 && < 40 turn around, 
                        # < 20 backward
    
    def main():
        try:
            px = Picarx()
            # px = Picarx(ultrasonic_pins=['D2','D3']) # tring, echo
           
            while True:
                distance = round(px.ultrasonic.read(), 2)
                print("distance: ",distance)
                if distance >= SafeDistance:
                    px.set_dir_servo_angle(0)
                    px.forward(POWER)
                elif distance >= DangerDistance:
                    px.set_dir_servo_angle(30)
                    px.forward(POWER)
                    time.sleep(0.1)
                else:
                    px.set_dir_servo_angle(-30)
                    px.backward(POWER)
                    time.sleep(0.5)
    
        finally:
            px.forward(0)
    
    
    if __name__ == "__main__":
        main()



**どのように動作するのか？**

* Picarx モジュールのインポートと定数の初期化: 

    このコードのセクションでは、Picarxロボットを制御するために不可欠な ``picarx`` モジュールから ``Picarx`` クラスをインポートします。後でスクリプト内で距離測定に基づいてロボットの動きを制御するために使用される ``POWER`` 、 ``SafeDistance`` 、 ``DangerDistance`` などの定数が定義されています。

    .. code-block:: python

        from picarx import Picarx
        import time

        POWER = 50
        SafeDistance = 40 # > 40 安全
        DangerDistance = 20 # > 20 && < 40 旋回
        # < 20 後退

* メイン関数の定義と超音波センサーの読み取り:

    ``main`` 関数は、Picarxロボットが制御される場所です。 ``Picarx`` のインスタンスが作成され、ロボットの機能が活性化します。コードは無限ループに入り、超音波センサーからの距離を常に読み取ります。この距離はロボットの動きを決定するために使用されます。

    .. code-block:: python
        
        def main():
        try:
            px = Picarx()

            while True:
                distance = round(px.ultrasonic.read(), 2)
                # [残りのロジック]

* 距離に基づく動きのロジック:

    ロボットの動きは、超音波センサーから読み取った ``distance`` に基づいて制御されます。 ``distance`` が ``SafeDistance`` より大きい場合、ロボットは前進します。距離が ``DangerDistance`` と ``SafeDistance`` の間であれば、わずかに旋回して前進します。もし ``distance`` が ``DangerDistance`` 未満であれば、ロボットは逆方向に旋回しながら後退します。

    .. code-block:: python

        if distance >= SafeDistance:
            px.set_dir_servo_angle(0)
            px.forward(POWER)
        elif distance >= DangerDistance:
            px.set_dir_servo_angle(30)
            px.forward(POWER)
            time.sleep(0.1)
        else:
            px.set_dir_servo_angle(-30)
            px.backward(POWER)
            time.sleep(0.5)

* 'finally' ブロックでの安全性とクリーンアップ:

    ``try...finally`` ブロックは、中断またはエラーが発生した場合にロボットの動きを停止させることで安全性を確保します。これは、ロボットの制御不能な振る舞いを防ぐために重要な部分です。

    .. code-block:: python
        
        try:
        # [制御ロジック]
        finally:
            px.forward(0)

* 実行エントリーポイント:

    標準的なPythonエントリーポイント ``if __name__ == "__main__":`` が使用され、スクリプトがスタンドアロンプログラムとして実行されたときにメイン関数を実行します。

    .. code-block:: python
        
        if __name__ == "main":
            main()

要約すると、このスクリプトはPicarxモジュールを使用してロボットを制御し、超音波センサーを利用して距離を測定します。ロボットの動きはこれらの測定値に基づいて適応され、finallyブロック内の安全メカニズムを通じて慎重な制御と安全な操作を保証します。
