.. note::

    Ciao, benvenuto nella SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community su Facebook! Scopri di più su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e Condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Accedi in anteprima agli annunci di nuovi prodotti e alle anticipazioni.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Giveaway Festivi**: Partecipa a giveaway e promozioni in occasione delle festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

16. Auto a Controllo Vocale con Vosk (Offline)
==============================================

Vosk è un motore di riconoscimento vocale (STT) leggero che supporta molte lingue e funziona completamente **offline** su Raspberry Pi.  
Serve la connessione a Internet solo la prima volta per scaricare un modello linguistico. Dopo di ciò, tutto funziona senza rete.  

In questa lezione impareremo a:  

* Controllare il microfono su Raspberry Pi.  
* Installare e testare Vosk con un modello linguistico scelto.  
* Costruire una **PiCar-X a controllo vocale** che ascolta una parola di attivazione e risponde ai comandi come **forward**, **backward**, **left** e **right**.  

----

Prima di iniziare
-----------------

Assicurati di aver completato:

* :ref:`install_all_modules` — Installa i moduli ``robot-hat``, ``vilib``, ``picar-x``, poi esegui lo script ``i2samp.sh``.

----

1. Controlla il tuo Microfono
-----------------------------

Prima di utilizzare il riconoscimento vocale, assicurati che il tuo microfono USB funzioni correttamente.

#. Elenca i dispositivi di registrazione disponibili:

   .. code-block:: bash

      arecord -l

   Cerca una riga simile a ``card 1: ... device 0``.  

#. Registra un breve campione (sostituisci ``1,0`` con i numeri trovati):

   .. code-block:: bash

      arecord -D plughw:1,0 -f S16_LE -r 16000 -d 3 test.wav

   * Esempio: se il tuo dispositivo è ``card 2, device 0``, usa:

   .. code-block:: bash

      arecord -D plughw:2,0 -f S16_LE -r 16000 -d 3 test.wav

#. Riproducilo per confermare la registrazione:

   .. code-block:: bash

      aplay test.wav

#. Regola il volume del microfono se necessario:

   .. code-block:: bash

      alsamixer

   * Premi **F6** per selezionare il tuo microfono USB.  
   * Trova il canale **Mic** o **Capture**.  
   * Assicurati che non sia silenziato (**[MM]** significa muto, premi ``M`` per riattivarlo → dovrebbe mostrare **[OO]**).  
   * Usa le frecce ↑ / ↓ per modificare il volume di registrazione.


.. _test_vosk:

2. Testare Vosk
---------------

**Passaggi per provarlo**:

#. Crea un nuovo file:

   .. code-block:: bash

      cd ~/picar-x/example
      sudo nano test_stt_vosk.py

#. Copia il codice di esempio al suo interno. Premi ``Ctrl+X``, poi ``Y`` e ``Enter`` per salvare ed uscire.

   .. code-block:: python

      from picarx.stt import Vosk

      vosk = Vosk(language="en-us")

      print(vosk.available_languages)

      while True:
          print("Say something")
          result = vosk.listen(stream=False)
          print(result)

#. Esegui il programma:

   .. code-block:: bash

      sudo python3 test_stt_vosk.py

#. La prima volta che esegui questo codice con una nuova lingua, Vosk **scaricherà automaticamente il modello linguistico** (per impostazione predefinita scarica la versione **small**).  
   Allo stesso tempo, stamperà l’elenco delle lingue supportate. Poi vedrai:

   .. code-block:: text

        vosk-model-small-en-us-0.15.zip: 100%|███████████████████| 39.3M/39.3M [00:05<00:00, 7.85MB/s]
        ['ar', 'ar-tn', 'ca', 'cn', 'cs', 'de', 'en-gb', 'en-in', 'en-us', 'eo', 'es', 'fa', 'fr', 'gu', 'hi', 'it', 'ja', 'ko', 'kz', 'nl', 'pl', 'pt', 'ru', 'sv', 'te', 'tg', 'tr', 'ua', 'uz', 'vn']
        Say something

   Questo significa:

   * Il file del modello (``vosk-model-small-en-us-0.15``) è stato scaricato.  
   * L’elenco delle lingue supportate è stato stampato.  
   * Il sistema è ora in ascolto — parla nel microfono della PiCar-X e il testo riconosciuto apparirà nel terminale.

   **Suggerimenti**:

   * Tieni il microfono a circa 15–30 cm di distanza.  
   * Scegli un modello che corrisponda alla tua lingua e accento.  

**Modalità Streaming (opzionale)**

Puoi anche trasmettere la voce in streaming continuo per vedere i risultati parziali mentre parli:

