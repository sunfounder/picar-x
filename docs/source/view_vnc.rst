View RPi Desktop by VNC
=============================

接下来的章节涉及 Computer Vision， 你需要借助VNC来实现远程桌面，从而查看PiCar-X看到的画面。

**Enable VNC service**

The VNC service has been installed in the system. By default, VNC is disabled. You need to enable it in config.

Input the following command:

.. image:: img/vnc1.png

.. code-block::

    sudo raspi-config

On the config interface, select **Interfacing Options** by the up, down, left and right keys on the keyboard.

.. image:: img/vnc2.png

Select VNC.

.. image:: img/vnc3.png

Select Yes -> OK -> Finish to exit the configuration.

.. image:: img/vnc4.png

**Login to VNC**

You need to install the `VNC Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ on personal computer. After the installation is done, open it.

Then select **New connection**.

.. image:: img/vnc5.png

Input IP address of Raspberry Pi and any Name.

.. image:: img/vnc6.png

Double click the connection just created:

.. image:: img/vnc7.png

Enter Username (pi) and Password (raspberry by default).

.. image:: img/vnc8.png

Now you can see the desktop of the Raspberry Pi:

.. image:: img/vnc9.png


.. note:: 在Raspberry pi OS的桌面，可以打开terminal来execute commands.

.. image:: img/vnc10.png