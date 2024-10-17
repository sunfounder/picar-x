.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

Adjust Servo for Assembly
==========================

Before assembling the servo, it is essential to set the angle to zero. Since servo motors have a limited range of motion, setting the angle to zero degrees ensures that the servo starts in its initial position and avoids exceeding its range when powered on. Failing to set the servo to zero beforehand may cause it to attempt to move beyond its allowed range when powered, potentially damaging both the servo and the mechanical system it's attached to. This step is crucial to guarantee safe and proper operation of the servo motor.

.. image:: img/IMG_9897.png


For Python Users
-----------------------

Refer to :ref:`quick_guide_python` to complete the installation of Raspberry Pi OS and adjust the servo angles.


For Ezblock Users
-------------------------

.. note::

    If you are using a Raspberry Pi 5, our graphical programming software, EzBlock, is not supported.


Once you have installed the Ezblock system, the P11 pin can be used to adjust the servo. For more details, please refer to :ref:`ezb_servo_adjust`.
