.. note::

    Ciao, benvenuto nella SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community su Facebook! Scopri di più su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e Condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Accedi in anteprima agli annunci di nuovi prodotti e alle anticipazioni.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Giveaway Festivi**: Partecipa a giveaway e promozioni in occasione delle festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _ai_voice_assistant_car:

21. Auto Assistente Vocale AI
=============================

Questa lezione trasforma il tuo PiCar-X in un **assistente vocale AI su ruote**.  
Il robot può svegliarsi alla tua voce, riconoscere ciò che dici, rispondere con emozione  
e manifestare i suoi “sentimenti” attraverso movimenti, gesti e luci.

Costruirai un’**auto assistente vocale completamente interattiva** utilizzando:

* **LLM** - Large Language Model (OpenAI GPT o Doubao).  
* **STT** - Speech-to-Text (voce in testo).  
* **TTS** - Text-to-Speech (testo in voce).  
* **Sensori + Azioni** - Ultrasuoni, fotocamera e azioni espressive integrate.

----

Prima di iniziare
-----------------

Assicurati di aver completato:

* :ref:`install_all_modules` — Installa i moduli ``robot-hat``, ``vilib``, ``picar-x``, poi esegui lo script ``i2samp.sh``.
* :ref:`test_piper` — Controlla le lingue supportate di **Piper TTS**.  
* :ref:`test_vosk` — Controlla le lingue supportate di **Vosk STT**.  
* :ref:`py_online_llm` — Questo passaggio è **molto importante**: ottieni la tua chiave API **OpenAI** o **Doubao**, o la chiave API di un altro LLM supportato.

Dovresti già avere:

* Un **microfono** e un **altoparlante** funzionanti sul tuo PiCar-X.  
* Una **chiave API valida** salvata in ``secret.py``.  
* Una connessione di rete stabile (è consigliata una connessione **cablata** per maggiore stabilità).

----

Eseguire l'esempio
------------------

Entrambe le versioni linguistiche si trovano nella stessa directory:

.. code-block:: bash

   cd ~/picar-x/example

**Versione inglese** (OpenAI GPT, istruzioni in inglese):

.. code-block:: bash

   sudo python3 21.voice_active_car_gpt.py

* LLM: ``OpenAI GPT-4o-mini``  
* TTS: ``en_US-ryan-low`` (Piper)  
* STT: Vosk (``en-us``)

Parola di attivazione:

.. code-block::

   "Hey buddy"

---

**Versione cinese** (Doubao, istruzioni in cinese):

.. code-block:: bash

   sudo python3 21.voice_active_car_doubao_cn.py

* LLM: ``Doubao-seed-1-6-250615``  
* TTS: ``zh_CN-huayan-x_low`` (Piper)  
* STT: Vosk (``cn``)

Parola di attivazione:

.. code-block::

   "你好 滴滴"

.. note::

   Puoi modificare la **parola di attivazione** e il **nome del robot** nel codice:
   ``NAME = "Buddy"`` oppure ``NAME = "滴滴"``  
   ``WAKE_WORD = ["hey buddy"]`` oppure ``WAKE_WORD = ["你好 滴滴"]``


----

Cosa Succederà
---------------

Quando esegui correttamente questo esempio:

* Il robot **attende la parola di attivazione** (ad es. “Hey Buddy” / “你好 滴滴”).  
* Quando sente la parola di attivazione:

  * I LED **lampeggeranno** e rimarranno accesi.  
  * Il robot **ti saluterà** con una voce allegra.

* Quindi inizierà ad **ascoltare la tua voce** in tempo reale.  
* Dopo aver riconosciuto ciò che hai detto:

  * Invierà la tua voce all’**LLM** (OpenAI o Doubao).  
  * **Penserà** e lampeggerà con i LED durante l’elaborazione.  
  * Risponderà con la **voce TTS**.  
  * Eseguirà **azioni corrispondenti** (ad es. annuire, girarsi, festeggiare).

* Se ti avvicini troppo, il sensore a ultrasuoni:

  * Attiverà un movimento automatico **indietro** per sicurezza.  
  * Interromperà il ciclo corrente con un messaggio di avviso.

**Esempio di interazione**

.. code-block:: text

   Tu: Hey Buddy
   Robot: Ciao!

   Tu: Gira a sinistra e guarda intorno.
   Robot: Ricevuto, sto girando la testa a sinistra come un gatto curioso!
   AZIONI: turn_left, look_left

----

Passare ad altri LLM o TTS
---------------------------

Puoi passare facilmente ad altri LLM, TTS o lingue STT con poche modifiche:

* LLM supportati:

  * OpenAI
  * Doubao
  * Deepseek
  * Gemini
  * Qwen
  * Grok

* :ref:`test_piper` — Controlla le lingue supportate di **Piper TTS**.  
* :ref:`test_vosk` — Controlla le lingue supportate di **Vosk STT**.  

Per cambiare, modifica semplicemente la parte di inizializzazione nel codice:

.. code-block:: python

   from picarx.llm import Gemini as LLM
   llm = LLM(api_key="YOUR_KEY", model="gemini-pro")

   # Imposta modelli e lingue
   TTS_MODEL = "en_US-ryan-low"
   STT_LANGUAGE = "en-us"

