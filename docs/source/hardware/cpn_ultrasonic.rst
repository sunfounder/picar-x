.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

Ultraschallmodul
================================

.. image:: img/ultrasonic_pic.png
    :width: 400
    :align: center

* **TRIG**: Trigger-Puls-Eingang
* **ECHO**: Echo-Puls-Ausgang
* **GND**: Masse
* **VCC**: 5V Stromversorgung

Dies ist der HC-SR04 Ultraschall-Distanzsensor, der eine berührungslose Messung von 2 cm bis 400 cm mit einer Reichweitengenauigkeit von bis zu 3 mm bietet. Das Modul enthält einen Ultraschallsender, einen Empfänger und eine Steuerungsschaltung.

Sie müssen nur 4 Pins anschließen: VCC (Stromversorgung), Trig (Trigger), Echo (Empfangen) und GND (Masse), um es für Ihre Messprojekte einfach zu verwenden.

**Eigenschaften**

* Betriebsspannung: DC5V
* Betriebsstrom: 16mA
* Arbeitsfrequenz: 40Hz
* Max. Reichweite: 500cm
* Min. Reichweite: 2cm
* Trigger-Eingangssignal: 10uS TTL-Puls
* Echo-Ausgangssignal: Eingangssignal im TTL-Pegel und die Reichweite proportional
* Anschluss: XH2.54-4P
* Abmessungen: 46x20.5x15 mm

**Prinzip**

Die grundlegenden Prinzipien sind wie folgt:

* Verwenden Sie IO-Trigger für ein mindestens 10us hohes Signal.
* Das Modul sendet einen 8-Zyklus-Ausbruch von Ultraschall bei 40 kHz und erkennt, ob ein Pulssignal empfangen wird.
* Echo gibt ein hohes Signal aus, wenn ein Signal zurückkommt; die Dauer des hohen Signals ist die Zeit vom Aussenden bis zum Empfang.
* Entfernung = (Zeit des hohen Signals x Schallgeschwindigkeit (340M/S)) / 2

    .. image:: img/ultrasonic_prin.jpg
        :width: 800

Formel: 

* us / 58 = Entfernung in Zentimetern
* us / 148 = Entfernung in Zoll
* Entfernung = Zeit des hohen Signals x Geschwindigkeit (340M/S) / 2


**Anwendungshinweise**

* Dieses Modul sollte nicht unter Spannung angeschlossen werden. Falls erforderlich, sollte zuerst die Masse (GND) des Moduls verbunden werden. Andernfalls wird die Funktion des Moduls beeinträchtigt.
* Die Fläche des zu messenden Objekts sollte mindestens 0,5 Quadratmeter betragen und so flach wie möglich sein. Andernfalls werden die Ergebnisse beeinträchtigt.
