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

Before assembling the servo, 
the angle needs to be set to zero. 
This is because the servo motor has a limited range of motion, 
setting the angle to zero degrees ensures that the servo is in its 
initial position and does not exceed its range of motion when the servo is powered on. 
If the servo is not set to zero degrees prior to assembly, 
it may attempt to exceed its range of motion when powered, 
potentially damaging the servo or the mechanical system it is connected to. 
Therefore, setting the angle to zero is an important step to ensure the 
safe and normal operation of the servo motor.

.. image:: img/IMG_9897.png


**For Python User**

Please refer to :ref:`quick_guide_python` to complete the 
installation of the Raspberry Pi OS and adjust the angle of the servos.


**For Ezblock User**

.. note::

    If you are using a Raspberry Pi 5, you will not be able to use our graphical programming software, EzBlock, to program the PiCrawler.

After you have installed the ezblock system, 
the P11 pin can be used to adjust the servo. 
Please refer to :ref:`ezb_servo_adjust` for details.