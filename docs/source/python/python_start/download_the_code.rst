下载并运行代码
============================

我们可以在终端用命令 ``git clone`` 来下载文件。

.. note:: 

    在下面的安装过程中，可能会由于网络问题导致失败，你需要参考 :ref:`pip_apt_change` 来修改配置。

首先安装 ``robot-hat`` 。

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/
    git clone https://github.com/sunfounder/robot-hat.git
    cd robot-hat
    sudo python3 setup.py install

.. note::
    运行 ``setup.py`` 会下载一些必要的组件。由于网络问题，您可能下载失败。此时您可能需要重新下载。
    见到如下界面, 输入 ``Y`` 然后按下回车。
	
	.. image:: img/dowload_code.png

然后下载并安装 ``vilib`` 模块。

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/
    git clone https://github.com/sunfounder/vilib.git
    cd vilib
    sudo python3 install.py

然后下载并安装 ``picar-x`` 模块。

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/
    git clone -b v2.0 https://github.com/sunfounder/picar-x.git
    cd picar-x
    sudo python3 setup.py install

这一步需要一点时间，所以请耐心等待。

最后需要运行脚本 ``i2samp.sh`` 来安装i2s功放所需的组件，否则 picar-x 会没有声音。

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/picar-x
    sudo bash i2samp.sh
	
.. image:: img/i2s.png

输入 ``y`` 并按下回车以继续运行脚本。

.. image:: img/i2s2.png

输入 ``y`` 并按下回车以在后台运行 ``/dev/zero`` 。

.. image:: img/i2s3.png

输入 ``y`` 并按下回车以重启机器。

.. note::
    如果重启后没有声音，可能需要多次运行 i2samp.sh 脚本。