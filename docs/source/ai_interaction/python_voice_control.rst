.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!


16. Sprachgesteuertes Auto mit Vosk (Offline)
==============================================

Vosk ist eine leichtgewichtige Speech-to-Text-(STT)-Engine, die viele Sprachen unterstützt und vollständig **offline** auf dem Raspberry Pi läuft.  
Du brauchst nur einmal eine Internetverbindung, um ein Sprachmodell herunterzuladen. Danach funktioniert alles **ohne** Netzwerkzugang.  

In dieser Lektion werden wir:

* Das Mikrofon auf dem Raspberry Pi überprüfen.  
* Vosk mit einem ausgewählten Sprachmodell installieren und testen.  
* Ein **sprachgesteuertes PiCar-X** bauen, das auf ein Weckwort hört und auf Befehle wie **forward**, **backward**, **left** und **right** reagiert.  

----

Bevor du beginnst
-----------------

Stelle sicher, dass du Folgendes abgeschlossen hast:

* :ref:`install_all_modules` — Installiere die Module ``robot-hat``, ``vilib``, ``picar-x`` und führe dann das Skript ``i2samp.sh`` aus.

----

1. Mikrofon überprüfen
--------------------------

Bevor du die Spracherkennung verwendest, stelle sicher, dass dein USB-Mikrofon korrekt funktioniert.

#. Verfügbare Aufnahmegeräte auflisten:

   .. code-block:: bash

      arecord -l

   Suche nach einer Zeile wie ``card 1: ... device 0``.  

#. Eine kurze Testaufnahme machen (ersetze ``1,0`` durch die gefundenen Werte):

   .. code-block:: bash

      arecord -D plughw:1,0 -f S16_LE -r 16000 -d 3 test.wav

   * Beispiel: Wenn dein Gerät ``card 2, device 0`` ist, verwende:

   .. code-block:: bash

      arecord -D plughw:2,0 -f S16_LE -r 16000 -d 3 test.wav

#. Aufnahme abspielen, um sie zu überprüfen:

   .. code-block:: bash

      aplay test.wav

#. Mikrofonlautstärke anpassen (falls nötig):

   .. code-block:: bash

      alsamixer

   * Drücke **F6**, um dein USB-Mikrofon auszuwählen.  
   * Suche den Kanal **Mic** oder **Capture**.  
   * Stelle sicher, dass es nicht stummgeschaltet ist (**[MM]** bedeutet stumm – drücke ``M``, um die Stummschaltung aufzuheben → sollte **[OO]** anzeigen).  
   * Verwende die Pfeiltasten ↑ / ↓, um die Aufnahme­lautstärke anzupassen.


.. _test_vosk:

2. Vosk testen
--------------------------

**So geht’s**:

#. Neue Datei erstellen:

   .. code-block:: bash

      cd ~/picar-x/example
      sudo nano test_stt_vosk.py

#. Beispielcode hineinkopieren. Mit ``Ctrl+X``, dann ``Y`` und ``Enter`` speichern und beenden.

   .. code-block:: python

      from picarx.stt import Vosk

      vosk = Vosk(language="en-us")

      print(vosk.available_languages)

      while True:
          print("Say something")
          result = vosk.listen(stream=False)
          print(result)

#. Programm ausführen:

   .. code-block:: bash

      sudo python3 test_stt_vosk.py

#. Beim ersten Start mit einer neuen Sprache lädt Vosk **automatisch das Sprachmodell herunter** (standardmäßig die **kleine Version**).  
   Gleichzeitig wird die Liste der unterstützten Sprachen ausgegeben. Anschließend siehst du:

   .. code-block:: text

        vosk-model-small-en-us-0.15.zip: 100%|███████████████████| 39.3M/39.3M [00:05<00:00, 7.85MB/s]
        ['ar', 'ar-tn', 'ca', 'cn', 'cs', 'de', 'en-gb', 'en-in', 'en-us', 'eo', 'es', 'fa', 'fr', 'gu', 'hi', 'it', 'ja', 'ko', 'kz', 'nl', 'pl', 'pt', 'ru', 'sv', 'te', 'tg', 'tr', 'ua', 'uz', 'vn']
        Say something

   Das bedeutet:

   * Die Modelldatei (``vosk-model-small-en-us-0.15``) wurde heruntergeladen.  
   * Die Liste der unterstützten Sprachen wurde ausgegeben.  
   * Das System hört nun zu — sprich etwas ins PiCar-X-Mikrofon, und der erkannte Text wird im Terminal angezeigt.

   **Tipps**:

   * Halte das Mikrofon etwa 15–30 cm entfernt.  
   * Wähle ein Modell, das zu deiner Sprache und deinem Akzent passt.  


**Streaming-Modus (optional)**

Du kannst die Spracherkennung auch im Streaming-Modus laufen lassen, um **Zwischenergebnisse in Echtzeit** zu sehen:

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


3. Sprachgesteuertes Auto
-------------------------

Jetzt verbinden wir die Spracherkennung mit dem PiCar-X!  

Wir verwenden ein **Weckwort** („hey robot“), sodass das Auto nur auf Befehle hört, **nachdem** es aktiviert wurde.  
Das spart CPU-Leistung und verhindert Fehltrigger.

**Code ausführen**

.. code-block:: bash

   cd ~/picar-x/example
   sudo python3 16.voice_controlled_car.py

In diesem Programm:

* Wartet das Auto auf das Weckwort **„hey robot“**.  
* Danach kannst du ganz normal sprechen — solange dein Satz eines der Schlüsselwörter (**forward**, **backward**, **left**, **right**) enthält, reagiert das Auto.  

  Beispiele:

  * „Can you move forward a little?“ → das Auto fährt vorwärts.  
  * „Please turn left now.“ → das Auto biegt nach links ab.  

* Der Befehl **„sleep“** beendet die Steuerung und versetzt das Auto zurück in den Wartezustand.

**Code**

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

Fehlerbehebung
-----------------

* **„No such file or directory“ (beim Ausführen von `arecord`)**

  Du hast möglicherweise die falsche Karten-/Gerätenummer verwendet.  
  Führe aus:

  .. code-block:: bash

     arecord -l

  und ersetze ``1,0`` durch die Nummern, die für dein USB-Mikrofon angezeigt werden.

* **Aufgenommene Datei hat keinen Ton**

  Öffne den Mixer und überprüfe die Mikrofonlautstärke:

  .. code-block:: bash

     alsamixer

  * Drücke **F6**, um dein USB-Mikrofon auszuwählen.  
  * Stelle sicher, dass **Mic/Capture** nicht stummgeschaltet ist (**[OO]** statt **[MM]**).  
  * Erhöhe die Lautstärke mit der ↑-Taste.

* **Vosk erkennt keine Sprache**

  * Achte darauf, dass der **Sprachcode** zu deinem Modell passt (z. B. ``en-us`` für Englisch, ``zh-cn`` für Chinesisch).  
  * Halte das Mikrofon 15–30 cm entfernt und vermeide Hintergrundgeräusche.  
  * Sprich deutlich und langsam.

* **Weckwort („hey robot“) wird nicht erkannt**

  * Sprich in natürlichem Tonfall, nicht zu schnell.  
  * Prüfe, ob das Programm überhaupt erkannten Text ausgibt. Wenn nicht, funktioniert das Mikrofon nicht.

* **Hohe Latenz / langsame Erkennung**

  * Das automatisch heruntergeladene Modell ist ein **kleines Modell** (schneller, aber weniger genau).  
  * Wenn es trotzdem langsam ist, schließe andere Programme, um CPU-Ressourcen freizugeben.
