障害物回避
=============================

このプロジェクトでは、PiCar-X は前進しながら前方の障害物を検出し、障害物が近すぎると前進方向を変更します。

**コードの実行**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/picar-x/example
    sudo python3 avoiding_obstacles.py
    
コードを実行するとPiCar-Xは前進します。

前方の障害物との距離が25cm以内になったことを感知すると左折します。

左折後の方向に障害物がない場合、または障害物との距離が25cm以上の場合に直進します。

**コード**

.. note::
    以下のコードを **変更/リセット/コピー/実行/停止** することができます。 しかし、その前に ``picar-x/example`` のようなソース コード パスに移動する必要があります。 コードを変更した後、直接実行して効果を確認できます。

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


**どんな動きをするの？**

超音波モジュールもpicarxに内蔵されており、カプセル化された関数の一部を使用して距離を検出できます。

.. code-block:: python

    from picarx import Picarx

超音波モジュールはpicarxモジュールにインポートされるため、直接 ``px.ultrasonic.read()`` を使用して距離を取得できます。

.. code-block:: python

    px = Picarx()
    px.forward(30)
    while True:
        distance = px.ultrasonic.read() 

次のコードは超音波モジュールによって報告された距離値を読み取り、距離が25cm未満の場合、ステアリング サーボを 0° (直進) から -35° (左折) に設定します。

.. code-block:: python

    while True:
        distance = px.ultrasonic.read()
        print("distance: ",distance)
        if distance > 0 and distance < 300:
            if distance < 25:
                px.set_dir_servo_angle(-35)
            else:
                px.set_dir_servo_angle(0)
