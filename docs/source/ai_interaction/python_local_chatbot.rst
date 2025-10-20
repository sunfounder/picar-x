.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!


19. Lokaler Sprach-Chatbot
===========================

In dieser Lektion kombinierst du alles, was du gelernt hast — **Spracherkennung (STT)**,  
**Text-zu-Sprache (TTS)** und ein **lokales LLM (Ollama)** — um einen vollständig offline laufenden **Sprach-Chatbot**  
auf deinem PiCar-X-System zu bauen.

Der Ablauf ist einfach:

#. **Zuhören** — Das Mikrofon erfasst deine Sprache und transkribiert sie mit **Vosk**.  
#. **Denken** — Der Text wird an ein lokales **LLM** gesendet, das auf Ollama läuft (z. B. ``llama3.2:3b``).  
#. **Sprechen** — Der Chatbot antwortet laut mit **Piper TTS**.  

So entsteht ein **freihändig bedienbarer Konversationsroboter**, der in Echtzeit verstehen und antworten kann.

----

Bevor du beginnst
-----------------

Stelle sicher, dass du Folgendes vorbereitet hast:

* :ref:`install_all_modules` — Installiere die Module ``robot-hat``, ``vilib``, ``picar-x`` und führe dann das Skript ``i2samp.sh`` aus.
* **Piper TTS** getestet (:ref:`test_piper`) und ein funktionierendes Stimmenmodell ausgewählt.  
* **Vosk STT** getestet (:ref:`test_vosk`) und das passende Sprachpaket gewählt (z. B. ``en-us``).  
* **Ollama** installiert (:ref:`download_ollama`) auf deinem Pi oder einem anderen Computer und ein Modell wie ``llama3.2:3b`` heruntergeladen (oder ein kleineres wie ``moondream:1.8b``, wenn der Speicher begrenzt ist).

----

Code ausführen
--------------

#. Öffne das Beispielskript:

   .. code-block:: bash

      cd ~/picar-x/example
      sudo nano 19.local_voice_chatbot.py

#. Passe die Parameter nach Bedarf an:

   * ``stt = Vosk(language="en-us")``: Ändere dies passend zu deinem Akzent/Sprachpaket (z. B. ``en-us``, ``zh-cn``, ``es``).  
   * ``tts.set_model("en_US-amy-low")``: Ersetze dies durch das Piper-Stimmenmodell, das du in :ref:`test_piper` verifiziert hast.  
   * ``llm = Ollama(ip="localhost", model="llama3.2:3b")``: Aktualisiere sowohl ``ip`` als auch ``model`` entsprechend deiner Umgebung.  

     * ``ip``: Wenn Ollama auf **demselben Pi** läuft, nutze ``localhost``. Läuft Ollama auf einem anderen Computer im LAN, aktiviere **Expose to network** in Ollama und setze ``ip`` auf die LAN-IP dieses Computers.  
     * ``model``: Muss exakt dem Modellnamen entsprechen, den du in Ollama heruntergeladen/aktiviert hast.  

#. Starte das Skript:

   .. code-block:: bash

      cd ~/picar-x/example
      sudo python3 19.local_voice_chatbot.py

#. Nach dem Start solltest du Folgendes sehen:

   * Der Bot begrüßt dich mit einer gesprochenen Willkommensnachricht.  
   * Er wartet auf gesprochene Eingaben.  
   * Vosk transkribiert deine Sprache in Text.  
   * Der Text wird an Ollama gesendet, das eine Antwort streamt.  
   * Die Antwort wird bereinigt (versteckte Begründungen werden entfernt) und von Piper laut gesprochen.  
   * Beende das Programm jederzeit mit ``Strg+C``.

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

Code-Analyse
-------------

**Imports und globale Einrichtung**

.. code-block:: python

   import re
   import time
   from picarx.llm import Ollama
   from picarx.stt import Vosk
   from picarx.tts import Piper

Bindet die drei zuvor erstellten Subsysteme ein:  
**Vosk** für Speech-to-Text (STT), **Ollama** für das LLM und **Piper** für Text-to-Speech (TTS).


**Initialisierung STT (Vosk)**

.. code-block:: python

   stt = Vosk(language="en-us")

Lädt das Vosk-Modell für US-Englisch.  
Ändere den Sprachcode (z. B. ``zh-cn``, ``es``), um die Erkennungsgenauigkeit an deine Sprache anzupassen.


**Initialisierung TTS (Piper)**

.. code-block:: python

   tts = Piper()
   tts.set_model("en_US-amy-low")

Erstellt eine Piper-Engine und wählt eine Stimme aus.  
Wähle ein Modell, das du zuvor in :ref:`test_piper` getestet hast. Niedrigere Qualität = schnellere Ausführung, geringere CPU-Last.


**LLM-Anweisungen und Willkommensnachricht**

.. code-block:: python

   INSTRUCTIONS = (
       "You are a helpful assistant. Answer directly in plain English. "
       "Do NOT include any hidden thinking, analysis, or tags like <think>."
   )
   WELCOME = "Hello! I'm your voice chatbot. Speak when you're ready."

Zwei wichtige UX-Designentscheidungen:

