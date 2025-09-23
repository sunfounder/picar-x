14. Voice Prompt Car with Espeak and Pico2Wave
=================================================

In this lesson, we'll use two built-in text-to-speech (TTS) engines on Raspberry Pi — **Espeak** and **Pico2Wave** — to make the PiCar-X talk.  

These two engines are both simple and run offline, but they sound quite different:

* **Espeak**: very lightweight and fast, but the voice is robotic. You can adjust speed, pitch, and volume.  
* **Pico2Wave**: produces a smoother and more natural voice than Espeak, but has fewer options to configure.  

You'll hear the difference in **voice quality** and **features**, and then build a "voice prompt car" that announces its actions before moving.  

----

1. Testing Espeak
--------------------

Espeak is a lightweight TTS engine included in Raspberry Pi OS.  
Its voice sounds robotic, but it is highly configurable: you can adjust volume, pitch, speed, and more.  

**Steps to try it out**:

* Create a new file with the command:

  .. code-block:: bash
  
      cd ~/picar-x/example
      sudo nano test_tts_espeak.py

* Then copy the example code into it. Press ``Ctrl+X``, then ``Y``, and finally ``Enter`` to save and exit.

  .. code-block:: python
  
      from picarx import Picarx
      from robot_hat.tts import Espeak
      import time
  
      px = Picarx()
      tts = Espeak()
  
      # Quick hello (sanity check)
      tts.say("Hello! I'm Espeak TTS.")
  
      # Optional voice tuning
      # tts.set_amp(100)   # 0 to 200
      # tts.set_speed(150) # 80 to 260
      # tts.set_gap(5)     # 0 to 200
      # tts.set_pitch(50)  # 0 to 99

* Run the program with:

  .. code-block:: bash

     sudo python3 test_tts_espeak.py

* You should hear the PiCar-X say: “Hello! I'm Espeak TTS.”
* Uncomment the voice tuning lines in the code to experiment with how ``amp``, ``speed``, ``gap``, and ``pitch`` affect the sound.

----

2. Testing Pico2Wave
---------------------

Pico2Wave produces a more natural, human-like voice than Espeak.  
It's simpler to use but less flexible — you can only change the language, not the pitch or speed.

**Steps to try it out**:

* Create a new file with the command:

  .. code-block:: bash

      cd ~/picar-x/example
      sudo nano test_tts_pico2wave.py

* Then copy the example code into it. Press ``Ctrl+X``, then ``Y``, and finally ``Enter`` to save and exit.

  .. code-block:: python
  
      from picarx import Picarx
      from robot_hat.tts import Pico2Wave
      import time
  
      px = Picarx()
      tts = Pico2Wave()
  
      tts.set_lang('en-US')  # en-US, en-GB, de-DE, es-ES, fr-FR, it-IT
  
      # Quick hello (sanity check)
      tts.say("Hello! I'm Pico2Wave TTS.")

* Run the program with:

  .. code-block::

    sudo python3 test_tts_pico2wave.py

* You should hear the PiCar-X say: “Hello! I'm Pico2Wave TTS.”
* Try switching the language (for example, ``es-ES`` for Spanish) and listen to the difference.  

----

3. Voice Prompt Car
--------------------

Now let's combine **Pico2Wave** or **Espeak** with PiCar-X driving code to create a “voice prompt car”:  
before every action, the car will announce what it's about to do.

**Run the Code**

.. code-block:: bash

    cd ~/picar-x/example
    sudo python3 14.voice_promt_car.py
    
Run this code and you'll see your PiCar-X drive forward, backward, and turn, each time announcing its move first.  
This makes your car safer, friendlier, and more interactive.  

**Code**

.. code-block:: python

  from picarx import Picarx
  from robot_hat.tts import Espeak
  import time

  # If you want to try Pico2Wave instead of Espeak, uncomment below:
  # from robot_hat.tts import Pico2Wave
  # tts = Pico2Wave()
  # tts.set_lang('en-US')  # Options: en-US, en-GB, de-DE, es-ES, fr-FR, it-IT

  px = Picarx()
  tts = Espeak()

  # Quick hello (test)
  tts.say("Hello! I'm PiCar-X.")

  def main():
      try:
          # Forward
          tts.say("Moving forward")
          px.forward(30)
          time.sleep(2)
          px.stop()

          # Backward
          tts.say("Moving backward")
          px.backward(30)
          time.sleep(2)
          px.stop()

          # Turn left
          tts.say("Turning left")
          px.set_dir_servo_angle(-20)
          px.forward(30)
          time.sleep(2)
          px.stop()
          px.set_dir_servo_angle(0)

          # Turn right
          tts.say("Turning right")
          px.set_dir_servo_angle(20)
          px.forward(30)
          time.sleep(2)
          px.stop()
          px.set_dir_servo_angle(0)

      except KeyboardInterrupt:
          # Stop if interrupted
          px.stop()
      finally:
          # Reset to safe state
          px.stop()
          px.set_dir_servo_angle(0)

  if __name__ == "__main__":
      main()

----

Troubleshooting
-------------------

* **No sound when running Espeak or Pico2Wave**

  * Check that your speakers/headphones are connected and volume is not muted.  
  * Run a quick test in terminal:

    .. code-block:: bash

       espeak "Hello world"
       pico2wave -w test.wav "Hello world" && aplay test.wav

  If you hear nothing, the issue is with audio output, not your Python code.

* **Espeak voice sounds too fast or too robotic**

  * Try adjusting the parameters in your code:

    .. code-block:: python

       tts.set_speed(120)   # slower
       tts.set_pitch(60)    # different pitch

* **Permission denied when running code**

  * Try running with ``sudo``:

    .. code-block:: bash

       sudo python3 test_tts_espeak.py


Comparison: Espeak vs Pico2Wave
-------------------------------------

.. list-table::
   :widths: 20 40 40
   :header-rows: 1

   * - Feature
     - Espeak
     - Pico2Wave
   * - Voice quality
     - Robotic, synthetic
     - More natural, human-like
   * - Languages
     - Default English
     - Fewer, but common ones
   * - Adjustable
     - Yes (speed, pitch, etc.)
     - No (only language)
   * - Performance
     - Very fast, lightweight
     - Slightly slower, heavier

