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
    # px = Picarx(grayscale_pins=['A0', 'A1', 'A2'])

    # Please run ./calibration/grayscale_calibration.py to Auto calibrate grayscale values
    # or manual modify reference value by follow code
    # px.set_line_reference([1400, 1400, 1400])

    current_state = None
    px_power = 10
    offset = 20
    last_state = "stop"

    def outHandle():
        global last_state, current_state
        if last_state == 'left':
            px.set_dir_servo_angle(-30)
            px.backward(10)
        elif last_state == 'right':
            px.set_dir_servo_angle(30)
            px.backward(10)
        while True:
            gm_val_list = px.get_grayscale_data()
            gm_state = get_status(gm_val_list)
            print("outHandle gm_val_list: %s, %s"%(gm_val_list, gm_state))
            currentSta = gm_state
            if currentSta != last_state:
                break
        sleep(0.001)

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

                if gm_state != "stop":
                    last_state = gm_state

                if gm_state == 'forward':
                    px.set_dir_servo_angle(0)
                    px.forward(px_power) 
                elif gm_state == 'left':
                    px.set_dir_servo_angle(offset)
                    px.forward(px_power) 
                elif gm_state == 'right':
                    px.set_dir_servo_angle(-offset)
                    px.forward(px_power) 
                else:
                    outHandle()
        finally:
            px.stop()
            print("stop and exit")
            sleep(0.1)
       

**How it works?** 

This Python script controls a Picarx robot car using grayscale sensors for navigation. Here's a breakdown of its main components:

* Import and Initialization:

    The script imports the Picarx class for controlling the robot car and the sleep function from the time module for adding delays.

    An instance of Picarx is created, and there's a commented line showing an alternative initialization with specific grayscale sensor pins.

    .. code-block:: python
        
        from picarx import Picarx
        from time import sleep

        px = Picarx()

* Configuration and Global Variables:

    ``current_state``, ``px_power``, ``offset``, and ``last_state`` are global variables used to track and control the car's movement. ``px_power`` sets the motor power, and ``offset`` is used for adjusting the steering angle.

    .. code-block:: python

        current_state = None
        px_power = 10
        offset = 20
        last_state = "stop"

* ``outHandle`` Function:

    This function is called when the car needs to handle an 'out of line' scenario.

    It adjusts the car's direction based on ``last_state`` and checks the grayscale sensor values to determine the new state.

    .. code-block:: python

        def outHandle():
            global last_state, current_state
            if last_state == 'left':
                px.set_dir_servo_angle(-30)
                px.backward(10)
            elif last_state == 'right':
                px.set_dir_servo_angle(30)
                px.backward(10)
            while True:
                gm_val_list = px.get_grayscale_data()
                gm_state = get_status(gm_val_list)
                print("outHandle gm_val_list: %s, %s"%(gm_val_list, gm_state))
                currentSta = gm_state
                if currentSta != last_state:
                    break
            sleep(0.001)

* ``get_status`` Function:

    It interprets the grayscale sensor data (``val_list``) to determine the car's navigation state.

    The car's state can be 'forward', 'left', 'right', or 'stop', based on which sensor detects the line.

    .. code-block:: python
        
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

* Main Loop:

    The ``while True`` loop continuously checks the grayscale data and adjusts the car's movement accordingly.

    Depending on the ``gm_state``, it sets the steering angle and movement direction.

    .. code-block:: python

        if __name__=='__main__':
            try:
                while True:
                    gm_val_list = px.get_grayscale_data()
                    gm_state = get_status(gm_val_list)
                    print("gm_val_list: %s, %s"%(gm_val_list, gm_state))

                    if gm_state != "stop":
                        last_state = gm_state

                    if gm_state == 'forward':
                        px.set_dir_servo_angle(0)
                        px.forward(px_power) 
                    elif gm_state == 'left':
                        px.set_dir_servo_angle(offset)
                        px.forward(px_power) 
                    elif gm_state == 'right':
                        px.set_dir_servo_angle(-offset)
                        px.forward(px_power) 
                    else:
                        outHandle()

* Safety and Cleanup:

    The ``try...finally`` block ensures the car stops when the script is interrupted or finished.

    .. code-block:: python
        
        finally:
        px.stop()
        print("stop and exit")
        sleep(0.1)

In summary, the script uses grayscale sensors to navigate the Picarx robot car. It continuously reads the sensor data to determine the direction and adjusts the car's movement and steering accordingly. The outHandle function provides additional logic for situations where the car needs to adjust its path significantly.