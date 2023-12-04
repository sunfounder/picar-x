6. Cliff Detection 
===========================

Let us give Pico-4wd a little self-protection awareness and let it learn to use its own grayscale module to avoid rushing down the cliff.

In this example, the car will be dormant. 
If you push it to a cliff, it will be awakened urgently, then back up, and say "danger".

**Run the Code**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 6.cliff_detection.py
    

**Code**

.. note::
    You can **Modify/Reset/Copy/Run/Stop** the code below. But before that, you need to go to  source code path like ``picar-x/example``. After modifying the code, you can run it directly to see the effect.

.. raw:: html

    <run></run>

.. code-block:: python

    from picarx import Picarx
    from time import sleep
    from robot_hat import TTS

    tts = TTS()
    tts.lang("en-US")

    px = Picarx()
    # px = Picarx(grayscale_pins=['A0', 'A1', 'A2'])
    # manual modify reference value
    px.set_cliff_reference([200, 200, 200])

    current_state = None
    px_power = 10
    offset = 20
    last_state = "safe"

    if __name__=='__main__':
        try:
            while True:
                gm_val_list = px.get_grayscale_data()
                gm_state = px.get_cliff_status(gm_val_list)
                # print("cliff status is:  %s"%gm_state)

                if gm_state is False:
                    state = "safe"
                    px.stop()
                else:
                    state = "danger"   
                    px.backward(80)
                    if last_state is "safe":
                        tts.say("danger")
                        sleep(0.1)
                last_state = state

        finally:
            px.stop()
            print("stop and exit")
            sleep(0.1)

**How it works?** 

The function to detect the cliff looks like this:

* ``get_grayscale_data()``: This method directly outputs the readings of the three sensors, from right to left. The brighter the area, the larger the value obtained.

* ``get_cliff_status(gm_val_list)``: This method compares the readings from the three probes and outputs a result. If the result is true, it is detected that there is a cliff in front of the car.
