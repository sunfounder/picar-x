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
    # manual modify reference value
    px.set_line_reference([500, 600, 600])

    current_state = None
    px_power = 10
    offset = 20

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

                if gm_state == "stop":
                    px.stop()
                elif gm_state == 'forward':
                    px.set_dir_servo_angle(0)
                    px.forward(px_power) 
                elif gm_state == 'left':
                    px.set_dir_servo_angle(offset)
                    px.forward(px_power) 
                elif gm_state == 'right':
                    px.set_dir_servo_angle(-offset)
                    px.forward(px_power) 
        finally:
            px.stop()
            print("stop and exit")
            sleep(0.1)


                

**Wie funktioniert des?** 

Das Graustufensensormodul ``grayscale_module`` wird ebenfalls im picarx-Modul importiert, und wir können einige dieser Methoden verwenden, um schwarze Linien zu erkennen.

Die Funktion zur Erkennung der schwarzen Linie sieht so aus:

* ``get_grayscale_data()``: Diese Methode gibt direkt die Messwerte der drei Sensoren von rechts nach links aus. Je heller die Fläche, desto größer der erhaltene Wert.

* ``get_line_status(gm_val_list)``: Diese Methode vergleicht die Messwerte der drei Sensoren und gibt ein Array mit drei booleschen Werten aus. Ein Wert von 1 bedeutet, dass Schwarz erkannt wurde, und ein Wert von 0 bedeutet Weiß.

* ``get_status(val_list)``: Diese Funktion generiert eine Aktion basierend auf den von den drei Sensoren erkannten booleschen Werten. Es gibt vier Arten von Aktionen: vorwärts, links, rechts und stoppen.

Die Auslösebedingungen für diese Aktionen sind wie folgt:
Ein Wert wird standardmäßig im Modul als Schwellenwert zur Erkennung von Schwarz oder Weiß zugewiesen.
Wenn die Erkennungswerte der drei Sensoren alle größer als der Schwellenwert sind,
bedeutet das, dass die Sensoren die Farbe Weiß wahrnehmen und keine schwarze Linie erkannt wird,
was dazu führt, dass ``get_status()`` einen Rückgabewert von ``stop`` generiert.

* Wenn der rechte (und erste) Sensor eine schwarze Linie erkennt, wird ``right`` zurückgegeben; 
* Wenn der mittlere Sensor eine schwarze Linie erkennt, wird ``forward`` zurückgegeben; 
* Wenn der linke Sensor eine schwarze Linie erkennt, wird ``left`` zurückgegeben;
* Wenn kein Sensor eine schwarze Linie erkennt, wird ``stop`` zurückgegeben.
