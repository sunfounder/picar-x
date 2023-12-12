Linux /Unix ユーザー
==========================


#. **Applications** -> **Utilities** に移動し、 **Terminal** を探して開きます。

    .. image:: img/image21.png
        :align: center

#. Raspberry Piが同じネットワーク上にあるかを確認するために、 ``ping <hostname>.local`` と入力します。

    .. code-block::

        ping raspberrypi.local

    .. image:: img/mac-ping.png
        :width: 550
        :align: center

    上記のように、ネットワークに接続された後、Raspberry PiのIPアドレスが表示されます。

    * ターミナルが ``Ping request could not find host pi.local. Please check the name and try again.`` と表示された場合、入力したホスト名が正しいか確認してください。
    * それでもIPを取得できない場合は、Raspberry PiのネットワークまたはWiFi設定を確認してください。


#. ``ssh <username>@<hostname>.local`` （または ``ssh <username>@<IP address>`` ）と入力します。

    .. code-block::

        ssh pi@raspberrypi.local

    .. note::

        ``The term 'ssh' is not recognized as the name of a cmdlet...`` というプロンプトが表示された場合、
        
        システムが古く、sshツールがプリインストールされていないことを意味します。手動で :ref:`openssh_powershell` を行う必要があります。
        
        または、 :ref:`login_windows` のようなサードパーティツールを使用することもできます。


#. 最初にログインする際にのみ、以下のメッセージが表示されるので、 ``yes`` と入力します。

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        This key is not known by any other names
        Are you sure you want to continue connecting (yes/no/[fingerprint])?


#. 以前に設定したパスワードを入力します（私の場合は ``raspberry`` です）。


    .. note::
        パスワードを入力するとき、ウィンドウ上に文字が表示されないのは正常です。正しいパスワードを入力してください。



#. これでRaspberry Piに接続され、次のステップに進む準備ができました。

    .. image:: img/mac-ssh-terminal.png
        :width: 550
        :align: center
