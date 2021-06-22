Test Ultrasonic Module
==============================

PiCar-X has Ultrasonic Sensor module that can be used for experiments such as obstacle avoidance and automatic follow. Here we will try to test this module and read the distance (unit: cm).

**TIPS**

.. image:: img/block/sp210512_114549.png 

You can directly use this block to read the distance to the obstacle right ahead.

.. image:: img/block/sp210512_114830.png

You may want to simplify your program with Variable. For example, when you have multiple functions that need to read the obstacle distance, you don't need to read the value for each function, just load the value into a variable and use it multiple times.

.. image:: img/block/sp210512_114916.png

Click the **Create variable** button on the **Variables** category to create a variable named distance.

.. image:: img/block/sp210512_114945.png

The **Print** function can print data such as variables and text for easy debugging.

.. image:: img/block/debug_monitor.png

Once the code is running, you need to enable the debug monitor by clicking the debug icon in the bottom left corner.

**EXAMPLE**

.. image:: img/block/sp210512_115125.png