* **Kurze und direkte Antworten** sorgen für bessere TTS-Verständlichkeit.  
* Versteckte „Gedanken“-Tags (z. B. <think>) werden verboten, um saubere Ausgaben zu gewährleisten.


**Verbindung zu Ollama und Gesprächskontext setzen**

.. code-block:: python

   llm = Ollama(ip="localhost", model="llama3.2:3b")
   llm.set_max_messages(20)
   llm.set_instructions(INSTRUCTIONS)

* ``ip="localhost"`` bedeutet, dass Ollama auf demselben Pi läuft. Läuft es auf einem anderen Rechner im LAN, aktiviere **Expose to network** und nutze dessen IP-Adresse.  
* ``set_max_messages(20)`` begrenzt den Gesprächsverlauf — wichtig für Speicher und Latenz.


**Verstecktes Denken / Tags entfernen**

.. code-block:: python

   def strip_thinking(text: str) -> str:
       if not text:
           return ""
       text = re.sub(r"<\s*think[^>]*>.*?<\s*/\s*think\s*>", "", text, flags=re.DOTALL|re.IGNORECASE)
       text = re.sub(r"<\s*thinking[^>]*>.*?<\s*/\s*thinking\s*>", "", text, flags=re.DOTALL|re.IGNORECASE)
       text = re.sub(r"```(?:\s*thinking)?\s*.*?```", "", text, flags=re.DOTALL|re.IGNORECASE)
       text = re.sub(r"\[/?thinking\]", "", text, flags=re.IGNORECASE)
       return re.sub(r"\s+\n", "\n", text).strip()

Manche Modelle geben interne Tags aus (z. B. ``<think>…``).  
Diese Funktion entfernt sie, damit die Sprachausgabe **nur die finale Antwort** wiedergibt.


**Hauptschleife: Begrüßen → Zuhören → Denken → Sprechen**

.. code-block:: python

   print(WELCOME)
   tts.say(WELCOME)

Begrüßt den Benutzer über Terminal und Lautsprecher — einmalig beim Start.


**Zuhören (Streaming-STT mit Live-Partials)**

.. code-block:: python

   print("\n🎤 Listening... (Press Ctrl+C to stop)")

   text = ""
   for result in stt.listen(stream=True):
       if result["done"]:
           text = result["final"].strip()
           print(f"[YOU] {text}")
       else:
           print(f"[YOU] {result['partial']}", end="\r", flush=True)

* ``stream=True`` liefert **partielle** Transkripte in Echtzeit.  
* Das finale Ergebnis wird in ``text`` gespeichert und ausgegeben.


**Sicherung:** Wenn nichts erkannt wurde, wird der LLM-Aufruf übersprungen:

.. code-block:: python

   if not text:
       print("[INFO] Nothing recognized. Try again.")
       time.sleep(0.1)
       continue

Dadurch werden leere Eingaben vermieden → schnellere Reaktionen und weniger Rechenlast.


**Denken (LLM) mit Token-Streaming**

.. code-block:: python

   reply_accum = ""
   response = llm.prompt(text, stream=True)
   for next_word in response:
       if next_word:
           print(next_word, end="", flush=True)
           reply_accum += next_word
   print("")

* Sendet das finale Transkript an das lokale LLM.  
* Antwort wird **während des Eintreffens** angezeigt → minimale Latenz.  
* Gleichzeitig wird die vollständige Antwort in ``reply_accum`` gespeichert.


**Hinweis:** Wenn du keine Token sehen möchtest, setze ``stream=False``.


**Sprechen (bereinigt + TTS)**

.. code-block:: python

   clean = strip_thinking(reply_accum)
   if clean:
       tts.say(clean)
   else:
       tts.say("Sorry, I didn't catch that.")

* Entfernt unerwünschte Tags und spricht **nur** die eigentliche Antwort.  
* Nur **ein TTS-Aufruf** pro Antwort → klare Sprachausgabe.


**Beenden und Aufräumen**

.. code-block:: python

   except KeyboardInterrupt:
       print("\n[INFO] Stopping...")
   finally:
       tts.say("Goodbye!")
       print("Bye.")

Mit **Strg+C** stoppen. Der Bot verabschiedet sich, bevor er sauber beendet.


----

Fehlerbehebung & FAQ
---------------------

* **Modell zu groß (Speicherfehler)**

  Kleineres Modell wie ``moondream:1.8b`` verwenden oder Ollama auf leistungsfähigerem Rechner ausführen.

* **Keine Antwort von Ollama**

  Stelle sicher, dass Ollama läuft (``ollama serve`` oder Desktop-App offen).  
    Bei Remote: *Expose to network* aktivieren + IP prüfen.

* **Vosk erkennt Sprache nicht** 

  Mikrofon überprüfen. Passendes Sprachpaket (z. B. ``zh-cn``) testen.

* **Piper bleibt stumm oder gibt Fehler** 

  Stimmenmodell herunterladen und in :ref:`test_piper` testen.

* **Antworten zu lang oder unpassend**  

  ``INSTRUCTIONS`` anpassen, z. B. „Keep answers short and to the point.“




