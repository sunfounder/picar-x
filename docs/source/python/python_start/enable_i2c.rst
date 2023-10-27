.. _i2c_config:

启用I2C接口（重要）
========================================

在这里，我们使用的是Raspberry Pi的I2C接口，但默认情况下它们是禁用的，所以我们首先需要启用它们。

#. 输入以下命令：

    .. raw:: html

        <run></run>

    .. code-block:: 

        sudo raspi-config

#. 使用键盘的向下箭头键选择 **Interfacing Options**，然后按**Enter**键。

    .. image:: img/image282.png
        :align: center

#. 接着选择 **I2C**。

    .. image:: img/image283.png
        :align: center

#. 使用键盘上的箭头键选择 **<Yes>** -> **<OK>** 以完成I2C的设置。

    .. image:: img/image284.png
        :align: center

#. 当你选择 **<Finish>** 后，会弹出一个提醒告诉你需要重启以使设置生效，选择**<Yes>**。

    .. image:: img/camera_enable2.png
        :align: center