.. code-block:: python

   from picarx.stt import Vosk

   vosk = Vosk(language="en-us")

   while True:
       print("Say something")
       for result in vosk.listen(stream=True):
           if result["done"]:
               print(f"final:   {result['final']}")
           else:
               print(f"partial: {result['partial']}", end="\r", flush=True)


3. Auto a Controllo Vocale
--------------------------

Ora colleghiamo il riconoscimento vocale alla PiCar-X!  

Useremo una **parola di attivazione** ("hey robot") così l’auto ascolterà i comandi solo dopo essere stata attivata. Questo risparmia CPU ed evita attivazioni indesiderate.  


**Esegui il codice**

.. code-block:: bash

   cd ~/picar-x/example
   sudo python3 16.voice_controlled_car.py

In questo programma, l’auto:

* Attende la parola di attivazione **"hey robot"**.  
* Dopo l’attivazione, puoi parlare naturalmente — finché la frase contiene una delle parole chiave (**forward**, **backward**, **left**, **right**), l’auto risponderà.  
   
  Ad esempio:

  * “Can you move forward a little?” → l’auto si muove in avanti.  
  * “Please turn left now.” → l’auto gira a sinistra. 

* Il comando **"sleep"** interrompe il ciclo di controllo e riporta l’auto in modalità attesa.  

**Codice**

.. code-block:: python

   from picarx import Picarx
   from picarx.stt import Vosk
   import time

   px = Picarx()
   stt = Vosk(language="en-us")

   WAKE_WORDS = ["hey robot"]

   print('Say "hey robot" to wake me up! Then say: forward / backward / left / right. Say "sleep" to stop listening.')

   try:
       while True:
           # --- wait for wake word once ---
           stt.wait_until_heard(WAKE_WORDS)
           print("Wake word detected. Listening for commands... (say 'sleep' to pause)")

           # --- command loop: multiple commands after one wake ---
           while True:
               res = stt.listen(stream=False)
               text = res.get("text", "") if isinstance(res, dict) else str(res)
               text = text.lower().strip()
               if not text:
                   continue

               print("Heard:", text)

               if "sleep" in text:
                   # pause command mode; go back to wait for wake word
                   px.stop(); px.set_dir_servo_angle(0)
                   print("Sleeping. Say 'hey robot' to wake me again.")
                   break

               elif "forward" in text:
                   px.set_dir_servo_angle(0)
                   px.forward(30); time.sleep(1); px.stop()

               elif "backward" in text:
                   px.set_dir_servo_angle(0)
                   px.backward(30); time.sleep(1); px.stop()

               elif "left" in text:
                   px.set_dir_servo_angle(-25)
                   px.forward(30); time.sleep(1)
                   px.stop(); px.set_dir_servo_angle(0)

               elif "right" in text:
                   px.set_dir_servo_angle(25)
                   px.forward(30); time.sleep(1)
                   px.stop(); px.set_dir_servo_angle(0)
               # (ignore other words)

   except KeyboardInterrupt:
       pass
   finally:
       px.stop(); px.set_dir_servo_angle(0)
       print("Stopped and centered. Bye.")

Risoluzione dei Problemi
------------------------

* **No such file or directory (quando esegui `arecord`)**

  Potresti aver usato il numero di scheda/dispositivo sbagliato.  
  Esegui:

  .. code-block:: bash

     arecord -l

  e sostituisci ``1,0`` con i numeri mostrati per il tuo microfono USB.

* **Il file registrato non ha audio**

  Apri il mixer e controlla il volume del microfono:

  .. code-block:: bash

     alsamixer

  * Premi **F6** per selezionare il tuo microfono USB.  
  * Assicurati che **Mic/Capture** non sia silenziato (**[OO]** invece di **[MM]**).  
  * Aumenta il livello con la freccia ↑.

* **Vosk non riconosce la voce**

  * Assicurati che il **codice lingua** corrisponda al tuo modello (ad esempio ``en-us`` per l’inglese, ``zh-cn`` per il cinese).  
  * Tieni il microfono a 15–30 cm di distanza ed evita rumori di fondo.  
  * Parla chiaramente e lentamente.

* **La parola di attivazione (“hey robot”) non viene mai rilevata**

  * Pronunciala con tono naturale, non troppo velocemente.  
  * Controlla che il programma stampi effettivamente il testo riconosciuto. Se non lo fa, il microfono non funziona.  

* **Latenza elevata / riconoscimento lento**

  * Il modello scaricato automaticamente è **small** (più veloce ma meno preciso).  
  * Se è ancora lento, chiudi altri programmi per liberare CPU.
