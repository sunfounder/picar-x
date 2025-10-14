.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

1. Was du sonst noch brauchst
===============================

Bevor wir mit dem PiCar-X loslegen, bereiten wir die wichtigste Hardware vor.  
Stell dir diese Komponenten als das **Gehirn, Herz und die Sinne** des PiCar-X vor — ohne sie kann das Auto nicht richtig funktionieren.

Erforderliche Komponenten
------------------------------

* **Raspberry Pi**

  Der Raspberry Pi fungiert als **Gehirn** des PiCar-X und übernimmt alle Rechen-, Sensor- und Steueraufgaben.
  
  .. image:: img/need_pi.jpg

  * **Kompatible Modelle**: Raspberry Pi 5, 4, 3 und Raspberry Pi Zero 2 W (am besten auf Pi 5 oder Pi 4)  
  * **Minimum**: **2 GB RAM** — ausreichend für alle Standardfunktionen des PiCar-X (Bewegung, Sensoren, Kamerastreaming) sowie für **Online-KI-Dienste** wie OpenAI Whisper, TTS oder LLMs.  
  * **Empfohlen**: **4 GB RAM oder mehr** — sorgt für eine flüssigere Leistung beim gleichzeitigen Ausführen **lokaler KI-Modelle** (z. B. Vosk-Spracherkennung, Piper TTS oder leichte LLMs) zusammen mit Kamerastreaming und Steuerung.

* **Netzteil**

  PiCar-X wird mit einem **18650-Akkupack** und einer **Robot HAT**-Platine mit integriertem Ladegerät geliefert.
  
  .. image:: img/need_power.png
    :width: 400

  * Zum Laden wird ein **5 V 3 A Netzteil** empfohlen, z. B. das offizielle **Raspberry Pi 15 W USB-C Netzteil**.  
  * Alternativ kannst du ein **USB-C Power Delivery (PD)**-Ladegerät oder ein **QC 2.0 Schnellladegerät** verwenden.  
  * Eine vollständige Ladung dauert etwa **2 Stunden** (von 0 % auf 100 %).

* **Micro-SD-Karte**

  Der Raspberry Pi hat **keine eingebaute Festplatte**. Er startet und speichert alle Dateien auf einer Micro-SD-Karte.
  
  .. image:: img/need_sd.jpg
    :width: 200

  * Minimum: **16 GB**  
  * Empfohlen: **32 GB** für mehr Stabilität  
  * Marke: Verwende zuverlässige Karten wie **SanDisk** oder **Samsung**, um Lese-/Schreibfehler zu vermeiden.

Optionale Komponenten
------------------------

Diese Komponenten sind nicht zwingend erforderlich, verbessern aber die Einrichtung und Fehlersuche deutlich:

* **Monitor (HDMI oder TV)**

  Für Anfänger empfehlen wir ein Display mit HDMI-Eingang, um das Raspberry Pi OS einfach zu konfigurieren und grafische Programme auszuführen.

  .. image:: img/need_screen.png
    :width: 400

* **HDMI-Kabel (Standard / Mini / Micro)**

  Je nach Raspberry Pi-Modell wird ein anderer HDMI-Typ benötigt. Prüfe dein Modell und verwende das passende Kabel.

  * **Raspberry Pi 4 / 5**: Micro HDMI  
  * **Raspberry Pi 3**: Standard HDMI  
  * **Raspberry Pi Zero 2W**: Mini HDMI

  .. image:: img/need_hdmi.png
    :width: 400

* **Tastatur & Maus**

  Sehr hilfreich bei der ersten Einrichtung des Raspberry Pi OS. Später kannst du per SSH oder VNC auf den Pi zugreifen, aber für den Einstieg empfehlen wir ein einfaches USB- oder Funkset.

  .. image:: img/need_keyboard_mouse.png
    :width: 500

**Vorbereitungstipps**

* Wenn du das **PiCar-X Kit** gekauft hast, sind die meisten Zubehörteile enthalten.  
  Du musst jedoch die **Raspberry Pi-Platine**, die **Micro-SD-Karte** und das **Netzteil** separat vorbereiten.  
* Nicht sicher, was du kaufen sollst? 👉 Die stabilste und universellste Wahl ist:  
  **Raspberry Pi 4 (2 GB) + offizielles Netzteil + 32 GB Micro-SD-Karte**.
