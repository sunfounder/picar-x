Servo-Justierung(Wichtig)
============================

Der Winkelbereich des Servos liegt bei -90~90 Grad, aber der in der Fabrik eingestellte Winkel ist zufällig, vielleicht 0°, vielleicht 45°. Wenn wir ihn direkt mit einem solchen Winkel montieren, führt dies nach dem Ausführen des Codes des Roboters zu einem chaotischen Zustand oder schlimmer noch, es kann dazu führen, dass der Servo blockiert und durchbrennt.

Daher müssen wir hier alle Servowinkel auf 0° einstellen und sie dann montieren, sodass der Servowinkel in der Mitte ist, egal in welche Richtung er sich dreht.

#. Um sicherzustellen, dass der Servo ordnungsgemäß auf 0° eingestellt wurde, stecken Sie zuerst den Servoarm in die Servowelle und drehen Sie dann vorsichtig den Schwenkarm in einen anderen Winkel. Dieser Servoarm dient lediglich dazu, Ihnen deutlich zu zeigen, dass der Servo sich dreht.

    .. image:: img/servo_arm.png

#. Führen Sie nun ``servo_zeroing.py`` im Ordner ``example/`` aus.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/picar-x/example
        sudo python3 servo_zeroing.py

#. Stecken Sie als Nächstes das Servokabel wie folgt in den P11-Port, gleichzeitig sehen Sie, dass sich der Servoarm in eine Position dreht (Dies ist die 0°-Position, die ein zufälliger Ort ist und möglicherweise nicht vertikal oder parallel ist).

    .. image:: img/Z_P11.JPG

#. Entfernen Sie jetzt den Servoarm, wobei das Servokabel angeschlossen bleibt, und schalten Sie den Strom nicht aus. Fahren Sie dann mit der Montage gemäß den Papieranweisungen fort.

.. note::

    * Ziehen Sie dieses Servokabel nicht ab, bevor Sie es mit der Servoschraube befestigt haben; Sie können es nach der Befestigung abziehen.
    * Drehen Sie den Servo nicht, während er eingeschaltet ist, um Schäden zu vermeiden. Wenn die Servowelle nicht im richtigen Winkel eingeführt ist, ziehen Sie den Servo heraus und stecken Sie ihn erneut ein.
    * Bevor Sie jeden Servo montieren, müssen Sie das Servokabel in P11 einstecken und den Strom einschalten, um seinen Winkel auf 0° einzustellen.


