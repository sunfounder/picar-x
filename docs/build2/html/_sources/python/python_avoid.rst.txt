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
                    px.set_dir_servo_angle(40)
                    px.forward(POWER)
                    time.sleep(0.1)
                else:
                    px.set_dir_servo_angle(-40)
                    px.backward(POWER)
                    time.sleep(0.5)

        finally:
            px.forward(0)


    if __name__ == "__main__":
        main()



**どのように動作するのか？**

picarxモジュールには超音波モジュールもインポートされており、
そのカプセル化された機能のいくつかを使用して距離を検出できます。

.. code-block:: python

    from picarx import Picarx

超音波モジュールがpicarxモジュールにインポートされているため、
``px.ultrasonic.read()`` を直接使用して距離を取得できます。

.. code-block:: python

    px = Picarx()
    px.forward(30)
    while True:
        distance = px.ultrasonic.read() 

以下のコードスニペットは、超音波モジュールによって報告される距離値を読み取り、
距離が40cm以下であればステアリングサーボを0°（直進）から-40°（左に曲がる）に設定します。


.. code-block:: python

    while True:
        distance = px.ultrasonic.read()
        print("distance: ",distance)
        if distance > 0 and distance < 300:
            if distance < 25:
                px.set_dir_servo_angle(-35)
            else:
                px.set_dir_servo_angle(0)
