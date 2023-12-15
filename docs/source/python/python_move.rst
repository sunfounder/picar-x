.. _py_move:

1. Lassen Sie PiCar-X sich bewegen
======================================

Dies ist das erste Projekt, testen wir die grundlegende Bewegung des Picar-X.

**Code ausführen**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 1.move.py

Nachdem der Code ausgeführt wurde, wird PiCar-X vorwärts fahren, in einer S-Form abbiegen, anhalten und den Kopf schütteln.

**Code**

.. note::
    Sie können den untenstehenden Code **modifizieren/zurücksetzen/kopieren/ausführen/stoppen**. Bevor Sie das tun, müssen Sie jedoch zum Quellcodepfad wie ``picar-x/example`` gehen. Nachdem Sie den Code modifiziert haben, können Sie ihn direkt ausführen, um den Effekt zu sehen.

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

**Wie funktioniert des?**

Die grundlegende Funktionalität von PiCar-X ist im Modul ``picarx`` enthalten,
welches zur Steuerung von Lenkservos und Rädern verwendet werden kann,
und lässt das PiCar-X vorwärtsfahren, in einer S-Form abbiegen oder den Kopf schütteln.

Nun werden die Bibliotheken importiert, die die grundlegende Funktionalität von PiCar-X unterstützen.
Diese Zeilen erscheinen in allen Beispielen, die die Bewegung von PiCar-X involvieren.

.. code-block:: python
    :emphasize-lines: 0

    from picarx import Picarx
    import time

Die folgende Funktion mit der ``for``-Schleife wird dann verwendet, um PiCar-X 
vorwärts zu bewegen, die Richtung zu ändern und die Schwenk-/Neigeplattform der Kamera zu bewegen.

.. code-block:: python

    px.forward(speed)    
    px.set_dir_servo_angle(angle)
    px.set_camera_servo1_angle(angle)
    px.set_camera_servo2_angle(angle)

* ``forward()``: Befiehlt dem PiCar-X, mit einer bestimmten ``speed`` vorwärtszufahren.
* ``set_dir_servo_angle``: Dreht den Lenkservo in einen bestimmten ``angle``.
* ``set_cam_pan_angle``: Dreht den Pan-Servo in einen bestimmten ``angle``.
* ``set_cam_tilt_angle``: Dreht den Neige-Servo in einen bestimmten ``angle``.

.. image:: img/pan_tilt_servo.png
    :width: 400
