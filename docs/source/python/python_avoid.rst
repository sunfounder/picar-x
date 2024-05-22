.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

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
                    px.set_dir_servo_angle(30)
                    px.forward(POWER)
                    time.sleep(0.1)
                else:
                    px.set_dir_servo_angle(-30)
                    px.backward(POWER)
                    time.sleep(0.5)
    
        finally:
            px.forward(0)
    
    
    if __name__ == "__main__":
        main()


**Wie funktioniert des?**

* Import des Picarx-Moduls und Initialisierung von Konstanten:

    Dieser Abschnitt des Codes importiert die Klasse ``Picarx`` aus dem Modul ``picarx``, die für die Steuerung des Picarx-Roboters entscheidend ist. Konstanten wie ``POWER``, ``SafeDistance`` und ``DangerDistance`` werden definiert, die später im Skript verwendet werden, um die Bewegung des Roboters basierend auf Distanzmessungen zu steuern.

    .. code-block:: python

        from picarx import Picarx
        import time

        POWER = 50
        SafeDistance = 40 # > 40 sicher
        DangerDistance = 20 # > 20 && < 40 umdrehen,
        # < 20 rückwärts

* Definition der Hauptfunktion und Auslesen des Ultraschallsensors:

    Die ``main`` Funktion ist der Ort, an dem der Picarx-Roboter gesteuert wird. Eine Instanz von ``Picarx`` wird erstellt, die die Funktionen des Roboters aktiviert. Das Skript tritt in eine endlose Schleife ein, liest ständig die Entfernung vom Ultraschallsensor und verwendet diese Entfernung, um die Bewegung des Roboters zu bestimmen.

    .. code-block:: python
        
        def main():
        try:
            px = Picarx()

            while True:
                distance = round(px.ultrasonic.read(), 2)
                # [Rest der Logik]

* Bewegungslogik basierend auf Distanz:

    Die Bewegung des Roboters wird basierend auf der vom Ultraschallsensor gelesenen ``distance`` gesteuert. Wenn die ``distance`` größer als ``SafeDistance`` ist, bewegt sich der Roboter vorwärts. Wenn die Distanz zwischen ``DangerDistance`` und ``SafeDistance`` liegt, dreht er sich leicht und bewegt sich vorwärts. Wenn die ``distance`` kleiner als ``DangerDistance`` ist, fährt der Roboter rückwärts und dreht sich in die entgegengesetzte Richtung.

    .. code-block:: python

        if distance >= SafeDistance:
            px.set_dir_servo_angle(0)
            px.forward(POWER)
        elif distance >= DangerDistance:
            px.set_dir_servo_angle(30)
            px.forward(POWER)
            time.sleep(0.1)
        else:
            px.set_dir_servo_angle(-30)
            px.backward(POWER)
            time.sleep(0.5)

* Sicherheit und Aufräumen mit dem 'finally' Block:

    Der ``try...finally`` Block stellt die Sicherheit sicher, indem er die Bewegung des Roboters im Falle einer Unterbrechung oder eines Fehlers stoppt. Dies ist ein entscheidender Teil, um unkontrollierbares Verhalten des Roboters zu verhindern.

    .. code-block:: python
        
        try:
        # [Steuerungslogik]
        finally:
            px.forward(0)

* Ausführungseinstiegspunkt:

    Der standardmäßige Python-Einstiegspunkt ``if __name__ == "__main__":`` wird verwendet, um die Hauptfunktion auszuführen, wenn das Skript als eigenständiges Programm ausgeführt wird.

    .. code-block:: python
        
        if __name__ == "__main__":
            main()

Zusammenfassend verwendet das Skript das Picarx-Modul, um einen Roboter zu steuern, wobei ein Ultraschallsensor zur Entfernungsmessung genutzt wird. Die Bewegung des Roboters wird anhand dieser Messungen angepasst und sorgt durch sorgfältige Steuerung und einen Sicherheitsmechanismus im finally-Block für einen sicheren Betrieb.
