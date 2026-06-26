.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

FAQ
===

Q1: Nach der Installation von Ezblock OS kann der Servo nicht auf 0° drehen?
-------------------------------------------------------------------------------

1) Überprüfen Sie, ob das Servokabel richtig angeschlossen ist und ob die Stromversorgung des Robot HAT eingeschaltet ist.
2) Drücken Sie den Reset-Knopf.
3) Wenn Sie bereits ein Programm im Ezblock Studio ausgeführt haben, ist das benutzerdefinierte Programm für P11 nicht mehr verfügbar. Sie können sich das untenstehende Bild ansehen und im Ezblock Studio ein Programm manuell erstellen, um den Servowinkel auf 0 zu setzen.

.. image:: img/faq_servo.png

Q2: Bei der Verwendung von VNC werde ich darauf hingewiesen, dass der Desktop momentan nicht angezeigt werden kann?
---------------------------------------------------------------------------------------------------------------------

Geben Sie im Terminal ``sudo raspi-config`` ein, um die Auflösung zu ändern.

Q3: Warum kehrt der Servo manchmal ohne Grund in die Mittelposition zurück?
-------------------------------------------------------------------------------

Wenn der Servo durch eine Struktur oder ein anderes Objekt blockiert wird und seine vorgesehene Position nicht erreichen kann, wird der Servo in den Stromabschalt-Schutzmodus versetzt, um zu verhindern, dass er durch zu hohen Stromfluss beschädigt wird.

Nach einer Zeit ohne Stromversorgung wird der Servo, wenn ihm kein PWM-Signal gegeben wird, automatisch in seine Ausgangsposition zurückkehren.

Q4: Wo finde ich ein detailliertes Tutorial zum Robot HAT?
----------------------------------------------------------

Hier finden Sie ein umfassendes Tutorial zum Robot HAT, einschließlich Informationen zu seiner Hardware und API.

* |link_robot_hat|

Q5: Über das Batterieladegerät
------------------------------

Um die Batterie aufzuladen, schließen Sie einfach ein 5V/2A Type-C-Netzteil an den Stromanschluss des Robot Hat an. Es ist nicht erforderlich, den Netzschalter des Robot Hat während des Ladevorgangs einzuschalten.
Das Gerät kann auch während des Ladevorgangs verwendet werden.

.. image:: img/robot_hat_pic.png
    :align: center
    :width: 500

Während des Ladevorgangs wird die Eingangsleistung durch den Ladechip verstärkt, um die Batterie zu laden und gleichzeitig den DC-DC-Wandler für die externe Nutzung zu versorgen. Die Ladeleistung beträgt dabei ungefähr 10W.
Wenn der externe Stromverbrauch über einen längeren Zeitraum hoch bleibt, kann die Batterie die Stromversorgung ergänzen, ähnlich wie bei der Nutzung eines Telefons während des Ladevorgangs. Beachten Sie jedoch die Kapazität der Batterie, um ein vollständiges Entladen während gleichzeitiger Nutzung und Aufladung zu vermeiden.

Q6: Kamera funktioniert nicht?
------------------------------

Falls die Kamera kein Bild anzeigt oder das Bild fehlerhaft ist, folgen Sie diesen Schritten zur Fehlerbehebung:

#. Stellen Sie sicher, dass das FPC-Kabel der Kamera fest angeschlossen ist. Es wird empfohlen, die Kamera erneut anzuschließen und dann das Gerät einzuschalten.

.. raw:: html

       <div style="text-align: center;">
           <video center loop autoplay muted style="max-width:90%">
               <source src="_static/video/rpi_connect1.mp4" type="video/mp4">
               Ihr Browser unterstützt das Video-Tag nicht.
           </video>
       </div>

2. Verwenden Sie den folgenden Befehl, um zu überprüfen, ob die Kamera erkannt wird.

.. code-block::

    libcamera-hello
