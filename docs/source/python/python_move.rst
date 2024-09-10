.. note::

    Ciao, benvenuto nella community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto Esperti**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara & Condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato a nuovi annunci di prodotti e anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a concorsi e promozioni durante le festività.

    👉 Pronto per esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _py_move:

1. Muovere PiCar-X
========================

Questo è il primo progetto: testiamo il movimento base del PiCar-X.

**Esegui il Codice**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 1.move.py

Dopo aver eseguito il codice, PiCar-X si muoverà in avanti, girerà in una forma a S, si fermerà e scuoterà la testa.

**Codice**

.. note::
    Puoi **Modificare/Resettare/Copiare/Eseguire/Interrompere** il codice qui sotto. Prima di farlo, devi andare nel percorso del codice sorgente come ``picar-x/example``. Dopo aver modificato il codice, puoi eseguirlo direttamente per vedere l'effetto.

.. raw:: html

    <run></run>

.. code-block:: python

    from picarx import Picarx
    import time


    if __name__ == "__main__":
        try:
            px = Picarx()
            px.forward(30)
            time.sleep(0.5)
            for angle in range(0,35):
                px.set_dir_servo_angle(angle)
                time.sleep(0.01)
            for angle in range(35,-35,-1):
                px.set_dir_servo_angle(angle)
                time.sleep(0.01)        
            for angle in range(-35,0):
                px.set_dir_servo_angle(angle)
                time.sleep(0.01)
            px.forward(0)
            time.sleep(1)

            for angle in range(0,35):
                px.set_camera_servo1_angle(angle)
                time.sleep(0.01)
            for angle in range(35,-35,-1):
                px.set_camera_servo1_angle(angle)
                time.sleep(0.01)        
            for angle in range(-35,0):
                px.set_camera_servo1_angle(angle)
                time.sleep(0.01)
            for angle in range(0,35):
                px.set_camera_servo2_angle(angle)
                time.sleep(0.01)
            for angle in range(35,-35,-1):
                px.set_camera_servo2_angle(angle)
                time.sleep(0.01)        
            for angle in range(-35,0):
                px.set_camera_servo2_angle(angle)
                time.sleep(0.01)
                
        finally:
            px.forward(0)

**Come funziona?**

Le funzionalità di base del PiCar-X sono nel modulo ``picarx``,
che può essere usato per controllare il servocomando dello sterzo e le ruote,
facendo muovere il PiCar-X in avanti, girare a forma di S o scuotere la testa.

Ora, le librerie che supportano le funzionalità di base di PiCar-X vengono importate. 
Queste righe appariranno in tutti gli esempi che riguardano il movimento di PiCar-X.

.. code-block:: python
    :emphasize-lines: 0

    from picarx import Picarx
    import time

La funzione seguente con il ciclo ``for`` viene utilizzata per far muovere PiCar-X 
in avanti, cambiare direzione e muovere la telecamera con il pan/tilt.

.. code-block:: python

    px.forward(speed)    
    px.set_dir_servo_angle(angle)
    px.set_camera_servo1_angle(angle)
    px.set_camera_servo2_angle(angle)

* ``forward()``: Ordina a PiCar-X di avanzare a una determinata ``velocità``.
* ``set_dir_servo_angle``: Ruota il servocomando dello sterzo a un angolo specifico ``angolo``.
* ``set_cam_pan_angle``: Ruota il servocomando del Pan a un angolo specifico ``angolo``.
* ``set_cam_tilt_angle``: Ruota il servocomando del Tilt a un angolo specifico ``angolo``.

.. image:: img/pan_tilt_servo.png
    :width: 400
