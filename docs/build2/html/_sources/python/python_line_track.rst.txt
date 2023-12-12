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
    # manual modify reference value
    px.set_line_reference([500, 600, 600])

    current_state = None
    px_power = 10
    offset = 20

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

                if gm_state == "stop":
                    px.stop()
                elif gm_state == 'forward':
                    px.set_dir_servo_angle(0)
                    px.forward(px_power) 
                elif gm_state == 'left':
                    px.set_dir_servo_angle(offset)
                    px.forward(px_power) 
                elif gm_state == 'right':
                    px.set_dir_servo_angle(-offset)
                    px.forward(px_power) 
        finally:
            px.stop()
            print("stop and exit")
            sleep(0.1)


                

**どのように動作するのか？**

picarxモジュールにもグレースケールセンサーモジュール ``grayscale_module`` がインポートされており、これらのメソッドのいくつかを使用して黒い線を検出できます。

黒い線を検出する機能は次のようになります：

* ``get_grayscale_data()``：このメソッドは直接3つのセンサーの読み取り値を出力します。右から左に向かっています。エリアが明るいほど、得られる値が大きくなります。

* ``get_line_status(gm_val_list)``：このメソッドは3つのプローブの読み取り値を比較し、3つのブール値の配列を出力します。1の値は黒が検出されたことを意味し、0の値は白が検出されたことを意味します。

* ``get_status(val_list)``：この関数は3つのプローブによって検出されたブール値に基づいてアクションを生成します。アクションのタイプは4つあります：前進、左、右、停止。

これらのアクションのトリガー条件は次のとおりです：
モジュール内にデフォルトで割り当てられた値が黒または白を検出するための閾値です。
3つのプローブの検出値がすべて閾値より大きい場合、
それはプローブが白い色を感知しており、黒い線が検出されていないことを意味します。
これにより ``get_status()`` は ``stop`` という戻り値を生成します。

* 右（最初の）プローブが黒い線を検出すると、 ``right`` が返されます。
* 中央のプローブが黒い線を検出すると、 ``forward`` が返されます。
* 左のプローブが黒い線を検出すると、 ``left`` が返されます。
* どのプローブも黒い線を検出しない場合は、 ``stop`` が返されます。