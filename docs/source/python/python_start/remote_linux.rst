Linux /Unix 用户
==========================

#. 跳转到 **应用程序**->\ **实用工具**，找到 **终端**，然后打开它。

    .. image:: img/image21.png
        :align: center

#. 通过输入 ``ping <主机名>.local`` 来检查你的Raspberry Pi是否在同一网络中。

    .. code-block::

        ping raspberrypi.local

    .. image:: img/mac-ping.png
        :width: 550
        :align: center

    如上图所示，当Raspberry Pi连接到网络后，你可以看到它的IP地址。

    * 如果终端提示 ``Ping request could not find host pi.local. Please check the name and try again.``，请按照提示确保你输入的主机名是正确的。
    * 仍然无法获得IP？请检查Raspberry Pi上的网络或WiFi配置。

#. 输入 ``ssh <用户名>@<主机名>.local`` (或 ``ssh <用户名>@<IP地址>``)。

    .. code-block::

        ssh pi@raspberrypi.local

    .. note::

        如果出现提示 ``The term 'ssh' is not recognized as the name of a cmdlet...``。
        
        这意味着你的系统太旧，没有预装ssh工具，你需要手动 :ref:`openssh_powershell`。
        
        或使用第三方工具如 :ref:`login_windows`。

#. 下面的信息只会在你第一次登录时显示，所以输入 ``yes``。

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        This key is not known by any other names
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. 输入你之前设置的密码。（我的是 ``raspberry``。）

    .. note::
        当你输入密码时，字符不会在窗口中显示，这是正常的。你需要做的是输入正确的密码。

#. 我们现在已经连接上Raspberry Pi，可以进入下一步了。

    .. image:: img/mac-ssh-terminal.png
        :width: 550
        :align: center
