.. _set_up_raspberrypi:

Raspberry Piの設定
============================

モニターに接続できる場合
-------------------------

PC用のモニター画面（あるいはHDMI入力のあるテレビ）があればRaspberry Piの操作は簡単です。

**必要なもの**


* Raspberry Pi 3または4   
* 1 \* 電源アダプター
* 1 \* マイクロSDカード    
* 1 \* モニター用電源アダプター（必要ならば）
* 1 \* HDMIケーブル       
* 1 \* モニター（もしくはTV）
* 1 \* マウス             
* 1 \* キーボード


1. Raspberry Pi OSをインストールしたSDカードを、Raspberry Piの底面にあるマイクロSDカード・スロットに挿入します。

#. マウスとキーボードを接続します。

#. モニターをRaspberry PiのHDMIポートに接続し、モニターの電源が壁のコンセントに差し込まれ電源が入っていることを確認します。

    .. note::

        Raspberry Pi 4を使用する場合はモニターをHDMI0（電源ポートに最も近い方）に接続する必要があります。

#. 電源アダプターを使用してRaspberry Piに電源を供給します。 少し待つとにRaspberry Pi OSデスクトップが表示されます。なおRaspberry piには電源スイッチがありませんので電源アダプターを接続するとそのまま起動します。

    .. image:: img/image20.png
        :align: center

モニターがない場合
--------------------------

モニターがない場合はRaspberry Piにリモートでログインできます。

SSHコマンドを適用してRaspberry PiのBash Shellを開くことができます。BashはLinuxの標準のデフォルト・シェルです。シェル自体はユーザーがUnix/Linuxを利用する際のコマンドラインインタプリタ（CLI）です。シェルを通して必要な作業のほとんどが行えます。

コマンド・ウィンドウを使用してRaspberry Piを利用するすることに満足できない場合はリモートデスクトップ機能を使用してGUIを利用してRaspberry Pi内のファイルを簡単に管理することもできます。

各システムの詳しいチュートリアルは下記をご覧ください。

.. toctree::
    :maxdepth: 1

    remote_macosx
    remote_windows
    remote_linux
