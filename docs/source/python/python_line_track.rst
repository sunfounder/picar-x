
ライン追跡
====================================

このプロジェクトでは、グレースケールモジュールを使用してPiCar-Xをラインに沿って前進させます。 
可能な限り直線に暗色のテープを使ってラインを作り、あまり曲げないようにします。
PiCar-Xが脱線する場合、いくつかの実験が必要になるかもしれません。

**コードを実行する**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 minecart_plus.py
    
コードを実行すると、PiCar-Xはラインに沿って前進します。

**コード**

.. note::
    下のコードは **変更/リセット/コピー/実行/停止** ができます。しかし、それをする前に、 ``picar-x/example`` のようなソースコードのパスに移動する必要があります。コードを変更した後、その効果を直接見るために実行することができます。

.. raw:: html

    <run></run>

.. code-block:: python

    from picarx import Picarx


    if __name__=='__main__':
        try:
            px = Picarx()
            # px = Picarx(grayscale_pins=['A0', 'A1', 'A2']) 
            px_power = 10
            while True:
                gm_val_list = px.get_grayscale_data()
                print("gm_val_list:",gm_val_list)
                gm_status = px.get_line_status(gm_val_list)
                print("gm_status:",gm_status)

                if gm_status == 'forward':
                    print(1)
                    px.forward(px_power) 

                elif gm_status == 'left':
                    px.set_dir_servo_angle(12)
                    px.forward(px_power) 

                elif gm_status == 'right':
                    px.set_dir_servo_angle(-12)
                    px.forward(px_power) 
                else:
                    px.set_dir_servo_angle(0)
                    px.stop()
        finally:
            px.stop()

**どのように動作するのか？** 

グレースケールセンサーモジュール ``grayscale_module`` もpicarxモジュールにインポートされており、これらのメソッドの一部を使用して黒いラインを検出することができます。

黒いラインを検出する関数は以下のようになっています：

* ``get_grayscale_data()``：このメソッドは、右から左への三つのセンサーの読み取り値を直接出力します。エリアが明るいほど、取得される値は大きくなります。

* ``get_line_status()``: このメソッドは、三つのプローブで検出された値に基づいてアクションを生成します。アクションには四つのタイプがあります：forward、left、right、およびstop。

これらのアクションのトリガ条件は以下のとおりです：
モジュールには、黒または白を検出するためのしきい値がデフォルトで割り当てられています。
三つのプローブの検出値がすべてしきい値よりも大きい場合、
それはプローブが白色を感知しており、黒いラインが検出されていないことを意味します。
これにより、 ``get_line_status()`` は ``stop`` の戻り値を生成します。

* 右側（そして最初の）プローブが黒いラインを検出すると、 ``right`` が返されます；
* 中央のプローブが黒いラインを検出すると、 ``forward`` が返されます；
* 左のプローブが黒いラインを検出すると、 ``left`` が返されます。
