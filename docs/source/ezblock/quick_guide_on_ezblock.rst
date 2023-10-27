.. _ezb_servo_adjust:

Quick Guide on EzBlock
===========================

The angle range of the servo is -90~90, but the angle set at the factory is random, maybe 0°, maybe 45°; if we assemble it with such an angle directly, it will lead to a chaotic state after the robot runs the code, or worse, it will cause the servo to block and burn out.

So here we need to set all the servo angles to 0° and then install them, so that the servo angle is in the middle, no matter which direction to turn.

#. Firstly, :ref:`ezblock:install_ezblock_os_latest` (EzBlock's own tutorials) onto a Micro SD card, once the installation is complete, insert it into the Raspberry Pi.

    .. note::
        After the installation is complete, please return to this page.

    .. image:: img/insert_sd_card.jpg
        :width: 500
        :align: center

#. To ensure that the servo has been properly set to 0°, first insert the servo arm into the servo shaft and then gently rotate the rocker arm to a different angle. This servo arm is just to allow you to clearly see that the servo is rotating.

    .. image:: img/servo_arm.png

#. Follow the instructions on the assembly foldout, insert the battery holder cable and turn the power switch to the ON. Wait for 1-2 minutes, there will be a sound to indicate that the Raspberry Pi boots successfully.

    .. image:: img/slide_to_power.png

#. Next, plug the servo cable into the P11 port as follows.

    .. image:: img/pin11_connect.png

#. Press and hold the **USR** key, then press the **RST** key to execute the servo zeroing script within the system. When you see the servo arm rotate to a position(This is the 0° position, which is a random location and may not be vertical or parallel.), it indicates that the program has run.

    .. note::

        This step only needs to be done once; afterward, simply insert other servo wires, and they will automatically zero.

    .. image:: img/Z_P11_BT.png
        :width: 400
        :align: center


#. Now, remove the servo arm, ensuring the servo wire remains connected, and do not turn off the power. Then continue the assembly following the paper assembly instructions.

.. note::

    * Do not unplug this servo cable before fastening this servo with the servo screw, you can unplug it after fastening.
    * Do not turn the servo while it is powered on to avoid damage; if the servo shaft is inserted at the wrong angle, pull out the servo and reinsert it.
    * Before assembling each servo, you need to plug the servo cable into P11 and turn on the power to set its angle to 0°.
    * This zeroing function will be disabled if you download a program to the robot later with the EzBlock APP.


