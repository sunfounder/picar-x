.. _install_os_sd:

2. 安装操作系统
============================================================

**所需组件**

* 一台个人电脑
* 一张 Micro SD 卡及读卡器

1. 安装 Raspberry Pi Imager
----------------------------------

#. 访问 Raspberry Pi 软件下载页面 `Raspberry Pi Imager <https://www.raspberrypi.org/software/>`_，选择与您的操作系统兼容的 Imager 版本，下载并打开文件以开始安装。

    .. image:: img/os_install_imager.png
        :align: center

#. 安装过程中，可能会出现安全提示，这取决于您的操作系统。例如，在 Windows 上可能会显示警告消息，此时选择 **More info** ，然后点击 **Run anyway** 。按照屏幕提示完成 Raspberry Pi Imager 的安装。

    .. image:: img/os_info.png
        :align: center

#. 安装完成后，点击图标或在终端中输入 ``rpi-imager`` 启动 Raspberry Pi Imager 应用程序。

    .. image:: img/os_open_imager.png
        :align: center

2. 将操作系统安装到 Micro SD 卡
----------------------------------

#. 使用读卡器将 SD 卡插入您的电脑或笔记本。

#. 在 Imager 中点击 **Raspberry Pi Device** ，从下拉列表中选择您的 Raspberry Pi 型号。

    .. image:: img/os_choose_device.jpg
        :align: center

#. 选择 **Operating System** ，并选择推荐的操作系统版本。

    .. image:: img/os_choose_os.png
        :align: center

#. 点击 **Choose Storage** ，选择用于安装的存储设备。

    .. note::

        请确保选择正确的存储设备。为避免混淆，如果连接了多个存储设备，建议断开其他设备。

    .. image:: img/os_choose_sd.png
        :align: center

#. 点击 **NEXT** ，然后点击 **EDIT SETTINGS** 以自定义操作系统设置。

    .. note::

        如果您有 Raspberry Pi 的显示器，可以跳过以下步骤，直接点击“是”开始安装，稍后通过显示器调整其他设置。

    .. image:: img/os_enter_setting.png
        :align: center

#. 设置 Raspberry Pi 的 **主机名** 。

    .. note::

        主机名是 Raspberry Pi 的网络标识符，您可以通过 ``<hostname>.local`` 或 ``<hostname>.lan`` 访问您的设备。

    .. image:: img/os_set_hostname.png
        :align: center

#. 为 Raspberry Pi 的管理员账户创建 **用户名** 和 **密码** 。

    .. note::

        设置唯一的用户名和密码对于保护您的 Raspberry Pi 非常重要，因为默认情况下没有设置密码。

    .. image:: img/os_set_username.png
        :align: center

#. 配置无线局域网（Wi-Fi），输入您的网络 **SSID** 和 **密码** 。

    .. note::

        将 ``Wireless LAN country`` 设置为与您所在位置对应的两字母 `ISO/IEC alpha2 代码 <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_。

    .. image:: img/os_set_wifi.png
        :align: center

#. 如果您需要远程连接到 Raspberry Pi，请在服务选项卡中启用 SSH。

    * 对于 **密码验证**，使用通用选项卡中的用户名和密码。
    * 对于公钥验证，选择“仅允许公钥验证”。如果您已有 RSA 密钥，将使用现有密钥。如果没有，请点击“Run SSH-keygen”生成新的密钥对。

    .. image:: img/os_enable_ssh.png
        :align: center

#. **选项** 菜单允许您配置 Imager 的写入行为，例如完成后播放声音、弹出媒体以及启用遥测功能。

    .. image:: img/os_options.png
        :align: center

#. 输入完操作系统自定义设置后，点击 **保存** 保存您的设置。然后点击 **是** 以在写入镜像时应用这些设置。

    .. image:: img/os_click_yes.png
        :align: center

#. 如果 SD 卡中有现存数据，请确保备份以防数据丢失。如果无需备份，请点击 **是** 继续。

    .. image:: img/os_continue.png
        :align: center

#. 当看到“写入成功”的弹窗时，说明镜像已完全写入并验证完成。现在，您可以通过 Micro SD 卡启动 Raspberry Pi。

    .. image:: img/os_finish.png
        :align: center

#. 现在，将已设置好 Raspberry Pi OS 的 SD 卡插入 Raspberry Pi 底部的 Micro SD 卡槽。

    .. image:: img/os_sd_to_pi.jpg
        :width: 500
        :align: center