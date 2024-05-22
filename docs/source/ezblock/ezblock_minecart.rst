.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _ezb_minecart:

Minenwagen
=====================

Lass uns ein Minenwagen-Projekt machen! In diesem Projekt verwenden wir das Grayscale-Modul, um den PiCar-X entlang einer Strecke vorwärts zu bewegen. 
Verwende dunkel gefärbtes Klebeband, um eine möglichst gerade und nicht zu kurvig verlaufende Strecke auf dem Boden zu markieren. Es kann sein, dass einige Experimente erforderlich sind, falls der PiCar-X entgleist.

Beim Fahren entlang der Strecke werden die Sonden auf der linken und rechten Seite des Grayscale-Moduls helle Bodenflächen erkennen, während die mittlere Sonde die Strecke erkennt. Wenn die Strecke einen Bogen hat, wird die Sonde auf der linken oder rechten Seite des Sensors das dunkel gefärbte Klebeband erkennen und die Räder in diese Richtung lenken. Wenn der Minenwagen das Ende der Strecke erreicht oder entgleist, erkennt das Grayscale-Modul das dunkel gefärbte Klebeband der Strecke nicht mehr und der PiCar-X bleibt stehen.


**TIPPS**

* Der Block **Set ref to ()**  wird verwendet, um den Graustufen-Schwellenwert einzustellen. Du musst ihn entsprechend der tatsächlichen Situation anpassen. Du kannst :ref:`test_grayscale` ausführen, um die Werte des Graustufen-Moduls auf weißen und schwarzen Flächen zu sehen, und deren Mittelwerte in diesem Block eintragen.


**BEISPIEL**

.. note::

    * Du kannst das Programm entsprechend dem folgenden Bild schreiben. Bitte beachte das Tutorial: :ref:`ezblock:create_project_latest`.
    * Oder finde den Code mit demselben Namen auf der **Examples**-Seite des EzBlock Studio und klicke direkt auf **Run** oder **Edit**.


.. image:: img/sp210512_170342.png

.. image:: img/sp210512_171425.png

.. image:: img/sp210512_171454.png