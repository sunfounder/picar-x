.. _openssh_powershell:

通过Powershell安装OpenSSH
-----------------------------------

当你使用 ``ssh <用户名>@<主机名>.local``（或 ``ssh <用户名>@<IP地址>``）连接到你的树莓派时，但以下错误信息出现。

    .. code-block::

        ssh: "ssh"不被识别为cmdlet、函数、脚本文件或可运行程序的名称。检查名称的拼写，或者如果包含了路径，请确认路径是否正确，然后再试。

这意味着你的计算机系统太旧，没有预先安装`OpenSSH <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui>`_，你需要按照下面的教程手动安装它。

#. 在你的Windows桌面的搜索框中输入 ``powershell``，右击 ``Windows PowerShell``，然后从出现的菜单中选择 ``以管理员身份运行``。

    .. image:: img/powershell_ssh.png
        :align: center

#. 使用以下命令安装 ``OpenSSH.Client``。

    .. code-block::

        Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

#. 安装后，将返回以下输出。

    .. code-block::

        Path          :
        Online        : True
        RestartNeeded : False

#. 使用以下命令验证安装。

    .. code-block::

        Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

#. 现在它告诉你 ``OpenSSH.Client`` 已成功安装。

    .. code-block::

        Name  : OpenSSH.Client~~~~0.0.1.0
        State : Installed

        Name  : OpenSSH.Server~~~~0.0.1.0
        State : NotPresent

    .. warning:: 
        如果上面的提示没有出现，意味着你的Windows系统仍然太旧，建议你安装第三方SSH工具，如 :ref:`login_windows`。

#. 现在重启PowerShell并继续以管理员身份运行它。此时，你将能够使用 ``ssh`` 命令登录到你的树莓派，在那里你将被提示输入你之前设置的密码。

    .. image:: img/powershell_login.png
