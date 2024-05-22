.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

Face Detection
======================

In addition to color detection, PiCar-X also includes a face detection function. In the following example the Joystick widget is used to adjust the direction of the camera, and the number of faces will be displayed in the debug monitor.

For more information on how to use the Video widget, please reference the tutorial on Ezblock video here: :ref:`ezblock:video_latest`.

.. image:: img/face_detection.PNG


**TIPS**

.. image:: img/sp210512_141947.png

Set the **face detection** widget to **on** to enable facial detection.

.. image:: img/sp210512_142327.png

These two blocks are used to adjust the orientation of the pan-tilt camera, similar to driving the PiCar-X in the :ref:`ezb_remote_control` tutorial. As the value increases, the camera will rotate to the right, or upwards, a decreasing value will rotate the camera right, or downwards.

.. image:: img/sp210512_142407.png

The image detection results are given through the of **detected face** block. Use the drop-down menu options to choose between reading the coordinates, size, or number of results from the image detection function.

.. image:: img/sp210512_142616.png

Use the **create text with** block to print the combination of **text** and of **detected face** data.

**EXAMPLE**

.. note::

    * You can write the program according to the following picture, please refer to the tutorial: :ref:`ezblock:create_project_latest`.
    * Or find the code with the same name on the **Examples** page of the EzBlock Studio and click **Run** or **Edit** directly.

.. image:: img/sp210512_142830.png