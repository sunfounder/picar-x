
.. _remote_desktop:

树莓派远程桌面访问
==================================================

如果你更喜欢使用 **图形界面 (GUI)** 而不是命令行，树莓派同样支持远程桌面功能。  
本指南将带你完成使用 VNC（虚拟网络计算）来实现远程访问的设置和使用。

我们推荐使用 `VNC® Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ 进行远程访问。

**在树莓派上启用 VNC 服务**

Raspberry Pi OS 已预装 VNC 服务，但默认是关闭的。按照以下步骤启用它：

#. 在树莓派终端输入以下命令：

    .. raw:: html

        <run></run>

    .. code-block::

        sudo raspi-config

#. 使用方向键选择 **Interfacing Options**，然后按 **Enter**。

    .. image:: img/config_interface.png
        :align: center

#. 从选项中选择 **VNC**。

    .. image:: img/vnc.png
        :align: center

#. 使用方向键选择 **<Yes>** -> **<OK>** -> **<Finish>**，完成 VNC 服务的启用。

    .. image:: img/vnc_yes.png
        :align: center

**通过 VNC Viewer 登录**

#. 在你的电脑上下载并安装 `VNC Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_。

#. 安装完成后，启动 VNC Viewer，输入树莓派的主机名或 IP 地址，然后按 Enter。

    .. image:: img/vnc_viewer1.png
        :align: center

#. 当系统提示时，输入树莓派的用户名和密码，然后点击 **OK**。

    .. image:: img/vnc_viewer2.png
        :align: center

#. 片刻后，你将看到树莓派的桌面界面。  
   这时你就可以打开终端，开始输入命令了。

    .. image:: img/bookwarm.png
        :align: center
