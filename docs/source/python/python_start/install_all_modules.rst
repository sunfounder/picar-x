.. note::

    你好，欢迎来到 SunFounder 树莓派、Arduino 和 ESP32 爱好者社区的 Facebook 页面！与其他爱好者一起深入探讨树莓派、Arduino 和 ESP32。

    **为什么加入？**

    - **专家支持**: 通过我们的社区和团队的帮助解决售后问题和技术挑战。
    - **学习与分享**: 交流技巧和教程，提升你的技能。
    - **独家预览**: 提前了解新产品发布和预告。
    - **特别折扣**: 尊享我们最新产品的专属折扣。
    - **节日促销和赠品**: 参与赠品活动和节日促销。

    👉 准备好与我们一起探索和创造了吗？点击 [|link_sf_facebook|] 加入我们吧！

.. _install_all_modules:

安装所有模块（重要）
=======================================

确保你已连接到互联网并更新你的系统：

.. raw:: html

    <run></run>

.. code-block::

    sudo apt update
    sudo apt upgrade

.. note::

    如果你安装的是Lite版本的操作系统，必须安装Python3相关的包。

    .. raw:: html

        <run></run>

    .. code-block::

        sudo apt install git python3-pip python3-setuptools python3-smbus

安装 ``robot-hat``。

.. raw:: html

    <run></run>

.. code-block::

    cd ~/
    git clone -b v2.0 https://github.com/sunfounder/robot-hat.git
    cd robot-hat
    sudo python3 setup.py install

接下来下载并安装 ``vilib`` 模块。

.. raw:: html

    <run></run>

.. code-block::

    cd ~/
    git clone -b picamera2 https://github.com/sunfounder/vilib.git
    cd vilib
    sudo python3 install.py

下载并安装 ``picar-x`` 模块。

.. raw:: html

    <run></run>

.. code-block::

    cd ~/
    git clone -b v2.0 https://github.com/sunfounder/picar-x.git
    cd picar-x
    sudo python3 setup.py install

这一步需要一点时间，请耐心等待。

最后，你需要运行脚本 ``i2samp.sh`` 来安装i2s放大器所需的组件，否则picar-x将没有声音。

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x
    sudo bash i2samp.sh

.. image:: img/i2s.png

输入 ``y`` 并按回车继续运行脚本。

.. image:: img/i2s2.png

输入 ``y`` 并按回车在后台运行 ``/dev/zero``。

.. image:: img/i2s3.png

输入 ``y`` 并按回车重启Picar-X。

.. note::
    如果重启后没有声音，你可能需要多次运行i2samp.sh脚本。
