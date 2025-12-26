
.. _install_all_modules:


安装所有模块（重要）
=========================================

#. **准备系统**

   确保你的 Raspberry Pi 已连接到互联网，然后更新系统：

   .. raw:: html

      <run></run>

   .. code-block::

      sudo apt update
      sudo apt upgrade

   .. note::
      
      如果你使用的是 Raspberry Pi OS Lite，请先安装所需的 Python 3 软件包：

   .. raw:: html

      <run></run>

   .. code-block::

         sudo apt install git python3-pip python3-setuptools python3-smbus

#. **安装 robot-hat**

   下载并安装 ``robot-hat`` 模块：

   .. raw:: html

      <run></run>

   .. code-block::

      cd ~/
      git clone -b 2.5.x https://github.com/sunfounder/robot-hat.git --depth 1
      cd robot-hat
      sudo python3 install.py

#. **安装 vilib**

   下载并安装 ``vilib`` 模块：

   .. raw:: html

      <run></run>

   .. code-block::

      cd ~/
      git clone https://github.com/sunfounder/vilib.git --depth 1
      cd vilib
      sudo python3 install.py

#. **安装 picar-x**

   下载并安装 ``picar-x`` 模块：

   .. raw:: html

      <run></run>

   .. code-block::

      cd ~/
      git clone -b 2.1.x https://github.com/sunfounder/picar-x.git --depth 1
      cd picar-x
      sudo pip3 install . --break

   此步骤可能需要一些时间，请耐心等待。

#. **启用声音（I2S 功放）**

   为了启用音频输出，请运行 ``i2samp.sh`` 脚本以安装所需的 I2S 功放组件：

   .. raw:: html

      <run></run>

   .. code-block::

      cd ~/robot-hat
      sudo bash i2samp.sh

   按照屏幕提示操作，输入 ``y`` 并按 Enter 继续，在后台运行 ``/dev/zero``，然后重启 PiCar-X。

   .. note::
      如果重启后仍然没有声音，请尝试多次运行 ``i2samp.sh`` 脚本。
