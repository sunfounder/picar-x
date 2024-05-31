.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

4. Set up Your Raspberry Pi
============================
If You Have a Screen
-------------------------

.. note:: The Raspberry Pi ZERO installed on the Robot is not easy to connect to the screen, please use the method without a screen to set it up.


If you have a screen, it will be easy for you to operate on the
Raspberry Pi.

**Required Components**

* Raspberry Pi
* Power Adapter
* Micro SD card
* Screen Power Adapter
* HDMI cable
* Screen
* Mouse
* Keyboard

#. Plug in the Mouse and Keyboard.

#. Connect the screen to Raspberry Pi's HDMI port and make sure your screen is plugged into a wall socket and switched on.

    .. note::

        If you use a Raspberry Pi 4, you need to connect the screen to the HDMI0 (nearest the power in port).

#. Use the power adapter to power the Raspberry Pi.

#. After a few seconds, the Raspberry Pi OS desktop will be displayed. Now you can open the Terminal to start entering commands.

    .. image:: img/bookwarm.png
        :align: center

If You Have No Screen
--------------------------

If you don't have a monitor, you can remotely log into your Raspberry Pi.

**Required Components**

* Raspberry Pi
* Power Adapter
* Micro SD card

You can apply the SSH command to open the Raspberry Pi's Bash shell. Bash is the standard default shell for Linux. The shell itself is a command (instruction) when the user uses Unix/Linux. Most of what you need to do can be done through the shell.

If you're not satisfied with using the command window to access your Raspberry Pi, you can also use the remote desktop feature to easily manage files on your Raspberry Pi using a GUI.

See below for detailed tutorials for each system.


.. toctree::

    remote_macosx
    remote_windows
    remote_linux
    remote_desktop

