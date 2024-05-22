.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _py_stare:

8. Blick auf Dich
==========================================

Dieses Projekt basiert ebenfalls auf dem :ref:`py_computer_vision`-Projekt, 
ergänzt um Algorithmen zur Gesichtserkennung.

Wenn Sie vor der Kamera erscheinen, wird sie Ihr Gesicht erkennen und ihr Gimbal so anpassen, dass Ihr Gesicht im Zentrum des Bildes bleibt.

Sie können den Bildschirm unter ``http://<Ihre IP>:9000/mjpg`` ansehen.

**Code ausführen**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 8.stare_at_you.py

Wenn der Code ausgeführt wird, wird die Kamera des Autos immer auf Ihr Gesicht starren.

**Code**

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
        Vilib.face_detect_switch(True)
        x_angle =0
        y_angle =0
        while True:
            if Vilib.detect_obj_parameter['human_n']!=0:
                coordinate_x = Vilib.detect_obj_parameter['human_x']
                coordinate_y = Vilib.detect_obj_parameter['human_y']
                
                # change the pan-tilt angle for track the object
                x_angle +=(coordinate_x*10/640)-5
                x_angle = clamp_number(x_angle,-35,35)
                px.set_cam_pan_angle(x_angle)

                y_angle -=(coordinate_y*10/480)-5
                y_angle = clamp_number(y_angle,-35,35)
                px.set_cam_tilt_angle(y_angle)

                sleep(0.05)

            else :
                pass
                sleep(0.05)

    if __name__ == "__main__":
        try:
        main()
        
        finally:
            px.stop()
            print("stop and exit")
            sleep(0.1)

**Wie funktioniert des?**

Diese Codezeilen in ``while True`` lassen die Kamera dem Gesicht folgen.

.. code-block:: python

    while True:
        if Vilib.detect_obj_parameter['human_n'] != 0:
            coordinate_x = Vilib.detect_obj_parameter['human_x']
            coordinate_y = Vilib.detect_obj_parameter['human_y']
            
            # Ändere den Schwenk-Neige-Winkel, um dem Objekt zu folgen
            x_angle += (coordinate_x*10/640) - 5
            x_angle = clamp_number(x_angle, -35, 35)
            px.set_cam_pan_angle(x_angle)

            y_angle -= (coordinate_y*10/480) - 5
            y_angle = clamp_number(y_angle, -35, 35)
            px.set_cam_tilt_angle(y_angle)

1. Überprüfe, ob ein menschliches Gesicht erkannt wurde

    .. code-block:: python

        Vilib.detect_obj_parameter['human_n'] != 0

2. Wenn ein menschliches Gesicht erkannt wird, erhalte die Koordinaten ( ``coordinate_x`` und ``coordinate_y`` ) des erkannten Gesichts.

3. Berechne neue Schwenk- und Neigewinkel ( ``x_angle`` und ``y_angle`` ) basierend auf der Position des erkannten Gesichts und passe sie an, um dem Gesicht zu folgen.

4. Begrenze die Schwenk- und Neigewinkel innerhalb des angegebenen Bereichs mithilfe der ``clamp_number``-Funktion.

5. Stelle die Schwenk- und Neigewinkel der Kamera mit ``px.set_cam_pan_angle()`` und ``px.set_cam_tilt_angle()`` ein.
