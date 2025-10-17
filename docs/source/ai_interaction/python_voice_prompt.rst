.. note::

    Ciao, benvenuto nella SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community su Facebook! Scopri di più su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e Condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Accedi in anteprima agli annunci di nuovi prodotti e alle anticipazioni.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Giveaway Festivi**: Partecipa a giveaway e promozioni in occasione delle festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

14. Auto con Comandi Vocali usando Espeak e Pico2Wave
=====================================================

In questa lezione useremo due motori di sintesi vocale (TTS) integrati in Raspberry Pi — **Espeak** e **Pico2Wave** — per far parlare la PiCar-X.  

Questi due motori sono semplici e funzionano offline, ma hanno caratteristiche vocali diverse:

* **Espeak**: molto leggero e veloce, ma con una voce robotica. Puoi regolare velocità, intonazione e volume.  
* **Pico2Wave**: produce una voce più fluida e naturale rispetto a Espeak, ma con meno opzioni di configurazione.  

Sentirai la differenza nella **qualità della voce** e nelle **funzionalità**, e poi costruirai un'“auto con prompt vocale” che annuncia le sue azioni prima di muoversi.  

----

1. Testare Espeak
-----------------

Espeak è un motore TTS leggero incluso in Raspberry Pi OS.  
La sua voce suona robotica, ma è altamente configurabile: puoi regolare volume, intonazione, velocità e altro.  

**Passaggi per provarlo**:

* Crea un nuovo file con il comando:

  .. code-block:: bash
  
      cd ~/picar-x/example
      sudo nano test_tts_espeak.py

* Copia il codice di esempio al suo interno. Premi ``Ctrl+X``, poi ``Y`` e infine ``Enter`` per salvare ed uscire.

  .. code-block:: python
  
      from picarx.tts import Espeak
      import time

      tts = Espeak()
  
      # Saluto veloce (verifica di funzionamento)
      tts.say("Hello! I'm Espeak TTS.")
  
      # Opzioni di regolazione voce
      # tts.set_amp(100)   # 0 a 200
      # tts.set_speed(150) # 80 a 260
      # tts.set_gap(5)     # 0 a 200
      # tts.set_pitch(50)  # 0 a 99

* Esegui il programma con:

  .. code-block:: bash

     sudo python3 test_tts_espeak.py

* Dovresti sentire la PiCar-X dire: “Hello! I'm Espeak TTS.”
* Prova a rimuovere il commento dalle linee di regolazione della voce nel codice per sperimentare come ``amp``, ``speed``, ``gap`` e ``pitch`` influenzano il suono.

----

2. Testare Pico2Wave
---------------------

Pico2Wave produce una voce più naturale e umana rispetto a Espeak.  
È più semplice da usare ma meno flessibile — puoi solo cambiare la lingua, non intonazione o velocità.

**Passaggi per provarlo**:

* Crea un nuovo file con il comando:

  .. code-block:: bash

      cd ~/picar-x/example
      sudo nano test_tts_pico2wave.py

* Copia il codice di esempio al suo interno. Premi ``Ctrl+X``, poi ``Y`` e infine ``Enter`` per salvare ed uscire.

  .. code-block:: python
  
      from picarx.tts import Pico2Wave

      tts = Pico2Wave()
  
      tts.set_lang('en-US')  # en-US, en-GB, de-DE, es-ES, fr-FR, it-IT
  
      # Saluto veloce (verifica di funzionamento)
      tts.say("Hello! I'm Pico2Wave TTS.")

* Esegui il programma con:

  .. code-block:: bash

    sudo python3 test_tts_pico2wave.py

* Dovresti sentire la PiCar-X dire: “Hello! I'm Pico2Wave TTS.”
* Prova a cambiare lingua (per esempio ``es-ES`` per lo spagnolo) e ascolta la differenza.

----

3. Auto con Prompt Vocale
-------------------------

Ora combiniamo **Pico2Wave** o **Espeak** con il codice di guida di PiCar-X per creare un’“auto con prompt vocale”:  
prima di ogni azione, l’auto annuncerà ciò che sta per fare.

**Esegui il Codice**

.. code-block:: bash

    cd ~/picar-x/example
    sudo python3 14.voice_promt_car.py
    
Esegui questo codice e vedrai la tua PiCar-X andare avanti, indietro e girare, annunciando ogni volta prima la manovra.  
Questo rende la tua auto più sicura, amichevole e interattiva.

**Codice**

.. code-block:: python

  from picarx import Picarx
  from picarx.tts import Espeak
  import time

  # If you want to try Pico2Wave instead of Espeak, uncomment below:
  # from picarx.tts import Pico2Wave
  # tts = Pico2Wave()
  # tts.set_lang('en-US')  # Options: en-US, en-GB, de-DE, es-ES, fr-FR, it-IT

  px = Picarx()
  tts = Espeak()

  # Quick hello (test)
  tts.say("Hello! I'm PiCar-X.")

  def main():
      try:
          # Forward
          tts.say("Moving forward")
          px.forward(30)
          time.sleep(2)
          px.stop()

          # Backward
          tts.say("Moving backward")
          px.backward(30)
          time.sleep(2)
          px.stop()

          # Turn left
          tts.say("Turning left")
          px.set_dir_servo_angle(-20)
          px.forward(30)
          time.sleep(2)
          px.stop()
          px.set_dir_servo_angle(0)

          # Turn right
          tts.say("Turning right")
          px.set_dir_servo_angle(20)
          px.forward(30)
          time.sleep(2)
          px.stop()
          px.set_dir_servo_angle(0)

      except KeyboardInterrupt:
          # Stop if interrupted
          px.stop()
      finally:
          # Reset to safe state
          px.stop()
          px.set_dir_servo_angle(0)

  if __name__ == "__main__":
      main()

----

Risoluzione dei Problemi
------------------------

* **Nessun suono quando esegui Espeak o Pico2Wave**

  * Controlla che altoparlanti/cuffie siano collegati e che il volume non sia disattivato.  
  * Esegui un test rapido nel terminale:

    .. code-block:: bash

       espeak "Hello world"
       pico2wave -w test.wav "Hello world" && aplay test.wav

  Se non senti nulla, il problema è nell’uscita audio, non nel tuo codice Python.

* **La voce di Espeak è troppo veloce o troppo “robotica”**

  * Prova a regolare i parametri nel tuo codice:

    .. code-block:: python

       tts.set_speed(120)   # più lento
       tts.set_pitch(60)    # diversa intonazione

* **Permission denied quando esegui il codice**

  * Prova a eseguire con ``sudo``:

    .. code-block:: bash

       sudo python3 test_tts_espeak.py


Confronto: Espeak vs Pico2Wave
-------------------------------------

.. list-table::
   :widths: 20 40 40
   :header-rows: 1

   * - Caratteristica
     - Espeak
     - Pico2Wave
   * - Qualità della voce
     - Robotica, sintetica
     - Più naturale, simile a una voce umana
   * - Lingue
     - Inglese predefinito
     - Meno lingue, ma le più comuni
   * - Regolazioni possibili
     - Sì (velocità, intonazione, ecc.)
     - No (solo lingua)
   * - Prestazioni
     - Molto veloce, leggero
     - Leggermente più lento, più pesante

