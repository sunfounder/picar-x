
障害物回避
=============================

このプロジェクトでは、PiCar-Xは前進しながら前方の障害物を検出し、障害物が近すぎる場合は前進の方向を変えます。

**コードを実行する**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 avoiding_obstacles.py
    
コードを実行すると、PiCar-Xは前進します。

障害物との距離が25cm未満であることを検出すると、左に曲がります。

左に曲がった後の方向に障害物がないか、または障害物との距離が25cmより大きい場合、前進を続けます。

**コード**

.. note::
    下のコードはv **変更/リセット/コピー/実行/停止** ができます。しかし、それをする前に、 ``picar-x/example`` のようなソースコードのパスに移動する必要があります。コードを変更した後、その効果を直接見るために実行することができます。

.. raw:: html

    <run></run>

.. code-block:: python

    from picarx import Picarx


    def main():
        try:
            px = Picarx()
            # px = Picarx(ultrasonic_pins=['D2','D3']) # tring, echo
            px.forward(30)
            while True:
                distance = px.ultrasonic.read()
                print("distance: ",distance)
                if distance > 0 and distance < 300:
                    if distance < 25:
                        px.set_dir_servo_angle(-35)
                    else:
                        px.set_dir_servo_angle(0)
        finally:
            px.forward(0)


    if __name__ == "__main__":
        main()


**どのように動作するのか？**

超音波モジュールもpicarxモジュールにインポートされており、距離を検出するための一部のカプセル化された関数を使用することができます。

.. code-block:: python

    from picarx import Picarx

超音波モジュールがpicarxモジュールにインポートされているので、 ``px.ultrasonic.read()`` を直接使用して距離を取得することができます。

.. code-block:: python

    px = Picarx()
    px.forward(30)
    while True:
        distance = px.ultrasonic.read() 

以下のコードスニペットは、超音波モジュールによって報告された距離の値を読み取り、距離が25cm（10インチ）未満の場合、操舵サーボを0°（直進）から-35°（左に曲がる）に設定します。

.. code-block:: python

    while True:
        distance = px.ultrasonic.read()
        print("distance: ",distance)
        if distance > 0 and distance < 300:
            if distance < 25:
                px.set_dir_servo_angle(-35)
            else:
                px.set_dir_servo_angle(0)
