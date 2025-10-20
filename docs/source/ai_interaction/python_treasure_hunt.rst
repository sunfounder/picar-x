.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!


.. _py_treasure:

20. Schatzsuche
============================

In dieser Lektion verwandelst du deinen PiCar-X in einen **Schatzsucher-Roboter**.  
Baue ein Labyrinth in deinem Zimmer auf und platziere sechs verschiedenfarbige Karten in unterschiedlichen Ecken.  
Dein PiCar-X wird **suchen, erkennen und feiern**, sobald er die Ziel­farbe gefunden hat.  

Dieses Projekt kombiniert drei Fähigkeiten, die du bisher gelernt hast:

* **Computer Vision** – Erkennung farbiger Karten mit der Pi-Kamera.  
* **Tastatursteuerung** – Manuelles Steuern des Roboters durch das Labyrinth.  
* **Sprach-Feedback** – Pico2Wave kündigt die Zielfarbe an und bestätigt den Erfolg.  

Ein Spaßspiel, das zeigt, wie Roboter **sehen, denken und handeln** können – wie echte Schatzsucher!
 
----

Bevor du beginnst
-----------------

Stelle sicher, dass du Folgendes abgeschlossen hast:

* :ref:`install_all_modules` — Installiere die Module ``robot-hat``, ``vilib``, ``picar-x`` und führe dann das Skript ``i2samp.sh`` aus.
* Du kannst die :download:`PDF-Farbkarten <https://github.com/sunfounder/sf-pdf/raw/master/prop_card/object_detection/color-cards.pdf>` herunterladen und ausdrucken, um eine zuverlässige Farberkennung zu erhalten.  

----

Code ausführen
--------------

.. raw:: html

    <run></run>

.. code-block:: bash

    cd ~/picar-x/example
    sudo python3 20.treasure_hunt.py

Nach dem Start siehst du eine Meldung wie diese:

.. code-block:: text

    * Running on http://0.0.0.0:9000/ (Press CTRL+C to quit)

Öffne anschließend ``http://<deine IP>:9000/mjpg`` im Browser, um den Live-Videostream zu sehen.  
Beispiel: ``http://192.168.18.113:9000/mjpg``  

.. image:: img/display.png

Spielregeln
-----------

1. Der Roboter wählt zufällig eine **Zielfarbe** und sagt: **„Suche nach Rot!“**  
2. Du steuerst den PiCar-X mit der Tastatur:  

   * ``w`` = vorwärts  
   * ``a`` = links drehen  
   * ``s`` = rückwärts  
   * ``d`` = rechts drehen  
   * ``space`` = Ziel wiederholen  
   * ``Ctrl+C`` = beenden  

3. Sobald die Kamera die Ziel-Farbkarte sieht, sagt PiCar-X **„Gut gemacht!“**  
4. Es wird eine neue Zielfarbe gewählt – die Jagd geht weiter!  

Code
----


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


Funktionsweise
------------------------

1. **Initialisierung** 

   * Module importieren und PiCar-X, Kamera sowie TTS konfigurieren.  
   * Farbliste, Geschwindigkeit und Lenkwinkel festlegen.  

2. **Zielauswahl**

   * ``renew_color_detect()`` wählt zufällig eine Zielfarbe aus.  
   * Der Roboter kündigt das Ziel mit Pico2Wave an.  

3. **Tastatursteuerung** 

   * ``key_scan_thread()`` läuft im Hintergrund und erfasst Tasteneingaben.  
   * Tasten ``w, a, s, d`` steuern die Bewegung; ``space`` wiederholt das Ziel.  

4. **Farberkennung**  

   * Die Kamera prüft kontinuierlich, ob die Zielfarbe sichtbar ist.  
   * Wird ein ausreichend großer Farbfleck erkannt, feiert PiCar-X den Fund.  

5. **Hauptschleife**

   * Steuert fortlaufend Bewegung, Erkennung und Rückmeldung.  
   * Stoppt Roboter und Kamera sauber beim Beenden.  


Fehlerbehebung
---------------

* **Kamerastream funktioniert nicht?**  

  Führe ``libcamera-hello`` aus, um zu überprüfen, ob die Pi-Kamera richtig angeschlossen ist.  

* **Roboter erkennt keine Farben?** 

  Achte darauf, dass die Karten klar gedruckt sind und bei guter Beleuchtung liegen.  
  Versuche, ``DETECTION_WIDTH_THRESHOLD`` anzupassen.  

* **Keine Sprachausgabe?**  

  Prüfe, ob ``pico2wave`` installiert ist und dein Audioausgang richtig konfiguriert wurde.  

* **Auto bewegt sich nicht?**  

  Stelle sicher, dass die Stromversorgung des PiCar-X aktiv ist und die Motorenkalibrierung stimmt.  

----

Mit dieser Lektion hast du ein **Mini-Schatzsuchspiel** mit PiCar-X gebaut,  
das **Bildverarbeitung, Steuerung und Interaktion** zu einem Projekt vereint!
