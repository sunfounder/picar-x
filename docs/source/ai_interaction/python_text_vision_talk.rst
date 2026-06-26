.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

17. Text Vision Talk mit Ollama
================================

In dieser Lektion lernst du, wie du **Ollama** verwendest — ein Tool, mit dem du große Sprach- und Vision-Modelle **lokal** ausführen kannst.
Wir zeigen dir, wie du Ollama installierst, ein Modell herunterlädst und den PiCar-X damit verbindest.

Mit dieser Einrichtung kann der PiCar-X ein Kamerabild aufnehmen und das Modell kann **sehen und erzählen** —
du kannst jede Frage zum Bild stellen, und das Modell antwortet in natürlicher Sprache.

Before You Start
----------------

Stelle sicher, dass du Folgendes abgeschlossen hast:

* :ref:`install_all_modules` — Installiere die Module ``robot-hat``, ``vilib``, ``picar-x`` und führe dann das Skript ``i2samp.sh`` aus.

.. _download_ollama:

1. Ollama (LLM) installieren und Modell herunterladen
-----------------------------------------------------

Du kannst **Ollama** entweder:

* direkt auf deinem Raspberry Pi installieren (lokaler Betrieb)
* oder auf einem anderen Computer (Mac/Windows/Linux) im **gleichen lokalen Netzwerk** installieren

**Empfohlene Modelle nach Hardware**

Du kannst jedes Modell aus dem |link_ollama_hub| wählen.
Die Modelle haben verschiedene Größen (3B, 7B, 13B, 70B ...).
Kleinere Modelle laufen schneller und benötigen weniger Speicher, während größere Modelle bessere Ergebnisse liefern, aber leistungsfähigere Hardware brauchen.

Die folgende Tabelle hilft dir, die passende Modellgröße für dein Gerät zu finden:

.. list-table::
   :header-rows: 1
   :widths: 20 20 40

   * - Modellgröße
     - Mindest-RAM
     - Empfohlene Hardware
   * - ~3B Parameter
     - 8 GB (16 GB besser)
     - Raspberry Pi 5 (16 GB) oder Mittelklasse-PC/Mac
   * - ~7B Parameter
     - 16 GB+
     - Pi 5 (16 GB, gerade noch nutzbar) oder Mittelklasse-PC/Mac
   * - ~13B Parameter
     - 32 GB+
     - Desktop-PC / Mac mit viel RAM
   * - 30B+ Parameter
     - 64 GB+
     - Workstation / Server / GPU empfohlen
   * - 70B+ Parameter
     - 128 GB+
     - High-End-Server mit mehreren GPUs

**Installation auf Raspberry Pi**

Wenn du Ollama direkt auf deinem Raspberry Pi installieren möchtest:

* Verwende ein **64-Bit Raspberry Pi OS**
* Starke Empfehlung: **Raspberry Pi 5 (16 GB RAM)**

Führe folgende Befehle aus:

.. code-block:: bash

   # Ollama installieren
   curl -fsSL https://ollama.com/install.sh | sh

   # Leichtgewichtiges Modell herunterladen (gut zum Testen)
   ollama pull llama3.2:3b

   # Kurzer Testlauf (tippe 'hi' und drücke Enter)
   ollama run llama3.2:3b

   # API bereitstellen (Standardport 11434)
   # Tipp: OLLAMA_HOST=0.0.0.0 setzen, um Zugriff aus dem LAN zu erlauben
   OLLAMA_HOST=0.0.0.0 ollama serve

**Installation auf Mac / Windows / Linux (Desktop-App)**

1. Lade Ollama von |link_ollama| herunter und installiere es.

   .. image:: img/llm_ollama_download.png

2. Öffne die Ollama-App, gehe zum **Model Selector**, und suche nach einem Modell, z. B. ``llama3.2:3b`` (leichtgewichtig zum Starten).

   .. image:: img/llm_ollama_choose.png

3. Nach Abschluss des Downloads kannst du im Chatfenster einfach „Hi“ eingeben. Ollama lädt das Modell beim ersten Gebrauch automatisch nach.

   .. image:: img/llm_olama_llama_download.png

