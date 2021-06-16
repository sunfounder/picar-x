Grayscale Sensor Test
==============================

PiCar-X has 3 channel Grayscale sensors for your implementing some fun experiments, such as walking along the line, detecting cliffs and so on. Its three detection 
heads will read the value according to the detected color shades, such as pure black reading is "0".

**TIPS**

.. image:: img/block/sp210512_115406.png

You can use this block to read the value of one of the probes of the 3ch Grayscale module.

.. image:: img/block/sp210512_120023.png

You may want to use List block to simplify your program. When you need to store the values of the three probes of 3ch Grayscale, you do not have to set three variables. Set one as a List.

**EXAMPLE**

.. image:: img/block/sp210512_120508.png