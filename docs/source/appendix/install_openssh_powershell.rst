.. _openssh_powershell:

Powershell経由でOpenSSHをインストールする
---------------------------------------------

``ssh <username>@<hostname>.local`` （または ``ssh <username>@<IP address>`` ）を使用してRaspberry Piに接続しようとすると、次のエラーメッセージが表示される場合があります。

    .. code-block::

        ssh: The term 'ssh' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the
        spelling of the name, or if a path was included, verify that the path is correct and try again.

これは、コンピュータのシステムが古く、 `OpenSSH <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui>`_ がプリインストールされていないことを意味します。以下のチュートリアルに従って手動でインストールする必要があります。

#. Windowsのデスクトップの検索ボックスに ``powershell`` と入力し、 ``Windows PowerShell`` を右クリックして、表示されるメニューから ``管理者として実行`` を選択します。

    .. image:: img/powershell_ssh.png
        :align: center

#. 以下のコマンドを使用して ``OpenSSH.Client`` をインストールします。

    .. code-block::

        Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

#. インストールが完了すると、以下の出力が返されます。

    .. code-block::

        Path          :
        Online        : True
        RestartNeeded : False

#. 以下のコマンドを使用してインストールを確認します。

    .. code-block::

        Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

#. これで ``OpenSSH.Client`` が正常にインストールされたことがわかります。

    .. code-block::

        Name  : OpenSSH.Client~~~~0.0.1.0
        State : Installed

        Name  : OpenSSH.Server~~~~0.0.1.0
        State : NotPresent

    .. warning:: 
        上記のプロンプトが表示されない場合、Windowsのシステムがまだ古いことを意味します。その場合は、 :ref:`login_windows` のようなサードパーティのSSHツールをインストールすることをおすすめします。

#. 今度はPowerShellを再起動し、管理者として実行し続けます。この時点で ``ssh`` コマンドを使用してRaspberry Piにログインすることができます。先に設定したパスワードの入力が求められます。

    .. image:: img/powershell_login.png
