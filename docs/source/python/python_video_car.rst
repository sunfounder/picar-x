.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _video_car:

11. Video-Auto
==========================================

Dieses Programm ermöglicht eine First-Person-Ansicht vom PiCar-X!
Verwenden Sie die WSAD-Tasten der Tastatur, um die Bewegungsrichtung zu steuern, 
sowie O und P, um die Geschwindigkeit anzupassen.

**Code ausführen**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/beispiel
    sudo python3 11.video_auto.py

Sobald der Code läuft, können Sie sehen, was PiCar-X filmt und es steuern, indem Sie die folgenden Tasten drücken.

* O: Geschwindigkeit erhöhen
* P: Geschwindigkeit verringern
* W: vorwärts
* S: rückwärts
* A: links abbiegen
* D: rechts abbiegen
* F: anhalten
* T: Foto aufnehmen
* Strg+C: beenden

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

.. code-block:: python
    
    #!/usr/bin/env python3

    from robot_hat.utils import reset_mcu
    from picarx import Picarx
    from vilib import Vilib
    from time import sleep, time, strftime, localtime
    import readchar

    import os
    user = os.getlogin()
    user_home = os.path.expanduser(f'~{user}')

    reset_mcu()
    sleep(0.2)

    manual = '''
    Press key to call the function(non-case sensitive):

        O: speed up
        P: speed down
        W: forward  
        S: backward
        A: turn left
        D: turn right
        F: stop
        T: take photo

        ctrl + c: Press twice to exit the program
    '''


    px = Picarx()

    def take_photo():
        _time = strftime('%Y-%m-%d-%H-%M-%S',localtime(time()))
        name = 'photo_%s'%_time
        path = f"{user_home}/Pictures/picar-x/"
        Vilib.take_photo(name, path)
        print('\nphoto save as %s%s.jpg'%(path,name))


    def move(operate:str, speed):

        if operate == 'stop':
            px.stop()  
        else:
            if operate == 'forward':
                px.set_dir_servo_angle(0)
                px.forward(speed)
            elif operate == 'backward':
                px.set_dir_servo_angle(0)
                px.backward(speed)
            elif operate == 'turn left':
                px.set_dir_servo_angle(-30)
                px.forward(speed)
            elif operate == 'turn right':
                px.set_dir_servo_angle(30)
                px.forward(speed)
            


    def main():
        speed = 0
        status = 'stop'

        Vilib.camera_start(vflip=False,hflip=False)
        Vilib.display(local=True,web=True)
        sleep(2)  # wait for startup
        print(manual)
        
        while True:
            print("\rstatus: %s , speed: %s    "%(status, speed), end='', flush=True)
            # readkey
            key = readchar.readkey().lower()
            # operation 
            if key in ('wsadfop'):
                # throttle
                if key == 'o':
                    if speed <=90:
                        speed += 10           
                elif key == 'p':
                    if speed >=10:
                        speed -= 10
                    if speed == 0:
                        status = 'stop'
                # direction
                elif key in ('wsad'):
                    if speed == 0:
                        speed = 10
                    if key == 'w':
                        # Speed limit when reversing,avoid instantaneous current too large
                        if status != 'forward' and speed > 60:  
                            speed = 60
                        status = 'forward'
                    elif key == 'a':
                        status = 'turn left'
                    elif key == 's':
                        if status != 'backward' and speed > 60: # Speed limit when reversing
                            speed = 60
                        status = 'backward'
                    elif key == 'd':
                        status = 'turn right' 
                # stop
                elif key == 'f':
                    status = 'stop'
                # move 
                move(status, speed)  
            # take photo
            elif key == 't':
                take_photo()
            # quit
            elif key == readchar.key.CTRL_C:
                print('\nquit ...')
                px.stop()
                Vilib.camera_close()
                break 

            sleep(0.1)


    if __name__ == "__main__":
        try:
            main()
        except Exception as e:    
            print("error:%s"%e)
        finally:
            px.stop()
            Vilib.camera_close()

