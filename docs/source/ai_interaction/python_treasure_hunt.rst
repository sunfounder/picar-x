.. note::

    Ciao, benvenuto nella SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community su Facebook! Scopri di più su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e Condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Accedi in anteprima agli annunci di nuovi prodotti e alle anticipazioni.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Giveaway Festivi**: Partecipa a giveaway e promozioni in occasione delle festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _py_treasure:

20. Caccia al Tesoro
============================

In questa lezione trasformerai la tua PiCar-X in un **robot cacciatore di tesori**.  
Allestisci un labirinto nella tua stanza e posiziona sei carte di colori diversi in angoli differenti.  
La tua PiCar-X **cercherà, riconoscerà e festeggerà** quando troverà il colore bersaglio.  

Questo progetto combina tre abilità che hai già imparato:

* **Visione artificiale** – rilevamento delle carte colorate con la fotocamera Pi.  
* **Controllo da tastiera** – guida manuale del robot attraverso il labirinto.  
* **Feedback vocale** – Pico2Wave annuncia il colore bersaglio e il successo.  

È un gioco divertente che mostra come i robot possano **vedere, pensare e agire** proprio come dei cacciatori di tesori!
   
.. note::
   Puoi scaricare e stampare le :download:`Carte Colori in PDF <https://github.com/sunfounder/sf-pdf/raw/master/prop_card/object_detection/color-cards.pdf>` per un rilevamento dei colori affidabile.

Prima di iniziare
-----------------

Assicurati di aver completato:

* :ref:`install_all_modules` — Installa i moduli ``robot-hat``, ``vilib``, ``picar-x``, poi esegui lo script ``i2samp.sh``.

Esegui il Codice
------------------

.. raw:: html

    <run></run>

.. code-block:: bash

    cd ~/picar-x/example
    sudo python3 20.treasure_hunt.py

Dopo l’esecuzione, vedrai un messaggio simile a questo:

.. code-block:: text

    * Running on http://0.0.0.0:9000/ (Press CTRL+C to quit)

Quindi, apri ``http://<il tuo IP>:9000/mjpg`` nel tuo browser per visualizzare il flusso video live.  
Esempio: ``http://192.168.18.113:9000/mjpg``  

.. image:: img/display.png

Regole del Gioco
----------------

1. Il robot seleziona casualmente un **colore bersaglio** e dice: **“Cerca il rosso!”**  
2. Guida PiCar-X con la tastiera:  

   * ``w`` = avanti  
   * ``a`` = gira a sinistra  
   * ``s`` = indietro  
   * ``d`` = gira a destra  
   * ``space`` = ripeti colore bersaglio  
   * ``Ctrl+C`` = esci  

3. Quando la fotocamera vede la carta del colore bersaglio, PiCar-X dice **“Ben fatto!”**  
4. Viene scelto un nuovo colore bersaglio e la caccia continua!  

Codice
---------

