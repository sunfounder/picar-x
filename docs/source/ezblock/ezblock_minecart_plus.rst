.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

Minenwagen Plus
=======================

In diesem Projekt wurde dem :ref:`ezb_minecart`-Projekt eine Entgleisungswiederherstellung hinzugefügt, um dem PiCar-X die Anpassung und Wiederherstellung bei stärkeren Kurven zu ermöglichen.

.. image:: img/minec.png


**TIPPS**

#. Verwende einen weiteren **to do something** -Block, um dem PiCar-X das Zurücksetzen und die Wiederherstellung nach einer scharfen Kurve zu ermöglichen. Beachte, dass die neue **to do something** -Funktion keine Werte zurückgibt, sondern ausschließlich zur Neuausrichtung des PiCar-X verwendet wird.

    .. image:: img/sp210512_171727.png

#. Der Block **Set ref to ()** wird verwendet, um den Graustufen-Schwellenwert festzulegen. Du musst ihn entsprechend der tatsächlichen Situation anpassen. Du kannst :ref:`test_grayscale` ausführen, um die Werte des Graustufen-Moduls auf weißen und schwarzen Oberflächen zu sehen und ihre mittleren Werte in diesem Block einzutragen.


**BEISPIEL**

.. note::

    * Du kannst das Programm gemäß der folgenden Abbildung schreiben. Bitte beachte das Tutorial: :ref:`ezblock:create_project_latest`.
    * Oder finde den Code mit demselben Namen auf der **Examples**-Seite des EzBlock Studios und klicke direkt auf **Run** oder **Edit**.

.. image:: img/sp210512_171914.png

.. image:: img/sp210512_171932.png

.. image:: img/sp210512_171425.png

.. image:: img/sp210512_171454.png