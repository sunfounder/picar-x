.. note::

    Ciao, benvenuto nella community di SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme agli altri appassionati.

    **Perché unirsi?**

    - **Supporto esperto**: Risolvi i problemi post-vendita e le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni l'accesso anticipato agli annunci di nuovi prodotti e anteprime esclusive.
    - **Sconti speciali**: Goditi sconti riservati sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa ai giveaway e alle promozioni speciali per le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca su [|link_sf_facebook|] e unisciti oggi stesso!


Interazione con l'IA utilizzando GPT-4O
=====================================================
Nei nostri precedenti progetti, abbiamo utilizzato la programmazione per dirigere PiCar-X in compiti predeterminati, che potrebbero sembrare un po' noiosi. Questo progetto introduce un emozionante passo avanti verso un'interazione dinamica. Attenzione a non cercare di ingannare la nostra macchina—ora è dotata di una comprensione molto più avanzata che mai!

Questo progetto descrive tutti i passaggi tecnici necessari per integrare GPT-4O nel tuo sistema, compresa la configurazione degli ambienti virtuali necessari, l'installazione delle librerie essenziali e la configurazione delle chiavi API e degli ID assistenti.

.. note::

   Questo progetto richiede l'uso di |link_openai_platform| e il pagamento per OpenAI. Inoltre, l'API di OpenAI viene fatturata separatamente rispetto a ChatGPT, con il proprio listino prezzi disponibile su https://openai.com/api/pricing/.

   Pertanto, è necessario decidere se proseguire con questo progetto o assicurarsi di aver finanziato l'API di OpenAI.

Sia che tu abbia un microfono per comunicare direttamente o preferisca digitare in una finestra di comando, le risposte di PiCar-X alimentate da GPT-4O ti sorprenderanno di sicuro!

Immergiamoci in questo progetto e sblocchiamo un nuovo livello di interazione con PiCar-X!

1. Installazione dei pacchetti e delle dipendenze richiesti
--------------------------------------------------------------
.. note::

   Prima di tutto, è necessario installare i moduli necessari per PiCar-X. Per i dettagli, fare riferimento a: :ref:`install_all_modules`.
   
In questa sezione, creeremo e attiveremo un ambiente virtuale, installando al suo interno i pacchetti e le dipendenze necessari. Questo garantisce che i pacchetti installati non interferiscano con il resto del sistema, mantenendo l'isolamento delle dipendenze del progetto e prevenendo conflitti con altri progetti o pacchetti di sistema.

#. Usa il comando ``python -m venv`` per creare un ambiente virtuale chiamato ``my_venv``, inclusi i pacchetti a livello di sistema. L'opzione ``--system-site-packages`` consente all'ambiente virtuale di accedere ai pacchetti installati a livello di sistema, utile quando sono necessarie librerie a livello di sistema.

   .. code-block:: shell

      python -m venv --system-site-packages my_venv

#. Passa alla directory ``my_venv`` e attiva l'ambiente virtuale utilizzando il comando ``source bin/activate``. Il prompt dei comandi cambierà per indicare che l'ambiente virtuale è attivo.

   .. code-block:: shell

      cd my_venv
      source bin/activate

#. Ora, installa i pacchetti Python richiesti nell'ambiente virtuale attivato. Questi pacchetti saranno isolati nell'ambiente virtuale e non influenzeranno altri pacchetti di sistema.

   .. code-block:: shell

      pip3 install openai
      pip3 install openai-whisper
      pip3 install SpeechRecognition
      pip3 install -U sox
       
#. Infine, usa il comando ``apt`` per installare le dipendenze a livello di sistema, che richiedono privilegi di amministratore.

   .. code-block:: shell

      sudo apt install python3-pyaudio
      sudo apt install sox


2. Ottenere la chiave API e l'ID assistente
------------------------------------------------------

**Ottenere la chiave API**

#. Visita |link_openai_platform| e clicca sul pulsante **Create new secret key** nell'angolo in alto a destra.

   .. image:: img/apt_create_api_key.png
      :width: 700
      :align: center

#. Seleziona il proprietario, il nome, il progetto e le autorizzazioni come necessario, quindi clicca su **Create secret key**.

   .. image:: img/apt_create_api_key2.png
      :width: 700
      :align: center

#. Una volta generata, salva questa chiave segreta in un luogo sicuro e accessibile. Per motivi di sicurezza, non potrai più visualizzarla tramite il tuo account OpenAI. Se perdi questa chiave segreta, dovrai generarne una nuova.

   .. image:: img/apt_create_api_key_copy.png
      :width: 700
      :align: center

**Ottenere l'ID assistente**

#. Successivamente, clicca su **Assistants**, quindi su **Create**, assicurandoti di essere sulla pagina **Dashboard**.

   .. image:: img/apt_create_assistant.png
      :width: 700
      :align: center

#. Muovi il cursore qui per copiare l'**ID assistente**, quindi incollalo in una casella di testo o altrove. Questo è l'identificatore univoco per questo assistente.

   .. image:: img/apt_create_assistant_id.png
      :width: 700
      :align: center

