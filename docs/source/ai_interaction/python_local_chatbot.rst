.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

19. Local Voice Chatbot
===========================

In this lesson, you will combine everything you've learned — **speech recognition (STT)**,  
**text-to-speech (TTS)**, and a **local LLM (Ollama)** — to build a fully offline **voice chatbot**  
that runs on your PiCar-X system.

The workflow is simple:

#. **Listen** — The microphone captures your speech and transcribes it with **Vosk**.  
#. **Think** — The text is sent to a local **LLM** running on Ollama (e.g., ``llama3.2:3b``).  
#. **Speak** — The chatbot answers aloud using **Piper TTS**.  

This creates a **hands-free conversational robot** that can understand and respond in real time.

----

Before You Start
----------------

Make sure you have prepared the following:

* :ref:`install_all_modules` — Install ``robot-hat``, ``vilib``, ``picar-x`` modules, then run the script ``i2samp.sh``.
* Tested **Piper TTS** (:ref:`test_piper`) and chosen a working voice model.  
* Tested **Vosk STT** (:ref:`test_vosk`) and chosen the right language pack (e.g., ``en-us``).  
* Installed **Ollama** (:ref:`download_ollama`) on your Pi or another computer, and downloaded a model such as ``llama3.2:3b`` (or a smaller one like ``moondream:1.8b`` if memory is limited).

----

Run the Code
--------------

#. Open the example script:

   .. code-block:: bash

      cd ~/picar-x/example
      sudo nano 19.local_voice_chatbot.py

#. Update the parameters as needed:

   * ``stt = Vosk(language="en-us")``: Change this to match your accent/language package (e.g., ``en-us``, ``zh-cn``, ``es``).  
   * ``tts.set_model("en_US-amy-low")``: Replace with the Piper voice model you verified in :ref:`test_piper`.  
   * ``llm = Ollama(ip="localhost", model="llama3.2:3b")``: Update both ``ip`` and ``model`` to your own setup.  

     * ``ip``: If Ollama runs on the **same Pi**, use ``localhost``. If Ollama runs on another computer in your LAN, enable **Expose to network** in Ollama and set ``ip`` to that computer’s LAN IP.  
     * ``model``: Must exactly match the model name you downloaded/activated in Ollama.  

#. Run the script:

   .. code-block:: bash

      cd ~/picar-x/example
      sudo python3 19.local_voice_chatbot.py

#. After running, you should see:

   * The bot greets you with a spoken welcome message.  
   * It waits for speech input.  
   * Vosk transcribes your speech into text.  
   * The text is sent to Ollama, which streams back a reply.  
   * The reply is cleaned (removing hidden reasoning) and spoken aloud by Piper.  
   * Stop the program anytime with ``Ctrl+C``.

----

Code
----

.. code-block:: python

   import re
   import time
   from picarx.llm import Ollama
   from picarx.stt import Vosk
   from picarx.tts import Piper

   # Initialize speech recognition
   stt = Vosk(language="en-us")

   # Initialize TTS
   tts = Piper()
   tts.set_model("en_US-amy-low")

   # Instructions for the LLM
   INSTRUCTIONS = (
       "You are a helpful assistant. Answer directly in plain English. "
       "Do NOT include any hidden thinking, analysis, or tags like <think>."
   )
   WELCOME = "Hello! I'm your voice chatbot. Speak when you're ready."

   # Initialize Ollama connection
   llm = Ollama(ip="localhost", model="llama3.2:3b")
   llm.set_max_messages(20)
   llm.set_instructions(INSTRUCTIONS)

   # Utility: clean hidden reasoning
   def strip_thinking(text: str) -> str:
       if not text:
           return ""
       text = re.sub(r"<\s*think[^>]*>.*?<\s*/\s*think\s*>", "", text, flags=re.DOTALL|re.IGNORECASE)
       text = re.sub(r"<\s*thinking[^>]*>.*?<\s*/\s*thinking\s*>", "", text, flags=re.DOTALL|re.IGNORECASE)
       text = re.sub(r"```(?:\s*thinking)?\s*.*?```", "", text, flags=re.DOTALL|re.IGNORECASE)
       text = re.sub(r"\[/?thinking\]", "", text, flags=re.IGNORECASE)
       return re.sub(r"\s+\n", "\n", text).strip()

   def main():
       print(WELCOME)
       tts.say(WELCOME)

       try:
           while True:
               print("\n🎤 Listening... (Press Ctrl+C to stop)")

               # Collect final transcript from Vosk
               text = ""
               for result in stt.listen(stream=True):
                   if result["done"]:
                       text = result["final"].strip()
                       print(f"[YOU] {text}")
                   else:
                       print(f"[YOU] {result['partial']}", end="\r", flush=True)

               if not text:
                   print("[INFO] Nothing recognized. Try again.")
                   time.sleep(0.1)
                   continue

               # Query Ollama with streaming
               reply_accum = ""
               response = llm.prompt(text, stream=True)
               for next_word in response:
                   if next_word:
                       print(next_word, end="", flush=True)
                       reply_accum += next_word
               print("")

               # Clean and speak
               clean = strip_thinking(reply_accum)
               if clean:
                   tts.say(clean)
               else:
                   tts.say("Sorry, I didn't catch that.")

               time.sleep(0.05)

       except KeyboardInterrupt:
           print("\n[INFO] Stopping...")
       finally:
           tts.say("Goodbye!")
           print("Bye.")

   if __name__ == "__main__":
       main()

----

Code Analysis
-------------

**Imports and global setup**

.. code-block:: python

   import re
   import time
   from picarx.llm import Ollama
   from picarx.stt import Vosk
   from picarx.tts import Piper

