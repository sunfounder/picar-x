Linienverfolgung
=======================

Dieses Projekt verwendet das Graustufen-Modul, um den PiCar-X entlang einer Linie vorwärts fahren zu lassen. Verwenden Sie ein dunkelfarbiges Klebeband, um eine möglichst gerade Linie zu ziehen, die nicht allzu stark gekrümmt ist. Einige Tests könnten erforderlich sein, falls der PiCar-X von der Spur abkommt.

**Code ausführen**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 minecart_plus.py

Nach dem Ausführen des Codes wird der PiCar-X entlang einer Linie vorwärts fahren.

**Code**

.. note::
    Sie können den folgenden Code **modifizieren/zurücksetzen/kopieren/ausführen/stoppen**. Bevor Sie das tun, navigieren Sie jedoch zum Quellcodepfad, beispielsweise ``picar-x/example``. Nachdem Sie den Code geändert haben, können Sie ihn direkt ausführen, um die Ergebnisse zu sehen.

.. raw:: html

    <run></run>

.. code-block:: python

    from picarx import Picarx

    if __name__=='__main__':
        try:
            px = Picarx()
            # px = Picarx(grayscale_pins=['A0', 'A1', 'A2']) 
            px_power = 10
            while True:
                gm_val_list = px.get_grayscale_data()
                print("gm_val_list:",gm_val_list)
                gm_status = px.get_line_status(gm_val_list)
                print("gm_status:",gm_status)

                if gm_status == 'forward':
                    print(1)
                    px.forward(px_power)

                elif gm_status == 'left':
                    px.set_dir_servo_angle(12)
                    px.forward(px_power)

                elif gm_status == 'right':
                    px.set_dir_servo_angle(-12)
                    px.forward(px_power)
                else:
                    px.set_dir_servo_angle(0)
                    px.stop()
        finally:
            px.stop()

**Wie funktioniert es?**

Das Graustufen-Sensormodul ``grayscale_module`` ist ebenfalls im picarx-Modul integriert, und wir können einige dieser Methoden verwenden, um schwarze Linien zu erkennen.

Die Funktion zur Erkennung der schwarzen Linie sieht wie folgt aus:

* ``get_grayscale_data()``: Diese Methode gibt direkt die Messwerte der drei Sensoren von rechts nach links aus. Je heller die Fläche, desto größer der erhaltene Wert.

* ``get_line_status()``: Diese Methode generiert eine Aktion basierend auf den von den drei Sonden erkannten Werten. Es gibt vier Arten von Aktionen: vorwärts, links, rechts und stoppen.

Die Auslösebedingungen für diese Aktionen sind wie folgt:
Ein Wert wird im Modul standardmäßig als Schwellenwert für die Erkennung von Schwarz oder Weiß festgelegt.
Wenn die Detektionswerte der drei Sonden alle größer als der Schwellenwert sind, bedeutet das, dass die Sonden die Farbe Weiß erfassen und keine schwarze Linie erkennen, was dazu führt, dass ``get_line_status()`` einen Rückgabewert von ``stop`` erzeugt.

* Wird von der rechten (und ersten) Sonde eine schwarze Linie erkannt, wird ``right`` zurückgegeben.
* Erkennt die mittlere Sonde eine schwarze Linie, wird ``forward`` zurückgegeben.
* Wird von der linken Sonde eine schwarze Linie erkannt, wird ``left`` zurückgegeben.
