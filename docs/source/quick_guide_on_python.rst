Quick Guide on Python
==========================

This section is to teach you how to install Raspberry Pi OS, configure wifi to Raspberry Pi, remote access to Raspberry Pi to run the corresponding code.

If you are familiar with Raspberry Pi and can open the command line successfully, then you can skip the first 3 parts and start directly from :ref:`download_code` all the way to :ref:`run_servo_zeroing.py`. 

.. note:: 

    servo_zeroing.py is what makes the P11 output a stable square wave that sets the servo angle to 0. You need to run this code before assembling each servo.


* :ref:`install_raspberry_pi_os`
* :ref:`configure_wifi_file`
* :ref:`remote_access_by_ssh`
* :ref:`download_code`
* :ref:`run_install.py`
* :ref:`run_servo_zeroing.py`


.. _install_raspberry_pi_os:

Install Raspberry Pi OS
-------------------------------
You are required to prepare the following items:

* Personal computer
* Raspberry Pi
* Card reader
* SD card
* Power supply

1. Insert the SD card (with card reader) into the PC and open `Raspberry Pi Imager <https://www.raspberrypi.org/downloads/>`_ .

    .. image:: img/RPi_imager.png

#. Click CHOOSE OS and Select the first one (Recommended) to download and write.

    .. image:: img/RPi_imager2.png

#. Click CHOOSE SD CARD. Select the one you just insert into PC.
    
    .. image:: img/RPi_imager3.png

#. Write!

    .. image:: img/RPi_imager4.png

.. note::
    
    For more ways to install Raspberry Pi OS, please click https://www.raspberrypi.org/documentation/installation/.

.. note::
    If you have a display, getting into the Raspberry Pi and opening Terminal to run the code is a simple task for you, for a detailed tutorial please refer to: `Setting up your Raspberry Pi <https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up>`_ .
    
    If you do not have a display, you will need to follow the tutorial below to access the Raspberry Pi remotely via your own PC.

.. _configure_wifi_file:

Configure Wi-Fi File
-----------------------------------------------

You will need to define a ``wpa_supplicant.conf`` file for your particular wireless network. Put this file in the ``boot`` folder, and when the Pi first boots, it will copy that file into the correct location and use those settings to start up wireless networking. 

Depending on the operating system and editor you are using, the file may have incorrect line breaks or the wrong file extension, so make sure the editor you are using can fix this.

Linux expects the line feed (LF) newline character. For more information, see this `Wikipedia article <https://en.wikipedia.org/wiki/Newline>`_ .

.. image:: img/setup_python1.png

.. code-block:: 

    ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev  
    update_config=1  
    country=<Insert 2 letter ISO 3166-1 country code here>
    
    network={
        ssid="<Name of your wireless LAN>" 
        psk="< Password for your wireless LAN>"  
    }

.. warning::

    * More information on the ``wpa_supplicant.conf`` file can be found in https://www.raspberrypi.org/documentation/configuration/wireless/wireless-cli.md. 
    * See `ISO_3166 - Wikipedia <https://en.wikipedia.org/wiki/ISO_3166-1>`_ for a list of 2 letter ISO 3166-1 country codes.
    * Note that some older wireless dongles don't support 5GHz networks.
    * For more ways to set up a wireless network, please click https://www.raspberrypi.org/documentation/configuration/wireless/README.md.


.. _remote_access_by_ssh:

Remote Access by SSH
------------------------------------

**Enable SSH** 

You can access the command line of a Raspberry Pi remotely from another computer or device on the same network using SSH.  

The Raspberry Pi will act as a remote device: you can connect to it using a client on another machine. In this way, you only have access to the command line, not the full desktop environment.

SSH can be enabled by placing a file named ``ssh``, without any extension, onto the ``boot`` partition of the SD card from another computer. When the Pi boots, it looks for the ssh file. If it is found, SSH is enabled and the file is deleted. The content of the file does not matter; it could contain text, or nothing at all.

.. image:: img/ssh.png

If you have loaded Raspberry Pi OS onto a blank SD card, you will have two partitions. The first one, which is the smaller one, is the boot partition. Place the file into this one.

.. image:: img/boot_disk.png

Now you can unplug the Micro SD, then plug it into the Raspberry Pi and power on the Raspberry Pi.


**Find the IP address**

Any device connected to a Local Area Network is assigned an IP address.
In order to connect to your Raspberry Pi from another machine using SSH, you need to know the Pi's IP address. 

On Raspberry Pi OS, **multicast DNS** is supported out-of-the-box by the Avahi service.

If your device supports mDNS, you can reach your Raspberry Pi by using its ``hostname`` and the ``.local`` suffix. The default hostname on a fresh Raspberry Pi OS install is ``raspberrypi``, so by default any Raspberry Pi running Raspberry Pi OS responds to:


