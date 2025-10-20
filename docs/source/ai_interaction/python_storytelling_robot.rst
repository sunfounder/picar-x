.. note::

    Ciao, benvenuto nella SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community su Facebook! Scopri di più su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e Condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Accedi in anteprima agli annunci di nuovi prodotti e alle anticipazioni.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Giveaway Festivi**: Partecipa a giveaway e promozioni in occasione delle festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

15. Robot Narratore AI con Piper e OpenAI
========================================================

Nella lezione precedente abbiamo provato due motori TTS integrati su Raspberry Pi (**Espeak** e **Pico2Wave**).  
Ora esploreremo due opzioni più potenti: **Piper** (offline, basato su rete neurale) e **OpenAI TTS** (online, basato su cloud).

* **Piper**: un motore TTS locale che funziona offline su Raspberry Pi.  
* **OpenAI TTS**: un servizio online che fornisce voci molto naturali e realistiche.  

Alla fine, il tuo PiCar-X si muoverà e racconterà barzellette come un piccolo narratore.  

----

Prima di iniziare
-----------------

Assicurati di aver completato:

* :ref:`install_all_modules` — Installa i moduli ``robot-hat``, ``vilib``, ``picar-x``, poi esegui lo script ``i2samp.sh``.

----

.. _test_piper:

1. Testare Piper
------------------

**Passaggi per provarlo**:

#. Crea un nuovo file:

   .. code-block:: bash

      cd ~/picar-x/example
      sudo nano test_tts_piper.py

#. Copia il codice di esempio qui sotto nel file. Premi ``Ctrl+X``, poi ``Y`` e infine ``Enter`` per salvare e uscire.

   .. code-block:: python

       from picarx.tts import Piper

       tts = Piper()

       # Elenca le lingue supportate
       print(tts.available_countrys())

       # Elenca i modelli per l’inglese (en_us)
       print(tts.available_models('en_us'))

       # Imposta un modello vocale (download automatico se non presente)
       tts.set_model("en_US-amy-low")

       # Pronuncia qualcosa
       tts.say("Hello! I'm Piper TTS.")

   * ``available_countrys()``: stampa le lingue supportate.  
   * ``available_models()``: elenca i modelli disponibili per quella lingua.  
   * ``set_model()``: imposta il modello vocale (scarica automaticamente se manca).  
   * ``say()``: converte il testo in voce e lo riproduce.

#. Esegui il programma:

   .. code-block:: bash

      sudo python3 test_tts_piper.py

#. Alla prima esecuzione, il modello vocale selezionato verrà scaricato automaticamente. 

   * Dovresti sentire il PiCar-X dire: ``Hello! I'm Piper TTS.``

   * Puoi cambiare lingua o voce chiamando ``set_model()`` con un nome diverso.


2. Testare OpenAI TTS
-------------------------------

**Ottieni e salva la tua API Key**

#. Vai su |link_openai_platform| ed effettua il login. Nella pagina **API keys**, clicca su **Create new secret key**.

   .. image:: img/llm_openai_create.png

#. Compila i dettagli (Proprietario, Nome, Progetto e permessi se necessario), poi clicca su **Create secret key**.

   .. image:: img/llm_openai_create_confirm.png

#. Una volta creata la chiave, copiala subito — non potrai più visualizzarla. Se la perdi, dovrai generarne una nuova.

   .. image:: img/llm_openai_copy.png

#. Nella cartella del tuo progetto (per esempio: ``/picar-x/example``), crea un file chiamato ``secret.py``:

   .. code-block:: bash

       cd ~/picar-x/example
       sudo nano secret.py

#. Incolla la tua chiave nel file in questo modo:

   .. code-block:: python

       # secret.py
       # Memorizza le chiavi qui. Non committare mai questo file su Git.
       OPENAI_API_KEY = "sk-xxx"

**Scrivi ed esegui un programma di test**

#. Crea un nuovo file:

   .. code-block:: bash

       cd ~/picar-x/example
       sudo nano test_tts_openai.py

#. Copia il codice di esempio seguente nel file. Premi ``Ctrl+X``, poi ``Y`` e infine ``Enter`` per salvare ed uscire.

   .. code-block:: python

      from picarx.tts import OpenAI_TTS
      from secret import OPENAI_API_KEY   # oppure usa la versione try/except mostrata sopra

      # Inizializza OpenAI TTS
      tts = OpenAI_TTS(api_key=OPENAI_API_KEY)
      tts.set_model('gpt-4o-mini-tts')  # modello TTS a bassa latenza
      tts.set_voice('alloy')            # scegli una voce

      # Saluto rapido (verifica base)
      tts.say("Hello! I'm OpenAI TTS.")

