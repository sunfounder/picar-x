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
===========================

Q1: Nach der Installation von Ezblock OS kann der Servo nicht auf 0° drehen?
----------------------------------------------------------------------------------

1) Überprüfen Sie, ob das Servokabel richtig angeschlossen ist und ob die Stromversorgung des Robot HAT eingeschaltet ist.
2) Drücken Sie den Reset-Knopf.
3) Wenn Sie bereits ein Programm im Ezblock Studio ausgeführt haben, ist das benutzerdefinierte Programm für P11 nicht mehr verfügbar. Sie können sich das untenstehende Bild ansehen und im Ezblock Studio ein Programm manuell erstellen, um den Servowinkel auf 0 zu setzen.

.. image:: img/faq_servo.png

Q2: Bei der Verwendung von VNC werde ich darauf hingewiesen, dass der Desktop momentan nicht angezeigt werden kann?
-------------------------------------------------------------------------------------------------------------------------------------

Geben Sie im Terminal ``sudo raspi-config`` ein, um die Auflösung zu ändern.

Q3: Warum kehrt der Servo manchmal ohne Grund in die Mittelposition zurück?
------------------------------------------------------------------------------------

Wenn der Servo durch eine Struktur oder ein anderes Objekt blockiert wird und seine vorgesehene Position nicht erreichen kann, wird der Servo in den Stromabschalt-Schutzmodus versetzt, um zu verhindern, dass er durch zu hohen Stromfluss beschädigt wird.

Nach einer Zeit ohne Stromversorgung wird der Servo, wenn ihm kein PWM-Signal gegeben wird, automatisch in seine Ausgangsposition zurückkehren.

Q4: Wo finde ich ein detailliertes Tutorial zum Robot HAT?
---------------------------------------------------------------

Hier finden Sie ein umfassendes Tutorial zum Robot HAT, einschließlich Informationen zu seiner Hardware und API.

* |link_robot_hat|
