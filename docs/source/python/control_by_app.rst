.. _control_by_app:

アプリによる制御
=======================

SunFounderのコントローラーは、Raspberry Pi/Picoベースのロボットを制御するために使用されます。

このアプリには、ボタン、スイッチ、ジョイスティック、D-pad、スライダー、スロットルスライダーウィジェット、デジタルディスプレイ、超音波レーダー、グレースケール検出、速度計入力ウィジェットが統合されています。

A-Qの17のエリアがあり、異なるウィジェットを配置して独自のコントローラーをカスタマイズできます。

さらに、このアプリはライブビデオストリーミングサービスも提供しています。

このアプリを使用して、PiCar-Xのコントローラーをカスタマイズしてみましょう。

**やり方は？**

#. ``sunfounder-controller`` モジュールをインストールします。

    まず、``robot-hat``, ``vilib``, ``picar-x`` モジュールをインストールする必要があります。詳細は :ref:`install_all_modules` を参照してください。

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~
        git clone https://github.com/sunfounder/sunfounder-controller.git
        cd ~/sunfounder-controller
        sudo python3 setup.py install

#. コードを実行します。

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/picar-x/example
        sudo python3 app_control.py

#. **APP Store(iOS)** または **Google Play(Android)** から `SunFounder Controller <https://docs.sunfounder.com/projects/sf-controller/en/latest/>`_ をインストールします。

#. 新しいコントローラーを開き、作成します。

    SunFounder Controller APPで+記号をクリックして新しいコントローラーを作成します。

    .. image:: img/app1.PNG

    名前を付け、コントローラーのタイプを選択します。Presetセクションには、一部の製品用のプリセットコントローラーがあり、必要に応じて使用できます。以下の手順に従って、独自のコントローラーもカスタマイズできます。

    .. image:: img/app2.PNG

#. このコントローラに異なるウィジェットを追加します。

    このコントローラの中の**A-Q** 17の小エリアに、異なるタイプと形のウィジェットを追加できます。

    .. image:: img/app3.PNG

    **A** エリアに、車の速度を表示するための **Speedometer** ウィジェットを追加します。

    .. image:: img/app4.PNG

    .. note::
    
        選択したウィジェットを削除するには、それをクリックし、左にスワイプして **Delete** ボタンを見つけ、それをクリックします。

        .. image:: img/app5.PNG

    右上の **Settings** アイコンをクリックして、名前、最大値、最小値、単位を設定します。

    .. image:: img/app6.PNG

    **D** エリアの **Grayscale Detection** ウィジェットのために、現在の環境の ``Line_Ref`` および ``Cliff_Ref`` を設定します。

    .. image:: img/app7.PNG

    最後に、残りのウィジェットを追加し、右上のボタンをクリックして保存します。

    .. image:: img/app8.PNG

#. PiCar-xに接続します。

    **Connect** ボタンをクリックすると、近くのロボットが自動的に検索されます。その名前は ``picarx_control.py`` で定義されており、常に実行されている必要があります。

    .. image:: img/app9.PNG

    製品名をクリックすると、「接続に成功しました」というメッセージが表示され、製品名が右上隅に表示されます。

    .. image:: img/app10.PNG

    .. note::

        * PiCar-Xと同じLANにモバイルデバイスが接続されていることを確認する必要があります。
        * 自動的に検索されない場合、IPを手動で入力して接続することもできます。

        .. image:: img/app11.PNG

#. このコントローラを実行します。

    **Run** ボタンをクリックしてコントローラを起動すると、車の撮影映像が表示され、これらのウィジェットでPiCar-Xを制御できるようになります。

    .. image:: img/app12.PNG

    ウィジェットの機能は以下の通りです。

    * **A**: 車の現在の速度を表示します。
    * **D**: グレースケールモジュール上の三つのセンサーのデータを表示します。三つの状態があります： **黒ブロック** : 黒線検出; **白** : 白検出; **感嘆符** : 崖検出。
    * **E**: 障害物回避機能をオンにします。
    * **I**: ライン追従機能をオンにします。
    * **J**: 音声認識、このウィジェットを押して話し始めると、放すと認識した音声を表示します。コードで ``forward`` 、 ``backard`` 、 ``left`` 、 ``right`` の4つのコマンドを設定しています。
    * **K**: 車の前、後ろ、左、右の動きを制御します。
    * **Q**: 頭（カメラ）を上、下、左、右に動かします。
    * **N**: カラー認識機能をオンにします。
    * **O**: 顔認識機能をオンにします。
    * **P**: オブジェクト認識機能をオンにします。それは約90種類のオブジェクトを認識することができます。モデルのリストについては、次のリンクを参照してください：https://github.com/sunfounder/vilib/blob/master/workspace/coco_labels.txt。
