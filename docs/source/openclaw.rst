.. _picarx_skill:

.. start_using_picarx

22. Usare OpenClaw per Controllare il PiCar-X
================================================


**Cos'è OpenClaw?**

Consideralo come una versione potenziata di ChatGPT. Mentre i chatbot tradizionali possono solo parlare (generare testo), OpenClaw può agire. Comprende le tue istruzioni in linguaggio naturale e può effettivamente eseguire operazioni sul tuo computer, come eseguire comandi, gestire file e chiamare vari strumenti.

Ecco alcuni scenari applicativi fantastici:

* **Assistente personale tuttofare:** Lascia che ti aiuti a gestire l'agenda, impostare promemoria e monitorare le attività. Ti basta dirglielo in un'app di messaggistica (come Telegram, WhatsApp) e lui ricorderà ed eseguirà.
* **Collante per l'automazione:** Può fungere da legante per i tuoi vari servizi. Ad esempio, puoi fargli monitorare un sito web per variazioni di prezzo. Una volta rilevato un calo di prezzo, può attivare automaticamente un flusso di lavoro n8n per inviarti una notifica via email.
* **Assistente di sviluppo dedicato:** Fatti aiutare a gestire server, eseguire script e controllare i log. Puoi semplicemente dire: "Controlla il carico di sistema per me", e lui può connettersi via SSH al tuo server, eseguire il comando e restituire i risultati.
* **Compagno hardware:** Questo è un caso d'uso molto interessante. Puoi far controllare a OpenClaw l'hardware collegato a un Raspberry Pi. Ad esempio, uno sviluppatore l'ha usato per controllare un aspirapolvere robotico con un braccio meccanico, o addirittura per analizzare i dati di un simulatore di corsa e visualizzarli su uno schermo LED. Il team ufficiale di Raspberry Pi l'ha persino usato per costruire un photobooth automatico per un matrimonio, semplicemente conversando, senza scrivere una sola riga di codice!


.. important::

   Il Raspberry Pi Zero 2W ha solo 512 MB di RAM, mentre OpenClaw richiede almeno 1 GB. Pertanto, non può funzionare correttamente. Si consiglia un Raspberry Pi 4/5 o superiore.

Avvio Rapido di OpenClaw
-------------------------------

Se vuoi sperimentare la potenza di OpenClaw il più rapidamente possibile, usa questo metodo. Installerà e avvierà automaticamente una procedura guidata di configurazione interattiva.

1.  Apri il terminale sul tuo Raspberry Pi ed esegui direttamente il seguente comando. Questo comando scarica lo script di installazione dal sito ufficiale e lo esegue:

    .. code-block:: bash

       curl -fsSL https://openclaw.ai/install.sh | bash

    .. note:: Poiché le nuove versioni vengono aggiornate rapidamente, è normale che i passaggi di installazione differiscano leggermente.

2.  Lo script scaricherà e installerà automaticamente OpenClaw.

    .. image:: /img/openclaw/install_open_claw.png


3.  Vedrai quindi un prompt di sicurezza che ti chiede se ti fidi di OpenClaw. Una volta sicuro che sia affidabile, usa i tasti freccia per navigare su "Yes" e premi Invio.

    .. image:: /img/openclaw/security_open_claw.png


4.  Seleziona Quick Start, quindi premi Invio.

    .. image:: /img/openclaw/quickstart_open_claw.png

5.  Seleziona il tuo modello, quindi premi Invio. Qui usiamo OpenAI come esempio.

    .. image:: /img/openclaw/model_provider_open_claw.png

6.  Seleziona OpenAI API Key.

    .. image:: /img/openclaw/api_key_open_claw.png

7.  Incolla la chiave API ora.

    .. image:: /img/openclaw/paste_api_key_open_claw.png

8.  Vai su |link_openai_platform| ed effettua il login. Nella pagina **API keys**, clicca su **Create new secret key**.

    .. image:: /img/openclaw/llm_openai_create.png

