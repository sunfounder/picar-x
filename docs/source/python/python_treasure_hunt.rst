.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_treasure:

12. Treasure Hunt
============================

Arrange a maze in your room and place six different color cards in six corners. Then control PiCar-X to search for these color cards one by one!

.. note:: You can download and print the :download:`PDF Color Cards <https://github.com/sunfounder/sf-pdf/raw/master/prop_card/object_detection/color-cards.pdf>` for color detection.


**Run the Code**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 12.treasure_hunt.py

**View the Image**

After the code runs, the terminal will display the following prompt:

.. code-block::

    No desktop !
    * Serving Flask app "vilib.vilib" (lazy loading)
    * Environment: production
    WARNING: Do not use the development server in a production environment.
    Use a production WSGI server instead.
    * Debug mode: off
    * Running on http://0.0.0.0:9000/ (Press CTRL+C to quit)

Then you can enter ``http://<your IP>:9000/mjpg`` in the browser to view the video screen. such as:  ``http://192.168.18.113:9000/mjpg``

.. image:: img/display.png

**Code**

.. code-block:: python

    from picarx import Picarx
    from time import sleep
    from robot_hat import Music,TTS
    from vilib import Vilib
    import readchar
    import random
    import threading
    
    px = Picarx()
    
    music = Music()
    tts = TTS()
    
    manual = '''
    Press keys on keyboard to control Picar-X!
        w: Forward
        a: Turn left
        s: Backward
        d: Turn right
        space: Say the target again
        ctrl+c: Quit
    '''
    
    color = "red"
    color_list=["red","orange","yellow","green","blue","purple"]
    
    def renew_color_detect():
        global color
        color = random.choice(color_list)
        Vilib.color_detect(color)
        tts.say("Look for " + color)
    
    key = None
    lock = threading.Lock()
    def key_scan_thread():
        global key
        while True:
            key_temp = readchar.readkey()
            print('\r',end='')
            with lock:
                key = key_temp.lower()
                if key == readchar.key.SPACE:
                    key = 'space'
                elif key == readchar.key.CTRL_C:
                    key = 'quit'
                    break
            sleep(0.01)
    
    def car_move(key):
        if 'w' == key:
            px.set_dir_servo_angle(0)
            px.forward(80)
        elif 's' == key:
            px.set_dir_servo_angle(0)
            px.backward(80)
        elif 'a' == key:
            px.set_dir_servo_angle(-30)
            px.forward(80)
        elif 'd' == key:
            px.set_dir_servo_angle(30)
            px.forward(80)
    
    
    def main():
        global key
        Vilib.camera_start(vflip=False,hflip=False)
        Vilib.display(local=False,web=True)
        sleep(0.8)
        print(manual)
    
        sleep(1)
        _key_t = threading.Thread(target=key_scan_thread)
        _key_t.setDaemon(True)
        _key_t.start()
    
        tts.say("game start")
        sleep(0.05)
        renew_color_detect()
        while True:
    
            if Vilib.detect_obj_parameter['color_n']!=0 and Vilib.detect_obj_parameter['color_w']>100:
                tts.say("will done")
                sleep(0.05)
                renew_color_detect()
    
            with lock:
                if key != None and key in ('wsad'):
                    car_move(key)
                    sleep(0.5)
                    px.stop()
                    key =  None
                elif key == 'space':
                    tts.say("Look for " + color)
                    key =  None
                elif key == 'quit':
                    _key_t.join()
                    print("\n\rQuit")
                    break
    
            sleep(0.05)
    
    if __name__ == "__main__":
        try:
            main()
        except KeyboardInterrupt:
            pass
        except Exception as e:
            print(f"ERROR: {e}")
        finally:
            Vilib.camera_close()
            px.stop()
            sleep(.2)


**How it works?**

To understand the basic logic of this code, you can focus on the following key parts:

1. **Initialization and Imports:**
   Import statements at the beginning of the code to understand the libraries being used.

2. **Global Variables:**
   Definitions of global variables, such as ``color`` and ``key``, which are used throughout the code to track the target color and keyboard input.

3. ``renew_color_detect()`` :
   This function selects a random color from a list and sets it as the target color for detection. It also uses text-to-speech to announce the selected color.

4. ``key_scan_thread()`` :
   This function runs in a separate thread and continuously scans for keyboard input, updating the ``key`` variable with the pressed key. It uses a lock for thread-safe access.

5. ``car_move(key)`` :
   This function controls the movement of the PiCar-X based on the keyboard input (``key``). It sets the direction and speed of the robot's movement.

6. ``main()`` :The primary function that orchestrates the overall logic of the code. It does the following:

    * Initializes the camera and starts displaying the camera feed.
    * Creates a separate thread to scan for keyboard input.
    * Announces the start of the game using text-to-speech.
    * Enters a continuous loop to:

        * Check for detected colored objects and trigger actions when a valid object is detected.
        * Handle keyboard input to control the robot and interact with the game.
    * Handles quitting the game and exceptions like KeyboardInterrupt.
    * Ensures that the camera is closed and the PiCar-X is stopped when exiting.

By understanding these key parts of the code, 
you can grasp the fundamental logic of how the PiCar-X robot responds to keyboard 
input and detects and interacts with objects of a 
specific color using the camera and audio output capabilities.