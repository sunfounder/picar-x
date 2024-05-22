.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _ezb_remote_control:

Remote Control
=======================

This project will teach how to remotely control the PiCar-X with the Joystick widget. 
Note: After dragging and dropping the Joystick widget from the Remote Control page, use the “Map” function to calibrate the Joysticks X-axis and Y-axis readings. For more information on the Remote Control function, please reference the following link:


* :ref:`ezblock:remote_control_latest`


.. image:: img/remote_control23.png

**TIPS**

.. image:: img/sp210512_114004.png

To use the remote control function, open the Remote Control page from the left side of the main page.

.. image:: img/sp210512_114042.png

Drag a Joystick to the central area of the Remote Control page. Toggling the white point in the center, and gently dragging in any direction will produce an (X,Y) coordinate. The range of the X-axis or Y-axis is defaulted to “-100” to “100”. Toggling the white point and dragging it directly to the far left of the Joystick will result in an X value of “-100” and a Y value of “0”.

.. image:: img/sp210512_114136.png

After dragging and dropping a widget on the remote control page, a new category-Remote with the above block will appear.
This block reads the Joystick value in the Remote Control page. You can click the drop-down menu to switch to the Y-axis reading.

.. image:: img/sp210512_114235.png

The map value block can remap a number from one range to another. If the range is set to 0 to 100, and the map value number is 50, then it is at a 50% position of the range, or “50”. If the range is set to 0 to 255 and the map value number is 50, then it is at a 50% position of the range, or “127.5”.

**EXAMPLE**

.. note::

    * You can write the program according to the following picture, please refer to the tutorial: :ref:`ezblock:create_project_latest`.
    * Or find the code with the same name on the **Examples** page of the EzBlock Studio and click **Run** or **Edit** directly.


.. image:: img/sp210512_114416.png

