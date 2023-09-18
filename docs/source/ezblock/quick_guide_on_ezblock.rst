Schnelle Anleitung zu EzBlock
======================================

Dieser Abschnitt ist zweigeteilt:

* :ref:`ezb_servo_adjust` ermöglicht Ihnen, alle Servos auf 0 Grad auszurichten, um eine ordnungsgemäße und sichere Montage zu gewährleisten (andernfalls könnten die Servos beschädigt werden).
* :ref:`install_ezblock` führt Sie durch den Download von EzBlock Studio, um mit Ihrem Roboter zu spielen.

.. _ezb_servo_adjust:

Servo-Einstellung
--------------------------

Der Winkelbereich des Servos liegt zwischen -90 und 90 Grad. Der in der Fabrik eingestellte Winkel ist jedoch zufällig, möglicherweise 0°, vielleicht 45°. Eine Montage in diesem Zustand könnte zu chaotischem Verhalten nach dem Code-Lauf führen oder schlimmer noch, das Servo blockieren und durchbrennen lassen.

Deshalb sollten alle Servo-Winkel auf 0° eingestellt und dann montiert werden. So steht der Servo-Winkel mittig, egal in welche Richtung er sich dreht.

Es wird empfohlen, die Picar-x nach der Montage über die App zu kalibrieren. Aufgrund möglicher Abweichungen während der Montage oder Einschränkungen des Servos selbst kann der Servo-Winkel abweichen; üblicherweise beträgt der Kalibrierungswinkel -5~5°.

Ist der Abweichungswinkel jedoch zu groß, müssen Sie zurück zu diesem Abschnitt und den Servo-Winkel erneut auf 0° setzen. Anschließend folgen Sie den Anweisungen zur erneuten Montage des Fahrzeugs.

#. Laden Sie zuerst :ref:`ezblock:install_ezblock_os_latest` auf eine Micro-SD-Karte. Nach Abschluss der Installation stecken Sie diese in den Raspberry Pi.

#. Um sicherzustellen, dass der Servo richtig auf 0° eingestellt ist, stecken Sie zuerst den Schalthebel in die Servo-Welle und drehen ihn dann vorsichtig auf einen anderen Winkel.

    .. image:: img/servo_arm.png

#. Befolgen Sie die Anweisungen auf dem Montageblatt, stecken Sie das Batteriekabel ein und schalten Sie den Netzschalter auf ON. Dann schließen Sie ein angeschlossenes USB-C-Kabel an, um den Akku zu aktivieren. Warten Sie 1-2 Minuten; ein Ton signalisiert den erfolgreichen Start des Raspberry Pi.

    .. image:: img/Z_BTR.JPG

#. Schließen Sie als Nächstes das Servokabel wie folgt an den P11-Port an.

    .. image:: img/Z_P11.JPG

#. Jetzt sollten Sie sehen, dass der Servoarm auf eine bestimmte Position (0°) rotiert. Sollte der Servoarm nicht auf 0° zurückkehren, halten Sie die USR-Taste gedrückt und drücken Sie die RST-Taste, um den Robot HAT neu zu starten.

#. Nun können Sie mit der Montage gemäß den Anweisungen auf dem Montageblatt fortfahren.

.. note::

    * Ziehen Sie dieses Servokabel nicht ab, bevor Sie den Servo mit der Servoschraube befestigt haben. Danach können Sie es abziehen.
    * Drehen Sie den Servo nicht, während er eingeschaltet ist, um Schäden zu vermeiden; falls die Servowelle in einem falschen Winkel eingesetzt ist, ziehen Sie den Servo heraus und setzen ihn erneut ein.
    * Bevor Sie jeden Servo montieren, müssen Sie das Servokabel in P11 einstecken und die Stromversorgung einschalten, um seinen Winkel auf 0° einzustellen.
    * Diese Nullstellfunktion wird deaktiviert, wenn Sie später mit der EzBlock APP ein Programm auf den Roboter laden.

.. _install_ezblock:

Installation und Konfiguration von EzBlock Studio
--------------------------------------------------------

Sobald der Roboter montiert ist, sind einige grundlegende Schritte erforderlich.

* :ref:`ezblock:install_ezblock_app_latest`: Laden Sie EzBlock Studio auf Ihr Gerät herunter und installieren Sie es oder nutzen Sie die webbasierte Version.
* :ref:`ezblock:connect_product_ezblock_latest`: Konfigurieren Sie Wi-Fi, Bluetooth und kalibrieren Sie vor der Benutzung.
* :ref:`ezblock:open_run_latest`: Sehen Sie sich das zugehörige Beispiel direkt an oder führen Sie es aus.

.. note::

    Nachdem Sie die Picar-x verbunden haben, gibt es einen Kalibrierungsschritt. Dies ist aufgrund möglicher Abweichungen im Montageprozess oder Einschränkungen der Servos selbst notwendig, die dazu führen könnten, dass einige Servowinkel leicht abweichen. Sie können diese in diesem Schritt kalibrieren.

    Wenn Sie jedoch der Meinung sind, dass die Montage perfekt ist und keine Kalibrierung erforderlich ist, können Sie diesen Schritt auch überspringen.
