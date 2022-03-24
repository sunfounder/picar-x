Calibrating PiCar-X
======================

Some servo angles may be slightly tilted due to possible deviations during PiCar-X installation or limitations of the servos themselves, so you can calibrate them.

Of course, you can skip this chapter if you think the assembly is perfect and doesn't require calibration.

#. Run the ``calibration.py``.

    .. raw:: html

        <run></run>

    .. code-block::

        cd /home/pi/picar-x/example/calibration
        sudo python3 calibration.py

#. After running the code, you will see the following interface displayed in the terminal.

    .. image:: img/calibrate1.png

#. The ``R`` key is used to test whether the servo that controls the direction of the front wheel can work normally and is not damaged.

#. Press the number key ``1`` to select the front wheel servo, and then press the ``W/S`` key to let the front wheel looks as forward as possible without skewing left and right.

    .. image:: img/calibrate2.png

#. Press the number key ``2`` to select the **Pan servo**, then press the ``W/S`` key to make the pan/tilt platform look straight ahead and not tilt left or right.

    .. image:: img/calibrate3.png

#. Press the number key ``3`` to select the **tilt servo**, then press the ``W/S`` key to make the pan/tilt platform look straight ahead and not tilt up and down.

    .. image:: img/calibrate4.png

#. Since the wiring of the motors may be reversed during installation, you can press ``E`` to test whether the car can move forward normally. If not, use the number keys ``4`` and ``5`` to select the left and right motors, then press the ``Q`` key to calibrate the rotation direction.

    .. image:: img/calibrate6.png

#. When the calibration is completed, press the ``Spacebar`` to save the calibration parameters. There will be a prompt to enter ``y`` to confirm, and then press ``esc`` to exit the program to complete the calibration.

    .. image:: img/calibrate5.png
