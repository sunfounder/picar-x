.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!


14. Sprachansage-Auto mit Espeak und Pico2Wave
=================================================

In dieser Lektion verwenden wir zwei in Raspberry Pi integrierte Text-to-Speech-(TTS)-Engines — **Espeak** und **Pico2Wave** —, um den PiCar-X sprechen zu lassen.  

Beide Engines sind einfach zu bedienen und funktionieren **offline**, unterscheiden sich aber deutlich in der Klangqualität:

* **Espeak**: sehr leichtgewichtig und schnell, aber mit roboterhafter Stimme. Geschwindigkeit, Tonhöhe und Lautstärke lassen sich anpassen.  
* **Pico2Wave**: erzeugt eine weichere und natürlichere Stimme als Espeak, bietet aber weniger Einstellmöglichkeiten.  

Du wirst den Unterschied in **Sprachqualität** und **Funktionsumfang** hören und anschließend ein „Sprachansage-Auto“ bauen, das seine Aktionen ansagt, bevor es sich bewegt.  

----

Bevor du beginnst
-----------------

Stelle sicher, dass du Folgendes abgeschlossen hast:

* :ref:`install_all_modules` — Installiere die Module ``robot-hat``, ``vilib``, ``picar-x`` und führe dann das Skript ``i2samp.sh`` aus.

----

1. Espeak testen
--------------------

Espeak ist eine leichtgewichtige TTS-Engine, die bereits in Raspberry Pi OS enthalten ist.  
Die Stimme klingt zwar roboterhaft, ist aber sehr flexibel konfigurierbar: Lautstärke, Tonhöhe, Geschwindigkeit und mehr lassen sich einstellen.

**So testest du Espeak**:

* Erstelle eine neue Datei mit folgendem Befehl:

  .. code-block:: bash
  
      cd ~/picar-x/example
      sudo nano test_tts_espeak.py

* Kopiere den Beispielcode hinein. Drücke anschließend ``Ctrl+X``, dann ``Y`` und schließlich ``Enter``, um zu speichern und zu beenden.

  .. code-block:: python
  
      from picarx.tts import Espeak

      tts = Espeak()
  
      # Optional voice tuning
      # tts.set_amp(100)   # 0 to 200
      # tts.set_speed(150) # 80 to 260
      # tts.set_gap(5)     # 0 to 200
      # tts.set_pitch(50)  # 0 to 99

      # Quick hello (sanity check)
      tts.say("Hello! I'm Espeak TTS.")


* Führe das Programm aus mit:

  .. code-block:: bash

     sudo python3 test_tts_espeak.py

* Du solltest hören, wie der PiCar-X sagt: „Hello! I'm Espeak TTS.“  
* Hebe die Kommentarzeichen bei den Zeilen zur Stimm­anpassung auf, um zu experimentieren, wie ``amp``, ``speed``, ``gap`` und ``pitch`` den Klang beeinflussen.

----

2. Pico2Wave testen
---------------------

Pico2Wave erzeugt eine natürlichere, menschlich klingende Stimme als Espeak.  
Es ist einfacher zu verwenden, bietet aber weniger Einstellmöglichkeiten — du kannst nur die Sprache ändern, nicht Tonhöhe oder Geschwindigkeit.

**So testest du Pico2Wave**:

* Erstelle eine neue Datei mit folgendem Befehl:

  .. code-block:: bash

      cd ~/picar-x/example
      sudo nano test_tts_pico2wave.py

* Kopiere dann den Beispielcode hinein. Drücke ``Ctrl+X``, dann ``Y`` und schließlich ``Enter``, um zu speichern und zu beenden.

  .. code-block:: python
  
      from picarx.tts import Pico2Wave

      tts = Pico2Wave()
  
      tts.set_lang('en-US')  # en-US, en-GB, de-DE, es-ES, fr-FR, it-IT
  
      # Kurzer Test
      tts.say("Hello! I'm Pico2Wave TTS.")

* Starte das Programm mit:

  .. code-block:: bash

    sudo python3 test_tts_pico2wave.py

* Du solltest hören, wie der PiCar-X sagt: „Hello! I'm Pico2Wave TTS.“  
* Probiere verschiedene Sprachen aus (z. B. ``es-ES`` für Spanisch), um die Unterschiede zu hören.

----

3. Sprachansage-Auto
--------------------

Jetzt kombinieren wir **Pico2Wave** oder **Espeak** mit dem Fahrcode des PiCar-X, um ein „Sprachansage-Auto“ zu bauen:  
Vor jeder Aktion kündigt das Auto an, was es gleich tun wird.

**Code ausführen**

.. code-block:: bash

    cd ~/picar-x/example
    sudo python3 14.voice_promt_car.py

Wenn du diesen Code ausführst, fährt dein PiCar-X vorwärts, rückwärts und macht Drehungen — und kündigt jede Bewegung vorher per Sprachausgabe an.  
So wird dein Auto sicherer, freundlicher und interaktiver.

**Code**


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

Fehlerbehebung
-------------------

* **Kein Ton bei der Ausführung von Espeak oder Pico2Wave**

  * Überprüfe, ob Lautsprecher oder Kopfhörer richtig angeschlossen sind und die Lautstärke nicht stummgeschaltet ist.  
  * Führe einen kurzen Test im Terminal aus:

    .. code-block:: bash

       espeak "Hello world"
       pico2wave -w test.wav "Hello world" && aplay test.wav

  Wenn du nichts hörst, liegt das Problem bei der Audioausgabe, nicht bei deinem Python-Code.

* **Espeak-Stimme klingt zu schnell oder zu roboterhaft**

  * Versuche, die Parameter in deinem Code anzupassen:

    .. code-block:: python

       tts.set_speed(120)   # langsamer
       tts.set_pitch(60)    # andere Tonhöhe

* **„Permission denied“ beim Ausführen des Codes**

  * Führe den Code mit ``sudo`` aus:

    .. code-block:: bash

       sudo python3 test_tts_espeak.py


Vergleich: Espeak vs Pico2Wave
-------------------------------------

.. list-table::
   :widths: 20 40 40
   :header-rows: 1

   * - Funktion
     - Espeak
     - Pico2Wave
   * - Sprachqualität
     - Roboterhaft, synthetisch
     - Natürlicher, menschlicher
   * - Sprachen
     - Standard: Englisch
     - Weniger, aber gängige Sprachen
   * - Anpassbar
     - Ja (Geschwindigkeit, Tonhöhe usw.)
     - Nein (nur Sprache)
   * - Leistung
     - Sehr schnell, leichtgewichtig
     - Etwas langsamer, ressourcenintensiver
