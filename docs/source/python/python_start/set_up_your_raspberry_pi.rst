.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _setup_pi:

4. Set up Your Raspberry Pi
============================

To start programming and controlling your PiCar-X, you first need to access your Raspberry Pi.
This section will guide you through two common methods: using a monitor, keyboard, and mouse, or setting up a headless connection so you can log in remotely from another computer.

If You Have a Screen
-------------------------

.. note:: The Raspberry Pi Zero 2W installed on the Robot is not easy to connect to a screen. We recommend the **headless (no-screen)** method.

**Required Components**

* Raspberry Pi
* Power Adapter
* Micro SD card
* HDMI cable
* Screen
* Mouse
* Keyboard

#. Insert the microSD card into your Raspberry Pi.
#. Connect mouse, keyboard, and screen (for Pi 4/5 use **HDMI0**, the port nearest to the power input).
#. Power on the Raspberry Pi.
#. After a short while, Raspberry Pi OS desktop will appear and you can open a Terminal to enter commands.

    .. image:: img/bookwarm.png
        :align: center


If You Have No Screen (Headless Setup)
-----------------------------------------

Without a monitor, you can configure and log into your Raspberry Pi remotely. This is the most convenient way to get started.

**Required Components**

* Raspberry Pi
* Power Adapter
* Micro SD card
* A computer on the same network

**Tips**
 
* Set the **Wireless LAN country** correctly using the ISO/IEC alpha-2 code (e.g., ``US``, ``UK``, ``CN``); otherwise Wi-Fi will not work.  
* Ensure that your Raspberry Pi and your computer are on the same local network.  
* For a more reliable connection, use a direct network connection (Ethernet) whenever possible.  


**Connect via SSH**

1. On your computer, open a terminal (Windows: **PowerShell**, macOS/Linux: **Terminal**) and type:

   .. code-block::

      ssh <username>@<hostname>.local
      # Example:
      ssh daisy@picarx.local

#. Alternatively, check your router’s DHCP/client list, find the Pi’s IP, and connect using:

   .. code-block::

      ssh <username>@<IP>
      
      # Example:

      ssh daisy@192.xxx.xx.xx

#. On first login, you will see a security prompt. Enter ``yes`` to proceed:

#. Enter the password you set in Raspberry Pi Imager. (Characters will not appear while typing; this is normal.)

   .. note::
      The absence of visible characters when typing the password is a standard security feature. Just type carefully.

#. Once connected, your Raspberry Pi is ready for remote operations.

   .. image:: img/ssh_login.png
      :align: center

**Troubleshooting**

* **ssh: Could not resolve hostname ...**  

  * Check that the hostname is correct.  
  * If it still fails, use the Pi’s IP address instead of ``<hostname>.local``.

* **The term 'ssh' is not recognized... (Windows)**  

  * Your system does not have OpenSSH installed. Install OpenSSH manually (see :ref:`openssh_powershell`), or use a third-party SSH client (see :ref:`login_windows`).  

* **Permission denied (publickey,password)**  

  * Make sure you are using the username and password you configured in Raspberry Pi Imager.  

* **Connection refused**  

  * Wait 1–2 minutes after powering on.  
  * Confirm that SSH was enabled in Raspberry Pi Imager.

**Graphical Access Options**

If you prefer a graphical interface instead of command line, you have two options:

    .. image:: img/bookwarm.png
        :align: center

* :ref:`remote_desktop`: Enable **VNC (Virtual Network Computing)** for a full desktop experience on your Pi.  
* |link_rpi_connect|: Use **Raspberry Pi Connect** for secure remote access from anywhere, directly in a browser.  

Now you cancontrol your Raspberry Pi without a monitor, either through SSH for command-line operations, or with VNC / Raspberry Pi Connect for a graphical desktop experience.
