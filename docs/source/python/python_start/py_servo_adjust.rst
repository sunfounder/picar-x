Servo Adjust
===============

The angle range of the servo is -90~90, but the angle set at the factory is random, maybe 0°, maybe 45°; if we assemble it with such an angle directly, it will lead to a chaotic state after the robot runs the code, or worse, it will cause the servo to block and burn out.

So here we need to set all the servo angles to 0° and then install them, so that the servo angle is in the middle, no matter which direction to turn.

It is recommended that you :ref:`py_calibrate` after assembling it. The servo angle will be tilted due to possible deviations during assembly or limitations of the servo itself, so you can get the servo to a perfect state by calibrating it, usually the calibration angle is -5~5°.

But if the deviation angle is too big, you still have to go back to this section to set the servo angle to 0°, and then follow the instructions to reassemble the car.

#. To ensure that the servo has been properly set to 0°, first insert the servo arm into the servo shaft and then gently rotate to a different angle.

    .. image:: img/servo_arm.png

#. Follow the instructions on the assembly foldout, insert the battery cable and turn the power switch to the ON. Then plug in a powered USB-C cable to activate the battery. Wait for 1-2 minutes, there will be a sound to indicate that the Raspberry Pi boots successfully.

    .. image:: img/Z_BTR.JPG

#. Now, run ``servo_zeroing.py`` in the ``example/`` folder.

    .. raw:: html

        <run></run>

    .. code-block::

        cd /home/pi/picar-x/example
        sudo python3 servo_zeroing.py

#. Next, plug the servo cable into the P11 port as follows.

    .. image:: img/Z_P11.JPG

#. At this point you will see the servo arm rotate to a specific position (0°). If the servo arm does not return to 0°, press the **RST** button to restart the Robot HAT.

Now you can continue the installation as instructed on the assembly foldout.

.. note::

    * Do not unplug this servo cable before fixing it with the servo screw, you can unplug it after fixing it.
    * Do not rotate the servo while it is powered on to avoid damage; if the servo shaft is not inserted at the right angle, pull the servo out and reinsert it.
    * Before assembling each servo, you need to plug the servo cable into P11 and turn on the power to set its angle to 0°.

