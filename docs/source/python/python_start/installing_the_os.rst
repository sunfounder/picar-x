安装操作系统
========================

**必需组件**

================== ======================
任意树莓派           1 \* 个人计算机
1 \* 微型 SD 卡
================== ======================

**第1步**

树莓派开发了一个图形 SD 卡写入工具，适用于 Mac OS、Ubuntu 18.04 和 Windows，对于大多数用户来说是最简单的选择，因为它会下载映像并将其自动安装到 SD 卡。

访问下载页面：https://www.raspberrypi.org/software/。 单击与您的操作系统匹配的 Raspberry Pi Imager 链接，下载完成后，单击它以启动安装程序。

.. image:: img/image11.png
    :align: center


**第2步**

当您启动安装程序时，您的操作系统可能会尝试阻止您运行它。 例如，在 Windows 上，我收到以下消息：

如果出现此消息，请点击 **更多信息** ，然后点击 **仍然运行** ，然后按照说明安装 Raspberry Pi Imager。

.. image:: img/image12.png
    :align: center

**第3步**

将 SD 卡插入计算机或笔记本电脑的 SD 卡插槽。

**第4步**

在 Raspberry Pi Imager 中，单击选择 **操作系统** -> **Raspberry Pi OS(Legacy)**。

.. warning::
    * 请不要安装 **Bookworm** 版本，因为扬声器将无法工作。
    * 您需要安装 **Raspberry Pi OS（legacy）** 版本 - **Debian Bullseye**。

.. image:: img/3d33.png
    :align: center



**第5步**

选择您正在使用的 SD 卡。

.. image:: img/image14.png
    :align: center

**第6步**

要打开高级选项页面，请单击设置按钮（选择操作系统后出现）或按Ctrl+Shift+X。

现在，设置主机名，启用 ssh 并设置用户名和密码。

.. warning::

    请务必记下 ``hostname``、 ``username``、 和 ``password``; 它们对于以后远程访问 Raspberry Pi 至关重要。

.. image:: img/image15.png
    :align: center

然后向下滚动以完成 wifi 配置并单击 **SAVE** 。

.. note::

    **wifi country** 选择 **CN**。

.. image:: img/image16.png
    :align: center

**第7步**

单击 **WRITE** 按钮。

.. image:: img/image17.png
    :align: center

**第8步**

如果您的 SD 卡上当前有任何文件，您可能希望先备份这些文件以防止永久丢失它们。 如果没有要备份的文件，请单击 **YES**。

.. image:: img/image18.png
    :align: center

**第9步**

等待一段时间后，会出现如下窗口，代表写入完成。

.. image:: img/image19.png
    :align: center