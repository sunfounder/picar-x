Über das Robot HAT
========================

.. image:: img/robot_hat_no_bluetooth.png

**Linker/Rechter Motor-Port**
    * 2-Kanal XH2.54 Motor-Ports.
    * Der linke Port ist mit GPIO 4 verbunden und der rechte Port ist mit GPIO 5 verbunden.

**I2C-Pin**
    * 2-Kanal I2C-Pins vom Raspberry Pi.

**PWM-Pin**
    * 12-Kanal PWM-Pins, P0-P12.

**ADC-Pin**
    * 4-Kanal ADC-Pins, A0-A3.

**Digitaler Pin**
    * 4-Kanal digitaler Pins, D0-D3.

**Batterieanzeige**
    * Zwei LEDs leuchten auf, wenn die Spannung höher als 7,8V ist.
    * Eine LED leuchtet im Bereich von 6,7V bis 7,8V.
    * Unterhalb von 6,7V werden beide LEDs ausgeschaltet.

**USR-LED**
    * Von Ihrem Programm festgelegt. (Eine Ausgabe von 1 schaltet die LED ein; eine Ausgabe von 0 schaltet sie aus.)

**RST-Taste**
    * Kurzes Drücken der RST-Taste führt zum Zurücksetzen des Programms.
    * Lange drücken Sie die RST-Taste, bis die LED aufleuchtet, dann lassen Sie los, und Sie trennen die Bluetooth-Verbindung.

**USR-Taste**
    * Die Funktionen der USR-Taste können von Ihrem Programm festgelegt werden. (Drücken erzeugt eine Eingabe "0"; Loslassen erzeugt eine Eingabe "1".)

**Ein-/Ausschalter**
    * Ein- und Ausschalten der Stromversorgung des Robot HAT.
    * Wenn Sie die Stromversorgung an den Stromanschluss anschließen, startet der Raspberry Pi. Sie müssen jedoch den Ein-/Ausschalter auf EIN schalten, um den Robot HAT zu aktivieren.

**Stromanschluss**
    * 7-12V PH2.0 2-poliger Stromeingang.
    * Versorgt gleichzeitig den Raspberry Pi und den Robot HAT mit Strom.

.. note::
    Weitere Details finden Sie in der `Robot HAT-Dokumentation <https://robot-hat.readthedocs.io/en/latest/index.html>`_.