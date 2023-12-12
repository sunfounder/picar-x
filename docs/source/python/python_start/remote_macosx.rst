
Mac OS Xユーザー
==========================

Macユーザーの場合、コマンドラインからよりもVNCを使って直接Raspberry Piのデスクトップにアクセスする方が便利です。Raspberry Pi側でVNCを有効にした後、Finderを介して設定されたアカウントのパスワードを入力することでアクセスできます。

この方法では、MacとRaspberry Pi間の通信は暗号化されません。 
通信は自宅やビジネスネットワーク内で行われるため、保護されていなくても問題ありません。 
ただし、気になる場合は、 `VNC® Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ などのVNCアプリケーションをインストールすることができます。

一時的にモニター（テレビ）、マウス、キーボードを使用して、直接Raspberry Piのデスクトップを開いてVNCをセットアップできると便利です。 
そうでない場合でも問題ありません。SSHコマンドを使用してRaspberry PiのBashシェルを開き、そのコマンドを使用してVNCを設定することができます。


* :ref:`have_temp_monitor`
* :ref:`no_temp_monitor`


.. _have_temp_monitor:

一時的にモニター（またはテレビ）を使用しますか？
---------------------------------------------------------------------

#. モニター（またはテレビ）、マウス、キーボードをRaspberry Piに接続し、電源を入れます。図の数字に従ってメニューを選択します。


    .. image:: img/mac_vnc1.png
        :align: center

#. 次の画面が表示されます。 **Interfaces** タブで **VNC** を **Enabled** に設定し、 **OK** をクリックします。

    .. image:: img/mac_vnc2.png
        :align: center


#. 画面の右上にVNCアイコンが表示され、VNCサーバーが起動します。

    .. image:: img/mac_vnc3.png
        :align: center


#. **VNC** アイコンをクリックしてVNCサーバーウィンドウを開き、右上隅の **Menu** ボタンをクリックし、 **Options** を選択します。

    .. image:: img/mac_vnc4.png
        :align: center

#. 次の画面が表示され、オプションを変更できます。

    .. image:: img/mac_vnc5.png
        :align: center

    **Encryption** を **Prefer off**、 **Authentication** を **VNC password** に設定します。
    
#. **OK** ボタンをクリックすると、パスワード入力画面が表示されます。Raspberry piのパスワードと同じものを使用することも、異なるパスワードを設定することもできるので、入力して **OK** をクリックします。

    .. image:: img/mac_vnc16.png
        :align: center

    これでMacからの接続が準備完了です。モニターを切断しても構いません。

**ここからはMac側の操作になります。**

#. Finderのメニューから **Connect to Server** を選択します。右クリックで開くことができます。

    .. image:: img/mac_vnc10.png
        :align: center

#. ``vnc://<username>@<hostname>.local``（または ``vnc://<username>@<IP address>`` ）を入力します。入力した後、 **Connect** をクリックします。

        .. image:: img/mac_vnc11.png
            :align: center


#. パスワードの入力を求められるので、入力してください。

        .. image:: img/mac_vnc12.png
            :align: center

#. Raspberry piのデスクトップが表示され、Macからそのまま操作することができます。

        .. image:: img/mac_vnc13.png
            :align: center


.. _no_temp_monitor:

一時的なモニター（またはテレビ）がない場合
---------------------------------------------------------------------------

* SSHコマンドを適用して、Raspberry PiのBashシェルを開くことができます。
* BashはLinuxの標準デフォルトシェルです。
* シェル自体は、ユーザーがUnix/Linuxを使用する際のコマンド（指示）です。
* 必要なことのほとんどはシェルを通じて行うことができます。
* Raspberry Pi側の設定が完了した後、Macの **Finder** からRaspberry Piのデスクトップにアクセスできます。


#. ``ssh <username>@<hostname>.local`` と入力してRaspberry Piに接続します。


    .. code-block::

        ssh pi@raspberrypi.local


    .. image:: img/mac_vnc14.png


#. 最初にログインする際にのみ、以下のメッセージが表示されますので、 **yes** と入力します。

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        This key is not known by any other names
        Are you sure you want to continue connecting (yes/no/[fingerprint])?


#. Raspberry Piのパスワードを入力します。入力されたパスワードは表示されませんので、間違えないよう注意してください。

    .. code-block::

        pi@raspberrypi.local's password: 
        Linux raspberrypi 5.15.61-v8+ #1579 SMP PREEMPT Fri Aug 26 11:16:44 BST 2022 aarch64

        The programs included with the Debian GNU/Linux system are free software;
        the exact distribution terms for each program are described in the
        individual files in /usr/share/doc/*/copyright.

        Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
        permitted by applicable law.
        Last login: Thu Sep 22 12:18:22 2022
        pi@raspberrypi:~ $ 


    

#. Raspberry Piに正常にログインできたら、次にVNC経由でMacからログインできるように設定します。最初のステップとして、以下のコマンドを実行してオペレーティングシステムを更新します。

    .. code-block::

        sudo apt update
        sudo apt upgrade


    ``Do you want to continue? [Y/n]`` と表示されたら、 ``Y`` と入力してください。

    更新には時間がかかることがあります。（その時の更新内容によります。）

#. **VNC Server** を有効にするために、以下のコマンドを入力します。

    .. code-block::

        sudo raspi-config

#. 次の画面が表示されます。キーボードの矢印キーを使って **Interface Options** を選択し、 **Enter** キーを押します。

    .. image:: img/image282.png
        :align: center

#. 次に **VNC** を選択します。

    .. image:: img/image288.png
        :align: center

#. キーボードの矢印キーで **<Yes>** -> **<OK>** -> **<Finish>** を選択して、設定を完了します。

    .. image:: img/mac_vnc8.png
        :align: center


#. VNCサーバーが起動したので、Macから接続するための設定を変更しましょう。

    コンピューター上のすべてのユーザーアカウントのすべてのプログラムのパラメータを指定するには、 ``/etc/vnc/config.d/common.custom`` を作成します。

    .. code-block::

        sudo nano /etc/vnc/config.d/common.custom

    ``Authentication=VncAuthenter`` と入力した後、 ``Ctrl+X`` -> ``Y`` -> ``Enter`` を押して保存して終了します。

    .. image:: img/mac_vnc15.png
        :align: center

#. さらに、MacからVNC経由でログインするためのパスワードを設定します。Raspberry Piのパスワードと同じものを使用することも、異なるパスワードを使用することもできます。


    .. code-block::

        sudo vncpasswd -service


#. 設定が完了したら、Raspberry Piを再起動して変更を適用します。

    .. code-block::

        sudo sudo reboot

#. これで、右クリックで開くことができる **Finder** のメニューから **Connect to Server** を選択します。

    .. image:: img/mac_vnc10.png
        :align: center

#. ``vnc://<username>@<hostname>.local``（または ``vnc://<username>@<IP address>``）を入力します。入力した後、 **Connect** をクリックします。

        .. image:: img/mac_vnc11.png
            :align: center


#. パスワードの入力を求められるので、入力してください。

        .. image:: img/mac_vnc12.png
            :align: center

#. Raspberry Piのデスクトップが表示され、Macからそのまま操作できるようになります。

        .. image:: img/mac_vnc13.png
            :align: center

