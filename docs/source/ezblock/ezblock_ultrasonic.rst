Test Ultrasonic Module
==============================

PiCar-X has a built-in Ultrasonic Sensor module that can be used for obstacle avoidance and automatic object-following experiments. In this lesson the module will read a distance in centimeters (24 cm = 1 inch), and **Print** the results in a **Debug** window.

**TIPS**

.. image:: img/sp210512_114549.png 

The **Ultrasonic get distance** block will read the distance from the PiCar-X to an obstacle directly ahead.

.. image:: img/sp210512_114830.png

This program is simplified with a **Variable**. For example, when there are multiple functions in a program that each need to use the distance to an obstacle, a **Variable** can be used to report the same distance value to each function, instead of each function reading the same value separately.

.. image:: img/sp210512_114916.png

Click the **Create variable...** button on the **Variables** category, and use the drop-down arrow to select the variable named “distance”.

.. image:: img/sp210512_114945.png

The **Print** function can print data such as variables and text for easy debugging.

.. image:: img/debug_monitor.png

Once the code is running, enable the debug monitor by clicking the **Debug** icon in the bottom left corner.

**EXAMPLE**

.. note::

    * You can write the program according to the following picture, please refer to the tutorial: `How to Create a New Project? <https://docs.sunfounder.com/projects/ezblock3/en/latest/create_new.html>`_
    * Or find the code with the same name on the **Examples** page of the EzBlock Studio and click **Run** or **Edit** directly.


.. image:: img/sp210512_115125.png