Linux /Unix ユーザー
==========================

#. **Applications** -> **Utilities** へ移動し、 **Terminal** を探して開きます。

    .. image:: img/image21.png
        :align: center

#. Raspberry Piが同じネットワーク上にあるかどうかを確認するために、 ``ping <hostname>.local`` を入力します。

    .. code-block::

        ping raspberrypi.local

    .. image:: img/mac-ping.png
        :width: 550
        :align: center

    上記の通り、Raspberry Piがネットワークに接続された後のIPアドレスを確認できます。

    * もしターミナルに ``Ping request could not find host pi.local. Please check the name and try again.`` と表示された場合、入力したホスト名が正しいか確認してください。
    * IPアドレスを取得できない場合は、Raspberry PiのネットワークまたはWiFiの設定を確認してください。

#. ``ssh <username>@<hostname>.local`` （もしくは ``ssh <username>@<IP address>`` ）を入力します。

    .. code-block::

        ssh pi@raspberrypi.local

    .. note::

        もし ``The term 'ssh' is not recognized as the name of a cmdlet...`` というメッセージが表示された場合、
        
        あなたのシステムが古く、SSHツールが事前にインストールされていないことを意味します。手動で :ref:`openssh_powershell` をインストールする必要があります。
        
        または、 :ref:`login_windows` のようなサードパーティのツールを使用することもできます。

#. 初めてログインする際、以下のメッセージが表示されるので、 ``yes`` と入力します。

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        This key is not known by any other names
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. 以前に設定したパスワードを入力します。(私の場合は ``raspberry`` です。)

    .. note::
        パスワードを入力する際、文字は画面上には表示されませんが、これは正常です。正しいパスワードを入力するだけで問題ありません。

#. Raspberry Piとの接続が完了したので、次のステップに進む準備ができました。

    .. image:: img/mac-ssh-terminal.png
        :width: 550
        :align: center
