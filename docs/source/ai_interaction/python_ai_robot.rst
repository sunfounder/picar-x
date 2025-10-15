.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _ai_voice_assistant_car:

21. AI Voice Assistant Car
===========================

This lesson turns your PiCar-X into an **AI-powered voice assistant on wheels**.  
The robot can wake up to your voice, recognize what you say, talk back with emotion,  
and act out its “feelings” through movements, gestures, and lights.

You'll build a **fully interactive voice assistant car** using:

* **LLM** - Large Language Model (OpenAI GPT or Doubao).  
* **STT** - Speech-to-Text (voice to text).  
* **TTS** - Text-to-Speech (text to voice).  
* **Sensors + Actions** - Ultrasonic, camera, and built-in expressive actions.

----

Before You Start
----------------

Make sure you‘ve completed:

* :ref:`test_piper` — Check the supported languages of **Piper TTS**.  
* :ref:`test_vosk` — Check the supported languages of **Vosk STT**.  
* :ref:`py_online_llm` — This step is **very important**: obtain your **OpenAI** or **Doubao** API key, or the API key for any other supported LLM.

You should already have:

* A working **microphone** and **speaker** on your PiCar-X.  
* A **valid API key** stored in ``secret.py``.  
* A stable network connection (a **wired connection** is recommended for better stability).

----

Run the Example
---------------

Both language versions are placed in the same directory:

.. code-block:: bash

   cd ~/picar-x/example

**English version** (OpenAI GPT, instructions in English):

.. code-block:: bash

   sudo python3 21.voice_active_car_gpt.py

* LLM: ``OpenAI GPT-4o-mini``  
* TTS: ``en_US-ryan-low`` (Piper)  
* STT: Vosk (``en-us``)

Wake word:

.. code-block::

   "Hey buddy"

---

**Chinese version** (Doubao, instructions in Chinese):

.. code-block:: bash

   sudo python3 21.voice_active_car_doubao_cn.py

* LLM: ``Doubao-seed-1-6-250615``  
* TTS: ``zh_CN-huayan-x_low`` (Piper)  
* STT: Vosk (``cn``)

Wake word:

.. code-block::

   "你好 滴滴"

.. note::

   You can modify the **wake word** and **robot name** in the code:
   ``NAME = "Buddy"`` or ``NAME = "滴滴"``  
   ``WAKE_WORD = ["hey buddy"]`` or ``WAKE_WORD = ["你好 滴滴"]``

----

What Will Happen
-----------------

When you run this example successfully:

* The robot **waits for the wake word** (e.g., “Hey Buddy” / “你好 滴滴”).  
* When it hears the wake word:

  * LEDs will **blink** and stay on.  
  * The robot **greets you** with a cheerful voice.

* It then starts **listening to your voice** in real time.  
* After recognizing what you said, it:

  * Sends your speech to the **LLM** (OpenAI or Doubao).  
  * **Thinks** and blinks LED while processing.  
  * Replies with **TTS voice**.
  * Executes **corresponding actions** (e.g., nodding, turning, celebrating).

* If you approach it too closely, the ultrasonic sensor:

  * Triggers an auto **backward** move for safety.
  * Interrupts the current round with a warning response.

**Example interaction**

.. code-block:: text

   You: Hey Buddy
   Robot: Hi there!

   You: Turn left and look around.
   Robot: Roger that, turning my head left like a curious cat!
   ACTIONS: turn_left, look_left

----

Switching to Other LLMs or TTS
------------------------------

You can easily switch to other LLMs, TTS, or STT languages with just a few edits:

* Supported LLMs:

  * OpenAI
  * Doubao
  * Deepseek
  * Gemini
  * Qwen
  * Grok

* :ref:`test_piper` — Check the supported languages of **Piper TTS**.  
* :ref:`test_vosk` — Check the supported languages of **Vosk STT**.  

To switch, simply modify the initialization part in the code:

.. code-block:: python

   from picarx.llm import Gemini as LLM
   llm = LLM(api_key="YOUR_KEY", model="gemini-pro")

   # Set models and languages
   TTS_MODEL = "en_US-ryan-low"
   STT_LANGUAGE = "en-us"

