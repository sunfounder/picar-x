.. note::

    Ciao, benvenuto nella SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community su Facebook! Scopri di più su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e Condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Accedi in anteprima agli annunci di nuovi prodotti e alle anticipazioni.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Giveaway Festivi**: Partecipa a giveaway e promozioni in occasione delle festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

19. Chatbot Vocale Locale
===========================

In questa lezione combinerai tutto ciò che hai imparato — **riconoscimento vocale (STT)**,  
**sintesi vocale (TTS)** e un **LLM locale (Ollama)** — per creare un **chatbot vocale** completamente offline  
che gira sul tuo sistema PiCar-X.

Il flusso di lavoro è semplice:

#. **Ascolta** — Il microfono cattura la tua voce e la trascrive con **Vosk**.  
#. **Pensa** — Il testo viene inviato a un **LLM locale** in esecuzione su Ollama (es. ``llama3.2:3b``).  
#. **Parla** — Il chatbot risponde ad alta voce usando **Piper TTS**.  

Questo crea un **robot conversazionale hands-free** che può capire e rispondere in tempo reale.

----

Prima di iniziare
--------------------

Assicurati di aver preparato quanto segue:

* :ref:`install_all_modules` — Installa i moduli ``robot-hat``, ``vilib``, ``picar-x``, quindi esegui lo script ``i2samp.sh``.
* Hai testato **Piper TTS** (:ref:`test_piper`) e scelto un modello vocale funzionante.  
* Hai testato **Vosk STT** (:ref:`test_vosk`) e scelto il pacchetto lingua corretto (es. ``en-us``).  
* Hai installato **Ollama** (:ref:`download_ollama`) sul tuo Pi o su un altro computer, e scaricato un modello come ``llama3.2:3b`` (oppure uno più piccolo come ``moondream:1.8b`` se la memoria è limitata).

----

Eseguire il codice
------------------

#. Apri lo script di esempio:

   .. code-block:: bash

      cd ~/picar-x/example
      sudo nano 19.local_voice_chatbot.py

#. Aggiorna i parametri secondo necessità:

   * ``stt = Vosk(language="en-us")``: Cambialo per abbinarlo al tuo accento/pacchetto lingua (es. ``en-us``, ``zh-cn``, ``es``).  
   * ``tts.set_model("en_US-amy-low")``: Sostituisci con il modello vocale Piper che hai verificato in :ref:`test_piper`.  
   * ``llm = Ollama(ip="localhost", model="llama3.2:3b")``: Aggiorna sia ``ip`` sia ``model`` in base alla tua configurazione.  

     * ``ip``: Se Ollama gira **sullo stesso Pi**, usa ``localhost``. Se Ollama gira su un altro computer della tua LAN, abilita **Expose to network** in Ollama e imposta ``ip`` all’IP LAN di quel computer.  
     * ``model``: Deve corrispondere **esattamente** al nome del modello che hai scaricato/attivato in Ollama.  

#. Esegui lo script:

   .. code-block:: bash

      cd ~/picar-x/example
      sudo python3 19.local_voice_chatbot.py

#. Dopo l’avvio dovresti vedere:

   * Il bot ti saluta con un messaggio vocale di benvenuto.  
   * Attende un input vocale.  
   * Vosk trascrive la tua voce in testo.  
   * Il testo viene inviato a Ollama, che restituisce la risposta in streaming.  
   * La risposta viene ripulita (rimozione del ragionamento nascosto) e letta ad alta voce da Piper.  
   * Puoi interrompere il programma in qualsiasi momento con ``Ctrl+C``.

----

Codice
--------


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

Analisi del Codice
------------------

**Import e configurazione globale**

.. code-block:: python

   import re
   import time
   from picarx.llm import Ollama
   from picarx.stt import Vosk
   from picarx.tts import Piper

Importa i tre sottosistemi costruiti in precedenza:
**Vosk** per speech-to-text (STT), **Ollama** per l’LLM e **Piper** per text-to-speech (TTS).

**Inizializza STT (Vosk)**

.. code-block:: python

   stt = Vosk(language="en-us")

Carica il modello Vosk per l’inglese USA.  
Cambia il codice della lingua (ad es. ``zh-cn``, ``es``) in base al tuo pacchetto vocale per una migliore accuratezza.

**Inizializza TTS (Piper)**

.. code-block:: python

   tts = Piper()
   tts.set_model("en_US-amy-low")

Crea un motore Piper e seleziona una voce specifica.  
Scegli un modello che hai già testato in :ref:`test_piper`. Le voci “low” consumano meno CPU e sono più veloci.

**Istruzioni per l’LLM e messaggio di benvenuto**

.. code-block:: python

   INSTRUCTIONS = (
       "You are a helpful assistant. Answer directly in plain English. "
       "Do NOT include any hidden thinking, analysis, or tags like <think>."
   )
   WELCOME = "Hello! I'm your voice chatbot. Speak when you're ready."

Due scelte UX fondamentali:

* Mantieni le **risposte brevi e dirette** (aiuta la chiarezza con TTS).
* Vietare esplicitamente i tag di “catena di pensiero” nascosti per ridurre output rumorosi.

