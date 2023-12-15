6. Klippenerkennung 
===========================

Geben wir PiCar-X ein wenig Selbstschutz-Bewusstsein und lassen es lernen, sein eigenes Graustufenmodul zu nutzen, um nicht über die Klippe zu stürzen.

In diesem Beispiel wird das Auto im Ruhezustand sein. 
Wenn Sie es an eine Klippe schieben, wird es dringend geweckt, fährt dann zurück und sagt „Gefahr“.

**Code ausführen**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 6.cliff_detection.py
    

**Code**

.. note::
    Sie können den untenstehenden Code **modifizieren/zurücksetzen/kopieren/ausführen/stoppen**. Bevor Sie das tun, müssen Sie jedoch zum Quellcodepfad wie ``picar-x/example`` gehen. Nachdem Sie den Code modifiziert haben, können Sie ihn direkt ausführen, um den Effekt zu sehen.

.. raw:: html

    <run></run>

.. code-block:: python

    from picarx import Picarx
    from time import sleep
    from robot_hat import TTS

    tts = TTS()
    tts.lang("en-US")

    px = Picarx()
    # px = Picarx(grayscale_pins=['A0', 'A1', 'A2'])
    # manual modify reference value
    px.set_cliff_reference([200, 200, 200])

    current_state = None
    px_power = 10
    offset = 20
    last_state = "safe"

    if __name__=='__main__':
        try:
            while True:
                gm_val_list = px.get_grayscale_data()
                gm_state = px.get_cliff_status(gm_val_list)
                # print("cliff status is:  %s"%gm_state)

                if gm_state is False:
                    state = "safe"
                    px.stop()
                else:
                    state = "danger"   
                    px.backward(80)
                    if last_state == "safe":
                        tts.say("danger")
                        sleep(0.1)
                last_state = state

        finally:
            px.stop()
            print("stop and exit")
            sleep(0.1)

**Wie funktioniert des?** 

Die Funktion zur Erkennung der Klippe sieht so aus:

* ``get_grayscale_data()``: Diese Methode gibt direkt die Messwerte der drei Sensoren von rechts nach links aus. Je heller die Fläche, desto größer der erhaltene Wert.

* ``get_cliff_status(gm_val_list)``: Diese Methode vergleicht die Messwerte der drei Sensoren und gibt ein Ergebnis aus. Wenn das Ergebnis wahr ist, wird erkannt, dass sich eine Klippe vor dem Auto befindet.

