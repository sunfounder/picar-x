15. AI Storytelling Robot with Piper and OpenAI
========================================================

In the previous lesson, we tried two built-in TTS engines on Raspberry Pi (**Espeak** and **Pico2Wave**). Now let's explore two more powerful options: **Piper** (offline, neural network-based) and **OpenAI TTS** (online, cloud-based).

* **Piper**: a local TTS engine that runs offline on Raspberry Pi.  
* **OpenAI TTS**: an online service that provides very natural, human-like voices.  

At the end, your PiCar-X will drive around and tell jokes like a little storyteller.  

.. _test_piper:

1. Testing Piper
------------------

**Steps to try it out**:

#. Create a new file:

   .. code-block:: bash

      cd ~/picar-x/example
      sudo nano test_tts_piper.py

#. Copy the example code below into the file. Press ``Ctrl+X``, then ``Y``, and finally ``Enter`` to save and exit.

   .. code-block:: python

       from picarx.tts import Piper

       tts = Piper()

       # List supported languages
       print(tts.available_countrys())

       # List models for English (en_us)
       print(tts.available_models('en_us'))

       # Set a voice model (auto-download if not already present)
       tts.set_model("en_US-amy-low")

       # Say something
       tts.say("Hello! I'm Piper TTS.")

   * ``available_countrys()``: print supported languages.  
   * ``available_models()``: list available models for that language.  
   * ``set_model()``: set the voice model (downloads automatically if missing).  
   * ``say()``: convert text to speech and play it.

#. Run the program:

   .. code-block:: bash

      sudo python3 test_tts_piper.py

#. The first time you run it, the selected voice model will be downloaded automatically. 

   * You should then hear the PiCar-X say: ``Hello! I'm Piper TTS.``

   * You can change to another language model by calling ``set_model()`` with a different name.


2. Testing OpenAI TTS
-------------------------------

**Get and save your API Key**

#. Go to |link_openai_platform| and log in. On the **API keys** page, click **Create new secret key**.

   .. image:: img/llm_openai_create.png

#. Fill in the details (Owner, Name, Project, and permissions if needed), then click **Create secret key**.

   .. image:: img/llm_openai_create_confirm.png

#. Once the key is created, copy it right away — you won't be able to see it again. If you lose it, you must generate a new one.

   .. image:: img/llm_openai_copy.png

#. In your project folder (for example: ``/picar-x/example``), create a file called ``secret.py``:

   .. code-block:: bash

       cd ~/picar-x/example
       sudo nano secret.py

#. Paste your key into the file like this:

   .. code-block:: python

       # secret.py
       # Store secrets here. Never commit this file to Git.
       OPENAI_API_KEY = "sk-xxx"

**Write and Run a Test Program**

#. Create a new file:

   .. code-block:: bash

       cd ~/picar-x/example
       sudo nano test_tts_openai.py

#. Copy the example code below into the file. Press ``Ctrl+X``, then ``Y``, and finally ``Enter`` to save and exit.

   .. code-block:: python

      from picarx.tts import OpenAI_TTS
      from secret import OPENAI_API_KEY   # or use the try/except version shown above

      # Initialize OpenAI TTS
      tts = OpenAI_TTS(api_key=OPENAI_API_KEY)
      tts.set_model('gpt-4o-mini-tts')  # low-latency TTS model
      tts.set_voice('alloy')            # pick a voice

      # Quick hello (sanity check)
      tts.say("Hello! I'm OpenAI TTS.")

#. Run the program:

   .. code-block:: bash

       sudo python3 test_tts_openai.py

#. You should hear the PiCar-X say:  

   ``Hello! I'm OpenAI TTS.``

**Available Models and Voices**

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Category
     - Options
   * - Models
     - 
       - ``tts-1``  
       - ``tts-1-hd``  
       - ``gpt-4o-mini-tts``  
       - ``accent``  
       - ``emotional-range``  
       - ``intonation``  
       - ``impressions``  
       - ``speed-of-speech``  
       - ``tone``  
       - ``whispering``
   * - Voices
     - 
       - ``alloy``  
       - ``ash``  
       - ``ballad``  
       - ``coral``  
       - ``echo``  
       - ``fable``  
       - ``nova``  
       - ``onyx``  
       - ``sage``  
       - ``shimmer``


3. Storytelling Robot
------------------------

Now that we have tested both **Piper** and **OpenAI TTS**, let’s use them in a real project:  
a **storytelling robot car** that drives around while telling jokes.  

In this program, the PiCar-X will: 

* Greet you with TTS when it starts.  
* Move forward and tell a first joke.  
* Move forward again and tell a second joke.  
* Finally drive backward, return “home,” and say goodbye.  

