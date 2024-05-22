.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _test_grayscale:

Test des Graustufenmoduls
==============================

Der PiCar-X beinhaltet ein Graustufenmodul, das sich für Anwendungen wie Linienverfolgung, Abgrund-Erkennung und weitere spannende Experimente eignet. Das Graustufenmodul besitzt drei Detektionssensoren, die jeweils einen Wert entsprechend der erkannten Farbschattierung zurückgeben. Zum Beispiel wird ein Sensor, der reines Schwarz erkennt, den Wert „0“ zurückgeben.

**TIPPS**

.. image:: img/sp210512_115406.png

Verwenden Sie den Block **Graustufenmodul** um den Wert eines der Sensoren auszulesen. Im obigen Beispiel ist der Sensor „A0“ der Sensor ganz links am PiCar-X. Verwenden Sie den Dropdown-Pfeil, um den Sensor auf „A1“ (Mittelsensor) oder „A2“ (rechter Sensor) zu wechseln.

.. image:: img/sp210512_120023.png

Das Programm wird mit einem Block **Liste erstellen mit** vereinfacht. 
Eine **Liste** wird ähnlich wie eine einzelne **Variable** verwendet, 
ist in diesem Fall jedoch effizienter als eine einzelne **Variable**, da das **Graustufenmodul** mehrere Sensorwerte zurückmeldet. 
Der Block **Liste erstellen mit** wird separate **Variablen** für jeden Sensor anlegen und sie in einer Liste zusammenfassen.

**BEISPIEL**

.. note::

    * Sie können das Programm gemäß dem folgenden Bild erstellen. Bitte beziehen Sie sich auf das Tutorial: :ref:`ezblock:create_project_latest`.
    * Oder suchen Sie den Code mit dem gleichen Namen auf der **Beispiele**-Seite des EzBlock Studios und klicken Sie direkt auf **Ausführen** oder **Bearbeiten**.

.. image:: img/sp210512_120508.png
