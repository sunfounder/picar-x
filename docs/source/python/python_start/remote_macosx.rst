Mac OS Xユーザー
==========================

Macのユーザーにとって、Raspberry Piのデスクトップへの直接的なVNCアクセスはコマンドラインからより便利です。Raspberry Pi側でVNCを有効にした後、Finderで指定されたアカウントのパスワードを入力することでアクセスできます。

この方法はMacとRaspberry Piの間の通信を暗号化しません。
通信はあなたの家庭やビジネスネットワーク内で行われるので、保護されていなくても問題になりません。
しかしながら、心配な場合は `VNC® Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ などのVNCアプリケーションをインストールすることができます。

もしあなたが一時的なモニター(TV)、マウス、キーボードを使ってRaspberry Piのデスクトップを直接開くことができると便利です。そうでなければ、SSHコマンドを使用してRaspberry PiのBashシェルを開き、コマンドを使用してVNCを設定することもできます。

* :ref:`have_temp_monitor`
* :ref:`no_temp_monitor`


.. _have_temp_monitor:

一時的なモニター（またはTV）がありますか？
---------------------------------------------------------------------

#. Raspberry Piにモニター（またはTV）、マウス、キーボードを接続し、電源を入れます。図の数字に従ってメニューを選択します。

    .. image:: img/mac_vnc1.png
        :align: center

#. 以下の画面が表示されます。 **Interfaces** タブで **VNC** を **有効** に設定し、 **OK** をクリックします。

    .. image:: img/mac_vnc2.png
        :align: center

#. VNCのアイコンが画面の右上に表示され、VNCサーバが起動します。

    .. image:: img/mac_vnc3.png
        :align: center

#. **VNC** のアイコンをクリックしてVNCサーバのウィンドウを開き、右上の **Menu** ボタンをクリックして **Options** を選択します。

    .. image:: img/mac_vnc4.png
        :align: center

#. 次のような画面が表示され、オプションを変更することができます。

    .. image:: img/mac_vnc5.png
        :align: center

    **Encryption** を **Prefer off** に設定し、 **Authentication** を **VNC password** に設定します。

#. **OK** ボタンをクリックすると、パスワード入力画面が表示されます。Raspberry piのパスワードと同じパスワードを使用するか、異なるパスワードを使用することができますので、入力して **OK** をクリックします。

    .. image:: img/mac_vnc16.png
        :align: center

    これでMacから接続する準備ができました。モニターを切断しても問題ありません。

**ここからは、Mac側での操作となります。**

#. Finderのメニューから **サーバに接続** を選択します。右クリックで開くことができます。

    .. image:: img/mac_vnc10.png
        :align: center

#. ``vnc://<username>@<hostname>.local`` （または ``vnc://<username>@<IPアドレス>`` ）を入力します。入力したら **接続** をクリックします。

        .. image:: img/mac_vnc11.png
            :align: center

#. パスワードを求められるので、入力してください。

        .. image:: img/mac_vnc12.png
            :align: center

#. Raspberry piのデスクトップが表示され、そのままMacから操作することができます。

        .. image:: img/mac_vnc13.png
            :align: center

.. _no_temp_monitor:

一時的なモニターやTVをお持ちでない場合
---------------------------------------------------------------------------

* Raspberry PiのBashシェルを開くためのSSHコマンドを使用できます。
* BashはLinuxのデフォルトのシェルです。
* シェル自体は、ユーザーがUnix/Linuxを使用する際のコマンド（指示）です。
* 必要なことの大半はシェルを通じて実行できます。
* Raspberry Piの設定を終えた後、Macの **Finder** を使用してRaspberry Piのデスクトップにアクセスできます。

#. ``ssh <username>@<hostname>.local`` と入力し、Raspberry Piに接続します。

    .. code-block::

        ssh pi@raspberrypi.local

    .. image:: img/mac_vnc14.png

#. 以下のメッセージは初めてログインする時だけ表示されますので、 **yes** と入力してください。

    .. code-block::

        'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' の信頼性が確認できません。
        ED25519 キーのフィンガープリントはSHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwgです。
        このキーは他の名前で知られていません
        接続を続けますか (yes/no/[fingerprint])?

#. Raspberry piのパスワードを入力してください。入力されるパスワードは表示されませんので、間違いのないように注意してください。

    .. code-block::

        pi@raspberrypi.localのパスワード: 
        Linux raspberrypi 5.15.61-v8+ #1579 SMP PREEMPT Fri Aug 26 11:16:44 BST 2022 aarch64

        Debian GNU/Linuxに含まれるプログラムはフリーソフトウェアです;
        各プログラムの具体的な配布条件は、/usr/share/doc/*/copyrightに記載されています。

        Debian GNU/Linuxには、法的に許容される範囲で何ら保証がありません。
        最後のログイン: Thu Sep 22 12:18:22 2022
        pi@raspberrypi:~ $ 

#. MacからVNCでログインできるようにRaspberry Piを設定します。最初のステップとして、以下のコマンドを実行してOSをアップデートします。

    .. code-block::

        sudo apt update
        sudo apt upgrade

    ``続行しますか？ [Y/n]`` と表示されたら、 ``Y`` を入力してください。

    アップデートの完了には時間がかかることがあります。（その時のアップデート量による。）

#. **VNCサーバー** を有効にするための次のコマンドを入力してください。

    .. code-block::

        sudo raspi-config

#. 以下の画面が表示されます。キーボードの矢印キーで **Interface Options** を選択し、 **Enter** キーを押します。

    .. image:: img/image282.png
        :align: center

#. 次に **VNC** を選択します。

    .. image:: img/image288.png
        :align: center

#. キーボードの矢印キーで **<はい>** -> **<OK>** -> **<終了>** を選択し、設定を完了させます。

    .. image:: img/mac_vnc8.png
        :align: center

#. VNCサーバーが起動したので、Macからの接続設定を変更しましょう。

    全てのユーザーアカウントの全てのプログラムのパラメータを指定するために、 ``/etc/vnc/config.d/common.custom`` を作成します。

    .. code-block::

        sudo nano /etc/vnc/config.d/common.custom

    ``Authentication=VncAuthenter`` と入力した後、 ``Ctrl+X`` -> ``Y`` -> ``Enter`` で保存して終了します。

    .. image:: img/mac_vnc15.png
        :align: center

#. さらに、MacからVNCでログインする際のパスワードを設定します。Raspberry piのパスワードと同じもの、もしくは異なるものを使用してもよいです。

    .. code-block::

        sudo vncpasswd -service

#. 設定が完了したら、変更を適用するためにRaspberry Piを再起動します。

    .. code-block::

        sudo sudo reboot

#. 今度は、 **Finder** のメニューから **サーバーに接続** を選択します。右クリックで開くことができます。

    .. image:: img/mac_vnc10.png
        :align: center

#. ``vnc://<username>@<hostname>.local``（または ``vnc://<username>@<IPアドレス>`` ）と入力し、 **接続** をクリックします。

        .. image:: img/mac_vnc11.png
            :align: center

#. パスワードが求められるので、入力してください。

        .. image:: img/mac_vnc12.png
            :align: center

#. Raspberry piのデスクトップが表示され、そのままMacから操作できるようになります。

        .. image:: img/mac_vnc13.png
            :align: center
