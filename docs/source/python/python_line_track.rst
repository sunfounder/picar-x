ライントレース
====================================

このプロジェクトではグレースケール モジュールを使用してPiCar-Xを線に沿って前進させます。
濃い色のテープを使用して、線をできるだけゆるく曲げるようにします。
PiCar-Xが脱線する場合はトライ＆エラーで修正が必要になる場合があります。

**コードの実行**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/picar-x/example
    sudo python3 minecart_plus.py
    
コードを実行するとPiCar-Xはに沿って前進します。

**コード**

.. note::
    以下のコードを **変更/リセット/コピー/実行/停止** することができます。 しかし、その前に ``picar-x/example`` のようなソース コード パスに移動する必要があります。 コードを変更した後、直接実行して効果を確認できます。

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

**どんな動きをするの？** 

グレースケール センサー モジュール ``grayscale_module`` も picarx モジュールにインポートされ、これらのメソッドのいくつかを使用して黒い線を検出できます。

黒い線を検出する関数は次のようになります。

* ``get_grayscale_data()``: このメソッドは、3 つのセンサーの読み取り値を右から左に直接出力します。 明るい領域ほど大きな値が得られます。

* ``get_line_status()``: このメソッドは、3 つのプローブによって検出された値に基づいてアクションを生成します。 アクションには、 forward 、 left 、 right 、および stop の4つのタイプがあります。

これらのアクションのトリガー条件は次のとおりです。 
黒または白を検出するためのしきい値として、値がモジュールにデフォルトで割り当てられます。
3 つのプローブの検出値がすべてしきい値よりも大きい場合、
これはプローブが白色を感知しており黒い線が検出されていないことを意味します。
これは ``get_line_status()`` が ``stop`` の戻り値を生成するようにします。


* 右の (そして最初の) プローブが黒い線を検出した場合は ``right`` が返されます；
* 中央のプローブが黒い線を検出した場合は ``forward`` を返します；
* 左のプローブが黒い線を検出した場合は ``left`` が返されます。
