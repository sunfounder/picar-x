Line Track
====================================

Tape a track on a light colored ground (or table) with 1 cm black insulating tape.
Run the program and you will see PiCar-X moving forward on the track.

.. warning::
    In sharp bend will cause derailment!

**code**

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

Here we call the ``Grayscale_Module`` library.

This library has two methods:

* ``get_grayscale_data()``: It will directly output the readings of the three probes (from right to left), and usually, the brighter the area, the larger the value obtained.

* ``get_line_status()``: It will generate the corresponding actions based on the values detected by the three probes. There are four types: ``forward`` , ``left`` , ``right`` , and ``stop``.

The trigger conditions for these actions are as follows: when generating the object, we pass in a number as a threshold (e.g. ``gm = Grayscale_Module(500)`` is to generate a gm object with a threshold of 500).
When the detection value of all three probes is greater than the threshold, it means that the probes are all white under the head and there are no black lines, ``get_line_status()`` generates the return value ``stop``.

* If the right (and the first) probe detects a black line, ``right`` is returned; 
* If the middle probe detects a black line, return ``forward`` ; 
* If the left probe detects a black line, ``left`` is returned.
