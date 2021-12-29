下载并运行代码
============================

通过在命令行中使用 ``git clone`` 下载PiCar-X文件。


首先通过 ``cd`` 改变目录到 ``/home/pi/``。

.. raw:: html

    <run></run>

.. code-block:: 

    cd /home/pi/

然后通过 ``git clone`` 命令从 github 克隆仓库。

.. raw:: html

    <run></run>

.. code-block:: 

    git clone -b v2.0 https://gitee.com/sunfounder/picar-x.git

.. _run_install.py:

运行 install.py
-----------------------------------

输入以下两条命令，运行 ``picar-x`` 文件夹中的 ``install.py`` 文件。

.. raw:: html

    <run></run>

.. code-block:: 

    cd picar-x

.. raw:: html

    <run></run>

.. code-block:: 

    sudo python3 install.py

``install.py`` 文件将完成所需Python库的安装，并配置PiCar-X。

.. image:: img/install_py.png

.. warning::
    
    ``install.py`` 程序可能会因为网络连接而遇到一些 **Error** 。如果出现错误提示，请检查网络并重新运行 ``install.py``，直到所有进程显示 **Done**，并在最后出现提示 **Done**。

这个步骤可能需要几分钟。在文件完全执行并出现提示 **Done** 后，请重新启动树莓派。

.. raw:: html

    <run></run>

.. code-block:: 

    sudo reboot