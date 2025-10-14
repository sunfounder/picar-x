.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _py_cliff:

5. Klippenerkennung 
===========================

Geben wir PiCar-X ein wenig Selbstschutz-Bewusstsein und lassen es lernen, sein eigenes Graustufenmodul zu nutzen, um nicht über die Klippe zu stürzen.

In diesem Beispiel wird das Auto im Ruhezustand sein. 
Wenn Sie es an eine Klippe schieben, wird es dringend geweckt, fährt dann zurück und sagt „Gefahr“.

**Code ausführen**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 5.cliff_detection.py
    
    

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
    # manual modify reference value
    px.set_cliff_reference([200, 200, 200])

    last_state = "safe"

    if __name__ == '__main__':
        try:
            while True:
                gm_val_list = px.get_grayscale_data()
                gm_state = px.get_cliff_status(gm_val_list)
                # print("cliff status is: %s" % gm_state)

                if gm_state is False:
                    state = "safe"
                    px.stop()
                else:
                    state = "danger"
                    px.backward(80)
                    if last_state == "safe":
                        sleep(0.1)

                last_state = state

        except KeyboardInterrupt:
            print("\nKeyboardInterrupt: stop and exit")

        finally:
            px.stop()
            sleep(0.1)



**Wie funktioniert des?** 

Die Funktion zur Erkennung der Klippe sieht so aus:

* ``get_grayscale_data()``: Diese Methode gibt direkt die Messwerte der drei Sensoren von rechts nach links aus. Je heller die Fläche, desto größer der erhaltene Wert.

* ``get_cliff_status(gm_val_list)``: Diese Methode vergleicht die Messwerte der drei Sensoren und gibt ein Ergebnis aus. Wenn das Ergebnis wahr ist, wird erkannt, dass sich eine Klippe vor dem Auto befindet.

