Quick Guide on EzBlock
===========================

There are 2 parts here:

* :ref:`ezb_servo_adjust` allows you to keep all the servos at 0 degrees to complete a proper and safe assembly (otherwise you will probably damage the servos).
* :ref:`install_ezblock` will guide you to download EzBlock Studio to play with your robot.

.. _ezb_servo_adjust:

Servo Adjust
--------------------------------

The angle range of the servo is -90~90, but the angle set at the factory is random, maybe 0°, maybe 45°; if we assemble it with such an angle directly, it will lead to a chaotic state after the robot runs the code, or worse, it will cause the servo to block and burn out.

So here we need to set all the servo angles to 0° and then install them, so that the servo angle is in the middle, no matter which direction to turn.

It is recommended that you follow the intructions on the APP to calibrate the picar-x after assembling it. The servo angle will be tilted due to possible deviations during assembly or limitations of the servo itself, so you can get the servo to a perfect state by calibrating it, usually the calibration angle is -5~5°.

But if the deviation angle is too big, you still have to go back to this section to set the servo angle to 0°, and then follow the instructions to reassemble the car.


#. Firstly, :ref:`ezblock:install_ezblock_os_latest` onto a Micro SD card, once the installation is complete, insert it into the Raspberry Pi.

#. To ensure that the servo has been properly set to 0°, first insert the rocker arm into the servo shaft and then gently rotate the rocker arm to a different angle.

    .. image:: img/servo_arm.png

#. Follow the instructions on the assembly foldout, insert the battery holder cable and turn the power switch to the ON. Wait for 1-2 minutes, there will be a sound to indicate that the Raspberry Pi boots successfully.

    .. image:: img/slide_to_power.png

#. Next, plug the servo cable into the P11 port as follows.

    .. image:: img/pin11_connect.png

#. At this point you will see the servo arm rotate to a specific position (0°). If the servo arm does not return to 0°, press the RST button to restart the Robot HAT.

#. Now you can continue the installation as instructed on the assembly foldout.

.. note::

    * Do not unplug this servo cable before fastening this servo with the servo screw, you can unplug it after fastening.
    * Do not turn the servo while it is powered on to avoid damage; if the servo shaft is inserted at the wrong angle, pull out the servo and reinsert it.
    * Before assembling each servo, you need to plug the servo cable into P11 and turn on the power to set its angle to 0°.
    * This zeroing function will be disabled if you download a program to the robot later with the EzBlock APP.


.. _install_ezblock:

Install and Configure EzBlock Studio
----------------------------------------

As soon as the robot is assembled, you will need to carry out some basic operations.

* :ref:`ezblock:install_ezblock_app_latest`: Download and install EzBlock Studio on your device or use the web-based version.
* :ref:`ezblock:connect_product_ezblock_latest`: Configure Wi-Fi, Bluetooth and calibrate before use.
* :ref:`ezblock:open_run_latest`: View or run the related example directly.

.. note::

    After you connect the Picar-x, there will be a calibration step. This is because of possible deviations in the installation process or limitations of the servos themselves, making some servo angles slightly tilted, so you can calibrate them in this step.
    
    But if you think the assembly is perfect and no calibration is needed, you can also skip this step.