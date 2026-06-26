.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

Bewegung
========

Dieses erste Projekt zeigt Ihnen, wie Sie Bewegungsabläufe für die PiCar-X programmieren können. In diesem Projekt wird das Programm die PiCar-X anweisen, fünf Aktionen in folgender Reihenfolge auszuführen: „Vorwärts“, „Rückwärts“, „Links abbiegen“, „Rechts abbiegen“ und „Stoppen“.

Um die grundlegende Bedienung von Ezblock Studio zu erlernen, lesen Sie bitte die folgenden beiden Abschnitte:

* :ref:`ezblock:create_project_latest`


.. image:: img/move.png

**TIPPS**

.. image:: img/sp210512_113300.png

Dieser Block veranlasst die PiCar-X, mit einer Geschwindigkeit vorwärts zu fahren, die sich an einem Prozentsatz der verfügbaren Leistung orientiert. Im untenstehenden Beispiel bedeutet „50“, dass die Geschwindigkeit bei 50 % der Leistung oder Halbgeschwindigkeit liegt.

.. image:: img/sp210512_113418.png

Dieser Block veranlasst die PiCar-X, mit einer an einem Prozentsatz der verfügbaren Leistung orientierten Geschwindigkeit rückwärts zu fahren.

.. image:: img/sp210512_113514.png

Dieser Block passt die Ausrichtung der Vorderräder an. Der Bereich liegt bei „-45“ bis „45“. Im untenstehenden Beispiel bedeutet „-30“, dass die Räder um 30° nach links drehen werden.

.. image:: img/BLK_Basic_delay.png
    :width: 200

Dieser Block bewirkt eine zeitliche Verzögerung zwischen den Befehlen, basierend auf Millisekunden. Im untenstehenden Beispiel wartet die PiCar-X 1 Sekunde (1000 Millisekunden) bevor der nächste Befehl ausgeführt wird.

.. image:: img/sp210512_113550.png

Dieser Block bringt die PiCar-X zum vollständigen Anhalten.

**BEISPIEL**

.. note::

    * Sie können das Programm entsprechend dem folgenden Bild schreiben. Bitte beachten Sie das Tutorial: :ref:`ezblock:create_project_latest`.
    * Oder suchen Sie den Code mit dem gleichen Namen auf der **Beispiele**-Seite von EzBlock Studio und klicken Sie direkt auf **Ausführen** oder **Bearbeiten**.


.. image:: img/sp210512_113827.png
