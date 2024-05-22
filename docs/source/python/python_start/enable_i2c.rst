.. note::

    你好，欢迎来到 SunFounder 树莓派、Arduino 和 ESP32 爱好者社区的 Facebook 页面！与其他爱好者一起深入探讨树莓派、Arduino 和 ESP32。

    **为什么加入？**

    - **专家支持**: 通过我们的社区和团队的帮助解决售后问题和技术挑战。
    - **学习与分享**: 交流技巧和教程，提升你的技能。
    - **独家预览**: 提前了解新产品发布和预告。
    - **特别折扣**: 尊享我们最新产品的专属折扣。
    - **节日促销和赠品**: 参与赠品活动和节日促销。

    👉 准备好与我们一起探索和创造了吗？点击 [|link_sf_facebook|] 加入我们吧！

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
