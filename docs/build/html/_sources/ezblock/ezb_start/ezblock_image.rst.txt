
.. _ezb_image:

安装EzBlock镜像
=========================

在组装机器人之前，按照下面的步骤给树莓派的Micro SD卡烧录EzBlock系统。

#. 树莓派开发了一个图形 SD 卡写入工具，适用于 Mac OS、Ubuntu 18.04 和 Windows，对于大多数用户来说是最简单的选择，因为它会下载映像并将其自动安装到 SD 卡。访问下载页面：https://www.raspberrypi.org/software/。 单击与您的操作系统匹配的 Raspberry Pi Imager 链接，下载完成后，单击它以启动安装程序。

    .. image:: img/image11.png
        :align: center



#. 当您启动安装程序时，您的操作系统可能会尝试阻止您运行它。 例如，在 Windows 上，我收到以下消息： 如果出现此消息，请点击 **更多信息** ，然后点击 **仍然运行** ，然后按照说明安装 Raspberry Pi Imager。

    .. image:: img/image12.png
        :align: center

#. 将 SD 卡用读卡器插入计算机或笔记本电脑的 SD 卡插槽。



#. 下载 EzBlock 镜像
 
    * 天翼网盘：链接：https://cloud.189.cn/t/QNrEJnEjYNRz
    * 百度网盘：链接：https://pan.baidu.com/s/1ku1VoukCebChq9-OzkHf_g?pwd=ezbl，提取码：ezbl。
    * 由于文件超过1G，需要在电脑上下载客户端之后才能下载文件。

#. 在 Raspberry Pi Imager 中选择刚下载的 EzBlock 镜像。

    .. image:: img/otherOS.png
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



#. 选择您正在使用的SD卡。

    .. image:: img/image14.png
        :align: center



#. 单击 **WRITE** 按钮。

    .. image:: img/image17.png
        :align: center



#. 如果您的 SD 卡上当前有任何文件，您可能希望先备份这些文件以防止永久丢失它们。 如果没有要备份的文件，请单击 **YES**。

    .. image:: img/image18.png
        :align: center



#. 等待一段时间后，会出现如下窗口，代表写入完成。现在你就可以将读卡器从电脑中拔出，并取出SD卡插入到树莓派上。

    .. image:: img/image19.png
        :align: center