9.  Compila i dettagli (Owner, Name, Project e permessi se necessario), quindi clicca su **Create secret key**.

    .. image:: /img/openclaw/llm_openai_create_confirm.png

10. Una volta creata la chiave, copiala immediatamente — non potrai più rivederla. Se la perdi, dovrai generarne una nuova.

    .. image:: /img/openclaw/llm_openai_copy.png

11. Incolla la chiave nella configurazione di OpenClaw.

    .. image:: /img/openclaw/paste_api_key_enter_open_claw.png

12. Seleziona il modello che desideri utilizzare. In questo esempio, useremo **Keep current**.

    .. image:: /img/openclaw/model_config_open_claw.png

13. Poi c'è la selezione del canale. I canali si riferiscono ai servizi di comunicazione supportati da OpenClaw, come Telegram, WhatsApp, Discord e altri. Usa il tasto freccia giù per selezionare l'opzione "Skip for now", quindi premi Invio.

    .. image:: /img/openclaw/channel_open_claw.png

14. Successivamente, ti verrà chiesto di configurare subito le competenze. Seleziona "Yes" e premi Invio.

    .. image:: /img/openclaw/config_skill_open_claw.png

15. Installa le competenze di cui hai bisogno. Nell'esempio seguente, selezioniamo l'opzione "Skip for now" (premi la barra spaziatrice per selezionare), quindi premi Invio.

    .. image:: /img/openclaw/install_skill_open_claw.png

16. Poi ci sono gli Hooks; selezioneremo "command-logger" e "session-memory".

    .. image:: /img/openclaw/hooks2_open_claw.png


17. L'installazione è ora completa. Puoi avviare OpenClaw selezionando "Hatch in TUI" e premendo Invio.

   .. image:: /img/openclaw/hatch_open_claw.png


.. note::

   Puoi avviare OpenClaw inserendo il seguente comando:

    .. code-block:: bash

       openclaw tui

   E puoi premere due volte ctrl+c per uscire dall'interfaccia TUI.

------------------------------------------------------------------------

Far Funzionare il PiCar-X con OpenClaw
----------------------------------------------

**Cos'è la competenza PiCar-X?**

La competenza PiCar-X è un'estensione per OpenClaw che ti permette di controllare la tua auto robot SunFounder PiCar-X attraverso il linguaggio naturale. Invece di scrivere script Python o memorizzare angoli dei servi, puoi semplicemente dire a OpenClaw cosa vuoi che il PiCar-X faccia — come "vai avanti", "controlla cosa c'è davanti" o "gira a sinistra" — e OpenClaw eseguirà automaticamente il codice Python appropriato.

Ecco alcune cose che puoi fare con la competenza PiCar-X:

* **Guida:** Avanti, indietro, gira a sinistra/destra con controllo del servo di sterzo
* **Telecamera orientabile:** Panoramica sinistra/destra, inclinazione su/giù tramite la telecamera a 2 assi
* **Sensori:** Leggi distanza ultrasonica, dati del sensore a scala di grigi per il tracciamento di linea e il rilevamento di burroni
* **Audio:** Riproduci effetti sonori e musica attraverso l'altoparlante dell'auto
* **Visione artificiale:** Scatta foto, rileva volti, traccia colori, riconosci QR code, gesti e segnali stradali

----------------------------------------------------------------

Prerequisiti
------------------------------

Prima di poter utilizzare la competenza PiCar-X con OpenClaw, assicurati di avere:

1. **PiCar-X** correttamente assemblato e collegato al tuo Raspberry Pi
2. **OpenClaw** installato e in esecuzione
3. Le seguenti librerie Python installate:

   - ``picarx``
   - ``robot_hat``
   - ``vilib``

Puoi verificare l'installazione eseguendo:

.. code-block:: bash

   python3 -c "import picarx"

Se questo comando viene eseguito senza errori, sei pronto a procedere.

----------------------------------------------------------------

Installare la Competenza PiCar-X
-----------------------------------

