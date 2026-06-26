.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

Servo einstellen (Wichtig)
==========================

.. note::

    Wenn Ihr Robot HAT die Version V44 oder höher ist (mit dem Lautsprecher oben auf der Platine) und über eine integrierte **Zero**-Taste verfügt, können Sie diesen Schritt überspringen und einfach die **Zero**-Taste drücken, um das Servo-Nullstellungsprogramm zu aktivieren.

    .. image:: img/robot_hat_v44.png
        :width: 500
        :align: center

Der Winkelbereich eines Servos beträgt -90° bis +90°, jedoch ist der werkseitig eingestellte Winkel zufällig – möglicherweise 0°, möglicherweise 45°.
Wenn wir das Servo mit einem solchen zufälligen Winkel direkt montieren, kann dies nach dem Start des Robotercodes zu einem chaotischen Zustand führen oder im schlimmsten Fall dazu, dass das Servo blockiert und durchbrennt.

Daher müssen wir hier zunächst alle Servos auf **0°** einstellen und sie erst danach montieren.
So befindet sich das Servo immer in der Mittelstellung, unabhängig davon, in welche Richtung es sich später drehen soll.

#. Um sicherzustellen, dass das Servo korrekt auf 0° eingestellt ist, stecken Sie zunächst den Servoarm auf die Servowelle und drehen Sie den Hebel vorsichtig in einen anderen Winkel.
   Dieser Servoarm dient lediglich dazu, dass Sie deutlich sehen können, wie sich das Servo bewegt.

    .. image:: img/servo_arm.png

#. Führen Sie nun ``servo_zeroing.py`` im Ordner ``example/`` aus.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/picar-x/example
        sudo python3 servo_zeroing.py

#. Stecken Sie anschließend das Servokabel wie unten gezeigt in den **P11**-Port.
   Gleichzeitig sehen Sie, wie sich der Servoarm in eine Position dreht (dies ist die **0°-Position**, die jedoch zufällig ist und nicht unbedingt senkrecht oder parallel sein muss).


    .. image:: img/Z_P11.JPG

#. Entfernen Sie nun den Servoarm, während das Servokabel weiterhin angeschlossen bleibt, und schalten Sie die Stromversorgung **nicht** aus.
   Setzen Sie anschließend die Montage gemäß der Papier-Anleitung fort.

.. note::

    * Ziehen Sie das Servokabel nicht ab, bevor das Servo mit der Schraube befestigt ist. Nach dem Befestigen können Sie es abziehen.
    * Drehen Sie das Servo nicht, während es unter Spannung steht, um Beschädigungen zu vermeiden. Wenn die Servowelle nicht im richtigen Winkel sitzt, ziehen Sie das Servo heraus und setzen Sie es erneut ein.
    * Vor dem Einbau jedes Servos müssen Sie das Servokabel an **P11** anschließen und die Stromversorgung einschalten, um den Winkel auf **0°** einzustellen.
