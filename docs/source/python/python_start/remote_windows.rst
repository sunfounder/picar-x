.. note::

    你好，欢迎来到 SunFounder 树莓派、Arduino 和 ESP32 爱好者社区的 Facebook 页面！与其他爱好者一起深入探讨树莓派、Arduino 和 ESP32。

    **为什么加入？**

    - **专家支持**: 通过我们的社区和团队的帮助解决售后问题和技术挑战。
    - **学习与分享**: 交流技巧和教程，提升你的技能。
    - **独家预览**: 提前了解新产品发布和预告。
    - **特别折扣**: 尊享我们最新产品的专属折扣。
    - **节日促销和赠品**: 参与赠品活动和节日促销。

    👉 准备好与我们一起探索和创造了吗？点击 [|link_sf_facebook|] 加入我们吧！

Windows用户
=======================

远程登录树莓派
-----------------------------

如果你正在使用Windows 10，你可以按照以下方式远程登录树莓派。

#. 在Windows桌面的搜索框中输入 ``powershell``，右键点击 ``Windows PowerShell``，然后从弹出的菜单中选择 ``以管理员身份运行`` 。

    .. image:: img/powershell_ssh.png
        :align: center

#. 接着，输入 ``ping -4 <主机名>.local`` 来查询你的树莓派的IP地址。

    .. code-block::

        ping -4 raspberrypi.local

    .. image:: img/sp221221_145225.png
        :width: 550
        :align: center

    如上图所示，一旦树莓派连接到网络，你就可以看到它的IP地址。

    * 如果终端提示 ``Ping request could not find host pi.local. Please check the name and try again.``，请按照提示确保您输入的主机名是正确的。
    * 如果还是无法获得IP地址，请检查树莓派上的网络或WiFi配置。

#. 此时，你可以使用 ``ssh <用户名>@<主机名>.local``（或 ``ssh <用户名>@<IP地址>``）登录到你的树莓派。

    .. code-block::

        ssh pi@raspberrypi.local

    .. warning::

        如果出现提示 ``The term 'ssh' is not recognized as the name of a cmdlet...``。
        
        这意味着你的系统版本较旧，没有预装ssh工具，你需要手动安装 :ref:`openssh_powershell`。
        
        或者使用第三方工具，例如 :ref:`login_windows`。

#. 当你首次登录时，会显示以下消息，请输入 ``yes``。

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        This key is not known by any other names
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. 输入你之前设置的密码。（我的是 ``raspberry``。）

    .. note::
        当你输入密码时，字符不会在窗口上显示，这是正常的。你只需输入正确的密码即可。

#. 现在，我们已经连接到了树莓派，并准备进行下一步操作。

    .. image:: img/sp221221_140628.png
        :width: 550
        :align: center

.. _remote_desktop:

远程桌面
------------------

如果你对使用命令窗口来访问树莓派不满意，你也可以使用远程桌面功能，用图形界面轻松管理树莓派上的文件。

这里我们使用 `VNC® Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_。

**启用VNC服务**

VNC服务已经安装在系统中。默认情况下，VNC是禁用的。你需要在配置中启用它。

#. 输入以下命令：

    .. raw:: html

        <run></run>

    .. code-block:: 

        sudo raspi-config

    .. image:: img/image287.png
        :align: center

#. 使用键盘上的向下箭头键选择 **Interfacing Options**，然后按 **Enter** 键。

    .. image:: img/image282.png
        :align: center

#. 然后选择 **VNC**。 

    .. image:: img/image288.png
        :align: center

#. 使用键盘上的箭头键选择 **<Yes>** -> **<OK>** -> **<Finish>** 完成设置。

    .. image:: img/mac_vnc8.png
        :align: center

**登录VNC**

#. 你需要在个人电脑上下载并安装 `VNC Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_。

#. 安装完成后，打开它。然后，输入主机名或IP地址并按Enter键。

    .. image:: img/vnc_viewer1.png
        :align: center

#. 在输入你的树莓派名字和密码后，点击 **OK**。

    .. image:: img/vnc_viewer2.png
        :align: center

#. 现在你可以看到树莓派的桌面了。

    .. image:: img/image294.png
        :align: center
