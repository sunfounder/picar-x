.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _ezb_servo_adjust:

Schnellanleitung für EzBlock
========================================

.. note::

  Wenn Sie einen Raspberry Pi 5 verwenden, wird unsere grafische Programmiersoftware EzBlock nicht unterstützt.


Der Drehwinkelbereich des Servos liegt zwischen -90° und 90°. Jedoch ist der im Werk eingestellte Winkel zufällig, vielleicht 0° oder vielleicht 45°. Wenn wir ihn direkt mit solch einem Winkel montieren, führt dies zu einem chaotischen Zustand, sobald der Roboter den Code ausführt. Schlimmer noch, es kann dazu führen, dass der Servo blockiert und durchbrennt.

Deshalb müssen wir alle Servo-Winkel auf 0° einstellen und dann installieren. So ist der Servo-Winkel immer mittig, egal in welche Richtung er dreht.

#. Zunächst :ref:`ezblock:install_ezblock_os_latest` (EzBlocks eigene Anleitungen) auf eine Micro-SD-Karte installieren. Nach Abschluss der Installation diese in den Raspberry Pi einsetzen.

    .. note::
        Nach Abschluss der Installation kehren Sie bitte zu dieser Seite zurück.

    .. image:: img/insert_sd_card.png
        :width: 500
        :align: center

#. Um sicherzustellen, dass der Servo korrekt auf 0° eingestellt ist, den Servoarm in die Servoachse einstecken und dann den Hebelarm sanft in einen anderen Winkel drehen. Dieser Servoarm dient lediglich dazu, deutlich zu machen, dass sich der Servo dreht.

    .. image:: img/servo_arm.png

#. Den Anweisungen auf dem Montageblatt folgen, das Batteriekabel einstecken und den Ein-/Ausschalter auf ON stellen. Dann ein USB-C-Kabel mit Stromquelle anschließen, um die Batterie zu aktivieren. 1-2 Minuten warten; ein Ton signalisiert das erfolgreiche Hochfahren des Raspberry Pi.

    .. image:: img/Z_BTR.JPG
        :width: 800
        :align: center

#. Nun das Servokabel wie folgt in den P11-Port einstecken.

    .. image:: img/Z_P11.JPG

#. Die **USR**-Taste gedrückt halten und dann die **RST**-Taste drücken, um das Servo-Nullstellungs-Skript im System auszuführen. Wenn der Servoarm sich dreht und eine Position einnimmt (dies ist die 0°-Position, die sich an einer zufälligen Stelle befindet und möglicherweise nicht senkrecht oder parallel ist), zeigt dies an, dass das Programm läuft.

    .. note::

        Dieser Schritt muss nur einmal durchgeführt werden; danach einfach andere Servokabel einstecken, und diese werden automatisch auf Null gestellt.

    .. image:: img/Z_P11_BT.png
        :width: 400
        :align: center

#. Jetzt den Servoarm entfernen, sicherstellen, dass das Servokabel verbunden bleibt und die Stromversorgung nicht abschalten. Dann die Montage gemäß der schriftlichen Montageanleitung fortsetzen.

.. note::

    * Das Servokabel nicht vor dem Festziehen des Servos mit der Servoschraube abziehen. Nach dem Festziehen kann es abgezogen werden.
    * Den Servo nicht drehen, solange er eingeschaltet ist, um Beschädigungen zu vermeiden. Wenn die Servoachse im falschen Winkel eingesetzt ist, den Servo herausziehen und erneut einsetzen.
    * Vor der Montage jedes Servos muss das Servokabel in P11 eingesteckt und die Stromversorgung eingeschaltet werden, um seinen Winkel auf 0° einzustellen.
    * Diese Nullstellungsfunktion wird deaktiviert, wenn Sie später ein Programm mit der EzBlock APP auf den Roboter herunterladen.

