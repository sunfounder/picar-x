.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

Hintergrundmusik
======================

Neben der Programmierung des PiCar-X, um Soundeffekte oder Text-to-Speech (TTS) abzuspielen, kann der PiCar-X auch Hintergrundmusik wiedergeben. In diesem Projekt wird außerdem ein **Schieberegler**-Widget zur Anpassung der Musiklautstärke verwendet.

* :ref:`ezblock:remote_control_latest`

Für ein detailliertes Tutorial zu den Fernsteuerungsfunktionen von Ezblock verweisen wir auf das :ref:`ezb_remote_control` Tutorial.

**TIPPS**

.. image:: img/sp210512_152803.png

Der **Hintergrundmusik abspielen**-Block muss der **Start**-Funktion hinzugefügt werden. Verwenden Sie das Dropdown-Menü, um unterschiedliche Hintergrundmusiken für den PiCar-X auszuwählen.

.. image:: img/sp210512_153123.png

Mit dem Block **Hintergrundmusik-Lautstärke einstellen auf** wird die Lautstärke im Bereich von 0 bis 100 angepasst.

.. image:: img/sp210512_154708.png

Ziehen Sie eine **Schieberegler**-Leiste von der **Fernsteuerung**-Seite, um die Musiklautstärke anzupassen.

.. image:: img/sp210512_154259.png

Der **Schieberegler [A] Wert abrufen**-Block liest den Wert des Schiebereglers aus. Im obigen Beispiel ist Schieberegler 'A' ausgewählt. Wenn es mehrere Schieberegler gibt, verwenden Sie das Dropdown-Menü, um den entsprechenden auszuwählen.

**BEISPIEL**

.. note::

    * Sie können das Programm gemäß dem folgenden Bild schreiben. Bitte beziehen Sie sich auf das Tutorial: :ref:`ezblock:create_project_latest`.
    * Oder finden Sie den Code mit dem gleichen Namen auf der **Beispiele**-Seite des EzBlock Studios und klicken Sie direkt auf **Ausführen** oder **Bearbeiten**.

.. image:: img/sp210512_155406.png
