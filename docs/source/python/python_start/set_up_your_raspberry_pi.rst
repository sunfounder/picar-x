.. _set_up_raspberrypi:

Raspberry Piのセットアップ
============================

Raspberry Piの電源供給（重要）
-------------------------------

#. Raspberry Pi OSでセットアップしたSDカードをRaspberry Piの下側にあるマイクロSDカードスロットに挿入します。

    .. image:: img/insert_sd_card.png
        :width: 500
        :align: center

#. 組み立て指示書に従って、バッテリーケーブルを挿入し、電源スイッチをONにします。次に、USB-Cケーブルを挿入してバッテリーを起動します。1-2分待つと、Raspberry Piが正常に起動したことを示す音がします。

    .. image:: img/Z_BTR.JPG
        :width: 800
        :align: center

    .. note::

        USB-Cケーブルを差し込んだままにしておくことをお勧めします。後続のソフトウェア設定プロセスはかなり長いためです。


画面がある場合
-------------------------

.. note:: ロボットにインストールされているRaspberry Pi ZEROは画面に接続するのが簡単ではありません。画面を使用せずにセットアップする方法を使用してください。

画面がある場合、Raspberry Piでの操作が簡単になります。

**必要な部品**

* 任意のRaspberry Pi   
* 1 * 電源アダプター
* 1 * マイクロSDカード
* 1 * 画面用の電源アダプター
* 1 * HDMIケーブル
* 1 * 画面
* 1 * マウス
* 1 * キーボード


#. マウスとキーボードを接続します。

#. Raspberry PiのHDMIポートに画面を接続し、画面が壁のコンセントに接続され、オンになっていることを確認します。

    .. note::

        Raspberry Pi 4を使用する場合、画面をHDMI0（電源入力ポートに最も近い）に接続する必要があります。

#. 電源アダプターを使用してRaspberry Piに電源を供給します。数秒後、Raspberry Pi OSのデスクトップが表示されます。

    .. image:: img/image20.png
        :align: center

画面がない場合
--------------------------

モニターがない場合は、リモートでRaspberry Piにログインできます。

**必要なコンポーネント**

* * Raspberry Pi 4B/Zero 2 w/3B 3B+/2B/Zero W  
* 1 * 電源アダプタ
* 1 * マイクロSDカード

SSHコマンドを使用してRaspberry PiのBashシェルを開くことができます。BashはLinuxの標準デフォルトシェルです。シェル自体は、ユーザーがUnix/Linuxを使用する際のコマンド（指示）です。必要なことのほとんどはシェルを通じて行うことができます。

コマンドウィンドウを使用してRaspberry Piにアクセスすることに満足していない場合は、リモートデスクトップ機能を使用して、GUIを使用してRaspberry Pi上のファイルを簡単に管理することもできます。

各システムの詳細なチュートリアルについては以下を参照してください。



.. toctree::

    remote_macosx
    remote_windows
    remote_linux

