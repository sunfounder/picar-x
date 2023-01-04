ムーブ（PiCar-Xを動かしてみよう）
==================================

初めてのプロジェクトです。 Picar-Xの基本の動きを試してみましょう。

**コードの実行**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/picar-x/example
    sudo python3 move.py

上記のプログラムを実行すると、PiCar-Xは前に動き出してＳ字カーブを描いて停止し、頭（カメラ）を振ります。

**コード**

.. note::
    以下のコードを **変更/リセット/コピー/実行/停止** することができます。 しかし、その前に ``picar-x/example`` のようなソース コード パスに移動する必要があります。 コードを変更した後、直接実行して効果を確認できます。

.. raw:: html

    <run></run>

.. code-block:: python

    from picarx import Picarx
    import time


    if __name__ == "__main__":
        try:
            px = Picarx()
            px.forward(30)
            time.sleep(0.5)
            for angle in range(0,35):
                px.set_dir_servo_angle(angle)
                time.sleep(0.01)
            for angle in range(35,-35,-1):
                px.set_dir_servo_angle(angle)
                time.sleep(0.01)        
            for angle in range(-35,0):
                px.set_dir_servo_angle(angle)
                time.sleep(0.01)
            px.forward(0)
            time.sleep(1)

            for angle in range(0,35):
                px.set_camera_servo1_angle(angle)
                time.sleep(0.01)
            for angle in range(35,-35,-1):
                px.set_camera_servo1_angle(angle)
                time.sleep(0.01)        
            for angle in range(-35,0):
                px.set_camera_servo1_angle(angle)
                time.sleep(0.01)
            for angle in range(0,35):
                px.set_camera_servo2_angle(angle)
                time.sleep(0.01)
            for angle in range(35,-35,-1):
                px.set_camera_servo2_angle(angle)
                time.sleep(0.01)        
            for angle in range(-35,0):
                px.set_camera_servo2_angle(angle)
                time.sleep(0.01)
                
        finally:
            px.forward(0)

**どんな動きをするの？**

Parker の基本機能は ``picarx`` モジュールにあります。
ステアリングと前後の動きのコントロールに利用できます。
PiCar-X を前進させたり、Ｓ字に曲がったり、頭を振ったりします。

これで、PiCar-X の基本機能をサポートするライブラリがインポートされます。 この行は、PiCar-X の動きのすべての例に表示されます。

.. code-block:: python
    :emphasize-lines: 0

    from picarx import Picarx
    import time

次の関数 for ループを使用して、PiCar-X を前進させ、方向を変え、カメラのパン（水平方向）とチルト（上下方向）を動かします。

.. code-block:: python

    px.forward(speed)    
    px.set_dir_servo_angle(angle)
    px.set_camera_servo1_angle(angle)
    px.set_camera_servo2_angle(angle)

* ``forward()``: PiCar-Xを ``speed`` で指示した速さで前進させます。（０〜１００）
* ``set_dir_servo_angle``:  ``angle`` で指示した角度にハンドルを切ります。（−４５〜４５：それ以下またはそれ以上だとサーボに無理がかかり最悪壊れます）
* ``set_camera_servo1_angle``:  ``angle`` で指定した角度にカメラを水平方向に動かします。（−９０〜９０）
* ``set_camera_servo2_angle``:  ``angle`` で指定した角度にカメラを上下方向に動かします。（−３０〜９０：それ以下だとサーボに無理がかかり最悪壊れます）

.. image:: img/pan_tilt_servo.png
    :width: 400