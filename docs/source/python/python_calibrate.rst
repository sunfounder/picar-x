.. _py_calibrate:

Calibrating the PiCar-X
==========================

Calibrate Motors & Servo
---------------------------

Some servo angles may be slightly tilted due to possible deviations during PiCar-X 
installation or limitations of the servos themselves, so you can calibrate them.

Of course, you can skip this chapter if you think the assembly is perfect and doesn't require calibration.

#. Run the ``calibration.py``.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/picar-x/example/calibration
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


Calibrate Grayscale Module
---------------------------

Due to varying environmental conditions and lighting situations, 
the preset parameters for the greyscale module might not be optimal. 
You can fine-tune these settings through this program to achieve better results.


#. Lay down a strip of black electrical tape, about 15cm long, on a light-colored floor. Center your PiCar-X so that it straddles the tape. In this setup, the middle sensor of the greyscale module should be directly above the tape, while the two flanking sensors should hover over the lighter surface.

..pic if have

#. Run the ``grayscale_calibration.py``.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/picar-x/example/calibration
        sudo python3 Grayscale.py

#. After running the code, you will see the following interface displayed in the terminal.

    .. image:: img/calibrate_g1.png

#. Press the "Q" key to initiate the greyscale calibration. You'll then observe the PiCar-X make minor movements to both the left and the right. During this process, each of the three sensors should sweep across the electrical tape at least once.

..pic if have

#. Additionally, you will notice three pairs of significantly different values appearing in the "threshold value" section, while the "line reference" will display two intermediate values, each representing the average of one of these pairs.

    .. image:: img/calibrate_g2.png

#. Next, suspend the PiCar-X in mid-air (or position it over a cliff edge) and press the "E" key. You'll observe that the "cliff reference" values are also updated accordingly.

    .. image:: img/calibrate_g3.png

#. Once you've verified that all the values are accurate, press the "space" key to save the data. You can then exit the program by pressing Ctrl+C.