.. note::

    你好，欢迎来到 SunFounder 树莓派、Arduino 和 ESP32 爱好者社区的 Facebook 页面！与其他爱好者一起深入探讨树莓派、Arduino 和 ESP32。

    **为什么加入？**

    - **专家支持**: 通过我们的社区和团队的帮助解决售后问题和技术挑战。
    - **学习与分享**: 交流技巧和教程，提升你的技能。
    - **独家预览**: 提前了解新产品发布和预告。
    - **特别折扣**: 尊享我们最新产品的专属折扣。
    - **节日促销和赠品**: 参与赠品活动和节日促销。

    👉 准备好与我们一起探索和创造了吗？点击 [|link_sf_facebook|] 加入我们吧！

.. _pip_apt_change:

apt 和pip更换国内源
=============================================

树莓派系统默认的apt源和pip源都是国外的服务器，使用国内网络访问可能会发生超时（ReadTimeoutErro），或被拒绝访问的情况，如果是这样我们可以将apt和pip更改为国内的源，步骤如下所示：

**1.apt更换国内源**

1）访问链接：https://mirrors.tuna.tsinghua.edu.cn/help/raspbian/ 以了解配置文件修改详情。

2）不同的树莓派系统版本修改不同，先选择对应的版本，比如我的是Debian 10 （buster），如果你的树莓派系统是bullseye则选择对应版本，若没有符合的版本则请重新安装buster及以下版本的系统。

.. image:: img/apt_ch.png

.. note::
    一般不删除原内容，可以将其用 ``#`` 注释掉。

3）我们这里以raspbian buster版本为例，用 nano命令打开 ``/etc/apt/sources.list`` 文件。 

.. code-block::

    sudo nano /etc/apt/sources.list

4）然后用 ``#`` 将原本的内容注释掉，在最后面附上下面的代码。

.. code-block::

    # deb http://raspbian.raspberrypi.org/raspbian/ buster main contrib non-free rpi
    # Uncomment line below then 'apt-get update' to enable 'apt-get source'
    #deb-src http://raspbian.raspberrypi.org/raspbian/ buster main contrib non-free rpi

    deb [arch=armhf] http://mirrors.tuna.tsinghua.edu.cn/raspbian/raspbian/ buster main non-free contrib rpi
    deb-src http://mirrors.tuna.tsinghua.edu.cn/raspbian/raspbian/ buster main non-free contrib rpi

5）按下 ``Ctrl+O`` 保存，按下 ``Ctrl+X`` 和 ``Y`` 退出。

6）用 nano 命令打开 ``etc/apt/sources.list.d/raspi.list`` 文件。

.. code-block::

    sudo nano /etc/apt/sources.list.d/raspi.list    

7）然后用#将原本的内容注释掉，在最后面附上deb...代码。

.. code-block::

    # deb http://archive.raspberrypi.org/debian/ buster main
    # Uncomment line below then 'apt-get update' to enable 'apt-get source'
    #deb-src http://archive.raspberrypi.org/debian/ buster main

    deb http://mirrors.tuna.tsinghua.edu.cn/raspberrypi/ buster main ui

8）按下 ``Ctrl+O`` 保存，按下 ``Ctrl+X`` 和 ``Y`` 退出。

9）用以下命令更新软件列表：

.. code-block::

    sudo apt update

**2.(Pypi) pip更换国内源** 

可以参考链接 https://mirrors.tuna.tsinghua.edu.cn/help/pypi/ 了解详情。

有两种方法修改配置文件。

方法一：使用pip指令设置

.. code-block::

    pip3 config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

方法二：手动编辑文件  

Linux/Mac os 环境中，配置文件位置在 ~/.pip/pip.conf（如果不存在则手动创建该目录和文件）。

.. code-block::

    sudo mkdir -p ~/.pip
    sudo nano ~/.pip/pip.conf    

然后按如下编辑文件内容

.. code-block::

    [global]
    index-url = https://pypi.tuna.tsinghua.edu.cn/simple
    [install]
    trusted-host = https://pypi.tuna.tsinghua.edu.cn

最后apt和pip都已经更换了国内下载源，这样下载速度就会提高很快不会导致下载失败了。  
