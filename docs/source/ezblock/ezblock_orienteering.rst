.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

Orienteering
==================

This project uses the remote control function to guide the PiCar-X through a competitive scavenger hunt!

First, set up either an obstacle course, or a maze, or even an empty room that the PiCar-X can drive through. Then, randomly place six markers along the route, and put a color-card at each of the six markers for the PiCar-X to find. 

The six color models for PiCar-X are: red, orange, yellow, green, blue and purple, and are ready to print from a colored printer from the PDF below. 

* :download:`[PDF]Color Cards <https://github.com/sunfounder/sf-pdf/raw/master/prop_card/object_detection/color-cards.pdf>`

.. image:: img/color_card.png

.. note::

    The printed colors may have a slightly different hue from the Ezblock color models due to printer toner differences, or the printed medium, such as a tan-colored paper. This can cause a less accurate color recognition.

The PiCar-X will be programmed to find three of the six colors in a random order, and will be using the TTS function to announce which color to look for next.

The objective is to help the PiCar-X find each of the three colors in as short of a time as possible.

Place PiCar-X in the middle of the field and click the Button on the Remote Control page to start the game. 


.. image:: img/orienteering.png

Take turns playing this game with friends to see who can help PiCar-X complete the objective the fastest!

**EXAMPLE**

.. note::

    * You can write the program according to the following picture, please refer to the tutorial: :ref:`ezblock:create_project_latest`.
    * Or find the code with the same name on the **Examples** page of the EzBlock Studio and click **Run** or **Edit** directly.


.. image:: img/sp210513_154117.png
    :width: 800

.. image:: img/sp210513_154256.png
    :width: 800

.. image:: img/sp210513_154425.png
    :width: 800