Windowsユーザー
=======================

Raspberry Piへのリモートログイン
-------------------------------------------------

Windows10を使用している場合、以下の方法でRaspberry Piにリモートログインすることができます。

#. Windowsのデスクトップの検索ボックスに ``powershell`` と入力し、表示される ``Windows PowerShell`` を右クリックして、メニューから ``管理者として実行`` を選択します。

    .. image:: img/powershell_ssh.png
        :align: center

#. 次に、 ``ping -4 <hostname>.local`` と入力して、Raspberry PiのIPアドレスを確認します。

    .. code-block::

        ping -4 raspberrypi.local

    .. image:: img/sp221221_145225.png
        :width: 550
        :align: center

    上記のように、Raspberry Piがネットワークに接続された後のIPアドレスを確認できます。

    * もし、ターミナルに ``Ping request could not find host pi.local. Please check the name and try again.`` と表示された場合は、ホスト名が正しいか確認してください。
    * IPアドレスが取得できない場合は、Raspberry PiのネットワークまたはWiFiの設定を確認してください。

#. この時点で、 ``ssh <username>@<hostname>.local`` （または ``ssh <username>@<IP address>`` ）を使用して、Raspberry Piにログインできるようになります。

    .. code-block::

        ssh pi@raspberrypi.local

    .. warning::

        ``The term 'ssh' is not recognized as the name of a cmdlet...`` というプロンプトが表示された場合、
        
        システムが古く、SSHツールが事前にインストールされていないことを意味します。手動で :ref:`openssh_powershell` をインストールする必要があります。
        
        または、 :ref:`login_windows` のようなサードパーティツールを使用することができます。

#. 初めてログインする際には以下のメッセージが表示されるので、 ``yes`` と入力します。

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        This key is not known by any other names
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. 以前設定したパスワードを入力します。(私の場合は ``raspberry`` です。)

    .. note::
        パスワードを入力する際、文字はウィンドウ上に表示されませんが、これは正常です。
        正しいパスワードを入力するだけで大丈夫です。

#. Raspberry Piに接続が完了したので、次のステップに進む準備ができました。

    .. image:: img/sp221221_140628.png
        :width: 550
        :align: center

リモートデスクトップ
-------------------------------------------

コマンドウィンドウを使用してRaspberry Piにアクセスするだけでは満足できない場合、リモートデスクトップ機能を使用して、GUIを使用してRaspberry Pi上のファイルを簡単に管理することができます。

ここでは、 `VNC® Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ を使用します。

**VNCサービスの有効化**

VNCサービスはシステムにインストールされています。デフォルトではVNCは無効になっています。それを設定で有効にする必要があります。

#. 以下のコマンドを入力します:

    .. raw:: html

        <run></run>

    .. code-block:: 

        sudo raspi-config

    .. image:: img/image287.png
        :align: center

#. キーボードの矢印キーを使用して **3 Interfacing Options** を選択し、 **Enter** キーを押します。

    .. image:: img/image282.png
        :align: center

#. 次に、 **P3 VNC** を選択します。

    .. image:: img/image288.png
        :align: center

#. キーボードの矢印キーを使用して、 **<Yes>** -> **<OK>** -> **<Finish>** を選択し、設定を完了します。

    .. image:: img/mac_vnc8.png
        :align: center

**VNCへのログイン**

#. まず、個人のコンピューターに `VNC Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ をダウンロードしてインストールする必要があります。

#. インストールが完了したら、ホスト名またはIPアドレスを入力してEnterキーを押します。

    .. image:: img/vnc_viewer1.png
        :align: center

#. Raspberry Piの名前とパスワードを入力した後、 **OK** をクリックします。

    .. image:: img/vnc_viewer2.png
        :align: center

#. Raspberry Piのデスクトップが表示されます。

    .. image:: img/image294.png
        :align: center
