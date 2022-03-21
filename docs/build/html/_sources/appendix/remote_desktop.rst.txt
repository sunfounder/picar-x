.. _remote_desktop:


远程桌面 
=====================

有两种方法可以远程控制树莓派的桌面。

**VNC** 和 **XRDP** ，你可以使用它们中的任何一种。

VNC 
--------------

你可以通过VNC使用远程桌面的功能。

**启用VNC服务**

系统中已经安装了VNC服务。默认情况下，VNC被禁用。
默认情况下，VNC是禁用的。你需要在配置中启用它。

**第1步**

输入以下命令。

.. raw:: html

    <run></run>

.. code-block:: 

    sudo raspi-config

.. image:: img/image287.png
   :align: center

**第2步**

选择 **3** **Interfacing Option**，按你键盘上的向下箭头键。
键盘上的向下箭头键，然后按 **Enter** 键。

.. image:: img/image282.png
   :align: center

**第3步**

**P3 VNC**

.. image:: img/image288.png
   :align: center

**第4步**

选择 **Yes -> OK -> Finish** 来退出配置。

.. image:: img/image289.png
   :align: center

**登录VNC**

**第1步**

你需要在个人电脑上下载并安装 `VNC Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_。安装完成后，打开它。

**第2步**

然后选择 \"**New connection**\".

.. image:: img/image290.png
   :align: center

**第3步**

输入树莓派的IP地址和任意 **名称**。

.. image:: img/image291.png
   :align: center

**第4步**

双击刚刚创建的 **连接**。

.. image:: img/image292.png
   :align: center

**第5步**

输入用户名（**pi**）和密码（默认为 **raspberry**）。

.. image:: img/image293.png
   :align: center

**第6步**

现在你可以看到树莓派的桌面了。

.. image:: img/image294.png
   :align: center

VNC部分就到此为止了。


XRDP
-----------------------

另一种远程桌面的方法是XRDP，它使用RDP（微软远程桌面协议）提供图形化登录到远程机器。
远程桌面协议）。

**安装XRDP**

**第1步**

通过使用SSH登录到树莓派。

**第2步**

输入以下说明来安装XRDP。

.. raw:: html

    <run></run>

.. code-block:: 

   sudo apt-get update
   sudo apt-get install xrdp

**第3步**

后来，安装开始了。

按 （"Y"），然后按 （"Enter"）来确认。

.. image:: img/image295.png
   :align: center

**第4步**

安装完成后，你应该使用Windows远程桌面应用程序登录到你的树莓派。
使用Windows远程桌面应用程序。

**登录到XRDP**

**第1步**

如果你是一个Windows用户，你可以使用Windows自带的远程桌面功能。
自带的远程桌面功能。如果你是Mac用户，你可以从APP Store下载并使用
微软远程桌面，两者之间没有太大区别。
两者之间没有什么区别。接下来的例子是Windows远程桌面。

**第2步**

在运行（WIN+R）中键入 \"**mstsc**\"，打开远程桌面
连接，并输入树莓派的IP地址，然后点击
\Connect\"。

.. image:: img/image296.png
   :align: center

**第3步**

然后弹出xrdp登录页面。请键入您的用户名和
密码。之后，请点击 "OK"。在你第一次登录的时候。
你的用户名是 "pi\"，密码是 "raspberry\"。

.. image:: img/image297.png
   :align: center

**第4步**

在这里，你通过使用远程桌面成功登录到RPi。

.. image:: img/image20.png
   :align: center


