.. _py_calibrate:

0. Kalibrierung des PiCar-X
=================================

Kalibrierung von Motoren & Servo
-----------------------------------

Einige Servowinkel können aufgrund möglicher Abweichungen bei der Montage des PiCar-X oder aufgrund der Einschränkungen der Servos selbst leicht geneigt sein, daher können Sie diese kalibrieren.

Natürlich können Sie dieses Kapitel überspringen, wenn Sie denken, dass die Montage perfekt ist und keine Kalibrierung erfordert.

#. Führen Sie ``calibration.py`` aus.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/picar-x/example/calibration
        sudo python3 calibration.py

#. Nachdem Sie den Code ausgeführt haben, wird folgende Oberfläche im Terminal angezeigt.

    .. image:: img/calibrate1.png

#. Die Taste ``R`` wird verwendet, um zu testen, ob die 3 Servos einwandfrei funktionieren. Nachdem ein Servo mit den Tasten ``1``, ``2`` oder ``3`` ausgewählt wurde, drücken Sie die Taste ``R``, um diesen Servo zu testen.

#. Drücken Sie die Zahlentaste ``1``, um den Servo des Vorderrads auszuwählen, und dann die Tasten ``W/S``, damit das Vorderrad so gerade wie möglich aussieht, ohne nach links oder rechts abzuweichen.

    .. image:: img/calibrate2.png

#. Drücken Sie die Zahlentaste ``2``, um den **Pan servo** auszuwählen, dann drücken Sie die Tasten ``W/S``, damit die Schwenk-/Neigeplattform geradeaus schaut und nicht nach links oder rechts kippt.

    .. image:: img/calibrate3.png

#. Drücken Sie die Zahlentaste ``3``, um den **tilt servo** auszuwählen, dann drücken Sie die Tasten ``W/S``, damit die Schwenk-/Neigeplattform geradeaus schaut und nicht nach oben oder unten kippt.

    .. image:: img/calibrate4.png

#. Da die Verkabelung der Motoren bei der Installation umgekehrt sein könnte, können Sie ``E`` drücken, um zu testen, ob das Auto normal vorwärtsfahren kann. Wenn nicht, verwenden Sie die Zahlentasten ``4`` und ``5``, um die linken und rechten Motoren auszuwählen, und dann drücken Sie die Taste ``Q``, um die Drehrichtung zu kalibrieren.

    .. image:: img/calibrate6.png

#. Wenn die Kalibrierung abgeschlossen ist, drücken Sie die ``Spacebar``, um die Kalibrierungsparameter zu speichern. Es erscheint eine Aufforderung, ``y`` zur Bestätigung einzugeben, und dann drücken Sie ``Ctrl+C``, um das Programm zu beenden und die Kalibrierung abzuschließen.

    .. image:: img/calibrate5.png


Kalibrierung des Graustufenmoduls
-------------------------------------

Aufgrund unterschiedlicher Umgebungsbedingungen und Beleuchtungssituationen 
sind die voreingestellten Parameter für das Graustufenmodul möglicherweise nicht optimal. 
Sie können diese Einstellungen über dieses Programm feinjustieren, um bessere Ergebnisse zu erzielen.


#. Legen Sie einen Streifen schwarzes Isolierband, etwa 15 cm lang, auf einen hellen Boden. Zentrieren Sie Ihr PiCar-X, sodass es über dem Band steht. Dabei sollte der mittlere Sensor des Graustufenmoduls direkt über dem Band sein, während die beiden flankierenden Sensoren über der helleren Oberfläche schweben sollten.


#. Führen Sie ``grayscale_calibration.py`` aus.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/picar-x/example/calibration
        sudo python3 grayscale_calibration.py

#. Nachdem Sie den Code ausgeführt haben, wird folgende Oberfläche im Terminal angezeigt.

    .. image:: img/calibrate_g1.png

#. Drücken Sie die Taste „Q“, um die Kalibrierung des Graustufenmoduls zu starten. Sie werden dann beobachten, wie das PiCar-X geringfügige Bewegungen nach links und rechts macht. Während dieses Vorgangs sollten alle drei Sensoren mindestens einmal über das Isolierband streichen.


#. Zusätzlich werden Sie drei Paare von deutlich unterschiedlichen Werten im Abschnitt „Schwellenwert“ bemerken, während „Linienreferenz“ zwei Zwischenwerte anzeigt, von denen jeder den Durchschnitt eines dieser Paare darstellt.

    .. image:: img/calibrate_g2.png

#. Suspendieren Sie anschließend das PiCar-X in der Luft (oder positionieren Sie es über einer Klippenkante) und drücken Sie die Taste „E“. Sie werden beobachten, dass auch die „Klippenreferenz“-Werte entsprechend aktualisiert werden.

    .. image:: img/calibrate_g3.png

#. Sobald Sie verifiziert haben, dass alle Werte korrekt sind, drücken Sie die „Leertaste“, um die Daten zu speichern. Sie können das Programm dann durch Drücken von Strg+C beenden.