**Connessione a Ollama e ambito della conversazione**

.. code-block:: python

   llm = Ollama(ip="localhost", model="llama3.2:3b")
   llm.set_max_messages(20)
   llm.set_instructions(INSTRUCTIONS)

* ``ip="localhost"`` presuppone che il server Ollama giri sullo stesso Pi. Se gira su un’altra macchina in LAN, usa l’**IP LAN** di quel computer e abilita *Expose to network* in Ollama.
* ``set_max_messages(20)`` mantiene una cronologia breve. Riducilo se memoria/latenza sono critici.

**Rimuovere ragionamenti/tag nascosti prima di parlare**

.. code-block:: python

   def strip_thinking(text: str) -> str:
       if not text:
           return ""
       text = re.sub(r"<\s*think[^>]*>.*?<\s*/\s*think\s*>", "", text, flags=re.DOTALL|re.IGNORECASE)
       text = re.sub(r"<\s*thinking[^>]*>.*?<\s*/\s*thinking\s*>", "", text, flags=re.DOTALL|re.IGNORECASE)
       text = re.sub(r"```(?:\s*thinking)?\s*.*?```", "", text, flags=re.DOTALL|re.IGNORECASE)
       text = re.sub(r"\[/?thinking\]", "", text, flags=re.IGNORECASE)
       return re.sub(r"\s+\n", "\n", text).strip()

Alcuni modelli possono emettere tag in stile interno (es. ``<think>…``).  
Questa funzione li rimuove così che il TTS **pronunci solo** la risposta finale.

**Suggerimento:** Se vedi altri artefatti a schermo (perché fai streaming dei token), questa funzione garantisce comunque che l’audio **resti pulito**.

**Loop principale: saluta una volta, poi ascolta → pensa → parla**

.. code-block:: python

   print(WELCOME)
   tts.say(WELCOME)

Saluta via terminale e altoparlante. Accade una sola volta all’avvio.

**Ascolto (STT in streaming con parziali live)**

.. code-block:: python

   print("\n🎤 Listening... (Press Ctrl+C to stop)")

   text = ""
   for result in stt.listen(stream=True):
       if result["done"]:
           text = result["final"].strip()
           print(f"[YOU] {text}")
       else:
           print(f"[YOU] {result['partial']}", end="\r", flush=True)

* ``stream=True`` produce trascrizioni **parziali** per un feedback immediato e una trascrizione **finale** al termine dell’enunciato.
* Il testo finale riconosciuto viene salvato in ``text`` e stampato una volta.

**Guardia:** se non è stato riconosciuto nulla, salta la chiamata all’LLM:

.. code-block:: python

   if not text:
       print("[INFO] Nothing recognized. Try again.")
       time.sleep(0.1)
       continue

Evita di inviare prompt vuoti al modello (risparmia tempo e token).

**Pensa (LLM) con stampa in streaming**

.. code-block:: python

   reply_accum = ""
   response = llm.prompt(text, stream=True)
   for next_word in response:
       if next_word:
           print(next_word, end="", flush=True)
           reply_accum += next_word
   print("")

* Invia la trascrizione finale all’LLM locale e **stampa i token in arrivo** per bassa latenza.
* Nel frattempo accumuli l’intera risposta in ``reply_accum`` per la post-elaborazione.

**Nota:** Se preferisci **non** mostrare i token grezzi, usa ``stream=False`` e stampa solo la stringa finale.

**Parla (prima pulisci, poi un solo passaggio TTS)**

.. code-block:: python

   clean = strip_thinking(reply_accum)
   if clean:
       tts.say(clean)
   else:
       tts.say("Sorry, I didn't catch that.")

* Pulisce il testo finale dai tag nascosti, poi **parla una sola volta**.  
* Un solo passaggio TTS evita ripetizioni tipo “[LLM] / [SAY]”.

**Uscita e chiusura**

.. code-block:: python

   except KeyboardInterrupt:
       print("\n[INFO] Stopping...")
   finally:
       tts.say("Goodbye!")
       print("Bye.")

Usa **Ctrl+C** per fermare. Il bot pronuncia un breve saluto per segnalare una chiusura pulita.

----

Risoluzione dei Problemi e FAQ
------------------------------

* **Il modello è troppo grande (errore di memoria)**

  Usa un modello più piccolo come ``moondream:1.8b`` oppure esegui Ollama su un computer più potente.

* **Nessuna risposta da Ollama**

  Assicurati che Ollama sia in esecuzione (``ollama serve`` oppure l’app desktop aperta).  
  Se è remoto, abilita **Expose to network** e controlla l’indirizzo IP.

* **Vosk non riconosce la voce**

  Verifica che il microfono funzioni. Se necessario, prova un altro pacchetto linguistico (``zh-cn``, ``es`` ecc.).

* **Piper muto o con errori**

  Controlla che il modello vocale scelto sia scaricato e testato in :ref:`test_piper`.

* **Risposte troppo lunghe o fuori tema**

  Modifica ``INSTRUCTIONS`` aggiungendo: **“Keep answers short and to the point.”** (Mantieni le risposte brevi e dirette).