.. code-block:: shell

    ping raspberrypi.local


.. image:: img/ping_rpi.png

If the Raspberry Pi is reachable, ping will show its IP address:

.. code-block:: shell

    Pinging raspberrypi.local [192.168.18.168] with 32 bytes of data:
    Reply from 192.168.18.168: bytes=32 time=54ms TTL=64
    Reply from 192.168.18.168: bytes=32 time=1ms TTL=64
    Reply from 192.168.18.168: bytes=32 time=1ms TTL=64
    Reply from 192.168.18.168: bytes=32 time=2ms TTL=64

    Ping statistics for 192.168.18.168:
        Packets: Sent = 4, Received = 4, Lost = 0 (0% loss),
    Approximate round trip times in milli-seconds:
        Minimum = 1ms, Maximum = 54ms, Average = 14ms


For more ways to find the IP address, please click https://www.raspberrypi.org/documentation/remote-access/ip-address.md .


**Remote Access**

You can use SSH to connect to your Raspberry Pi from a **Windows 10** computer that is using **October 2018 Update or later** without having to use third-party clients.

* For use SSH from a Linux computer, or a Mac, please click https://www.raspberrypi.org/documentation/remote-access/ssh/unix.md .
* For older version of Windows, please click https://www.raspberrypi.org/documentation/remote-access/ssh/windows.md .

To connect to your Pi from a different computer, copy and paste the following command into the terminal window, but replace ``<IP>`` with the IP address of the Raspberry Pi.

.. code-block:: shell

    ssh pi@<IP>

.. image:: img/ssh_pi_ip.png

When the connection works, you will see a security/authenticity warning, type ``yes`` to continue. You will only see this warning the first time you connect.

.. image:: img/secure_warning.png

.. warning::

    In the event that your Pi has taken the IP address of a device to which your computer has connected before (even if this was on another network), you may be given a **warning** and asked to clear the record from your list of known devices. Following it and try to ssh again please.

Next you will be prompted for the password for the user as which you are trying to connect: the default password for the pi user on Raspberry Pi OS is  ``raspberry``.

* When you input the password, the characters do not display on window accordingly, which is normal. What you need is to input the correct password.

* For security reasons it is highly recommended to change the default password on the Raspberry Pi. You should now be able to see the Raspberry Pi prompt, which will be identical to the one found on the Raspberry Pi itself.

.. image:: img/ssh_pi_terminal.png

You are now connected to the Raspberry Pi remotely, and can execute commands in this terminal.


.. _download_code:

Download Code
-----------------

We can download the files by using ``git clone`` in the command line.

Change directory to **/home/pi/** via `cd command <https://en.wikipedia.org/wiki/Cd_(command)>`_ .

.. code-block:: shell

    cd /home/pi/

Clone the repository from github via `git clone command <https://github.com/git-guides/git-clone>`_ .

.. code-block:: shell

    git clone -b v2.0 https://github.com/sunfounder/picar-x.git

.. _run_install.py:

Run install.py
-----------------------------------

Enter the following two commands to run the ``install.py`` file in the ``picar-x`` folder.

.. code-block:: shell

    cd picar-x

.. code-block:: shell

    sudo python3 install.py

This file will help you finish the installation of the required library and configuration of Raspberry Pi.

.. image:: img/install_py.png

.. warning::
    
    For the reason of the network, ``install.py`` may encounter some **Errors** in some processes. If there is an error prompt, please check the network and re-run ``install.py`` until all processes show **Done** and prompt **Finished** at the end.

This step will take a little time, so please be patient. After the file is fully executed and the prompt ``Finished`` is issued, please restart the Raspberry Pi.

.. code-block:: shell

    sudo reboot

.. _run_servo_zeroing.py:

Run servo_zeroing.py
---------------------------------
Because the servo is powered by the power supply on the Robot HAT, when you only supply power to the Raspberry Pi, the servo will not work. You need to make sure that the batterries are placed in the battery box and the Robot HAT is powered on.

.. image:: img/slide_to_power.png
    :width: 400

Run the file ``servo_zeroing.py`` in the **example** folder.

.. code-block:: shell

    cd /home/pi/picar-x/example

.. code-block::  shell

    sudo python3 servo_zeroing.py

To make sure you can see that the servo has been set to 0°, you can insert a rocker arm in the servo shaft first and then turn the servo to another angle.

.. image:: img/servo_arm.png

Now follow the diagram below and insert the servo to the P11 position.

.. image:: img/pin11_connect.png
    :width: 600

So now if the servo arm returns after the servo arm returns, this function will take effect. If not, If not, please check the insertion direction of the servo cable and re-run the code.

.. note::
    Before assembling each servo, you need to plug the servo pin into P11 and keep the power on.