.. code-block:: python

    #!/usr/bin/env python3

    from picarx import Picarx
    from vilib import Vilib
    from picarx.tts import Pico2Wave

    from time import sleep
    import threading
    import readchar
    import random

    # -----------------------
    # Settings
    # -----------------------
    COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
    DETECTION_WIDTH_THRESHOLD = 100  # how wide the color blob must be
    DRIVE_SPEED = 80
    TURN_ANGLE = 30

    MANUAL = """
    Press keys to control PiCar-X:
      w: forward    a: turn left    s: backward    d: turn right
      space: repeat target          Ctrl+C: quit
    """

    # -----------------------
    # Init
    # -----------------------
    px = Picarx()

    tts = Pico2Wave()
    tts.set_lang("en-US")

    current_color = "red"
    key = None
    lock = threading.Lock()

    def say(line: str):
        print(f"[SAY] {line}")
        tts.say(line)

    def renew_color_detect():
        """Choose a new target color and start detection."""
        global current_color
        current_color = random.choice(COLORS)
        Vilib.color_detect(current_color)
        say(f"Look for {current_color}!")

    def key_scan_thread():
        """Background thread reading keys."""
        global key
        while True:
            k = readchar.readkey()
            # Map special keys before lowercasing
            if k == readchar.key.SPACE:
                mapped = "space"
            elif k == readchar.key.CTRL_C:
                mapped = "quit"
            else:
                mapped = k.lower()

            with lock:
                key = mapped

            if mapped == "quit":
                return
            sleep(0.01)

    def car_move(k: str):
        if k == "w":
            px.set_dir_servo_angle(0)
            px.forward(DRIVE_SPEED)
        elif k == "s":
            px.set_dir_servo_angle(0)
            px.backward(DRIVE_SPEED)
        elif k == "a":
            px.set_dir_servo_angle(-TURN_ANGLE)
            px.forward(DRIVE_SPEED)
        elif k == "d":
            px.set_dir_servo_angle(TURN_ANGLE)
            px.forward(DRIVE_SPEED)

    def main():
        global key

        # Start camera and web preview
        Vilib.camera_start(vflip=False, hflip=False)
        Vilib.display(local=False, web=True)
        sleep(0.8)

        print(MANUAL.strip())
        say("Game start!")
        sleep(0.1)
        renew_color_detect()

        # Start keyboard thread (modern style)
        key_thread = threading.Thread(target=key_scan_thread, daemon=True)
        key_thread.start()

        try:
            while True:
                # Check detection: if target color present and wide enough
                if (Vilib.detect_obj_parameter.get("color_n", 0) != 0 and
                    Vilib.detect_obj_parameter.get("color_w", 0) > DETECTION_WIDTH_THRESHOLD):
                    say("Well done!")
                    sleep(0.1)
                    renew_color_detect()

                # Take a snapshot of the last key (and clear it)
                with lock:
                    k = key
                    key = None

                # Handle movement / actions
                if k in ("w", "a", "s", "d"):
                    car_move(k)
                    sleep(0.5)
                    px.stop()
                elif k == "space":
                    say(f"Look for {current_color}!")
                elif k == "quit":
                    print("\n[INFO] Quit requested.")
                    break

                sleep(0.05)

        except KeyboardInterrupt:
            print("\n[INFO] Stopped by user.")
        finally:
            try:
                Vilib.camera_close()
            except Exception:
                pass
            px.stop()
            say("Goodbye!")
            sleep(0.2)

    if __name__ == "__main__":
        main()


Come Funziona
-------------

1. **Inizializzazione**

   * Importa i moduli e configura PiCar-X, la fotocamera e il TTS.  
   * Imposta l’elenco dei colori, la velocità e l’angolo di sterzata.  

2. **Selezione del Bersaglio**

   * ``renew_color_detect()`` sceglie casualmente un colore bersaglio.  
   * Il robot annuncia il colore bersaglio con Pico2Wave.  

3. **Controllo da Tastiera**

   * ``key_scan_thread()`` viene eseguito in background per catturare i tasti.  
   * I tasti ``w, a, s, d`` controllano il movimento; ``space`` ripete il bersaglio.  

4. **Rilevamento Colore**

   * La fotocamera controlla costantemente se il colore bersaglio è visibile.  
   * Se la macchia rilevata è abbastanza grande, PiCar-X festeggia.  

5. **Ciclo Principale**

   * Gestisce continuamente movimento, rilevamento e feedback.  
   * Arresta ordinatamente il robot e la fotocamera all’uscita.  

Risoluzione dei Problemi
------------------------

* **Il feed della fotocamera non funziona?**  

  Esegui ``libcamera-hello`` per verificare che la fotocamera Pi sia correttamente collegata.  

* **Il robot non rileva i colori?**

  Assicurati che le carte siano stampate chiaramente e posizionate in buona illuminazione. Prova ad adattare ``DETECTION_WIDTH_THRESHOLD``.  

* **Nessun feedback vocale?**

  Controlla che ``pico2wave`` sia installato e che l’uscita audio sia configurata correttamente.  

* **L’auto non si muove?**

  Verifica che l’alimentazione di PiCar-X sia attiva e che la calibrazione dei motori sia corretta.  

----

Completando questa lezione, hai realizzato un **mini gioco di caccia al tesoro** con PiCar-X,  
combinando **visione, controllo e interazione** in un unico progetto!
