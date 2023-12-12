Windowsユーザー
=======================

リモートでRaspberry Piにログイン
------------------------------------

win10を使用している場合、以下の方法でリモートでRaspberry Piにログインできます。

#. Windowsデスクトップの検索ボックスに ``powershell`` と入力し、 ``Windows PowerShell`` を右クリックして、表示されるメニューから ``Run as administrator`` を選択します。

    .. image:: img/powershell_ssh.png
        :align: center

#. ``ping -4 <hostname>.local`` と入力して、Raspberry PiのIPアドレスを確認します。

    .. code-block::

        ping -4 raspberrypi.local

    .. image:: img/sp221221_145225.png
        :width: 550
        :align: center

    上記のように、ネットワークに接続された後、Raspberry PiのIPアドレスが表示されます。

    * ターミナルが ``Ping request could not find host pi.local. Please check the name and try again.`` と表示された場合は、入力したホスト名が正しいか確認してください。
    * それでもIPを取得できない場合は、Raspberry PiのネットワークまたはWiFi設定を確認してください。


#. これで、 ``ssh <username>@<hostname>.local`` （または ``ssh <username>@<IP address>`` ）を使用してRaspberry Piにログインできます。

    .. code-block::

        ssh pi@raspberrypi.local

    .. warning::

        ``The term 'ssh' is not recognized as the name of a cmdlet...`` というプロンプトが表示された場合、
        
        システムが古く、sshツールがプリインストールされていないことを意味します。手動で :ref:`openssh_powershell` を行う必要があります。
        
        または、:ref:`login_windows` のようなサードパーティツールを使用することもできます。


#. 最初にログインする際にのみ、以下のメッセージが表示されるので、 ``yes`` と入力します。

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        This key is not known by any other names
        Are you sure you want to continue connecting (yes/no/[fingerprint])?


#. 以前に設定したパスワードを入力します（私の場合は ``raspberry`` ）。

    .. note::
        パスワードを入力するとき、ウィンドウ上に文字が表示されないのは正常です。正しいパスワードを入力してください。

#. これでRaspberry Piに接続され、次のステップに進む準備ができました。

    .. image:: img/sp221221_140628.png
        :width: 550
        :align: center

.. _remote_desktop:

リモートデスクトップ
---------------------

コマンドウィンドウを使用してRaspberry Piにアクセスすることに満足していない場合、リモートデスクトップ機能を使用して、GUIを使用してRaspberry Pi上のファイルを簡単に管理することもできます。

ここでは `VNC® Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ を使用します。

**VNCサービスの有効化**

VNCサービスはシステムにインストールされています。デフォルトでは、VNCは無効になっています。configで有効にする必要があります。

#. 次のコマンドを入力します：

    .. raw:: html

        <run></run>

    .. code-block:: 

        sudo raspi-config

    .. image:: img/image287.png
        :align: center

#. キーボードの下矢印キーを押して **3 Interfacing Options** を選択し、 **Enter** キーを押します。

    .. image:: img/image282.png
        :align: center

#. 次に **VNC** を選択します。

    .. image:: img/image288.png
        :align: center

#. キーボードの矢印キーで **<Yes>** -> **<OK>** -> **<Finish>** を選択して、設定を完了します。

    .. image:: img/mac_vnc8.png
        :align: center

**VNCでログイン**

#. 個人用コンピューターに `VNC Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ をダウンロードしてインストールします。

#. インストールが完了したら、開いてホスト名またはIPアドレスを入力してEnterキーを押します。

    .. image:: img/vnc_viewer1.png
        :align: center

#. Raspberry Piの名前とパスワードを入力した後、 **OK** をクリックします。

    .. image:: img/vnc_viewer2.png
        :align: center

#. これでRaspberry Piのデスクトップが表示されます。

    .. image:: img/image294.png
        :align: center

