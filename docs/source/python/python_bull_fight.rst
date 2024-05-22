.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _py_bull_fight:

10. Stierkampf
=============================

Mache PiCar-X zu einem wütenden Stier! Verwende seine Kamera, um das rote Tuch zu verfolgen und darauf zuzurasen!

**Code ausführen**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 10.bull_fight.py

**Das Bild ansehen**

Nachdem der Code ausgeführt wurde, zeigt das Terminal folgende Aufforderung an:

.. code-block::

    No desktop !
    * Serving Flask app "vilib.vilib" (lazy loading)
    * Environment: production
    WARNING: Do not use the development server in a production environment.
    Use a production WSGI server instead.
    * Debug mode: off
    * Running on http://0.0.0.0:9000/ (Press CTRL+C to quit)

Anschließend können Sie ``http://<Ihre IP>:9000/mjpg`` im Browser eingeben, um das Videosignal zu sehen, z.B.: ``https://192.168.18.113:9000/mjpg``

.. image:: img/display.png

**Code**

.. note::
    Sie können den untenstehenden Code **modifizieren/zurücksetzen/kopieren/ausführen/stoppen**. Bevor Sie das tun, sollten Sie zum Quellcodepfad wie ``picar-x\beispiele`` gehen. Nachdem Sie den Code modifiziert haben, können Sie ihn direkt ausführen, um die Wirkung zu sehen.



.. raw:: html

    <run></run>

.. code-block:: python

    from picarx import Picarx
    from time import sleep
    from vilib import Vilib

    px = Picarx()

    def clamp_number(num,a,b):
    return max(min(num, max(a, b)), min(a, b))

    def main():
        Vilib.camera_start()
        Vilib.display()
        Vilib.color_detect("red")
        speed = 50
        dir_angle=0
        x_angle =0
        y_angle =0
        while True:
            if Vilib.detect_obj_parameter['color_n']!=0:
                coordinate_x = Vilib.detect_obj_parameter['color_x']
                coordinate_y = Vilib.detect_obj_parameter['color_y']
                
                # change the pan-tilt angle for track the object
                x_angle +=(coordinate_x*10/640)-5
                x_angle = clamp_number(x_angle,-35,35)
                px.set_cam_pan_angle(x_angle)

                y_angle -=(coordinate_y*10/480)-5
                y_angle = clamp_number(y_angle,-35,35)
                px.set_cam_tilt_angle(y_angle)

                # move
                # The movement direction will change slower than the pan/tilt direction 
                # change to avoid confusion when the picture changes at high speed.
                if dir_angle > x_angle:
                    dir_angle -= 1
                elif dir_angle < x_angle:
                    dir_angle += 1
                px.set_dir_servo_angle(x_angle)
                px.forward(speed)
                sleep(0.05)

            else :
                px.forward(0)
                sleep(0.05)


    if __name__ == "__main__":
        try:
        main()
        
        finally:
            px.stop()
            print("stop and exit")
            sleep(0.1)

**Wie funktioniert des?**

Sie sollten auf die folgenden drei Teile dieses Beispiels achten:

1. Die Hauptfunktion definieren:

    * Starten Sie die Kamera mit ``Vilib.camera_start()``.
    * Zeigen Sie das Kamera-Feed mit ``Vilib.display()`` an.
    * Aktivieren Sie die Farberkennung und legen Sie die Zielfarbe als „rot“ fest mit ``Vilib.color_detect("red")``.
    * Initialisieren Sie Variablen: ``speed`` für die Bewegungsgeschwindigkeit des Autos, ``dir_angle`` für den Richtungswinkel der Bewegung des Autos, ``x_angle`` für den Schwenkwinkel der Kamera und ``y_angle`` für den Neigungswinkel der Kamera.

2. Treten Sie in eine kontinuierliche Schleife (while True), um das rotfarbene Objekt zu verfolgen:

    * Überprüfen Sie, ob ein rotfarbenes Objekt erkannt wurde (``Vilib.detect_obj_parameter['color_n'] != 0``).
    * Wenn ein rotfarbenes Objekt erkannt wird, erhalten Sie dessen Koordinaten (``coordinate_x`` und ``coordinate_y``).
    * Berechnen Sie neue Schwenk- und Neigungswinkel (``x_angle`` und ``y_angle``) basierend auf der Position des erkannten Objekts und passen Sie diese an, um das Objekt zu verfolgen.
    * Begrenzen Sie die Schwenk- und Neigungswinkel innerhalb des festgelegten Bereichs mit der Funktion ``clamp_number``.
    * Stellen Sie die Schwenk- und Neigungswinkel der Kamera mit ``px.set_cam_pan_angle()`` und ``px.set_cam_tilt_angle()`` ein, um das Objekt im Blick zu behalten.

3. Steuern Sie die Bewegung des Autos basierend auf dem Unterschied zwischen ``dir_angle`` und ``x_angle``:

    * Wenn ``dir_angle`` größer als ``x_angle`` ist, verringern Sie ``dir_angle`` um 1, um den Richtungswinkel allmählich zu ändern.
    * Wenn ``dir_angle`` kleiner als ``x_angle`` ist, erhöhen Sie ``dir_angle`` um 1.
    * Stellen Sie den Lenkservo-Winkel mit ``px.set_dir_servo_angle()`` ein, um die Räder des Autos entsprechend zu steuern.
    * Bewegen Sie das Auto vorwärts mit der festgelegten Geschwindigkeit mit ``px.forward(speed)``.
