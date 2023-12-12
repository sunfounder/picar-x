歩行者に注意
=============================

このプロジェクトは、PiCar-X が道路状況に基づいて適切な措置を実行するようにします。 走行中に歩行者を検知すると、PiCar-X は完全に停止します。

プログラムが実行されたら、PiCar-X の前に人物の写真をかざします。 ビデオモニターが人物の顔を検出し、PiCar-X が自動的に停止します。

運転安全プロトコルをシミュレートするために、 **[count]** 値を **if do else** ブロックに送信する判断手順が作成されます。 判定手順は人間の顔を 10 回探し、顔が現れた場合は **[count]** を +1 増やします。 **[count]** が 3 より大きい場合、PiCar-X は動きを止めます。

* :ref:`ezblock:remote_control_latest`

.. image:: img/face_detection.PNG


**例：**

.. note::

    * 次の例を参考にしてプログラムを作成してください。またチュートリアルを参照してください。:ref:`ezblock:create_project_latest`
    * またはEzBlock Studioの **Examples** 画面から「 **Beware of Pedestrians** 」を探し **Run** か **Edit** を直接クリックしてください。

.. image:: img/sp210512_185509.png