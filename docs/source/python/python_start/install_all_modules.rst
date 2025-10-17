.. _install_all_modules:

5. 安装所有模块（重要）
========================================

确保你的树莓派已连接到互联网，并先更新系统：

.. raw:: html

    <run></run>

.. code-block::

    sudo apt update
    sudo apt upgrade

.. note::

    如果你安装的是 Lite 版本系统，还需要安装 Python3 相关的依赖包：

    .. raw:: html

        <run></run>

    .. code-block::
    
        sudo apt install git python3-pip python3-setuptools python3-smbus


安装 ``robot-hat`` 模块：

.. raw:: html

    <run></run>

.. code-block::

    cd ~/
    git clone -b 2.5.x https://github.com/sunfounder/robot-hat.git --depth 1
    cd robot-hat
    sudo python3 install.py


然后下载并安装 ``vilib`` 模块：

.. raw:: html

    <run></run>

.. code-block::

    cd ~/
    git clone -b picamera2 https://github.com/sunfounder/vilib.git --depth 1
    cd vilib
    sudo python3 install.py

下载并安装 ``picar-x`` 模块：

.. raw:: html

    <run></run>

.. code-block::

    cd ~/
    git clone -b 2.1.x https://github.com/sunfounder/picar-x.git --depth 1
    cd picar-x
    sudo pip3 install . --break

此步骤会花费一些时间，请耐心等待。

最后，你需要运行 ``i2samp.sh`` 脚本来安装 i2s 放大器所需的组件，否则 PiCar-X 将无法发声：

.. raw:: html

    <run></run>

.. code-block::

    cd ~/robot-hat
    sudo bash i2samp.sh
	
.. image:: img/i2s.png

输入 ``y`` 并按回车继续运行脚本。

.. image:: img/i2s2.png

输入 ``y`` 并按回车运行 ``/dev/zero`` 后台程序。

.. image:: img/i2s3.png

输入 ``y`` 并按回车重启 PiCar-X。

.. note::
    如果重启后仍然没有声音，可能需要多次运行 ``i2samp.sh`` 脚本。
