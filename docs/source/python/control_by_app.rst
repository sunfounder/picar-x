.. _control_by_app:

13. アプリによる制御
==================================

SunFounderコントローラーは、Raspberry Pi/Picoベースのロボットを制御するために使用されます。

このアプリには、ボタン、スイッチ、ジョイスティック、Dパッド、スライダー、スロットルスライダーウィジェット、デジタルディスプレイ、超音波レーダー、グレースケール検出、スピードメーター入力ウィジェットが統合されています。

A-Qまでの17エリアがあり、異なるウィジェットを配置して独自のコントローラーをカスタマイズできます。

さらに、このアプリケーションはライブビデオストリーミングサービスも提供しています。

このアプリを使用してPiCar-Xコントローラーをカスタマイズしましょう。

**どうやって？**

#. ``sunfounder-controller`` モジュールをインストールします。

    最初に ``robot-hat``、 ``vilib``、 ``picar-x`` モジュールをインストールする必要があります。詳細は： :ref:`install_all_modules` を参照してください。


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
        sudo python3 13.app_control.py

#. **APP Store(iOS)** または **Google Play(Android)** から `SunFounder Controller <https://docs.sunfounder.com/projects/sf-controller/en/latest/>`_ をインストールします。


#. アプリを開き、新しいコントローラーを作成します。

    SunFounder Controllerアプリ内の+記号をクリックして新しいコントローラーを作成します。

    .. image:: img/app1.PNG

    プリセットセクションには、いくつかの製品に対するプリセットコントローラーがあり、必要に応じて使用できます。ここでは、PiCar-Xを選択します。

    .. image:: img/app_control_preset.jpg


#. PiCar-xに接続する。

    **Connect** ボタンをクリックすると、近くのロボットを自動的に検索します。その名前は ``picarx_control.py`` で定義されており、常に実行されている必要があります。

    .. image:: img/app9.PNG
    
    製品名をクリックすると「接続成功」というメッセージが表示され、製品名が右上に表示されます。

    .. image:: img/app10.PNG

    .. note::

        * モバイルデバイスがPiCar-Xと同じLANに接続されていることを確認する必要があります。
        * 自動検索されない場合は、手動でIPを入力して接続することもできます。

        .. image:: img/app11.PNG

#. このコントローラーを実行する。

    **Run** ボタンをクリックしてコントローラーを起動すると、車が撮影した映像が表示され、これらのウィジェットでPiCar-Xを操作できます。

    .. image:: img/app12.PNG
    
    ウィジェットの機能は次のとおりです。

    * **A**: 車の現在の速度を表示します。
    * **E**: 障害物回避機能をオンにします。
    * **I**: ラインフォロー機能をオンにします。
    * **J**: 音声認識。このウィジェットを押して話し始め、離すと認識された音声が表示されます。 ``forward``、 ``backward``、 ``left``、 ``right`` の4つのコマンドをコードに設定し、車を制御します。
    * **K**: 車の前進、後進、左折、右折を制御します。
    * **Q**: カメラ（頭部）を上下左右に動かします。
    * **N**: 色認識機能をオンにします。
    * **O**: 顔認識機能をオンにします。
    * **P**: 物体認識機能をオンにし、約90種類の物体を認識できます。モデルのリストについては、こちらを参照してください： https://github.com/sunfounder/vilib/blob/master/workspace/coco_labels.txt。