Segui questi passaggi per installare la competenza PiCar-X per OpenClaw:

1. **Copia i file della competenza PiCar-X** nella directory delle competenze di OpenClaw:

   .. code-block:: bash

      cp -r ~/picar-x/picarx-control ~/.openclaw/workspace/skills/

2. **Verifica l'installazione** controllando i file della competenza:

   .. code-block:: bash

      ls ~/.openclaw/workspace/skills/picarx-control/

   Dovresti vedere ``SKILL.md``, ``install.sh``, ``scripts/`` e ``references/`` nell'output.

Il file ``SKILL.md`` della competenza contiene tutte le istruzioni di cui OpenClaw ha bisogno — regole di sicurezza, modelli di codice per ogni capacità e una mappatura dalle richieste in linguaggio naturale al codice Python. OpenClaw legge questo file e lo usa per decidere quale codice eseguire sul tuo PiCar-X.

----------------------------------------------------------------

Testare la Competenza PiCar-X dalla CLI
----------------------------------------------

Prima di utilizzare la competenza con OpenClaw, potresti voler testare le funzionalità di base direttamente dal terminale usando lo strumento CLI incluso.

**Controllare la distanza ultrasonica:**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/picarx-control/scripts/pc.py sensor distance

**Andare avanti:**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/picarx-control/scripts/pc.py move forward --speed 60

**Andare indietro:**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/picarx-control/scripts/pc.py move backward --speed 60

**Girare a sinistra:**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/picarx-control/scripts/pc.py turn left --angle 30

**Girare a destra:**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/picarx-control/scripts/pc.py turn right --angle 30

**Impostare l'angolo di panoramica della telecamera:**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/picarx-control/scripts/pc.py cam pan --angle 30

**Impostare l'angolo di inclinazione della telecamera:**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/picarx-control/scripts/pc.py cam tilt --angle 20

**Riprodurre un effetto sonoro:**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/picarx-control/scripts/pc.py sound play /path/to/sound.wav --volume 80

**Leggere i dati del sensore a scala di grigi (tracciamento di linea):**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/picarx-control/scripts/pc.py sensor grayscale

**Eseguire la calibrazione dei servi:**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/picarx-control/scripts/pc.py calibrate

----------------------------------------------------------------

Usare la Competenza PiCar-X in OpenClaw
----------------------------------------------------

Una volta verificato che la competenza PiCar-X funziona dalla riga di comando, puoi iniziare a usarla all'interno di OpenClaw.

1. **Avvia OpenClaw TUI**:

   .. code-block:: bash

      openclaw tui

2. **Invia comandi in linguaggio naturale** per controllare il PiCar-X. Ecco alcuni esempi:

   * "Vai avanti"
   * "Vai indietro"
   * "Gira a sinistra"
   * "Gira a destra"
   * "Controlla se c'è qualcosa davanti"
   * "Guarda a sinistra"
   * "Guarda in alto"
   * "Guarda in basso"
   * "Scatta una foto"
   * "Rileva volti"
   * "Trova il colore rosso"
   * "Segui la linea"
   * "Controlla se c'è un burrone davanti"

3. **OpenClaw tradurrà automaticamente** la tua richiesta nel codice Python appropriato e lo eseguirà sul PiCar-X.

----------------------------------------------------------------

Azioni e Comandi Disponibili
-------------------------------------------

Ecco l'elenco completo delle capacità supportate dalla competenza PiCar-X:

