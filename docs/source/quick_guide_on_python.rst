Quick Guide on Python
==========================





This chapter is used to set up Raspberry Pi, from configure the Raspberry Pi environment to run the ``servo_zeroing.py`` file of PiCar-X. 

接下来是远程访问PiCar-X的教程。

您需要准备以下物件:
1. 个人电脑
2. 树莓派
3. 读卡器
4. SD卡
5. 电源
    
    .. note:: 在本页的步骤中，直到Run Servo-zeroing Code之前都与Robot HAT无关，可以仅为树莓派供电。而在进行 **servo zeroing** 时，为Robot HAT供电是必须的。为Robot HAT供电时，Robot HAT也将驱动树莓派。）



Setup Raspberry Pi OS
-------------------------------

1. Insert the SD card (with card reader) into the PC and run `Raspberry Pi Imager <https://www.raspberrypi.org/downloads/>`_ .
   
    .. image:: img/RPi_imager.png

#. Click CHOOSE OS. Select the first one (Recommended) to download and burn the OS.
   
    .. image:: img/RPi_imager2.png

#. Click CHOOSE SD CARD. Select the one you just insert into PC.
    
    .. image:: img/RPi_imager3.png

#. Write!

    .. image:: img/RPi_imager4.png

.. note:: For more ways to install Raspberry Pi OS, please click https://www.raspberrypi.org/documentation/installation/.


Connect the Raspberry Pi to the Internet
-----------------------------------------------

You will need to define a ``wpa_supplicant.conf`` file for your particular wireless network. Put this file in the ``boot`` folder, and when the Pi first boots, it will copy that file into the correct location in the Linux root file system and use those settings to start up wireless networking. 

Depending on the OS and editor you are creating this on, the file could have incorrect newlines or the wrong file extension so make sure you use an editor that accounts for this. 

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
    * More information on the ``wpa_supplicant.conf`` file can be found in https://www.raspberrypi.org/documentation/configuration/wireless/wireless-cli.md . 
    * See `ISO_3166 - Wikipedia <https://en.wikipedia.org/wiki/ISO_3166-1>`_ for a list of 2 letter ISO 3166-1 country codes.
    * Note that some older wireless dongles don't support 5GHz networks.
    * For more ways to set up a wireless network, please click https://www.raspberrypi.org/documentation/configuration/wireless/README.md .


Remote Access by SSH
------------------------------------

**Enable SSH** 

You can access the command line of a Raspberry Pi remotely from another computer or device on the same network using SSH.  

The Raspberry Pi will act as a remote device: you can connect to it using a client on another machine.  In this way, you only have access to the command line, not the full desktop environment.

SSH can be enabled by placing a file named ``ssh`` , without any extension, onto the ``boot`` partition of the SD card from another computer. When the Pi boots, it looks for the ssh file. If it is found, SSH is enabled and the file is deleted. The content of the file does not matter; it could contain text, or nothing at all.


.. image:: img/ssh.png


If you have loaded Raspberry Pi OS onto a blank SD card, you will have two partitions. The first one, which is the smaller one, is the boot partition. Place the file into this one.

.. image:: img/boot_disk.png

Then insert the SD card into Raspberry Pi.



**Find the IP address**

Any device connected to a Local Area Network is assigned an IP address.
In order to connect to your Raspberry Pi from another machine using SSH, you need to know the Pi's IP address. 

On Raspberry Pi OS, **multicast DNS** is supported out-of-the-box by the Avahi service.

If your device supports mDNS, you can reach your Raspberry Pi by using its ``hostname`` and the ``.local`` suffix. The default hostname on a fresh Raspberry Pi OS install is ``raspberrypi``, so by default any Raspberry Pi running Raspberry Pi OS responds to:


.. code-block::

    ping raspberrypi.local


.. image:: img/ping_rpi.png

If the Raspberry Pi is reachable, ping will show its IP address:

.. code-block::

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

.. code-block::

    ssh pi@<IP>

.. image:: img/ssh_pi_ip.png

When the connection works you will see a security/authenticity warning. Type ``yes`` to continue. You will only see this warning the first time you connect.

.. image:: img/secure_warning.png

.. warning::
    In the event that your Pi has taken the IP address of a device to which your computer has connected before (even if this was on another network), you may be given a **warning** and asked to clear the record from your list of known devices. Following it and try to ssh again please.

Next you will be prompted for the password for the user as which you are trying to connect: the default password for the pi user on Raspberry Pi OS is  ``raspberry``.

* When you input the password, the characters do not display on window accordingly, which is normal. What you need is to input the correct passcode.

* For security reasons it is highly recommended to change the default password on the Raspberry Pi. You should now be able to see the Raspberry Pi prompt, which will be identical to the one found on the Raspberry Pi itself.

.. image:: img/ssh_pi_terminal.png

You are now connected to the Raspberry Pi remotely, and can execute commands in this terminal.



Download Code
-----------------

We can download the files by using ``git clone`` in the Terminal.

Change directory to **/home/pi/** via `cd command <https://en.wikipedia.org/wiki/Cd_(command)>`_ .

.. code-block::

    cd /home/pi/

Clone the repository from github via `git clone command <https://github.com/git-guides/git-clone>`_ .

.. code-block::

    git clone -b v2.0 https://github.com/sunfounder/picar-x.git 


Run install.py file
-----------------------------------

请执行 **picar-x** 目录下的 ``install.py`` 文件。在terminal中键入以下两句指令。

.. code-block::

    cd picar-x

.. code-block::

    sudo python3 install.py

    
这个file会帮你完成所需要的库的安装及树莓派配置工作。

.. image:: img/install_py.png

.. warning:: 由于网络等原因，``install.py`` 在一些过程将可能会有 **Error** 。如遇到错误提示，请检查网络并重新运行 ``install.py`` ，直到所有过程显示 **Done** 并在最后提示 ``Finished`` 。

这将会花上少许时间，请耐心等待。等文件执行完毕，并提示 ``Finished`` 后，请重启树莓派。

.. code-block::

    sudo reboot


Run Servo-zeroing Code
---------------------------------

让我们为Robot HAT插上电源，打开开关，运行 **example** 目录下的 ``servo_zeroing.py`` 文件，来初始化Servo的输出轴角度。

.. code-block::

    cd /home/pi/picar-x/example

.. code-block::

    sudo python3 servo_zeroing.py

现在你只要将servo pin 插入P11 port即可对其进行调零了。