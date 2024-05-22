.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

.. _py_stare:

8. あなたを見つめる
==========================================

このプロジェクトは、 :ref:`py_computer_vision` プロジェクトに基づいており、
顔検出アルゴリズムが追加されています。

カメラの前に現れると、顔を認識し、ジンバルを調整して顔をフレームの中心に保ちます。

``http://<your IP>:9000/mjpg`` で画面を表示できます。

**コードの実行**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 8.stare_at_you.py

コードが実行されると、車のカメラは常にあなたの顔を見つめ続けます。

**コード**

.. code-block:: python

    from picarx import Picarx
    from time import sleep
    from vilib import Vilib

    px = Picarx()

    def clamp_number(num,a,b):
        return max(min(num, max(a, b)), min(a, b))

    def main():
        Vilib.camera_start()
        Vilib.display()
        Vilib.face_detect_switch(True)
        x_angle =0
        y_angle =0
        while True:
            if Vilib.detect_obj_parameter['human_n']!=0:
                coordinate_x = Vilib.detect_obj_parameter['human_x']
                coordinate_y = Vilib.detect_obj_parameter['human_y']
                
                # change the pan-tilt angle for track the object
                x_angle +=(coordinate_x*10/640)-5
                x_angle = clamp_number(x_angle,-35,35)
                px.set_cam_pan_angle(x_angle)

                y_angle -=(coordinate_y*10/480)-5
                y_angle = clamp_number(y_angle,-35,35)
                px.set_cam_tilt_angle(y_angle)

                sleep(0.05)

            else :
                pass
                sleep(0.05)

    if __name__ == "__main__":
        try:
        main()
        
        finally:
            px.stop()
            print("stop and exit")
            sleep(0.1)

**どのように動作するのか？**

``while True`` の中のこれらのコード行により、カメラが顔を追いかけます。


.. code-block:: python

    while True:
        if Vilib.detect_obj_parameter['human_n']!=0:
            coordinate_x = Vilib.detect_obj_parameter['human_x']
            coordinate_y = Vilib.detect_obj_parameter['human_y']
            
            # change the pan-tilt angle for track the object
            x_angle +=(coordinate_x*10/640)-5
            x_angle = clamp_number(x_angle,-35,35)
            px.set_cam_pan_angle(x_angle)

            y_angle -=(coordinate_y*10/480)-5
            y_angle = clamp_number(y_angle,-35,35)
            px.set_cam_tilt_angle(y_angle)

1. 検出された人間の顔があるかどうかをチェックします

    .. code-block:: python

        Vilib.detect_obj_parameter['human_n'] != 0

2. 人間の顔が検出された場合、検出された顔の座標（ ``coordinate_x`` と ``coordinate_y`` ）を取得します。

3. 検出された顔の位置に基づいて新しいパンとチルト角度（ ``x_angle`` と ``y_angle`` ）を計算し、それらを調整して顔を追いかけます。

4. ``clamp_number`` 関数を使用してパンとチルト角度を指定された範囲内に制限します。

5. ``px.set_cam_pan_angle()`` と ``px.set_cam_tilt_angle()`` を使用してカメラのパンとチルト角度を設定します。
