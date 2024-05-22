.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

Stierkampf
==============

Verwandeln Sie den PiCar-X in einen wütenden Stier! Bereiten Sie ein rotes Tuch, wie ein Taschentuch, vor und werden Sie ein Stierkämpfer. Achten Sie darauf, nicht getroffen zu werden, wenn der PiCar-X dem roten Tuch hinterherjagt!

.. note::

    Dieses Projekt ist anspruchsvoller als die vorhergehenden Projekte. Der PiCar-X wird die Farberkennungsfunktion nutzen müssen, um die Kamera auf das rote Tuch auszurichten. Die Körperausrichtung muss sich automatisch an die Richtung anpassen, in die die Kamera zeigt.

**TIPPS**

.. image:: img/sp210512_174650.png

Beginnen Sie damit, den Block **color detection [red]** zum **Start**-Widget hinzuzufügen, um den PiCar-X nach einem roten Objekt suchen zu lassen. In der Dauerschleife fügen Sie den Block **[Breite] der erkannten Farbe** hinzu, um die Eingabe in ein "Objekterkennungs"-Raster zu transformieren.

.. image:: img/sp210512_174807.png

Die "Objekterkennung" gibt die erkannten Koordinaten in (x, y)-Werten aus, basierend auf dem Mittelpunkt des Kamerabildes. Der Bildschirm ist in ein 3x3-Raster unterteilt, wie unten dargestellt. Wenn sich das rote Tuch oben links im Kamerabild befindet, lauten die (x, y)-Koordinaten (-1, 1).

.. image:: img/sp210512_174956.png

Die "Objekterkennung" erkennt die Breite und Höhe der Grafik. Wenn mehrere Ziele identifiziert werden, werden die Abmessungen des größten Ziels erfasst.

**BEISPIEL**

.. note::

    * Sie können das Programm gemäß der folgenden Abbildung schreiben. Bitte beachten Sie das Tutorial: :ref:`ezblock:create_project_latest`.
    * Oder finden Sie den Code mit demselben Namen auf der **Examples** -Seite des EzBlock Studios und klicken Sie direkt auf **Run** oder **Edit**.

.. image:: img/sp210512_175519.png
    :width: 800