Guida (``pc.py move``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Azione
     - Descrizione
   * - ``forward``
     - Andare avanti
   * - ``backward``
     - Andare indietro

Sterzo (``pc.py turn``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Azione
     - Descrizione
   * - ``left``
     - Girare a sinistra regolando l'angolo di sterzo
   * - ``right``
     - Girare a destra regolando l'angolo di sterzo

Telecamera orientabile (``pc.py cam``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Capacità
     - Descrizione
   * - Panoramica
     - Ruotare la telecamera orizzontalmente (da -90° a 90°)
   * - Inclinazione
     - Inclinare la telecamera verticalmente (da -35° a 65°)

Sensori
^^^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Comando
     - Descrizione
   * - ``sensor distance``
     - Leggere il sensore di distanza ultrasonico (restituisce cm)
   * - ``sensor grayscale``
     - Leggere i valori del modulo a scala di grigi a 3 canali (per tracciamento di linea e rilevamento burroni)

Audio (``pc.py sound``)
^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Comando
     - Descrizione
   * - ``sound play <file>``
     - Riprodurre un file di effetto sonoro
   * - ``sound music <file>``
     - Riprodurre musica di sottofondo
   * - ``sound volume <0-100>``
     - Impostare il volume dell'altoparlante
   * - ``sound stop``
     - Fermare la riproduzione

.. note::

   I file audio possono essere qualsiasi file in formato ``.wav`` accessibile sul tuo Raspberry Pi. Puoi anche usare ``sound music`` per riprodurre file di musica di sottofondo.

Telecamera e Visione (via linguaggio naturale / exec)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Capacità
     - Descrizione
   * - Scattare foto
     - Catturare e salvare una foto in ``~/Pictures/``
   * - Rilevamento volti
     - Rilevare volti umani e segnalare la posizione
   * - Rilevamento colori
     - Localizzare oggetti per colore (rosso, blu, verde, ecc.)
   * - Riconoscimento gesti
     - Riconoscere i gesti sasso/carta/forbici
   * - Rilevamento segnali stradali
     - Riconoscere i segnali stop/sinistra/destra/avanti
   * - Scansione QR code
     - Leggere dati e posizione dei QR code

Tracciamento di Linea e Rilevamento Burroni
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Capacità
     - Descrizione
   * - Tracciamento di linea
     - Seguire una linea nera su una superficie chiara usando il sensore a scala di grigi a 3 canali
   * - Rilevamento burroni
     - Rilevare bordi/dislivelli usando i valori di soglia del sensore a scala di grigi

----------------------------------------------------------------

Risoluzione dei Problemi
------------------------------

Problemi con OpenClaw
^^^^^^^^^^^^^^^^^^^^^^^^

D. Durante l'installazione, ottengo l'errore ``Error: systemctl is-enabled unavailable: Command failed: systemctl --user is-enabled openclaw-gateway.service``. Cosa devo fare?

   Puoi ignorarlo per ora, ma potresti incontrare problemi nei passaggi successivi. Ti preghiamo di fare riferimento a loro uno per uno in quel momento.


D. Quando eseguo ``openclaw tui``, ottengo l'errore ``-bash: openclaw: command not found``. Cosa devo fare?

   Esegui il seguente comando:

   .. code-block:: bash

      echo 'export PATH="$HOME/.npm-global/bin:$PATH"' >> ~/.bashrc
      source ~/.bashrc

   Ora dovresti essere in grado di avviare l'interfaccia TUI con ``openclaw tui``.



D. In ``openclaw tui``, incontro ``not connected to gateway — message not sent`` o il messaggio ``gateway disconnected: closed``.

   Questo perché il tuo servizio OpenClaw Gateway non è avviato. Apri un altro terminale ed esegui il seguente comando per avviare l'OpenClaw Gateway:

   .. code-block:: bash

      openclaw gateway

   Quindi riavvia ``openclaw tui`` e potrai usarlo direttamente.


D. Voglio impostare il servizio OpenClaw Gateway per l'esecuzione in background / avvio automatico all'accensione. Come faccio?

   Normalmente, il tuo servizio OpenClaw Gateway dovrebbe avviarsi automaticamente all'accensione. In caso contrario, puoi avviarlo manualmente con il seguente comando.

   1. Crea la directory ``~/.config/systemd/user``:

   .. code-block:: bash

      mkdir -p ~/.config/systemd/user


   2. Crea il file ``openclaw-gateway.service``:

   .. code-block:: bash

      cat > ~/.config/systemd/user/openclaw-gateway.service << EOF
      [Unit]
      Description=OpenClaw Gateway
      After=network.target

      [Service]
      Type=simple
      ExecStart=$HOME/.npm-global/bin/openclaw gateway run
      Restart=on-failure
      RestartSec=10
      Environment="PATH=$HOME/.npm-global/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin"
      Environment="NODE_ENV=production"

      [Install]
      WantedBy=default.target
      EOF


   3. Quindi ricarica la configurazione di systemd:

   .. code-block:: bash

      systemctl --user daemon-reload

   4. Avvia il servizio:

   .. code-block:: bash

      systemctl --user start openclaw-gateway

   A questo punto, riavvia ``openclaw tui`` e potrai usarlo direttamente.

   5. Abilitalo per l'avvio automatico:

   .. code-block:: bash

      systemctl --user enable openclaw-gateway


D. Il mio OpenClaw non può interagire con il sistema, cosa devo fare?

   Un OpenClaw appena installato potrebbe non avere il permesso di interagire con il tuo sistema Raspberry Pi per impostazione predefinita; può solo chattare. Dobbiamo configurare manualmente i permessi.

   1.  Apri il file di configurazione di OpenClaw:

      .. code-block:: bash

         nano ~/.openclaw/openclaw.json

   2.  Trova l'opzione ``tools`` e modifica ``profile`` ed ``exec`` come mostrato.

      .. code-block:: json

        "tools": {
            "profile": "coding",
            "exec": {
                "secrity": "full"
            }
        },

   3.  Salva ed esci.

   4.  Inserisci il seguente comando nel terminale per riavviare l'OpenClaw Gateway:

      .. code-block:: bash

         openclaw gateway restart

   Ora OpenClaw dovrebbe avere i permessi di lettura e scrittura ed essere in grado di interagire con il tuo sistema Raspberry Pi.

Problemi con il PiCar-X
^^^^^^^^^^^^^^^^^^^^^^^^


D. Il PiCar-X non risponde ai comandi. Cosa devo fare?

   Per prima cosa, verifica che il PiCar-X sia correttamente collegato e acceso. Quindi testa le funzionalità di base:

   .. code-block:: bash

      python3 ~/.openclaw/workspace/skills/picarx-control/scripts/pc.py sensor distance

   Se fallisce, assicurati che le librerie Python richieste siano installate:

   .. code-block:: bash

      python3 -c "import picarx; import robot_hat; import vilib"

D. Il test ``import picarx`` fallisce.

   Ciò significa che la libreria Python PiCar-X non è installata correttamente. Consulta la guida ufficiale all'installazione di PiCar-X per installare le librerie necessarie. Puoi anche eseguire lo script di installazione incluso:

   .. code-block:: bash

      bash ~/.openclaw/workspace/skills/picarx-control/install.sh

D. OpenClaw non riconosce la competenza PiCar-X.

   Ricorda a OpenClaw di sincronizzare le competenze dicendo nel TUI: *"Please rsync my skills"* o riavvia l'OpenClaw Gateway:

   .. code-block:: bash

      openclaw gateway restart

D. I movimenti del PiCar-X sembrano a scatti o lo sterzo è fuori centro.

   Questo è solitamente causato da valori di calibrazione dei servi errati. Esegui lo script di calibrazione per regolare il servo di sterzo e la telecamera orientabile:

   .. code-block:: bash

      python3 ~/.openclaw/workspace/skills/picarx-control/scripts/pc.py calibrate

   Puoi anche regolare il parametro di velocità (ad esempio, usa ``--speed 40``) per un movimento più fluido, o aggiungere brevi pause tra comandi consecutivi.

D. Il tracciamento di linea o la scala di grigi non funziona correttamente.

   Assicurati che il modulo a scala di grigi sia correttamente calibrato per la tua superficie. Puoi impostare i valori di riferimento della linea usando la configurazione. Consulta la documentazione principale di PiCar-X per le procedure di calibrazione della scala di grigi.

----------------------------------------------------------------

.. end_using_picarx
