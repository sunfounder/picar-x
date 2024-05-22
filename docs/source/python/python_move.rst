.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

.. _py_move:

1. PiCar-Xを動かす
========================

これは最初のプロジェクトです。PiCar-Xの基本的な動きをテストしましょう。

**コードの実行**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 1.move.py

このコードを実行すると、PiCar-Xは前進し、S字型に曲がり、停止して頭を振ります。

**コード**

.. note::
    以下のコードは **変更/リセット/コピー/実行/停止** が可能です。しかし、それをする前に、 ``picar-x/example`` のようなソースコードのパスに移動する必要があります。コードを変更した後、直接実行して効果を確認できます。

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

**それはどのように機能するのですか？**

PiCar-Xの基本機能は、 ``picarx`` モジュールにあります。
これは、ステアリングギアやホイールの制御に使用され、
PiCar-Xを前進させたり、S字型に曲がらせたり、頭を振らせたりすることができます。

現在、PiCar-Xの基本機能をサポートするライブラリがインポートされています。
これらの行は、PiCar-Xの動きを伴うすべての例に表示されます。

.. code-block:: python
    :emphasize-lines: 0

    from picarx import Picarx
    import time

次に、 ``for`` ループを使用する以下の関数は、PiCar-Xを前進させ、
方向を変え、カメラのパン/チルトを動かすために使用されます。

.. code-block:: python

    px.forward(speed)    
    px.set_dir_servo_angle(angle)
    px.set_camera_servo1_angle(angle)
    px.set_camera_servo2_angle(angle)

* ``forward()``：PiCar-Xに指定された ``speed`` で前進するよう命令します。
* ``set_dir_servo_angle``：ステアリングサーボを特定の ``angle`` に回転させます。
* ``set_cam_pan_angle``：パンサーボを特定の ``angle`` に回転させます。
* ``set_cam_tilt_angle``：チルトサーボを特定の ``angle`` に回転させます。

.. image:: img/pan_tilt_servo.png
    :width: 400