----

Riferimento Azioni e Suoni
--------------------------

Di seguito sono riportate le **parole chiave di azione** che l’LLM può restituire (dopo la riga ``ACTIONS:``) e ciò che fanno sul robot.

.. list-table::
   :header-rows: 1
   :widths: 20 55 25

   * - **Azione**
     - **Cosa fa (da preset_actions.py)**
     - **Effetto / Note**
   * - ``shake head``
     - Muove rapidamente la telecamera a destra↔sinistra con passi decrescenti, poi la riporta al centro.
     - Gesto di “No”; le ruote rimangono ferme.
   * - ``nod``
     - Muove la telecamera su↔giù due volte, poi la centra.
     - Gesto di “Sì”; le ruote rimangono ferme.
   * - ``wave hands``
     - Inclina la telecamera, poi sterza a sinistra/destra due volte (±25°) e la riporta al centro.
     - Saluto giocoso (usa il servo dello sterzo come “braccia”).
   * - ``resist``
     - Piccola inclinazione; alterna (sterzo ±15°, pan ±15°) 3 volte; ferma e centra.
     - Movimento di “rifiuto”/difensivo.
   * - ``act cute``
     - Inclina la testa verso il basso; piccoli micro-movimenti avanti/indietro, poi resetta.
     - Mossa “carina” e rimbalzante; movimenti brevissimi.
   * - ``rub hands``
     - Piccola oscillazione dello sterzo (±6°) ripetuta cinque volte; resetta.
     - Imita il gesto di “sfregarsi le mani”.
   * - ``think``
     - Movimento fluido pan a destra + inclinazione verso il basso + sterzo a destra; breve pausa; posa riflessiva; resetta.
     - Usato come singola animazione di “riflessione”.
   * - ``twist body``
     - Tre cicli di breve avanzamento/stop/pan-sinistra/sterzo-sinistra, poi breve indietro/stop/pan-destra/sterzo-destra.
     - Dà una sensazione di “torsione” del corpo.
   * - ``celebrate``
     - Inclinazione verso l’alto; due movimenti decorativi a destra, poi due a sinistra; ritorna al centro.
     - Movimento festoso e simmetrico.
   * - ``depressed``
     - Serie di inclinazioni verso il basso con angolazioni e pause variabili; termina dopo una lunga pausa e resetta.
     - Sequenza posturale “triste”.

Movimento e Utilità
~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 22 58 20

   * - **Azione**
     - **Cosa fa**
     - **Note**
   * - ``forward``
     - Avanza a bassa velocità per circa 1 secondo, poi si ferma.
     - Implementato da ``forward(car)`` (velocità 5% + 1s).
   * - ``backward``
     - Retrocede a bassa velocità per circa 1 secondo, poi si ferma.
     - Implementato da ``backward(car)`` (velocità 5% + 1s).

Effetti Sonori
~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 24 56 20

   * - **Suono**
     - **Cosa fa**
     - **Note**
   * - ``honking``
     - Riproduce ``car-double-horn.wav`` in modo asincrono (volume ~100).
     - Attivato tramite ``Music.sound_play_threading``.
   * - ``start engine``
     - Riproduce ``car-start-engine.wav`` in modo asincrono (volume ~50).
     - Segnale di avvio/pronto.

Trigger Sensori (Automatici)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Prossimità a ultrasuoni**

  * Trigger: distanza < 10 cm  
  * Effetto collaterale: auto ``backward`` + disabilita immagine per questo ciclo  
  * Messaggio iniettato: ``<<<Ultrasonic sense too close: {distance}cm>>>``

Hook del Ciclo di Vita (Indicatori LED)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ``before_listen`` → lampeggia due volte (pronto per ascoltare)  
* ``before_think`` → lampeggiante (in elaborazione)  
* ``before_say`` → LED acceso (sta parlando)  
* ``after_say`` → attende azioni → LED spento  
* ``on_stop`` → ferma le azioni, chiude i dispositivi

----

Risoluzione dei Problemi
------------------------

* **Il robot non risponde alla parola di attivazione**

  * Controlla se il microfono funziona.  
  * Assicurati che ``WAKE_ENABLE = True``.  
  * Adatta la parola di attivazione alla tua pronuncia.

* **Nessun suono dall’altoparlante**
 
  * Verifica la configurazione del modello TTS.  
  * Testa Piper o Espeak manualmente.  
  * Controlla il collegamento e il volume dell’altoparlante.

* **Errore API Key o timeout**
 
  * Controlla la chiave in ``secret.py``.  
  * Assicurati che la connessione di rete funzioni.  
  * Conferma che l’LLM sia supportato.

* **Picar-X non si muove o non agisce**
 
  * Controlla che il nome dell’azione corrisponda a ``actions_dict``.  
  * Verifica i collegamenti dei motori e dei servi.

* **Il sensore a ultrasuoni si attiva inaspettatamente**

  * Controlla l’altezza e l’angolo di installazione del sensore.  
  * Regola la soglia di distanza ``TOO_CLOSE`` nel codice.
