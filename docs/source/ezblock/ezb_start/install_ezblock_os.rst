.. _install_ezblock_os_latest:

安装 EzBlock OS
===========================

#. 在以下地址下载 **内置 EzBlock 的树莓派操作系统镜像文件**：

 
    * 天翼网盘：链接：https://cloud.189.cn/web/share?code=QRvYJzaeamM3 （访问码：mvb5）
    * 百度网盘：链接：https://pan.baidu.com/s/1ku1VoukCebChq9-OzkHf_g?pwd=ezbl，提取码：ezbl。
    * 由于文件超过1G，需要在电脑上下载客户端之后才能下载文件。


#. 解压下载的文件包后，您将看到其中包含的 ``.img`` 文件。

    .. note::
        不要提取 .img 文件。

#. 下载工具 **Raspberry Pi Imager** ，链接地址：https://www.raspberrypi.org/software/。点击与您的操作系统匹配的下载链接，下载完成后点击启动安装程序。

    .. image:: img/image11.png
        :align: center

#. 启动安装程序时，您的操作系统可能会尝试阻止运行。例如，在 Windows 上可能会弹出以下提示。如果出现，请点击 **更多信息** ，然后点击 **仍要运行** ，并按照提示完成安装。

    .. image:: img/image121.png
        :align: center

#. 将 SD 卡插入电脑或笔记本的 SD 卡插槽。然后打开 Raspberry Pi Imager，点击 **CHOOSE DEVICE** 选择你的设备，然后点击 **选择操作系统** 。

    .. image:: img/choose_os.jpg
        :align: center

#. 滑到页面底部并选择 **Use Custom** 。在弹出的窗口中选择您在 **步骤 1** 中下载的 **RaspiOS-xxx_EzBlockOS-xxx.img** 文件，然后点击 **Open** 。

    .. image:: img/use_custom.jpg
        :align: center

#. 点击 **选择SD卡** ，选择您正在使用的 SD 卡。

    .. image:: img/image14.png
        :align: center

#. 按下 **NEXT** ，点击 **编辑设置** 打开页面，设置主机名、启用 SSH 并设置用户名和密码。您可以选择始终使用此镜像的自定义选项。

    .. .. note::
    ..     主机名用于在 :ref:`web_ezblock` 时通过主机名连接到您的产品。也可以选择不设置。

    .. image:: img/os_enable_ssh.png
        :align: center

#. 向下滚动完成 WiFi 配置，然后点击 **SAVE** 。

    .. note::

        **WiFi 国家** 应设置为使用树莓派所在国家的两字母 `ISO/IEC alpha2 代码 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_。

        此步骤为可选。如果未在此步骤中配置 WiFi，稍后也可以通过应用直接配置。完成后点击 **保存**

    .. image:: img/os_set_wifi.png
        :align: center

#. 点击 **是** 按钮。

    .. image:: img/os_click_yes.png
        :align: center

#. 稍等片刻后，系统将提示镜像已写入您的 Micro SD 卡，您可以移除它。然后将其插入树莓派中。

    .. image:: img/burning2.png
        :align: center
