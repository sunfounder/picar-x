.. _py_calibrate:

Kalibrierung des PiCar-X
========================

Motoren & Servo kalibrieren
---------------------------

Einige Servowinkel könnten aufgrund möglicher Abweichungen bei der Installation des PiCar-X oder durch Limitationen der Servos selbst leicht schief sein, daher können Sie diese kalibrieren.

Natürlich können Sie dieses Kapitel überspringen, wenn Sie der Meinung sind, die Montage sei perfekt und benötige keine Kalibrierung.

#. Führen Sie ``calibration.py`` aus.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/picar-x/example/calibration
        sudo python3 calibration.py

#. Nachdem der Code ausgeführt wurde, wird die folgende Schnittstelle im Terminal angezeigt.

    .. image:: img/calibrate1.png

#. Die Taste ``R`` dient dazu, zu testen, ob der Servo, der die Lenkrichtung des Vorderrads steuert, einwandfrei funktioniert und nicht beschädigt ist.

#. Drücken Sie die Zahlentaste ``1``, um den Servo des Vorderrads auszuwählen, und dann die Tasten ``W/S``, um das Vorderrad so gerade wie möglich auszurichten, ohne nach links oder rechts zu verziehen.

    .. image:: img/calibrate2.png

#. Drücken Sie die Zahlentaste ``2``, um den **Pan-Servo** auszuwählen, und dann die Tasten ``W/S``, um die Schwenk-/Neigeplattform geradeaus auszurichten, ohne nach links oder rechts zu neigen.

    .. image:: img/calibrate3.png

#. Drücken Sie die Zahlentaste ``3``, um den **Tilt-Servo** auszuwählen, und dann die Tasten ``W/S``, um die Schwenk-/Neigeplattform geradeaus auszurichten, ohne nach oben oder unten zu neigen.

    .. image:: img/calibrate4.png

#. Da die Verkabelung der Motoren während der Installation vertauscht sein könnte, können Sie die Taste ``E`` drücken, um zu testen, ob das Auto normal vorwärts fahren kann. Falls nicht, verwenden Sie die Zahlentasten ``4`` und ``5``, um die linken und rechten Motoren auszuwählen, und drücken Sie dann die Taste ``Q``, um die Drehrichtung zu kalibrieren.

    .. image:: img/calibrate6.png

#. Wenn die Kalibrierung abgeschlossen ist, drücken Sie die Leertaste, um die Kalibrierungsparameter zu speichern. Ein Aufforderung erscheint, ``y`` zur Bestätigung einzugeben, und dann drücken Sie ``esc``, um das Programm zu beenden und die Kalibrierung abzuschließen.

    .. image:: img/calibrate5.png


Graumodul kalibrieren
---------------------

Aufgrund variabler Umgebungsbedingungen und Lichtverhältnisse könnten die voreingestellten Parameter des Graumoduls suboptimal sein. Diese Einstellungen können Sie durch dieses Programm feinabstimmen, um bessere Ergebnisse zu erzielen.

#. Legen Sie ein etwa 15 cm langes Stück schwarzes Isolierband auf einen hellfarbigen Boden. Positionieren Sie Ihr PiCar-X so, dass es über dem Band steht. In dieser Konfiguration sollte der mittlere Sensor des Graumoduls direkt über dem Band sein, während die beiden seitlichen Sensoren über der helleren Oberfläche schweben.

#. Führen Sie ``grayscale_calibration.py`` aus.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/picar-x/example/calibration
        sudo python3 Grayscale.py

#. Nachdem der Code ausgeführt wurde, wird die folgende Schnittstelle im Terminal angezeigt.

    .. image:: img/calibrate_g1.png

#. Drücken Sie die Taste "Q", um die Grauskalibrierung zu starten. Sie werden beobachten, wie das PiCar-X leichte Bewegungen nach links und rechts ausführt. Während dieses Vorgangs sollte jeder der drei Sensoren mindestens einmal über das Isolierband fahren.

#. Zusätzlich werden drei Paare von deutlich unterschiedlichen Werten im Abschnitt "Schwellenwert" erscheinen, während die "Linienreferenz" zwei mittlere Werte anzeigt, die jeweils den Durchschnitt eines dieser Paare darstellen.

    .. image:: img/calibrate_g2.png

#. Heben Sie anschließend das PiCar-X in die Luft (oder positionieren Sie es über einer Klippe) und drücken Sie die Taste "E". Sie werden feststellen, dass die Werte der "Klippenreferenz" entsprechend aktualisiert werden.

    .. image:: img/calibrate_g3.png

#. Sobald Sie überprüft haben, dass alle Werte korrekt sind, drücken Sie die Leertaste, um die Daten zu speichern. Sie können das Programm dann durch Drücken von Strg+C beenden.