4. Gehe zu **Settings** → aktiviere **Expose Ollama to the network**. Damit kann dein Raspberry Pi über das LAN darauf zugreifen.

   .. image:: img/llm_olama_windows_enable.png

.. warning::

   Wenn du eine Fehlermeldung wie:

   ``Error: model requires more system memory ...``

   siehst, ist das Modell zu groß für dein Gerät.
   Verwende ein **kleineres Modell** oder einen Computer mit mehr RAM.

2. Ollama testen
-----------------

Sobald Ollama installiert ist und das Modell bereitsteht, kannst du es mit einer einfachen Chat-Schleife testen.

**Schritte**

#. Neue Datei erstellen:

   .. code-block:: bash

      cd ~/picar-x/example
      nano test_llm_ollama.py

#. Füge den folgenden Code ein und speichere (``Ctrl+X`` → ``Y`` → ``Enter``):

   .. code-block:: python

      from picarx.llm import Ollama

      INSTRUCTIONS = "You are a helpful assistant."
      WELCOME = "Hello, I am a helpful assistant. How can I help you?"

      # If Ollama runs on the same Raspberry Pi, use "localhost".
      # If it runs on another computer in your LAN, replace with that computer's IP address.
      llm = Ollama(
          ip="localhost",
          model="llama3.2:3b"   # you can replace with any model
      )

      # Basic configuration
      llm.set_max_messages(20)
      llm.set_instructions(INSTRUCTIONS)
      llm.set_welcome(WELCOME)

      print(WELCOME)

      while True:
          text = input(">>> ")
          if text.strip().lower() in {"exit", "quit"}:
              break

          # Response with streaming output
          response = llm.prompt(text, stream=True)
          for token in response:
              if token:
                  print(token, end="", flush=True)
          print("")

#. Programm ausführen:

   .. code-block:: bash

      python3 test_llm_ollama.py

#. Jetzt kannst du direkt über das Terminal mit dem PiCar-X chatten.

   * Du kannst **jedes Modell** aus dem |link_ollama_hub| verwenden — für Geräte mit 8–16 GB RAM werden jedoch kleinere Modelle wie ``moondream:1.8b`` oder ``phi3:mini`` empfohlen.
   * Achte darauf, dass das Modell im Code genau dem Modell entspricht, das du in Ollama bereits heruntergeladen hast.
   * Tippe ``exit`` oder ``quit``, um das Programm zu beenden.
   * Wenn keine Verbindung möglich ist, überprüfe, ob Ollama läuft und ob beide Geräte sich im selben LAN befinden (bei Remote-Host).



3. Vision Talk mit Ollama
--------------------------

In dieser Demo nimmt die Pi-Kamera **jedes Mal ein Foto auf**, wenn du eine Frage eintippst.
Das Programm sendet **deinen eingegebenen Text + das neue Foto** an ein lokales Vision-Modell über Ollama
und streamt die Antwort des Modells auf Englisch zurück ins Terminal.
Dies ist eine minimale „See & Tell“-Basis, die du später z. B. um Farb-, Gesichts- oder QR-Erkennung erweitern kannst.

**Vorbereitung**

#. Öffne die **Ollama**-App (oder starte den Dienst) und stelle sicher, dass ein **vision-fähiges Modell** heruntergeladen wurde.

   * Wenn du genügend Speicher hast (≥16 GB RAM), kannst du ``llava:7b`` ausprobieren.
   * Mit **8 GB RAM** solltest du ein kleineres Modell verwenden, z. B. ``moondream:1.8b`` oder ``granite3.2-vision:2b``.

   .. image:: img/llm_ollama_image_model.png

**Demo ausführen**

#. Wechsle in den Beispielordner und führe das Skript aus:

   .. code-block:: bash

      cd ~/picar-x/example
      python3 17.text_vision_talk.py

