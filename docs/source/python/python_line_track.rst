.. _py_line_tracking:

5. Line Tracking
====================================

This project will use the Grayscale module to make the PiCar-X move forward along a line. 
Use dark-colored tape to make a line as straight as possible, and not too curved. 
Some experimenting might be needed if the PiCar-X is derailed.

**Run the Code**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 5.minecart_plus.py
    
After running the code, PiCar-X will move forward along a line.

**Code**

.. note::
    You can **Modify/Reset/Copy/Run/Stop** the code below. But before that, you need to go to  source code path like ``picar-x/example``. After modifying the code, you can run it directly to see the effect.

.. raw:: html

    <run></run>

.. code-block:: python

    from picarx import Picarx
    from time import sleep

    px = Picarx()
    # manual modify reference value
    px.set_line_reference([500, 600, 600])

    current_state = None
    px_power = 10
    offset = 20

    def get_status(val_list):
        _state = px.get_line_status(val_list)  # [bool, bool, bool], 0 means line, 1 means background
        if _state == [0, 0, 0]:
            return 'stop'
        elif _state[1] == 1:
            return 'forward'
        elif _state[0] == 1:
            return 'right'
        elif _state[2] == 1:
            return 'left'

    if __name__=='__main__':
        try:
            while True:
                gm_val_list = px.get_grayscale_data()
                gm_state = get_status(gm_val_list)
                print("gm_val_list: %s, %s"%(gm_val_list, gm_state))

                if gm_state == "stop":
                    px.stop()
                elif gm_state == 'forward':
                    px.set_dir_servo_angle(0)
                    px.forward(px_power) 
                elif gm_state == 'left':
                    px.set_dir_servo_angle(offset)
                    px.forward(px_power) 
                elif gm_state == 'right':
                    px.set_dir_servo_angle(-offset)
                    px.forward(px_power) 
        finally:
            px.stop()
            print("stop and exit")
            sleep(0.1)


                

**How it works?** 

The grayscale sensor module ``grayscale_module`` is also imported in the picarx module, and we can use some of these methods to detect black lines.

The function to detect the black line looks like this:

* ``get_grayscale_data()``: This method directly outputs the readings of the three sensors, from right to left. The brighter the area, the larger the value obtained.

* ``get_line_status(gm_val_list)``: This method compares the readings from the three probes and outputs an array of three Boolean values. A value of 1 means black is detected, and a value of 0 means white.

* ``get_status(val_list)``: This function will generate an action based on the boolean values detected by the three probes. There are four types of actions: forward , left , right , and stop.

The trigger conditions for these actions are as follows: 
A value is assigned by default in the module as the threshold for detecting black or white.
When the detection values of the three probes are all greater than the threshold,
it means that the probes are sensing the color white, and no black line is detected, 
which makes the ``get_status()`` to generate a return value of ``stop``.

* If the right (and the first) probe detects a black line, ``right`` is returned; 
* If the middle probe detects a black line, return ``forward``; 
* If the left probe detects a black line, ``left`` is returned;
* If no probe detects a black line, return ``stop``.