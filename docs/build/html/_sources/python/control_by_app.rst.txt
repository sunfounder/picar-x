.. _control_by_app:

アプリからのコントロール
==========================

SunFounderコントローラーはRaspberry Pi/Picoベースのロボットを制御するのに使用できます。

APP は、ボタン、スイッチ、ジョイスティック、方向パッド、スライダー、スロットル・スライダー、デジタル表示、超音波センサー、グレースケール・センサー、速度計などの部品を使用できます。 

A ～ Q の 17 のエリアがあり、さまざまな部品を配置して自分専用のコントローラーを作り上げることができます。

さらに、このアプリケーションはビデオのストリーミング表示ができます。

このアプリを使ってPiCar-Xコントローラーをカスタマイズしてみましょう。

**使い方**

#. ``sunfounder-controller`` モジュールをインストールします。

    ``robot-hat``、 ``vilib``、 ``picar-x`` の各モジュールを先にインストールする必要があります。 詳しくは :ref:`install_all_modules` を参照ください。


    .. raw:: html

        <run></run>

    .. code-block::

        $ cd ~
        $ git clone https://github.com/sunfounder/sunfounder-controller.git
        $ cd ~/sunfounder-controller
        $ sudo python3 setup.py install

#. コードの実行

    .. raw:: html

        <run></run>

    .. code-block::

        $ cd ~/sunfounder-controller/examples
        $ sudo python3 picarx_control.py

#. **APP Store(iOS)** または **Google Play(Android)** から `SunFounder Controller <https://docs.sunfounder.com/projects/sf-controller/en/latest/>`_ のアプリをインストールする。


#. アプリを起動して新しいコントローラーを作成します。
    アプリの画面から「＋」をタップして新しいコントローラーを作成します。

    .. image:: img/app1.PNG

    名前を付けてコントローラーの種類を選択します。 一部の製品ではプリセット・セクションにプリセットされたコントローラーがあり必要に応じて使用できます。 以下の手順に従って独自のコントローラーを作成することもできます。
    最後に「Confirm」をタップします。
    
    .. image:: img/app2.PNG

#. コントローラーに部品をセットします。

    このコントローラー内の **A-Q** の17個の小さな領域に好きな種類と形状の部品を追加できます。

    .. image:: img/app3.PNG

    **A** のエリアに **Speedometer** を追加して車の速度を表示します。

    .. image:: img/app4.PNG
    
    .. note::
    
        選択したウィジェットをクリックして削除できます。左にスワイプして **Delete** ボタンを見つけてクリックします。

        .. image:: img/app5.PNG

    右上隅の **Settings** アイコンをクリックして、名前、最大値と最小値、および単位を設定します。

    .. image:: img/app6.PNG

    **D** 領域の **グレースケール検出** ウィジェット用に、現在の環境の ``Line_Ref`` と ``Cliff_Ref`` を設定します。

    .. image:: img/app7.PNG

    最後に、残りのウィジェットを追加し、右上のボタンをクリックして保存します。

    .. image:: img/app8.PNG

#. PiCar-xに接続する。

    **Connect** ボタンをクリックすると、近くにあるロボットを自動的に検索します。 その名前は ``picarx_control.py`` で定義されており、事前に動作（起動）している必要があります。

    .. image:: img/app9.PNG
    
    製品名をクリックすると「Connected Successfully」というメッセージが表示され、製品名が右上隅に表示されます。

    .. image:: img/app10.PNG

    .. note::

        * モバイル デバイスが PiCar-X と同じ LAN に接続されていることを確認する必要があります。
        * 自動的に検索されない場合はIPアドレスを手動で入力して接続することもできます。

        .. image:: img/app11.PNG

#. Run this controller.

    **Run** ボタンをクリックしてコントローラーを起動すると、車のカメラの映像が表示され、これらのウィジェットを使用してPiCar-Xをコントロールできるようになります。

    .. image:: img/app12.PNG
    
    Here are the functions of the widgets.

    * **A**: 車の現在の速度を表示します。
    * **D**: 3つの状態を持つグレースケール・モジュール上の3つのセンサーのデータを表示します。 **black block**: 黒線が検出されました。 **white**: 白が検出されました。 **exclamation point**: 崖が検出されました。
    * **E**: 障害物回避機能をオンにします。
    * **I**: ライン追従機能をオンにします。
    * **J**: 音声認識、このウィジェットを押したままにして話し始め、離すと認識された音声が表示されます。 車を制御するコードには、``forward``、``backard``、``left``、``right`` の4つのコマンドを設定しました。
    * **K**: 車の前後左右の動きを制御します。
    * **Q**: 頭 (カメラ) を上下左右に回します。
    * **N**: 色認識機能をオンにします。
    * **O**: 顔認識機能をオンにします。
    * **P**: オブジェクト認識機能をオンにすると、ほぼ 90 種類のオブジェクトを認識できます。モデルのリストについては https://github.com/sunfounder/vilib/blob/master/workspace/coco_labels.txt を参照してください。