#. Ablauf beim Start:

   * Das Programm gibt eine Willkommenszeile aus und wartet auf deine Eingabe (``>>>``).
   * **Jedes Mal, wenn du etwas eingibst** (z. B. „hello“, „Is there yellow?“, „Any faces?“, „What is on the desk?“), wird:

     * ein **Foto** mit der Pi-Kamera aufgenommen (gespeichert unter ``/tmp/llm-img.jpg``),
     * **dein Text + das Foto** an das Vision-Modell über Ollama gesendet,
     * die Antwort des Modells **gestreamt und im Terminal angezeigt**.

   * Tippe ``exit`` oder ``quit``, um das Programm zu beenden.

**Code**

.. code-block:: python

   from picarx.llm import Ollama
   from picamera2 import Picamera2
   import time

   """
   You need to set up Ollama first.

   Note: At least 8GB RAM is recommended for small vision models (e.g., moondream:1.8b).
         For llava:7b, more memory is preferred (>=16GB).
   """

   INSTRUCTIONS = "You are a helpful assistant."
   WELCOME = "Hello, I am a helpful assistant. How can I help you?"

   # If Ollama runs on the same Pi, use "localhost".
   # If it runs on another computer in your LAN, replace with that computer's IP.
   llm = Ollama(
       ip="localhost",          # e.g., "192.168.100.145" if remote
       model="llava:7b"         # change to "moondream:1.8b" or "granite3.2-vision:2b" for 8GB RAM
   )

   # Basic configuration
   llm.set_max_messages(20)
   llm.set_instructions(INSTRUCTIONS)
   llm.set_welcome(WELCOME)

   # Init camera
   camera = Picamera2()
   config = camera.create_still_configuration(
       main={"size": (1280, 720)},
   )
   camera.configure(config)
   camera.start()
   time.sleep(2)

   print(WELCOME)

   while True:
       input_text = input(">>> ")
       if input_text.strip().lower() in {"exit", "quit"}:
           break

       # Capture image
       img_path = "/tmp/llm-img.jpg"
       camera.capture_file(img_path)

       # Response with stream (text + image)
       response = llm.prompt(input_text, stream=True, image_path=img_path)
       for next_word in response:
           if next_word:
               print(next_word, end="", flush=True)
       print("")

Fehlerbehebung
---------------

* **Fehlermeldung: `model requires more system memory ...`**

  * Das bedeutet, dass das gewählte Modell zu groß für dein Gerät ist.
  * Verwende ein kleineres Modell wie ``moondream:1.8b`` oder ``granite3.2-vision:2b``.
  * Alternativ kannst du auf einen leistungsfähigeren Rechner mit mehr RAM wechseln und Ollama im Netzwerk freigeben.

* **Der Code kann keine Verbindung zu Ollama herstellen (connection refused).**

  Überprüfe Folgendes:

  * Stelle sicher, dass Ollama läuft (``ollama serve`` oder die Desktop-App ist geöffnet).
  * Wenn du einen entfernten Rechner verwendest, aktiviere **Expose to network** in den Ollama-Einstellungen.
  * Überprüfe, ob die ``ip="..."`` in deinem Code der richtigen LAN-IP entspricht.
  * Vergewissere dich, dass beide Geräte im selben lokalen Netzwerk sind.

* **Die Pi-Kamera nimmt kein Bild auf.**

  * Prüfe, ob ``Picamera2`` installiert ist und mit einem einfachen Testskript funktioniert.
  * Überprüfe, ob das Kamerakabel korrekt angeschlossen und die Kamera in ``raspi-config`` aktiviert ist.
  * Stelle sicher, dass dein Skript Schreibrechte für den Zielpfad (``/tmp/llm-img.jpg``) hat.

* **Die Ausgabe ist zu langsam.**

  * Kleinere Modelle liefern schnellere Antworten, jedoch oft mit einfacheren Inhalten.
  * Reduziere die Kameraauflösung (z. B. 640×480 statt 1280×720), um die Bildverarbeitung zu beschleunigen.
  * Schließe andere Programme auf deinem Pi, um CPU- und RAM-Ressourcen freizugeben.
