.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _py_line_tracking:

5. Linienverfolgung
====================================

Dieses Projekt wird das Graustufenmodul verwenden, um den PiCar-X entlang einer Linie vorwärtsfahren zu lassen. 
Verwenden Sie dunkelfarbiges Klebeband, um eine Linie so gerade wie möglich zu machen und nicht zu sehr gekrümmt. 
Einige Experimente könnten notwendig sein, wenn der PiCar-X entgleist.

**Code ausführen**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 5.minecart_plus.py
    
Nachdem der Code ausgeführt wurde, wird PiCar-X entlang einer Linie vorwärtsfahren.

**Code**

.. note::
    Sie können den untenstehenden Code **modifizieren/zurücksetzen/kopieren/ausführen/stoppen**. Bevor Sie das tun, müssen Sie jedoch zum Quellcodepfad wie ``picar-x/example`` gehen. Nachdem Sie den Code modifiziert haben, können Sie ihn direkt ausführen, um den Effekt zu sehen.

.. raw:: html

    <run></run>

.. code-block:: python

    from picarx import Picarx
    from time import sleep

    px = Picarx()
    # px = Picarx(grayscale_pins=['A0', 'A1', 'A2'])

    # Please run ./calibration/grayscale_calibration.py to Auto calibrate grayscale values
    # or manual modify reference value by follow code
    # px.set_line_reference([1400, 1400, 1400])

    current_state = None
    px_power = 10
    offset = 20
    last_state = "stop"

    def outHandle():
        global last_state, current_state
        if last_state == 'left':
            px.set_dir_servo_angle(-30)
            px.backward(10)
        elif last_state == 'right':
            px.set_dir_servo_angle(30)
            px.backward(10)
        while True:
            gm_val_list = px.get_grayscale_data()
            gm_state = get_status(gm_val_list)
            print("outHandle gm_val_list: %s, %s"%(gm_val_list, gm_state))
            currentSta = gm_state
            if currentSta != last_state:
                break
        sleep(0.001)

    def get_status(val_list):
        _state = px.get_line_status(val_list)  # [bool, bool, bool], 0 means line, 1 means background
        if _state == [0, 0, 0]:
            return 'stop'
        elif _state[1] == 1:
            return 'forward'
        elif _state[0] == 1:
            return 'right'
        elif _state[2] == 1:
            return 'left'

    if __name__=='__main__':
        try:
            while True:
                gm_val_list = px.get_grayscale_data()
                gm_state = get_status(gm_val_list)
                print("gm_val_list: %s, %s"%(gm_val_list, gm_state))

                if gm_state != "stop":
                    last_state = gm_state

                if gm_state == 'forward':
                    px.set_dir_servo_angle(0)
                    px.forward(px_power) 
                elif gm_state == 'left':
                    px.set_dir_servo_angle(offset)
                    px.forward(px_power) 
                elif gm_state == 'right':
                    px.set_dir_servo_angle(-offset)
                    px.forward(px_power) 
                else:
                    outHandle()
        finally:
            px.stop()
            print("stop and exit")
            sleep(0.1)


                

**Wie funktioniert des?** 

Dieses Python-Skript steuert ein Picarx-Roboterauto mithilfe von Graustufensensoren zur Navigation. Hier ist eine Zusammenfassung seiner Hauptkomponenten:

* Import und Initialisierung:

    Das Skript importiert die Picarx-Klasse zur Steuerung des Roboterwagens und die Sleep-Funktion aus dem Time-Modul, um Verzögerungen hinzuzufügen.

    Eine Instanz von Picarx wird erstellt, und es gibt eine auskommentierte Zeile, die eine alternative Initialisierung mit spezifischen Graustufensensor-Pins zeigt.

    .. code-block:: python
        
        from picarx import Picarx
        from time import sleep

        px = Picarx()

* Konfiguration und Globale Variablen:

    ``current_state``, ``px_power``, ``offset`` und ``last_state`` sind globale Variablen, die verwendet werden, um die Bewegung des Autos zu verfolgen und zu steuern. ``px_power`` setzt die Motorleistung, und ``offset`` wird zur Einstellung des Lenkwinkels verwendet.

    .. code-block:: python

        current_state = None
        px_power = 10
        offset = 20
        last_state = "stop"

* ``outHandle`` Funktion:

    Diese Funktion wird aufgerufen, wenn das Auto ein 'Aus-der-Linie'-Szenario behandeln muss.

    Sie passt die Fahrtrichtung basierend auf ``last_state`` an und überprüft die Graustufensensorwerte, um den neuen Zustand zu bestimmen.

    .. code-block:: python

        def outHandle():
            global last_state, current_state
            if last_state == 'left':
                px.set_dir_servo_angle(-30)
                px.backward(10)
            elif last_state == 'right':
                px.set_dir_servo_angle(30)
                px.backward(10)
            while True:
                gm_val_list = px.get_grayscale_data()
                gm_state = get_status(gm_val_list)
                print("outHandle gm_val_list: %s, %s"%(gm_val_list, gm_state))
                currentSta = gm_state
                if currentSta != last_state:
                    break
            sleep(0.001)

* ``get_status`` Funktion:

    Sie interpretiert die Graustufensensordaten (``val_list``), um den Navigationszustand des Autos zu bestimmen.

    Der Zustand des Autos kann ``vorwärts``, ``links``, ``rechts`` oder ``stop`` sein, je nachdem, welcher Sensor die Linie erkennt.

    .. code-block:: python
        
        def get_status(val_list):
            _state = px.get_line_status(val_list)  # [bool, bool, bool], 0 bedeutet Linie, 1 bedeutet Hintergrund
            if _state == [0, 0, 0]:
                return 'stop'
            elif _state[1] == 1:
                return 'vorwärts'
            elif _state[0] == 1:
                return 'rechts'
            elif _state[2] == 1:
                return 'links'

* Hauptschleife:

    Die ``while True``-Schleife überprüft kontinuierlich die Graustufendaten und passt die Bewegung des Autos entsprechend an.

    Abhängig vom ``gm_state`` wird der Lenkwinkel und die Bewegungsrichtung eingestellt.

    .. code-block:: python

        if __name__=='__main__':
            try:
                while True:
                    gm_val_list = px.get_grayscale_data()
                    gm_state = get_status(gm_val_list)
                    print("gm_val_list: %s, %s"%(gm_val_list, gm_state))

                    if gm_state != "stop":
                        last_state = gm_state

                    if gm_state == 'vorwärts':
                        px.set_dir_servo_angle(0)
                        px.forward(px_power) 
                    elif gm_state == 'links':
                        px.set_dir_servo_angle(offset)
                        px.forward(px_power) 
                    elif gm_state == 'rechts':
                        px.set_dir_servo_angle(-offset)
                        px.forward(px_power) 
                    else:
                        outHandle()

* Sicherheit und Aufräumen:

    Der ``try...finally``-Block stellt sicher, dass das Auto stoppt, wenn das Skript unterbrochen oder beendet wird.

    .. code-block:: python
        
        finally:
            px.stop()
            print("stop and exit")
            sleep(0.1)

Zusammenfassend verwendet das Skript Graustufensensoren zur Navigation des Picarx-Roboterwagens. Es liest kontinuierlich die Sensordaten, um die Richtung zu bestimmen und passt die Bewegung und Lenkung des Autos entsprechend an. Die outHandle-Funktion bietet zusätzliche Logik für Situationen, in denen das Auto seinen Weg deutlich anpassen muss.