#. Assegna un nome a caso, quindi copia il seguente contenuto nella casella **Instructions** per descrivere il tuo assistente.

   .. image:: img/apt_create_assistant_instructions.png
      :width: 700
      :align: center

   .. code-block::

         You are a small car with AI capabilities named PaiCar-X. You can engage in conversations with people and react accordingly to different situations with actions or sounds. You are driven by two rear wheels, with two front wheels that can turn left and right, and equipped with a camera mounted on a 2-axis gimbal.

         ## Response with Json Format, eg:
         {"actions": ["start engine", "honking", "wave hands"], "answer": "Hello, I am PaiCar-X, your good friend."}

         ## Response Style
         Tone: Cheerful, optimistic, humorous, childlike
         Preferred Style: Enjoys incorporating jokes, metaphors, and playful banter; prefers responding from a robotic perspective
         Answer Elaboration: Moderately detailed

         ## Actions you can do:
         ["shake head", "nod", "wave hands", "resist", "act cute", "rub hands", "think", "twist body", "celebrate, "depressed"]
         ## Sound effects:
         ["honking", "start engine"]


#. PiCar-X è dotato di un modulo fotocamera che puoi abilitare per catturare immagini di ciò che vede e caricarle su GPT utilizzando il nostro codice di esempio. Pertanto, ti consigliamo di scegliere GPT-4O, che ha capacità di analisi delle immagini. Naturalmente, puoi anche scegliere gpt-3.5-turbo o altri modelli.

   .. image:: img/apt_create_assistant_model.png
      :width: 700
      :align: center

#. Ora, clicca su **Playground** per vedere se il tuo account funziona correttamente.

   .. image:: img/apt_playground.png

#. Se i tuoi messaggi o le immagini caricate vengono inviati con successo e ricevi risposte, significa che il tuo account non ha raggiunto il limite di utilizzo.


   .. image:: img/apt_playground_40.png
      :width: 700
      :align: center

#. Se ricevi un messaggio di errore dopo aver inserito le informazioni, potresti aver raggiunto il tuo limite di utilizzo. Controlla il dashboard di utilizzo o le impostazioni di fatturazione.

   .. image:: img/apt_playground_40mini_3.5.png
      :width: 700
      :align: center

3. Inserire la chiave API e l'ID assistente
--------------------------------------------------

#. Usa il comando per aprire il file ``keys.py``.

   .. code-block:: shell

      nano ~/picar-x/gpt_examples/keys.py

#. Inserisci la chiave API e l'ID assistente che hai appena copiato.

   .. code-block:: shell

      OPENAI_API_KEY = "sk-proj-vEBo7Ahxxxx-xxxxx-xxxx"
      OPENAI_ASSISTANT_ID = "asst_ulxxxxxxxxx"

#. Premi ``Ctrl + X``, ``Y`` e poi ``Enter`` per salvare il file ed uscire.

4. Esecuzione dell'esempio
----------------------------------
Comunicazione Testuale
^^^^^^^^^^^^^^^^^^^^^^^^^^

Se il tuo PiCar-X non ha un microfono, puoi usare il testo di input della tastiera per interagire con esso eseguendo i seguenti comandi.

#. Ora, esegui i seguenti comandi utilizzando sudo, poiché l'altoparlante di PiCar-X non funzionerà senza di esso. Il processo richiederà un po' di tempo.

   .. code-block:: shell

      cd ~/picar-x/gpt_examples/
      sudo ~/my_venv/bin/python3 gpt_car.py --keyboard

#. Una volta che i comandi sono stati eseguiti con successo, vedrai il seguente output, che indica che tutti i componenti di PiCar-X sono pronti.

   .. code-block:: shell

      vilib 0.3.8 launching ...
      picamera2 0.3.19

      Web display on:
         http://rpi_ip:9000/mjpg

      Starting web streaming ...
      * Serving Flask app 'vilib.vilib'
      * Debug mode: off

      input:

#. Ti verrà fornito anche un link per visualizzare il feed della fotocamera di PiCar-X nel tuo browser: ``http://rpi_ip:9000/mjpg``.

   .. image:: img/apt_ip_camera.png
      :width: 700
      :align: center

#. Ora puoi digitare i tuoi comandi nella finestra del terminale e premere Invio per inviarli. Le risposte di PiCar-X potrebbero sorprenderti.

   .. note::
      
      PiCar-X deve ricevere il tuo input, inviarlo a GPT per l'elaborazione, ricevere la risposta e poi riprodurla tramite sintesi vocale. Questo processo richiede un po' di tempo, quindi sii paziente.

   .. image:: img/apt_keyboard_input.png
      :width: 700
      :align: center

#. Se stai utilizzando il modello GPT-4O, puoi anche fare domande in base a ciò che PiCar-X vede.

Comunicazione Vocale
^^^^^^^^^^^^^^^^^^^^^^^^

Se il tuo PiCar-X è dotato di un microfono, o puoi acquistarne uno cliccando su |link_microphone|, puoi interagire con PiCar-X utilizzando i comandi vocali.

#. Innanzitutto, verifica che il Raspberry Pi abbia rilevato il microfono.

   .. code-block:: shell

      arecord -l

   Se ha avuto successo, riceverai le seguenti informazioni, che indicano che il tuo microfono è stato rilevato.

   .. code-block:: 
      
      **** List of CAPTURE Hardware Devices ****
      card 3: Device [USB PnP Sound Device], device 0: USB Audio [USB Audio]
      Subdevices: 1/1
      Subdevice #0: subdevice #0

#. Esegui il seguente comando, quindi parla a PiCar-X o emetti alcuni suoni. Il microfono registrerà i suoni nel file ``op.wav``. Premi ``Ctrl + C`` per interrompere la registrazione.

   .. code-block:: shell

      rec op.wav

#. Infine, usa il comando seguente per riprodurre il suono registrato, confermando che il microfono funziona correttamente.

   .. code-block:: shell

      sudo play op.wav

#. Ora, esegui i seguenti comandi utilizzando sudo, poiché l'altoparlante di PiCar-X non funzionerà senza di esso. Il processo richiederà un po' di tempo.

   .. code-block:: shell

      cd ~/picar-x/gpt_examples/
      sudo ~/my_venv/bin/python3 gpt_car.py

#. Una volta che i comandi sono stati eseguiti con successo, vedrai il seguente output, che indica che tutti i componenti di PiCar-X sono pronti.

   .. code-block:: shell
      
      vilib 0.3.8 launching ...
      picamera2 0.3.19

      Web display on:
         http://rpi_ip:9000/mjpg

      Starting web streaming ...
      * Serving Flask app 'vilib.vilib'
      * Debug mode: off

      listening ...

#. Ti verrà fornito anche un link per visualizzare il feed della fotocamera di PiCar-X nel tuo browser: ``http://rpi_ip:9000/mjpg``.

   .. image:: img/apt_ip_camera.png
      :width: 700
      :align: center

#. Ora puoi parlare a PiCar-X e le sue risposte potrebbero sorprenderti.

   .. note::
      
      PiCar-X deve ricevere il tuo input, convertirlo in testo, inviarlo a GPT per l'elaborazione, ricevere la risposta e poi riprodurla tramite sintesi vocale. Questo processo richiede un po' di tempo, quindi sii paziente.

   .. image:: img/apt_speech_input.png
      :width: 700
      :align: center

#. Se stai utilizzando il modello GPT-4O, puoi anche fare domande in base a ciò che PiCar-X vede.


5. Modifica dei parametri [opzionale]
-------------------------------------------

Nel file ``gpt_car.py``, trova le seguenti righe. Puoi modificare questi parametri per configurare la lingua STT, il guadagno del volume TTS e il ruolo della voce.

* **STT (Speech to Text)** si riferisce al processo in cui il microfono di PiCar-X cattura la voce e la converte in testo da inviare a GPT. Puoi specificare la lingua per una maggiore precisione e riduzione della latenza in questa conversione.

* **TTS (Text to Speech)** è il processo di conversione delle risposte testuali di GPT in parlato, che viene riprodotto attraverso l'altoparlante di PiCar-X. Puoi regolare il guadagno del volume e selezionare un ruolo di voce per l'output TTS.

.. code-block:: python

   # openai assistant init
   # =================================================================
   openai_helper = OpenAiHelper(OPENAI_API_KEY, OPENAI_ASSISTANT_ID, 'picrawler')

   # LANGUAGE = ['zh', 'en'] # config stt language code, https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes
   LANGUAGE = []

   VOLUME_DB = 3 # tts volume gain, preferably less than 5db

   # select tts voice role, could be "alloy, echo, fable, onyx, nova, and shimmer"
   # https://platform.openai.com/docs/guides/text-to-speech/supported-languages
   TTS_VOICE = 'nova'


* Variabile ``LANGUAGE``:

  * Migliora l'accuratezza e i tempi di risposta del Speech-to-Text (STT).
  * ``LANGUAGE = []`` significa supportare tutte le lingue, ma questo potrebbe ridurre l'accuratezza dello STT e aumentare la latenza.
  * Si consiglia di impostare una o più lingue specifiche utilizzando i codici di lingua |link_iso_language_code| per migliorare le prestazioni.

* Variabile ``VOLUME_DB``:

  * Controlla il guadagno applicato all'output del Text-to-Speech (TTS).
  * Aumentare il valore aumenterà il volume, ma è meglio mantenere il valore inferiore a 5dB per evitare distorsioni audio.

* Variabile ``TTS_VOICE``:

  * Seleziona il ruolo della voce per l'output del Text-to-Speech (TTS).
  * Opzioni disponibili: ``alloy, echo, fable, onyx, nova, shimmer``.
  * Puoi sperimentare diverse voci da |link_voice_options| per trovare quella che si adatta meglio al tono e al pubblico desiderati. Le voci disponibili sono attualmente ottimizzate per l'inglese.
