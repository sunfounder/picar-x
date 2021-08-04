About Robot HAT
-----------------------------

.. image:: img/picar_x_pic7.png

**RST Button**
    * A short-press of the RST Button will cause any running programs to reset.
    * A long-press of the RST Button until the LED lights up, and then releasing will disconnect the Robot HAT’s Bluetooth chip.

**USR Button**
    * The functions of the USR Button can be configured through programming. (Pressing down leads to a input of “0”, and releasing produces a input of “1” )

**LED**
    * Configured through programming (Outputting ‘1’ turns the LED on, Outputting ‘0’ turns the LED off.)

**Battery Indicator**
    * Battery voltage above 7.8V will light up the two indicator LEDs. Battery voltage ranging from 6.7V to 7.8V will only light up one LED, voltage below 6.7V will turn both LEDs off.

**Bluetooth Indicator**
    * The Bluetooth indicator LED will stay on with a solid Bluetooth connection, and blink rapidly during a signal transmission. The LED will blink at 1-second intervals if the Bluetooth is disconnected.  