It’s like having a little robot storyteller on wheels! 

**Run the code**

.. code-block:: bash

    cd ~/picar-x/example
    sudo python3 15.storytelling_robot.py

**Code**


.. code-block:: python

   from picarx import Picarx
   import time

   # === TTS Configuration ===
   # Default: Piper
   from picarx.tts import Piper
   tts = Piper()
   tts.set_model("en_US-amy-low")  # use the voice model you installed

   # Optional: switch to OpenAI TTS
   # from picarx.tts import OpenAI_TTS
   # from secret import OPENAI_API_KEY
   # tts = OpenAI_TTS(api_key=OPENAI_API_KEY)
   # tts.set_model("gpt-4o-mini-tts")  # low-latency TTS model
   # tts.set_voice("alloy")            # choose a voice

   # === PiCar-X Setup ===
   px = Picarx()

   # Quick hello (sanity check)
   tts.say("Hello! I'm PiCar-X speaking with Piper.")

   def main():
       try:
           # Leg 1
           px.forward(30)
           time.sleep(3)
           px.stop()
           tts.say("Why can't your nose be twelve inches long? Because then it would be a foot!")

           # Leg 2
           px.forward(30)
           time.sleep(3)
           px.stop()
           tts.say("Why did the cow go to outer space? To see the moooon!")

           # Wrap-up
           tts.say("That's all for today. Goodbye, let's go home and sleep.")
           px.backward(30)
           time.sleep(6)
           px.stop()

       except KeyboardInterrupt:
           px.stop()
       finally:
           px.stop()
           px.set_dir_servo_angle(0)

   if __name__ == "__main__":
       main()

----

Troubleshooting
-------------------

* **No module named 'secret'**

  This means ``secret.py`` is not in the same folder as your Python file.
  Move ``secret.py`` into the same directory where you run the script, e.g.:

  .. code-block:: bash

     ls ~/picar-x/example
     # Make sure you see both: secret.py and your .py file

* **OpenAI: Invalid API key / 401**

  * Check that you pasted the full key (starts with ``sk-``) and there are no extra spaces/newlines.
  * Ensure your code imports it correctly:

    .. code-block:: python

       from secret import OPENAI_API_KEY

  * Confirm network access on your Pi (try ``ping api.openai.com``).  

* **OpenAI: Quota exceeded / billing error**

  * You may need to add billing or increase quota in the OpenAI dashboard.
  * Try again after resolving the account/billing issue.

* **Piper: tts.say() runs but no sound**

  * Make sure a voice model is actually present:

    .. code-block:: bash

       ls ~/.local/share/piper/voices

  * Confirm your model name matches exactly in code:

    .. code-block:: python

       tts.set_model("en_US-amy-low")

  * Check the audio output device/volume on your Pi (``alsamixer``), and that speakers are connected and powered.

* **ALSA / sound device errors (e.g., “Audio device busy” or “No such file or directory”)**

  * Close other programs using audio.
  * Reboot the Pi if the device stays busy.
  * For HDMI vs. headphone jack output, select the correct device in Raspberry Pi OS audio settings.

* **Permission denied when running Python**

  * Try with ``sudo`` if your environment requires it:

    .. code-block:: bash

       sudo python3 test_tts_piper.py



Comparison of TTS Engines
-------------------------

.. list-table:: Feature comparison: Espeak vs Pico2Wave vs Piper vs OpenAI TTS
   :header-rows: 1
   :widths: 18 18 20 22 22

   * - Item
     - Espeak
     - Pico2Wave
     - Piper
     - OpenAI TTS
   * - Runs on
     - Built-in on Raspberry Pi (offline)
     - Built-in on Raspberry Pi (offline)
     - Raspberry Pi / PC (offline, needs model)
     - Cloud (online, needs API key)
   * - Voice quality
     - Robotic
     - More natural than Espeak
     - Natural (neural TTS)
     - Very natural / human-like
   * - Controls
     - Speed, pitch, volume
     - Limited controls
     - Choose different voices/models
     - Choose model and voices
   * - Languages
     - Many (quality varies)
     - Limited set
     - Many voices/languages available
     - Best in English (others vary by availability)
   * - Latency / speed
     - Very fast
     - Fast
     - Real-time on Pi 4/5 with “low” models
     - Network-dependent (usually low latency)
   * - Setup
     - Minimal
     - Minimal
     - Download ``.onnx`` + ``.onnx.json`` models
     - Create API key, install client
   * - Best for
     - Quick tests, basic prompts
     - Slightly better offline voice
     - Local projects with better quality
     - Highest quality, rich voice options
