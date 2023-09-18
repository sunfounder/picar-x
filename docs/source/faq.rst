FAQ
===========================

**Q1: Nach der Installation von Ezblock OS kann sich der Servo nicht auf 0° drehen?**

1) Überprüfen Sie, ob das Servokabel ordnungsgemäß angeschlossen ist und ob die Stromversorgung des Robot HAT eingeschaltet ist.
2) Drücken Sie die Reset-Taste.
3) Wenn Sie das Programm bereits in Ezblock Studio ausgeführt haben, ist das benutzerdefinierte Programm für P11 nicht mehr verfügbar. Sie können sich das Bild unten ansehen und manuell ein Programm in Ezblock Studio schreiben, um den Servowinkel auf 0 einzustellen.

.. image:: img/faq_servo.png

**Q2: Bei Verwendung von VNC wird mir angezeigt, dass der Desktop momentan nicht angezeigt werden kann?**

Geben Sie im Terminal ``sudo raspi-config`` ein, um die Auflösung zu ändern.

**Q3: Warum kehrt der Servo manchmal ohne Grund in die mittlere Position zurück?**

Wenn der Servo durch eine Struktur oder ein anderes Objekt blockiert ist und seine beabsichtigte Position nicht erreichen kann, wechselt der Servo in den Abschaltmodus, um zu verhindern, dass der Servo durch zu viel Strom ausgebrannt wird.

Nach einem Stromausfall kehrt der Servo automatisch in seine Ausgangsposition zurück, wenn kein PWM-Signal an den Servo gesendet wird.