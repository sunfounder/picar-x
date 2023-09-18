Hindernisvermeidung
====================

In diesem Projekt wird PiCar-X Hindernisse vor sich erkennen, während es vorwärts fährt. Bei zu großer Annäherung wird die Fahrtrichtung geändert.

**Den Code ausführen**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 avoiding_obstacles.py

Nach dem Ausführen des Codes wird der PiCar-X vorwärts fahren.

Erkennt das Auto, dass der Abstand zum Hindernis vor ihm weniger als 25 cm beträgt, wird es nach links abbiegen.

Ist nach dem Abbiegen nach links kein Hindernis im Weg oder liegt die Hindernisdistanz bei mehr als 25 cm, wird die Vorwärtsfahrt fortgesetzt.

**Code**

.. note::
    Sie können den untenstehenden Code **ändern/zurücksetzen/kopieren/ausführen/stoppen**. Zuvor müssen Sie jedoch zum Quellcodepfad, etwa ``picar-x/example``, navigieren. Nach der Modifikation können Sie den Code direkt ausführen, um die Auswirkungen zu sehen.

.. raw:: html

    <run></run>

.. code-block:: python

    from picarx import Picarx

    def main():
        try:
            px = Picarx()
            # px = Picarx(ultrasonic_pins=['D2','D3']) # tring, echo
            px.forward(30)
            while True:
                distance = px.ultrasonic.read()
                print("distance: ",distance)
                if distance > 0 and distance < 300:
                    if distance < 25:
                        px.set_dir_servo_angle(-35)
                    else:
                        px.set_dir_servo_angle(0)
        finally:
            px.forward(0)

    if __name__ == "__main__":
        main()

**Wie funktioniert das?**

Das Ultraschallmodul ist ebenfalls im picarx-Modul importiert, und wir können einige seiner integrierten Funktionen zur Distanzerkennung verwenden.

.. code-block:: python

    from picarx import Picarx

Da das Ultraschallmodul ins picarx-Modul importiert ist, können wir direkt ``px.ultrasonic.read()`` verwenden, um die Distanz zu erhalten.

.. code-block:: python

    px = Picarx()
    px.forward(30)
    while True:
        distance = px.ultrasonic.read()

Im folgenden Codesegment wird der vom Ultraschallmodul gemeldete Abstandswert ausgelesen. Wenn dieser unter 25 cm (10 Zoll) liegt, wird das Lenkservo von 0° (geradeaus) auf -35° (nach links abbiegen) eingestellt.

.. code-block:: python

    while True:
        distance = px.ultrasonic.read()
        print("distance: ",distance)
        if distance > 0 and distance < 300:
            if distance < 25:
                px.set_dir_servo_angle(-35)
            else:
                px.set_dir_servo_angle(0)
