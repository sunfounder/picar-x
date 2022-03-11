EzBlock 快速指南
============================

这里有两个部分：

* :ref:`组装帕克之前` 允许您将所有舵机保持在 0 度以完成正确和安全的装配（否则您可能会损坏舵机）。
* :ref:`EzBlock 编程前` 将指导您下载 EzBlock Studio 与您的机器人一起玩。

组装帕克之前
--------------------------------

在组装帕克之前，请按照此处有关如何在 Micro SD 卡上安装 EzBlock 的说明进行操作： 

.. `下载并安装 EzBlock <https://docs.sunfounder.com/projects/ezblock3/en/latest/quick_user_guide_for_ezblock3 .html#download-and-install-ezblock-os>`_.

**安装Ezblock系统**

#. 树莓派开发了一个图形 SD 卡写入工具，适用于 Mac OS、Ubuntu 18.04 和 Windows，对于大多数用户来说是最简单的选择，因为它会下载映像并将其自动安装到 SD 卡。访问下载页面：https://www.raspberrypi.org/software/。 单击与您的操作系统匹配的 Raspberry Pi Imager 链接，下载完成后，单击它以启动安装程序。

    .. image:: preparation/media/image11.png
        :align: center



#. 当您启动安装程序时，您的操作系统可能会尝试阻止您运行它。 例如，在 Windows 上，我收到以下消息： 如果出现此消息，请点击 **更多信息** ，然后点击 **仍然运行** ，然后按照说明安装 Raspberry Pi Imager。

    .. image:: preparation/media/image12.png
        :align: center

#. 将 SD 卡插入计算机或笔记本电脑的 SD 卡插槽。



#. 下载 EzBlock 镜像
 
  * 天翼网盘：链接：https://cloud.189.cn/t/QNrEJnEjYNRz
  * 百度网盘：链接：https://pan.baidu.com/s/1ku1VoukCebChq9-OzkHf_g?pwd=ezbl，提取码：ezbl。
  * 由于文件超过1G，需要在电脑上下载客户端之后才能下载文件。

#. 在 Raspberry Pi Imager 中选择刚下载的 EzBlock 镜像。

    .. image:: preparation/media/otherOS.png
        :align: center


#. 按下 **Ctrl+Shift+X** 或者点击 **设置** 按钮来打开 **Advanced options** 页面来设置 ``hostname`` 和启动 ``SSH``。你可以选择 “always use this image customization options”（始终使用该定制选项）。

    .. note::

        ``hostname`` 是让你在使用 :ref:`web_ezblock`, 可以用它来连接到你的产品，你也可以不设置。

    .. image:: img/configure.png
        :align: center

#. 下拉到底完成 WiFi配置，然后点击 **SAVE**。

    .. note::

        **wifi country** 选择 **CN**
    .. image:: img/image16.png
        :align: center



#. 选择您正在使用的 SD 卡。

    .. image:: preparation/media/image14.png
        :align: center



#. 单击 **WRITE** 按钮。

.. image:: preparation/media/image17.png
    :align: center



#. 如果您的 SD 卡上当前有任何文件，您可能希望先备份这些文件以防止永久丢失它们。 如果没有要备份的文件，请单击 **YES**。

    .. image:: preparation/media/image18.png
        :align: center



#. 等待一段时间后，会出现如下窗口，代表写入完成。

    .. image:: preparation/media/image19.png
        :align: center


**舵机调零**

在Micro SD卡上烧录EzBlock镜像后，你将可以设置Robot HAT上的P11口将舵机角度校准为0°角。 为确保舵机已正确设置为 0°，首先将摇臂轻轻插入舵机轴，然后将摇臂轻轻旋转到不同的角度。

.. image:: img/servo_arm.png

接下来，将伺服电缆插入 P11 端口，如下所示：

.. image:: img/pin11_connect.png
    :width: 600

打开Robot HAT的 **电源开关**，舵机臂应回到0°位置。 如果伺服臂没有返回到 0°，请按 **RST** 按钮重新启动Robot HAT。

.. note::
    在连接每个舵机之前，将舵机电缆插入 P11 并打开电源，将舵机设置为 0°。
    向 Micro SD 卡写入任何程序后，此功能将失效。




EzBlock 编程前
---------------------


扫描下方二维码，下载 EzBlock Studio APP。

.. image:: img/Ezblock_Studio_v3.0.1_App.png
    :align: center


或者使用 :ref:`web_ezblock`