Brings in the three subsystems you built earlier:
**Vosk** for speech-to-text (STT), **Ollama** for the LLM, and **Piper** for text-to-speech (TTS).



**Initialize STT (Vosk)**

.. code-block:: python

   stt = Vosk(language="en-us")

Loads the Vosk model for US English.  
Change the language code (e.g., ``zh-cn``, ``es``) to match your voice pack for better accuracy.



**Initialize TTS (Piper)**

.. code-block:: python

   tts = Piper()
   tts.set_model("en_US-amy-low")

Creates a Piper engine and selects a specific voice.  
Pick a model you’ve tested in :ref:`test_piper`. Lower-quality voices are faster and use less CPU.



**LLM instructions and welcome line**

.. code-block:: python

   INSTRUCTIONS = (
       "You are a helpful assistant. Answer directly in plain English. "
       "Do NOT include any hidden thinking, analysis, or tags like <think>."
   )
   WELCOME = "Hello! I'm your voice chatbot. Speak when you're ready."

Two key UX choices:

* Keep **answers short and direct** (helps with TTS clarity).
* Explicitly forbid hidden “chain-of-thought” tags to reduce noisy outputs.



**Connect to Ollama and set conversation scope**

.. code-block:: python

   llm = Ollama(ip="localhost", model="llama3.2:3b")
   llm.set_max_messages(20)
   llm.set_instructions(INSTRUCTIONS)

* ``ip="localhost"`` assumes the Ollama server runs on the same Pi. If it runs on another LAN machine, put that computer’s **LAN IP** and enable *Expose to network* in Ollama.
* ``set_max_messages(20)`` keeps a short conversational history. Lower this if memory/latency is tight.

**Strip hidden reasoning / tags before speaking**

.. code-block:: python

   def strip_thinking(text: str) -> str:
       if not text:
           return ""
       text = re.sub(r"<\s*think[^>]*>.*?<\s*/\s*think\s*>", "", text, flags=re.DOTALL|re.IGNORECASE)
       text = re.sub(r"<\s*thinking[^>]*>.*?<\s*/\s*thinking\s*>", "", text, flags=re.DOTALL|re.IGNORECASE)
       text = re.sub(r"```(?:\s*thinking)?\s*.*?```", "", text, flags=re.DOTALL|re.IGNORECASE)
       text = re.sub(r"\[/?thinking\]", "", text, flags=re.IGNORECASE)
       return re.sub(r"\s+\n", "\n", text).strip()

Some models may emit internal-style tags (e.g., ``<think>…``).  
This function removes those so your TTS **only** speaks the final answer.

**Tip:** If you see other artifacts on screen (because you stream raw tokens), this function already ensures **spoken** output stays clean.

**Main loop: greet once, then listen → think → speak**

.. code-block:: python

   print(WELCOME)
   tts.say(WELCOME)

Greets the user via terminal and speaker. Happens once at startup.

**Listen (streaming STT with live partials)**

.. code-block:: python

   print("\n🎤 Listening... (Press Ctrl+C to stop)")

   text = ""
   for result in stt.listen(stream=True):
       if result["done"]:
           text = result["final"].strip()
           print(f"[YOU] {text}")
       else:
           print(f"[YOU] {result['partial']}", end="\r", flush=True)

* ``stream=True`` yields **partial** transcripts for immediate feedback and a **final** transcript when the utterance ends.
* The final recognized text is stored in ``text`` and printed once.

**Guard:** If nothing was recognized, you skip the LLM call:

.. code-block:: python

   if not text:
       print("[INFO] Nothing recognized. Try again.")
       time.sleep(0.1)
       continue

This avoids sending empty prompts to the model (saves time and tokens).

**Think (LLM) with streamed printing**

.. code-block:: python

   reply_accum = ""
   response = llm.prompt(text, stream=True)
   for next_word in response:
       if next_word:
           print(next_word, end="", flush=True)
           reply_accum += next_word
   print("")

* Sends the final transcript to the local LLM and **prints tokens as they arrive** for low latency.
* Meanwhile, you accumulate the full reply in ``reply_accum`` for post-processing.

**Note:** If you’d rather **not** show raw tokens, set ``stream=False`` and just print the final string.

**Speak (clean first, then TTS once)**

.. code-block:: python

   clean = strip_thinking(reply_accum)
   if clean:
       tts.say(clean)
   else:
       tts.say("Sorry, I didn't catch that.")

* Cleans the final text to remove hidden tags, then **speaks exactly once**.  
* Keeping TTS to a single pass avoids repeated prompts like “[LLM] / [SAY]”.


**Exit and teardown**

.. code-block:: python

   except KeyboardInterrupt:
       print("\n[INFO] Stopping...")
   finally:
       tts.say("Goodbye!")
       print("Bye.")

Use **Ctrl+C** to stop. The bot says a short goodbye to signal a clean exit.


----

Troubleshooting & FAQ
---------------------

* **Model is too large (memory error)**

  Use a smaller model like ``moondream:1.8b`` or run Ollama on a more powerful computer.  

* **No response from Ollama**

  Make sure Ollama is running (``ollama serve`` or desktop app open). If remote, enable **Expose to network** and check IP address.  

* **Vosk not recognizing speech** 

  Verify your microphone works. Try another language pack (``zh-cn``, ``es`` etc.) if needed.  

* **Piper silent or errors**  

  Confirm the chosen voice model is downloaded and tested in :ref:`test_piper`.  

* **Answers too long or off-topic**

  Edit ``INSTRUCTIONS`` to add: **“Keep answers short and to the point.”**  




