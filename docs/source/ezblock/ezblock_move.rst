Move
============

This first project teaches how to program movement actions for the PiCar-X. In this project, the program will tell the PiCar-X to execute five actions in order: “forward”, “backward”, “turn left”, “turn right”, and “stop”.

To learn the basic usage of Ezblock Studio, please read through the following two sections:

* :ref:`ezblock:create_project_latest`


.. image:: img/move.png

**TIPS**

.. image:: img/sp210512_113300.png

This block will make the PiCar-X move forward at a speed based on a percentage of available power. In the example below “50” is 50% of power, or half-speed.

.. image:: img/sp210512_113418.png

This block will make the PiCar-X move backward at a speed based on a percentage of available power.

.. image:: img/sp210512_113514.png

This block adjusts the orientation of the front wheels. The range is “-45” to ”45”. In the example below, “-30” means the wheels will turn 30° to the left.

.. image:: img/BLK_Basic_delay.png
    :width: 200

This block will cause a timed break between commands, based on milliseconds. In the example below, the PiCar-X will wait for 1 second (1000 milliseconds) before executing the next command.

.. image:: img/sp210512_113550.png

This block will bring the PiCar-X to a complete stop.

**EXAMPLE**

.. note::

    * You can write the program according to the following picture, please refer to the tutorial: :ref:`ezblock:create_project_latest`.
    * Or find the code with the same name on the **Examples** page of the EzBlock Studio and click **Run** or **Edit** directly.


.. image:: img/sp210512_113827.png

