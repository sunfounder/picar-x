

PiCar-X in Bewegung setzen
==========================

Dies ist das erste Projekt, in dem wir die grundlegende Bewegung des PiCar-X testen.

**Den Code ausführen**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 move.py

Nach dem Ausführen des Codes wird der PiCar-X vorwärts fahren, eine S-förmige Kurve machen, anhalten und den Kopf schütteln.

**Code**

.. note::
    Sie können den untenstehenden Code **ändern/zurücksetzen/kopieren/ausführen/stoppen**. Bevor Sie dies tun, navigieren Sie zum Quellcodepfad, beispielsweise ``picar-x/example``. Nach der Änderung können Sie den Code direkt ausführen, um die Auswirkungen zu sehen.

.. raw:: html

    <run></run>

.. code-block:: python

    from picarx import Picarx
    import time

    if __name__ == "__main__":
        try:
            px = Picarx()
            px.forward(30)
            time.sleep(0.5)
            for angle in range(0,35):
                px.set_dir_servo_angle(angle)
                time.sleep(0.01)
            for angle in range(35,-35,-1):
                px.set_dir_servo_angle(angle)
                time.sleep(0.01)        
            for angle in range(-35,0):
                px.set_dir_servo_angle(angle)
                time.sleep(0.01)
            px.forward(0)
            time.sleep(1)

            for angle in range(0,35):
                px.set_camera_servo1_angle(angle)
                time.sleep(0.01)
            for angle in range(35,-35,-1):
                px.set_camera_servo1_angle(angle)
                time.sleep(0.01)        
            for angle in range(-35,0):
                px.set_camera_servo1_angle(angle)
                time.sleep(0.01)
            for angle in range(0,35):
                px.set_camera_servo2_angle(angle)
                time.sleep(0.01)
            for angle in range(35,-35,-1):
                px.set_camera_servo2_angle(angle)
                time.sleep(0.01)        
            for angle in range(-35,0):
                px.set_camera_servo2_angle(angle)
                time.sleep(0.01)
                
        finally:
            px.forward(0)

**Wie funktioniert das?**

Die Grundfunktionalitäten von PiCar-X sind im ``picarx`` Modul hinterlegt.
Damit lassen sich Lenkgetriebe und Räder steuern,
und der PiCar-X wird vorwärts fahren, eine S-förmige Kurve machen oder den Kopf schütteln.

Nun sind die Bibliotheken für die grundlegende Funktionalität des PiCar-X importiert. Diese Zeilen werden in allen Beispielen auftauchen, die die Bewegung des PiCar-X betreffen.

.. code-block:: python
    :emphasize-lines: 0

    from picarx import Picarx
    import time

Die nachfolgende Funktion mit der ``for``-Schleife wird dann genutzt, um den PiCar-X vorwärts fahren zu lassen, die Richtung zu ändern und die Neigung/Schwenkung der Kamera zu steuern.

.. code-block:: python

    px.forward(speed)    
    px.set_dir_servo_angle(angle)
    px.set_camera_servo1_angle(angle)
    px.set_camera_servo2_angle(angle)

* ``forward()``: Veranlasst den PiCar-X, mit einer gegebenen ``Geschwindigkeit`` vorwärts zu fahren.
* ``set_dir_servo_angle``: Dreht das Lenkservo auf einen bestimmten ``Winkel``.
* ``set_camera_servo1_angle``: Dreht das Pan-Servo auf einen spezifischen ``Winkel``.
* ``set_camera_servo2_angle``: Dreht das Tilt-Servo auf einen spezifischen ``Winkel``.

.. image:: img/pan_tilt_servo.png
    :width: 400
