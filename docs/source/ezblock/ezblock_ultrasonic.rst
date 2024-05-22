.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

Test des Ultraschallmoduls
==============================

Der PiCar-X verfügt über ein integriertes Ultraschall-Sensormodul, das für Hindernisvermeidung und automatische Objektverfolgungsexperimente verwendet werden kann. In dieser Lektion wird das Modul eine Entfernung in Zentimetern messen (24 cm = 1 Zoll) und die Ergebnisse in einem **Debug**-Fenster **ausgeben**.

**TIPPS**

.. image:: img/sp210512_114549.png 

Der Block **Ultraschall Entfernung ablesen** ermittelt die Entfernung von PiCar-X zu einem direkt vorausliegenden Hindernis.

.. image:: img/sp210512_114830.png

Dieses Programm wird durch eine **Variable** vereinfacht. Wenn beispielsweise mehrere Funktionen in einem Programm jeweils die Entfernung zu einem Hindernis nutzen müssen, kann eine **Variable** verwendet werden, um den gleichen Entfernungswert an jede Funktion zu übermitteln, statt dass jede Funktion den Wert separat ausliest.

.. image:: img/sp210512_114916.png

Klicken Sie auf die Schaltfläche **Variable erstellen...** in der Kategorie **Variablen** und verwenden Sie den Dropdown-Pfeil, um die Variable mit dem Namen „Entfernung“ auszuwählen.

.. image:: img/sp210512_114945.png

Die **Ausgabefunktion** kann Daten wie Variablen und Text zur einfachen Fehlersuche ausgeben.

.. image:: img/debug_monitor.png

Sobald der Code läuft, aktivieren Sie den Debug-Monitor, indem Sie auf das **Debug**-Symbol in der unteren linken Ecke klicken.

**BEISPIEL**

.. note::

    * Sie können das Programm gemäß dem folgenden Bild erstellen. Bitte beziehen Sie sich auf das Tutorial: :ref:`ezblock:create_project_latest`.
    * Oder finden Sie den Code mit dem gleichen Namen auf der **Beispiele**-Seite des EzBlock Studios und klicken Sie direkt auf **Ausführen** oder **Bearbeiten**.

.. image:: img/sp210512_115125.png
