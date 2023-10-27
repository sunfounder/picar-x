Mac OS X 用户
==========================

对于Mac用户，通过VNC直接访问Raspberry Pi桌面比从命令行更方便。通过在Raspberry Pi端启用VNC后，可以通过Finder输入设置的账户密码来访问它。

请注意，此方法不会加密Mac与Raspberry Pi之间的通信。通信将在您的家庭或商业网络内进行，所以即使它是不受保护的，也不会有问题。但是，如果你担心这个问题，你可以安装像 `VNC® Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ 这样的VNC应用程序。

另外，如果您可以使用临时的显示器（电视）、鼠标和键盘直接打开Raspberry Pi桌面以设置VNC，那将非常方便。如果没有，也没关系，您也可以使用SSH命令打开Raspberry Pi的Bash shell，然后使用命令设置VNC。

* :ref:`have_temp_monitor`
* :ref:`no_temp_monitor`


.. _have_temp_monitor:

有临时显示器（或电视）吗？
---------------------------------------------------------------------

#. 将显示器（或电视）、鼠标和键盘连接到Raspberry Pi并开机。根据图中的数字选择菜单。

    .. image:: img/mac_vnc1.png
        :align: center

#. 将显示以下屏幕。在 **Interfaces** 选项卡上将 **VNC** 设置为 **Enabled**，然后点击 **OK**。

    .. image:: img/mac_vnc2.png
        :align: center

#. VNC图标出现在屏幕的右上方，VNC服务器启动。

    .. image:: img/mac_vnc3.png
        :align: center

#. 通过点击 **VNC** 图标打开VNC服务器窗口，然后点击右上角的 **Menu** 按钮并选择 **Options**。

    .. image:: img/mac_vnc4.png
        :align: center

#. 您将看到以下屏幕，您可以在此更改选项。

    .. image:: img/mac_vnc5.png
        :align: center

    将 **Encryption** 设置为 **Prefer off**，将 **Authentication** 设置为 **VNC password**。

#. 当您点击 **OK** 按钮时，会显示密码输入屏幕。您可以使用与Raspberry pi密码相同的密码或不同的密码，输入后点击 **OK**。

    .. image:: img/mac_vnc16.png
        :align: center

    您现在可以从Mac连接了。可以断开显示器了。

**从这里开始，将在Mac端操作。**

#. 现在，在Finder的菜单中选择 **Connect to Server**，可以通过右键单击打开。

    .. image:: img/mac_vnc10.png
        :align: center

#. 输入 ``vnc://<用户名>@<主机名>.local`` （或 ``vnc://<用户名>@<IP地址>``）。输入后，点击**Connect**。

        .. image:: img/mac_vnc11.png
            :align: center

#. 会要求您输入密码，请输入。

        .. image:: img/mac_vnc12.png
            :align: center

#. Raspberry pi的桌面将被显示，您将能够从Mac上操作它。

        .. image:: img/mac_vnc13.png
            :align: center

.. _no_temp_monitor:

没有临时显示器（或电视）吗？
---------------------------------------------------------------------------

* 您可以应用SSH命令打开Raspberry Pi的Bash shell。
* Bash是Linux的标准默认shell。
* shell本身是用户使用Unix/Linux时的命令（指令）。
* 您需要做的大部分操作都可以通过shell完成。
* 设置了Raspberry pi端后，您可以从Mac的 **Finder** 访问Raspberry Pi的桌面。

#. 输入 ``ssh <用户名>@<主机名>.local`` 连接到Raspberry Pi。

    .. code-block::

        ssh pi@raspberrypi.local

    .. image:: img/mac_vnc14.png

#. 下面的信息只会在你第一次登录时显示，所以输入 **yes**。

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        This key is not known by any other names
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. 输入Raspberry pi的密码。您输入的密码不会显示，所以请注意不要出错。

    .. code-block::

        pi@raspberrypi.local's password: 
        Linux raspberrypi 5.15.61-v8+ #1579 SMP PREEMPT Fri Aug 26 11:16:44 BST 2022 aarch64

        The programs included with the Debian GNU/Linux system are free software;
        the exact distribution terms for each program are described in the
        individual files in /usr/share/doc/*/copyright.

        Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
        permitted by applicable law.
        Last login: Thu Sep 22 12:18:22 2022
        pi@raspberrypi:~ $ 

#. 一旦成功登录，设置Raspberry Pi以便您可以从Mac通过VNC登录。首先更新您的操作系统，运行以下命令。

    .. code-block::

        sudo apt update
        sudo apt upgrade

    当提示 ``Do you want to continue? [Y/n]`` 时，输入 ``Y``。

    更新可能需要一段时间才能完成。（这取决于那时的更新量。）

#. 输入以下命令以启用 **VNC服务器**。

    .. code-block::

        sudo raspi-config

#. 将显示以下屏幕。使用键盘上的箭头键选择 **3 Interface Options**，然后按 **Enter** 键。

    .. image:: img/image282.png
        :align: center

#. 然后选择 **VNC**。

    .. image:: img/image288.png
        :align: center

#. 使用键盘上的箭头键选择 **<Yes>** -> **<OK>** -> **<Finish>** 完成设置。

    .. image:: img/mac_vnc8.png
        :align: center

#. 现在VNC服务器已经启动，让我们更改从Mac连接的设置。

    要为计算机上的所有用户账户的所有程序指定参数，请创建 ``/etc/vnc/config.d/common.custom``。

    .. code-block::

        sudo nano /etc/vnc/config.d/common.custom

    输入 ``Authentication=VncAuthenter`` 后，按 ``Ctrl+X`` -> ``Y`` -> ``Enter`` 保存并退出。

    .. image:: img/mac_vnc15.png
        :align: center

#. 此外，设置一个密码以便从Mac通过VNC登录。您可以使用与Raspberry pi密码相同的密码或不同的密码。

    .. code-block::

        sudo vncpasswd -service

#. 一旦设置完成，重新启动Raspberry Pi应用更改。

    .. code-block::

        sudo sudo reboot

#. 现在，在Finder的菜单中选择 **Connect to Server**，可以通过右键单击打开。

    .. image:: img/mac_vnc10.png
        :align: center

#. 输入 ``vnc://<用户名>@<主机名>.local`` （或 ``vnc://<用户名>@<IP地址>``）。输入后，点击 **Connect**。

        .. image:: img/mac_vnc11.png
            :align: center

#. 会要求您输入密码，请输入。

        .. image:: img/mac_vnc12.png
            :align: center

#. Raspberry pi的桌面将被显示，您将能够从Mac上操作它。

        .. image:: img/mac_vnc13.png
            :align: center
