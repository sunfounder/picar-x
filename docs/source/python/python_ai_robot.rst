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

You can easily switch to other **supported LLMs** or **TTS voices**:

* LLM:

  * OpenAI (gpt-4o-mini)
  * Doubao
  * Deepseek
  * Gemini
  * Qwen
  * Grok

* TTS:

  * Piper (local)
  * Espeak / Pico2Wave (lightweight)
  * OpenAI TTS (online)

To switch, simply modify the initialization part in the code:

.. code-block:: python

   from picarx.llm import Gemini as LLM
   llm = LLM(api_key="YOUR_KEY", model="gemini-pro")

   tts_model = "en_US-ryan-low"

----

Action & Sound Reference
------------------------

Below are the **action keywords** the LLM can return (after the ``ACTIONS:`` line) and what they do on the robot.

.. list-table::
   :header-rows: 1
   :widths: 18 42 40

   * - **Action**
     - **What it does**
     - **Effect**
   * - ``shake head``
     - Gimbal yaws left↔right (like “no”).
     - Pan servo oscillates; LEDs may blink.
   * - ``nod``
     - Gimbal pitches up↔down (like “yes”).
     - Tilt servo oscillates; LEDs may blink.
   * - ``wave hands``
     - Playful wave animation (gimbal/LED substitute).
     - Gimbal sweeps; LED pattern.
   * - ``resist``
     - “Refuse” gesture; reverse or shake.
     - Short backward + head shake.
   * - ``act cute``
     - Friendly pose (head tilt + blink).
     - Tilt + LED pulses.
   * - ``rub hands``
     - Anticipation motion.
     - Tiny yaw oscillations + twinkle.
   * - ``think``
     - “Thinking” pose while composing reply.
     - Slow pan/tilt + LED blink.
   * - ``twist body``
     - Steer left/right quickly in place.
     - Steering servo pulses.
   * - ``celebrate``
     - Celebration animation.
     - Wiggle + LED sparkle; optional beep.
   * - ``depressed``
     - Sad pose and fade LED.
     - Tilt down slightly; LEDs dim.

Movement & Utility
~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 22 48 30

   * - **Action**
     - **What it does**
     - **Notes**
   * - ``forward``, ``backward``
     - Drive straight for preset duration.
     - Indoor safe.
   * - ``turn_left``, ``turn_right``
     - Steer and rotate.
     - Servo angle + forward tick.
   * - ``stop``
     - Stop current motion.
     - Default if no actions.
   * - ``look_left`` / ``look_right`` / ``look_up`` / ``look_down``
     - Point gimbal in direction.
     - Scan action.
   * - ``scan``
     - Sweep head.
     - Non-blocking.

Sound Effects
~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 24 56 20

   * - **Sound**
     - **What it does**
     - **Use**
   * - ``honking``
     - Short horn sound.
     - Signal / celebrate.
   * - ``start engine``
     - Engine start sound.
     - Boot up / ready.

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

Response Format Reminder
------------------------

The LLM **must** respond in this format:

.. code-block:: text

   RESPONSE_TEXT
   ACTIONS: ACTION1, ACTION2, ...

Examples:

.. code-block:: text

   Turning my head to check the hallway. Be right back!
   ACTIONS: look_left

.. code-block:: text

   Whoa—too close! I’ll back up and beep so we stay safe.
   ACTIONS: backward, honking

.. code-block:: text

   I’m awake and listening. What’s our mission?
   ACTIONS:

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
