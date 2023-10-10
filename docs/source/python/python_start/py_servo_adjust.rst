Servo-Einstellung (Wichtig)
=====================================

Der Winkelbereich des Servos liegt zwischen -90 und 90 Grad, aber der im Werk eingestellte Winkel ist zufällig, vielleicht 0°, vielleicht 45°. Würden wir ihn in diesem Zustand direkt montieren, würde dies nach dem Ausführen des Codes zu einem chaotischen Zustand führen. Im schlimmsten Fall könnte der Servo blockieren und durchbrennen.

Deshalb sollten alle Servowinkel auf 0° eingestellt und dann montiert werden, sodass der Servowinkel mittig ist, egal in welche Richtung gedreht wird.

Es wird empfohlen, nach der Montage die :ref:`py_calibrate` durchzuführen. Aufgrund möglicher Abweichungen bei der Montage oder Einschränkungen des Servos selbst kann der Servowinkel schief sein. Durch die Kalibrierung können Sie den Servo in einen optimalen Zustand versetzen; der Kalibrierungswinkel liegt üblicherweise zwischen -5 und 5 Grad.

Wenn der Abweichungswinkel jedoch zu groß ist, müssen Sie in diesem Abschnitt zurückkehren, den Servowinkel wieder auf 0° einstellen und den Anweisungen folgen, um das Auto erneut zusammenzubauen.

#. Um sicherzustellen, dass der Servo korrekt auf 0° eingestellt ist, stecken Sie zuerst den Servoarm in die Servowelle und drehen Sie ihn dann vorsichtig in einen anderen Winkel.

    .. image:: img/servo_arm.png

#. Führen Sie nun ``servo_zeroing.py`` im Ordner ``example/`` aus.

    .. raw:: html

        <run></run>

    .. code-block::

        cd /home/pi/picar-x/example
        sudo python3 servo_zeroing.py

#. Stecken Sie als Nächstes das Servokabel wie folgt in den P11-Port.

    .. image:: img/Z_P11.JPG

#. Zu diesem Zeitpunkt wird der Servoarm in eine bestimmte Position (0°) rotieren.

Nun können Sie die Montage gemäß den Anweisungen auf dem Montageblatt fortsetzen.

.. note::

    * Ziehen Sie das Servokabel nicht ab, bevor Sie es mit der Servoschraube fixiert haben; Sie können es nach der Fixierung abziehen.
    * Drehen Sie den Servo nicht, während er eingeschaltet ist, um Schäden zu vermeiden; wenn die Servowelle nicht im richtigen Winkel eingesetzt ist, ziehen Sie den Servo heraus und setzen Sie ihn erneut ein.
    * Bevor Sie jeden Servo montieren, müssen Sie das Servokabel in den P11-Port stecken und die Stromversorgung einschalten, um den Winkel auf 0° einzustellen.