#. Esegui il programma:

   .. code-block:: bash

       sudo python3 test_tts_openai.py

#. Dovresti sentire il PiCar-X dire:  

   ``Hello! I'm OpenAI TTS.``

**Modelli e Voci Disponibili**

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - Categoria
     - Opzioni
   * - Modelli
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
   * - Voci
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

3. Robot Narratore
------------------------

Ora che abbiamo testato sia **Piper** che **OpenAI TTS**, usiamoli in un vero progetto:  
una **macchinina robot narratrice** che si muove e racconta barzellette.

In questo programma, il PiCar-X:

* Ti saluterà con la voce TTS all’avvio.  
* Si muoverà in avanti e racconterà la prima barzelletta.  
* Si muoverà ancora in avanti e racconterà la seconda barzelletta.  
* Infine tornerà indietro “a casa” e dirà addio.

È come avere un piccolo robot narratore su ruote!

**Esegui il codice**

.. code-block:: bash

    cd ~/picar-x/example
    sudo python3 15.storytelling_robot.py

**Codice**

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

  Significa che ``secret.py`` non si trova nella stessa cartella del tuo file Python.
  Sposta ``secret.py`` nella stessa directory in cui esegui lo script, ad esempio:

  .. code-block:: bash

     ls ~/picar-x/example
     # Assicurati di vedere entrambi: secret.py e il tuo file .py

* **OpenAI: Invalid API key / 401**

  * Verifica di aver incollato l’intera chiave (inizia con ``sk-``) e che non ci siano spazi/a-capo extra.
  * Assicurati che il codice la importi correttamente:

    .. code-block:: python

       from secret import OPENAI_API_KEY

  * Conferma l’accesso di rete sul tuo Pi (prova ``ping api.openai.com``).  

* **OpenAI: Quota exceeded / billing error**

  * Potrebbe essere necessario aggiungere un metodo di pagamento o aumentare la quota nella dashboard OpenAI.
  * Riprova dopo aver risolto il problema di account/fatturazione.

* **Piper: tts.say() viene eseguito ma non si sente nulla**

  * Assicurati che un modello vocale sia effettivamente presente:

    .. code-block:: bash

       ls ~/.local/share/piper/voices

  * Verifica che il nome del modello coincida esattamente nel codice:

    .. code-block:: python

       tts.set_model("en_US-amy-low")

  * Controlla dispositivo/volume di uscita audio sul tuo Pi (``alsamixer``) e che gli altoparlanti siano collegati e alimentati.

* **Errori ALSA / dispositivo audio (es., “Audio device busy” o “No such file or directory”)**

  * Chiudi altri programmi che usano l’audio.
  * Riavvia il Pi se il dispositivo resta occupato.
  * Per uscita HDMI vs. jack cuffie, seleziona il dispositivo corretto nelle impostazioni audio di Raspberry Pi OS.

* **Permission denied durante l’esecuzione di Python**

  * Prova con ``sudo`` se il tuo ambiente lo richiede:

    .. code-block:: bash

       sudo python3 test_tts_piper.py



Comparison of TTS Engines
----------------------------

.. list-table:: Feature comparison: Espeak vs Pico2Wave vs Piper vs OpenAI TTS
   :header-rows: 1
   :widths: 18 18 20 22 22

   * - Item
     - Espeak
     - Pico2Wave
     - Piper
     - OpenAI TTS
   * - Runs on
     - Integrato su Raspberry Pi (offline)
     - Integrato su Raspberry Pi (offline)
     - Raspberry Pi / PC (offline, richiede modello)
     - Cloud (online, richiede chiave API)
   * - Voice quality
     - Robotica
     - Più naturale di Espeak
     - Naturale (neural TTS)
     - Molto naturale / simile a umana
   * - Controls
     - Velocità, intonazione, volume
     - Controlli limitati
     - Scelta di voci/modelli diversi
     - Scelta di modello e voci
   * - Languages
     - Molte (qualità variabile)
     - Set limitato
     - Molte voci/lingue disponibili
     - Migliore in inglese (altre variano per disponibilità)
   * - Latency / speed
     - Molto veloce
     - Veloce
     - In tempo reale su Pi 4/5 con modelli “low”
     - Dipendente dalla rete (di solito bassa latenza)
   * - Setup
     - Minimo
     - Minimo
     - Download modelli ``.onnx`` + ``.onnx.json``
     - Creare chiave API, installare client
   * - Best for
     - Test rapidi, prompt di base
     - Voce offline leggermente migliore
     - Progetti locali con qualità superiore
     - Massima qualità, ampia scelta di voci
