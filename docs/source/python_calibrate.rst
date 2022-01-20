Calibrating PiCar-X
======================

Some servo angles may be slightly tilted due to possible deviations during PiCar-X installation or limitations of the servos themselves, so you can calibrate them.

Of course, you can skip this chapter if you think the assembly is perfect and doesn't require calibration.

Run the calibration program ``calibration.py``.

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/picar-x/examples/calibration
    sudo python3 calibration.py

After running the above code, you will see the following interface displayed in the terminal.

.. image:: img/calibrate1.png

The R key is used to test whether the steering gear that controls the direction of the front wheel can work normally and is not damaged.

Press the number key 1 to select the front wheel servo, and then press the W/S key to slowly calibrate the direction of the front wheel so that it looks as forward as possible without skewing left and right.

.. image:: img/calibrate2.png

Press the number key 2 to select the servo in the left and right directions of the camera, and then press the W/S key to slowly calibrate the left and right directions of the camera, so that it looks straight ahead and does not tilt left and right.

.. image:: img/calibrate3.png

Press the number key 3 to select the servo in the up and down direction of the camera, and then press the W/S key to slowly calibrate the up and down direction of the camera, so that it does not tilt up and down when looking straight ahead.

.. image:: img/calibrate4.png

Since the wiring of the rear wheel motor may be reversed during installation, it cannot move forward normally. You can press E to test whether the car can move forward normally.
If the rotation direction of the rear wheel is reversed, you can press the number keys 4 and 5 to select the left and right motors of the rear wheel respectively, and then press the Q key to calibrate the rotation direction.

.. image:: img/calibrate6.png

When the calibration is completed, press the space bar to save the calibration parameters, there will be a prompt to enter ``y`` to confirm, and then press ``esc`` to exit the program to complete the calibration.

.. image:: img/calibrate5.png
