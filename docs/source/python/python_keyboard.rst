.. _py_keyboard_control:

2. Tastatursteuerung
================================

In diesem Projekt lernen wir, wie man die Tastatur verwendet, um den PiCar-X aus der Ferne zu steuern.
Sie können den PiCar-X vorwärts, rückwärts, nach links und nach rechts steuern.

**Code ausführen**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 2.keyboard_control.py

Drücken Sie Tasten auf der Tastatur, um PiCar-X zu steuern!

    * w: Vorwärts 
    * a: Links abbiegen 
    * s: Rückwärts 
    * d: Rechts abbiegen
    * i: Kopf hoch
    * k: Kopf runter
    * j: Kopf nach links drehen
    * l: Kopf nach rechts drehen     
    * Strg + c: Beenden

**Code**

.. code-block:: python

    from picarx import Picarx
    from time import sleep
    import readchar

    manual = '''
    Press keys on keyboard to control PiCar-X!
        w: Forward
        a: Turn left
        s: Backward
        d: Turn right
        i: Head up
        k: Head down
        j: Turn head left
        l: Turn head right
        ctrl+c: Quit
    '''

    def show_info():
        print("\033[H\033[J",end='')  # clear terminal windows
        print(manual)


    if __name__ == "__main__":
        try:
            pan_angle = 0
            tilt_angle = 0
            px = Picarx()
            show_info()
            while True:
                key = readchar.readkey()
                key = key.lower()
                if key in('wsadikjl'): 
                    if 'w' == key:
                        px.set_dir_servo_angle(0)
                        px.forward(80)
                    elif 's' == key:
                        px.set_dir_servo_angle(0)
                        px.backward(80)
                    elif 'a' == key:
                        px.set_dir_servo_angle(-35)
                        px.forward(80)
                    elif 'd' == key:
                        px.set_dir_servo_angle(35)
                        px.forward(80)
                    elif 'i' == key:
                        tilt_angle+=5
                        if tilt_angle>35:
                            tilt_angle=35
                    elif 'k' == key:
                        tilt_angle-=5
                        if tilt_angle<-35:
                            tilt_angle=-35
                    elif 'l' == key:
                        pan_angle+=5
                        if pan_angle>35:
                            pan_angle=35
                    elif 'j' == key:
                        pan_angle-=5
                        if pan_angle<-35:
                            pan_angle=-35                 

                    px.set_cam_tilt_angle(tilt_angle)
                    px.set_cam_pan_angle(pan_angle)      
                    show_info()                     
                    sleep(0.5)
                    px.forward(0)
            
                elif key == readchar.key.CTRL_C:
                    print("\n Quit")
                    break

        finally:
            px.set_cam_tilt_angle(0)
            px.set_cam_pan_angle(0)  
            px.set_dir_servo_angle(0)  
            px.stop()
            sleep(.2)


**Wie funktioniert des?**

PiCar-X sollte entsprechende Aktionen basierend auf den gelesenen Tastaturzeichen ausführen. 
Die Funktion ``lower()`` wandelt Großbuchstaben in Kleinbuchstaben um, 
damit der Buchstabe unabhängig von der Groß- oder Kleinschreibung gültig bleibt.

.. code-block:: python

    while True:
        key = readchar.readkey()
        key = key.lower()
        if key in('wsadikjl'): 
            if 'w' == key:
                pass
            elif 's' == key:
                pass
            elif 'a' == key:
                pass
            elif 'd' == key:
                pass
            elif 'i' == key:
                pass
            elif 'k' == key:
                pass
            elif 'l' == key:
                pass
            elif 'j' == key:
                pass             
    
        elif key == readchar.key.CTRL_C:
            print("\n Quit")
            break
