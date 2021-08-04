Remote Desktop via VNC
=============================

The following sections are related to computer vision. In order to check the images recognized by PiCar-X, first implement a remote desktop viewer with VNC.

**Enable VNC service**

The VNC service has been installed in the system. By default, VNC is disabled, and will need to be enabled through raspi-config.

Input the following command:

.. image:: img/vnc1.png

.. code-block::

    sudo raspi-config

Once inside the raspi-config interface, select Interfacing Options by using the up, down, left and right keys on the keyboard.

.. image:: img/vnc2.png

Select VNC.

.. image:: img/vnc3.png

Select Yes -> OK -> Finish to exit the configuration.

.. image:: img/vnc4.png

**Login to VNC**

Install `VNC Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ on a personal computer. After the installation is done, open the program.

Then select **New connection**.

.. image:: img/vnc5.png

Input the IP address of the Raspberry Pi and assign it a Name, like “My_PiCar-X”, or “Daisy”.

.. image:: img/vnc6.png

Double click the connection that was just created:

.. image:: img/vnc7.png

Enter the Username “pi” and the default Password “raspberry”.

.. image:: img/vnc8.png

The desktop of the Raspberry Pi should now be visible.

.. image:: img/vnc9.png


.. note::
    
    On the desktop of the Raspberry Pi OS, commands can be executed by opening a terminal window.

.. image:: img/vnc10.png