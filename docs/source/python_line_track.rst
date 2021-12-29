Line Tracking
====================================

This project will use the Grayscale module to make the PiCar-X move forward along a line. 
Use dark-colored tape to make a line as straight as possible, and not too curved. 
Some experimenting might be needed if the PiCar-X is derailed.

**Run the Code**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/picar-x/example
    sudo python3 minecart_plus.py
    
After running the code, PiCar-X will move forward along a line.

**Code**

.. note::
    You can **Modify/Reset/Copy/Run/Stop** the code below. But before that, you need to go to  source code path like ``picar-x/example``. After modifying the code, you can run it directly to see the effect.

.. raw:: html

    <run></run>

.. code-block:: python

    import sys
    sys.path.append(r'/home/pi/picar-x/lib')
    from utils import reset_mcu
    reset_mcu()
    from grayscale_module import Grayscale_Module
    from picarx import Picarx

    if __name__=='__main__':
    try:
        gm = Grayscale_Module(500)
        px = Picarx()
        px_power = 10
        while True:
            gm_val_list = gm.get_grayscale_data()
            print("gm_val_list:",gm_val_list)
            gm_status = gm.get_line_status(gm_val_list)
            print("gm_status:",gm_status)

            if gm_status == 'forward':
                px.forward(px_power) 

            elif gm_status == 'left':
                px.set_dir_servo_angle(12)
                px.forward(px_power) 

            elif gm_status == 'right':
                px.set_dir_servo_angle(-12)
                px.forward(px_power) 
            else:
                px.set_dir_servo_angle(0)
                px.stop()
    
    finally:
        px.stop()

**How it works?** 

To use the grayscale sensor module, import the ``Grayscale_Module`` library.

The ``Grayscale_Module`` library has two methods:

* ``get_grayscale_data()``: This method directly outputs the readings of the three sensors, from right to left. The brighter the area, the larger the value obtained.

* ``get_line_status()``: get_line_status(): This method will generate an action based on the values detected by the three probes. There are four types of actions: forward , left , right , and stop.

The trigger conditions for these actions are as follows: 
when generating the object, a number is assigned as a threshold. 
For example, ``gm = Grayscale_Module(500)`` will generate a ``gm`` object with a threshold of 500. 
When the detection value of all three probes is greater than the threshold, 
it means that the probes are sensing the color white, and no black line is detected, 
which makes the ``get_line_status()`` to generate a return value of ``stop``.


* If the right (and the first) probe detects a black line, ``right`` is returned; 
* If the middle probe detects a black line, return ``forward``; 
* If the left probe detects a black line, ``left`` is returned.
