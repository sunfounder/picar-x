.. _py_avoid:

4. Hindernisvermeidung
=============================

In diesem Projekt wird PiCar-X Hindernisse vor sich erkennen, während es vorwärtsfährt, 
und wenn die Hindernisse zu nah sind, wird es die Fahrtrichtung ändern.

**Code ausführen**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 4.avoiding_obstacles.py
    
Nachdem der Code ausgeführt wurde, fährt PiCar-X vorwärts.

Wenn es erkennt, dass die Entfernung des Hindernisses vor ihm weniger als 20 cm beträgt, wird es rückwärtsfahren.

Wenn ein Hindernis innerhalb von 20 bis 40 cm ist, wird es nach links abbiegen.

Wenn nach dem Linksabbiegen kein Hindernis in der Richtung ist oder die Hindernisentfernung größer als 25 cm ist, 
wird es weiter vorwärtsfahren.

**Code**

.. note::
    Sie können den untenstehenden Code **modifizieren/zurücksetzen/kopieren/ausführen/stoppen**. Bevor Sie das tun, müssen Sie jedoch zum Quellcodepfad wie ``picar-x/example`` gehen. Nachdem Sie den Code modifiziert haben, können Sie ihn direkt ausführen, um den Effekt zu sehen.

.. raw:: html

    <run></run>

.. code-block:: python

    from picarx import Picarx
    import time

    POWER = 50
    SafeDistance = 40   # > 40 safe
    DangerDistance = 20 # > 20 && < 40 turn around, 
                        # < 20 backward

    def main():
        try:
            px = Picarx()
            # px = Picarx(ultrasonic_pins=['D2','D3']) # tring, echo
        
            while True:
                distance = round(px.ultrasonic.read(), 2)
                print("distance: ",distance)
                if distance >= SafeDistance:
                    px.set_dir_servo_angle(0)
                    px.forward(POWER)
                elif distance >= DangerDistance:
                    px.set_dir_servo_angle(40)
                    px.forward(POWER)
                    time.sleep(0.1)
                else:
                    px.set_dir_servo_angle(-40)
                    px.backward(POWER)
                    time.sleep(0.5)

        finally:
            px.forward(0)


    if __name__ == "__main__":
        main()



**Wie funktioniert des?**

Das Ultraschallmodul wird ebenfalls im picarx-Modul importiert, 
und wir können einige seiner gekapselten Funktionen nutzen, um die Entfernung zu erkennen.

.. code-block:: python

    from picarx import Picarx

Da das Ultraschallmodul in das picarx-Modul importiert wird, 
können wir direkt ``px.ultrasonic.read()`` verwenden, um die Entfernung zu ermitteln.

.. code-block:: python

    px = Picarx()
    px.forward(30)
    while True:
        distance = px.ultrasonic.read() 

Der folgende Codeausschnitt liest den vom Ultraschallmodul gemeldeten Entfernungswert, 
und wenn die Entfernung unter 40 cm liegt, wird der Lenkservo von 0° (geradeaus) auf -40° 
(nach links abbiegen) eingestellt.

.. code-block:: python

    while True:
        distance = px.ultrasonic.read()
        print("distance: ",distance)
        if distance > 0 and distance < 300:
            if distance < 25:
                px.set_dir_servo_angle(-35)
            else:
                px.set_dir_servo_angle(0)
