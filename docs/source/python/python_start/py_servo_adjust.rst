Servo-Einstellung (Wichtig)
============================

Der Drehwinkelbereich des Servos liegt zwischen -90° und 90°. Der im Werk eingestellte Winkel ist jedoch zufällig, vielleicht 0° oder vielleicht 45°. Montiert man ihn direkt mit einem solchen Winkel, führt dies nach Ausführung des Robotercodes zu einem chaotischen Zustand. Im schlimmsten Fall blockiert der Servo und brennt durch.

Daher müssen wir alle Servo-Winkel auf 0° einstellen und dann installieren. So ist der Servo-Winkel zentral, egal in welche Richtung er dreht.

#. Um sicherzustellen, dass der Servo korrekt auf 0° eingestellt ist, zuerst den Servoarm in die Servoachse einsetzen und dann den Hebelarm sanft in einen anderen Winkel drehen. Dieser Servoarm dient lediglich dazu, deutlich zu machen, dass der Servo sich dreht.

    .. image:: img/servo_arm.png

#. Führen Sie nun ``servo_zeroing.py`` im Ordner ``example/`` aus.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/picar-x/example
        sudo python3 servo_zeroing.py

#. Anschließend das Servokabel wie abgebildet in den P11-Port stecken. Gleichzeitig wird der Servoarm zu einer Position drehen (dies ist die 0°-Position, die sich an einer zufälligen Stelle befindet und möglicherweise nicht senkrecht oder parallel ist).

    .. image:: img/Z_P11.JPG

#. Jetzt den Servoarm entfernen, sicherstellen, dass das Servokabel verbunden bleibt und die Stromversorgung nicht abschalten. Danach die Montage gemäß der schriftlichen Anleitung fortsetzen.

.. note::

    * Das Servokabel nicht vor dem Befestigen mit der Servoschraube abziehen. Nach dem Befestigen kann es abgezogen werden.
    * Den Servo nicht drehen, solange er eingeschaltet ist, um Beschädigungen zu vermeiden. Wenn die Servoachse nicht im richtigen Winkel eingesetzt ist, den Servo herausziehen und erneut einsetzen.
    * Vor der Montage jedes Servos muss das Servokabel in P11 eingesteckt und die Stromversorgung eingeschaltet werden, um seinen Winkel auf 0° einzustellen.