----

Action & Sound Reference
------------------------

Below are the **action keywords** the LLM can return (after the ``ACTIONS:`` line) and what they do on the robot.

.. list-table::
   :header-rows: 1
   :widths: 20 55 25

   * - **Action**
     - **What it does (per preset_actions.py)**
     - **Effect / Notes**
   * - ``shake head``
     - Quickly swings camera pan angle right↔left in diminishing steps, then centers.
     - “No” gesture; wheels remain stopped.
   * - ``nod``
     - Bobs camera tilt up↔down twice, then centers.
     - “Yes” gesture; wheels remain stopped.
   * - ``wave hands``
     - Tilts camera, then steers left/right twice (±25°) and centers.
     - Playful wave (uses steering servo as “arms”).
   * - ``resist``
     - Small tilt; alternates (steer ±15°, pan ±15°) 3 times; stops and centers.
     - “Refuse”/defensive motion.
   * - ``act cute``
     - Head tilt down; quick forward/back micro-shuffles (short motor pulses), then reset.
     - Bouncy “cute” move; very short motions.
   * - ``rub hands``
     - Repeated small steering oscillation (±6°) five times; reset.
     - Mimics “rubbing hands together”.
   * - ``think``
     - Smooth pan right + tilt down + steer right sweep; brief hold; small poised pose; reset.
     - Used as a single “thinking” animation.
   * - ``twist body``
     - Three cycles of short forward/stop/pan-left/steer-left, then short backward/stop/pan-right/steer-right.
     - Gives a body “twist” vibe.
   * - ``celebrate``
     - Tilt up; two right pan/steer flourishes, then two left flourishes; returns to center.
     - Festive, symmetrical flourish.
   * - ``depressed``
     - Series of downward tilt pulses with varying angles and pauses; ends after a long beat and resets.
     - “Sad” posture sequence.

Movement & Utility
~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 22 58 20

   * - **Action**
     - **What it does**
     - **Notes**
   * - ``forward``
     - Drive forward at low speed for ~1 second, then stop.
     - Implemented by ``forward(car)`` (5% speed + 1s).
   * - ``backward``
     - Drive backward at low speed for ~1 second, then stop.
     - Implemented by ``backward(car)`` (5% speed + 1s).

Sound Effects
~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 24 56 20

   * - **Sound**
     - **What it does**
     - **Notes**
   * - ``honking``
     - Plays ``car-double-horn.wav`` asynchronously (volume ~100).
     - Triggered via ``Music.sound_play_threading``.
   * - ``start engine``
     - Plays ``car-start-engine.wav`` asynchronously (volume ~50).
     - Boot/ready cue.

Sensor Triggers (Automatic)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Ultrasonic proximity** 

  * Trigger: distance < 10 cm  
  * Side effect: auto ``backward`` + disable image for this round  
  * Injected message: ``<<<Ultrasonic sense too close: {distance}cm>>>``

Lifecycle Hooks (LED Indicators)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ``before_listen`` → blink twice (ready to listen)  
* ``before_think`` → blinking (thinking)  
* ``before_say`` → LED on (speaking)  
* ``after_say`` → wait for actions → LED off  
* ``on_stop`` → stop actions, close devices


----

Troubleshooting
---------------

* **The robot doesn’t respond to wake word**  

  * Check if the microphone works.  
  * Ensure ``WAKE_ENABLE = True``.  
  * Adjust wake word to match your pronunciation.

* **No sound from the speaker**
 
  * Verify TTS model setup.  
  * Test Piper or Espeak manually.  
  * Check speaker connection and volume.

* **API Key error or timeout** 
 
  * Check your key in ``secret.py``.  
  * Ensure network connection.  
  * Confirm the LLM is supported.

* **Picar-X doesn't move or act**
 
  * Check that the action name matches ``actions_dict``.  
  * Verify motor and servo connections.

* **Ultrasonic sensor keeps triggering unexpectedly.**  

  * Check sensor installation height and angle.  
  * Adjust the ``TOO_CLOSE`` distance threshold in code.
