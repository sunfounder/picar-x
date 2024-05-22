.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _py_treasure:

12. Schatzsuche
============================

Richten Sie ein Labyrinth in Ihrem Zimmer ein und platzieren Sie sechs verschiedenfarbige Karten in sechs Ecken. Steuern Sie dann PiCar-X, um diese Farbkarten nacheinander zu suchen!

.. note:: Sie können die :download:`PDF-Farbkarten <https://github.com/sunfounder/sf-pdf/raw/master/prop_card/object_detection/color-cards.pdf>` für die Farberkennung herunterladen und ausdrucken.

**Code ausführen**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/beispiel
    sudo python3 12.schatzsuche.py

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

Anschließend können Sie ``http://<Ihre IP>:9000/mjpg`` im Browser eingeben, um das Videosignal zu sehen, z.B.: ``http://192.168.18.113:9000/mjpg``

.. image:: img/display.png

**Code**

.. code-block:: python

    from picarx import Picarx
    from time import sleep
    from robot_hat import Music,TTS
    from vilib import Vilib
    import readchar
    import random
    import threading
    
    px = Picarx()
    
    music = Music()
    tts = TTS()
    
    manual = '''
    Press keys on keyboard to control Picar-X!
        w: Forward
        a: Turn left
        s: Backward
        d: Turn right
        space: Say the target again
        ctrl+c: Quit
    '''
    
    color = "red"
    color_list=["red","orange","yellow","green","blue","purple"]
    
    def renew_color_detect():
        global color
        color = random.choice(color_list)
        Vilib.color_detect(color)
        tts.say("Look for " + color)
    
    key = None
    lock = threading.Lock()
    def key_scan_thread():
        global key
        while True:
            key_temp = readchar.readkey()
            print('\r',end='')
            with lock:
                key = key_temp.lower()
                if key == readchar.key.SPACE:
                    key = 'space'
                elif key == readchar.key.CTRL_C:
                    key = 'quit'
                    break
            sleep(0.01)
    
    def car_move(key):
        if 'w' == key:
            px.set_dir_servo_angle(0)
            px.forward(80)
        elif 's' == key:
            px.set_dir_servo_angle(0)
            px.backward(80)
        elif 'a' == key:
            px.set_dir_servo_angle(-30)
            px.forward(80)
        elif 'd' == key:
            px.set_dir_servo_angle(30)
            px.forward(80)
    
    
    def main():
        global key
        Vilib.camera_start(vflip=False,hflip=False)
        Vilib.display(local=False,web=True)
        sleep(0.8)
        print(manual)
    
        sleep(1)
        _key_t = threading.Thread(target=key_scan_thread)
        _key_t.setDaemon(True)
        _key_t.start()
    
        tts.say("game start")
        sleep(0.05)
        renew_color_detect()
        while True:
    
            if Vilib.detect_obj_parameter['color_n']!=0 and Vilib.detect_obj_parameter['color_w']>100:
                tts.say("will done")
                sleep(0.05)
                renew_color_detect()
    
            with lock:
                if key != None and key in ('wsad'):
                    car_move(key)
                    sleep(0.5)
                    px.stop()
                    key =  None
                elif key == 'space':
                    tts.say("Look for " + color)
                    key =  None
                elif key == 'quit':
                    _key_t.join()
                    print("\n\rQuit")
                    break
    
            sleep(0.05)
    
    if __name__ == "__main__":
        try:
            main()
        except KeyboardInterrupt:
            pass
        except Exception as e:
            print(f"ERROR: {e}")
        finally:
            Vilib.camera_close()
            px.stop()
            sleep(.2)

**Wie funktioniert des?**

Um die grundlegende Logik dieses Codes zu verstehen, sollten Sie sich auf die folgenden Schlüsselteile konzentrieren:

1. **Initialisierung und Importe:**
   Importanweisungen am Anfang des Codes, um die verwendeten Bibliotheken zu verstehen.

2. **Globale Variablen:**
   Definitionen von globalen Variablen, wie ``color`` und ``key``, die im gesamten Code verwendet werden, um die Ziel-Farbe zu verfolgen und Tastatureingaben zu erfassen.

3. ``renew_color_detect()`` :
   Diese Funktion wählt eine zufällige Farbe aus einer Liste aus und setzt sie als Ziel-Farbe für die Erkennung. Sie verwendet auch Text-to-Speech, um die ausgewählte Farbe anzusagen.

4. ``key_scan_thread()`` :
   Diese Funktion läuft in einem separaten Thread und scannt kontinuierlich nach Tastatureingaben, wobei sie die Variable ``key`` mit der gedrückten Taste aktualisiert. Sie verwendet ein Lock für threadsicheren Zugriff.

5. ``car_move(key)`` :
   Diese Funktion steuert die Bewegung des PiCar-X basierend auf der Tastatureingabe (``key``). Sie legt die Richtung und Geschwindigkeit der Bewegung des Roboters fest.

6. ``main()`` :Die Hauptfunktion, die die gesamte Logik des Codes koordiniert. Sie macht Folgendes:

    * Initialisiert die Kamera und startet die Anzeige des Kamerabilds.
    * Erstellt einen separaten Thread, um Tastatureingaben zu scannen.
    * Kündigt den Spielstart mit Text-to-Speech an.
    * Tritt in eine kontinuierliche Schleife ein, um:

        * Nach erkannten farbigen Objekten zu suchen und Aktionen auszulösen, wenn ein gültiges Objekt erkannt wird.
        * Tastatureingaben zu verarbeiten, um den Roboter zu steuern und mit dem Spiel zu interagieren.
    * Behandelt das Beenden des Spiels und Ausnahmen wie KeyboardInterrupt.
    * Stellt sicher, dass die Kamera geschlossen und der PiCar-X beim Beenden angehalten wird.

Indem Sie diese Schlüsselteile des Codes verstehen, 
können Sie die grundlegende Logik erfassen, wie der PiCar-X-Roboter auf Tastatureingaben reagiert und 
Objekte einer bestimmten Farbe mit der Kamera und den Audioausgabefähigkeiten erkennt und interagiert.
