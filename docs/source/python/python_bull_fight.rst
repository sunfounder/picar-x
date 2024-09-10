.. note::

    Ciao, benvenuto nella community di appassionati di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato ai nuovi annunci di prodotto e anteprime esclusive.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa a promozioni e omaggi durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _py_bull_fight:

10. Lotta col toro
=============================


Trasforma PiCar-X in un toro arrabbiato! Usa la sua fotocamera per seguire e caricare un panno rosso!

**Esegui il Codice**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 10.bull_fight.py


**Visualizza l'immagine**

Dopo aver eseguito il codice, il terminale mostrerà il seguente messaggio:

.. code-block::

    No desktop !
    * Serving Flask app "vilib.vilib" (lazy loading)
    * Environment: production
    WARNING: Do not use the development server in a production environment.
    Use a production WSGI server instead.
    * Debug mode: off
    * Running on http://0.0.0.0:9000/ (Press CTRL+C to quit)

Ora puoi inserire ``http://<your IP>:9000/mjpg`` nel browser per visualizzare il video in diretta. Per esempio:  ``https://192.168.18.113:9000/mjpg``

.. image:: img/display.png

**Codice**

.. note::
    Puoi **Modificare/Reimpostare/Copiare/Eseguire/Interrompere** il codice qui sotto. Prima di farlo, devi andare nel percorso del codice sorgente come ``picar-x\examples``. Dopo aver modificato il codice, puoi eseguirlo direttamente per vedere l'effetto.

.. raw:: html

    <run></run>


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
        Vilib.color_detect("red")
        speed = 50
        dir_angle=0
        x_angle =0
        y_angle =0
        while True:
            if Vilib.detect_obj_parameter['color_n']!=0:
                coordinate_x = Vilib.detect_obj_parameter['color_x']
                coordinate_y = Vilib.detect_obj_parameter['color_y']
                
                # change the pan-tilt angle for track the object
                x_angle +=(coordinate_x*10/640)-5
                x_angle = clamp_number(x_angle,-35,35)
                px.set_cam_pan_angle(x_angle)

                y_angle -=(coordinate_y*10/480)-5
                y_angle = clamp_number(y_angle,-35,35)
                px.set_cam_tilt_angle(y_angle)

                # move
                # The movement direction will change slower than the pan/tilt direction 
                # change to avoid confusion when the picture changes at high speed.
                if dir_angle > x_angle:
                    dir_angle -= 1
                elif dir_angle < x_angle:
                    dir_angle += 1
                px.set_dir_servo_angle(x_angle)
                px.forward(speed)
                sleep(0.05)

            else :
                px.forward(0)
                sleep(0.05)


    if __name__ == "__main__":
        try:
        main()
        
        finally:
            px.stop()
            print("stop and exit")
            sleep(0.1)


**Come funziona?**

Presta attenzione a queste tre parti dell'esempio:

1. Definizione della funzione principale:

    * Avvia la fotocamera con ``Vilib.camera_start()``.
    * Visualizza il feed della fotocamera con ``Vilib.display()``.
    * Attiva il rilevamento del colore e specifica "rosso" come colore target con ``Vilib.color_detect("red")``.
    * Inizializza le variabili: ``speed`` per la velocità del movimento della macchina, ``dir_angle`` per l'angolo di direzione del movimento della macchina, ``x_angle`` per l'angolo di rotazione della fotocamera, e ``y_angle`` per l'inclinazione della fotocamera.

2. Entra in un ciclo continuo (while True) per seguire l'oggetto di colore rosso:

    * Verifica se viene rilevato un oggetto di colore rosso (``Vilib.detect_obj_parameter['color_n'] != 0``).
    * Se viene rilevato un oggetto di colore rosso, ottieni le sue coordinate (``coordinate_x`` e ``coordinate_y``).
    * Calcola nuovi angoli di pan e tilt (``x_angle`` e ``y_angle``) in base alla posizione dell'oggetto rilevato e regolali per seguirlo.
    * Limita gli angoli di pan e tilt entro un intervallo specifico utilizzando la funzione ``clamp_number``.
    * Imposta gli angoli di pan e tilt della fotocamera utilizzando ``px.set_cam_pan_angle()`` e ``px.set_cam_tilt_angle()`` per mantenere l'oggetto nell'inquadratura.

3. Controlla il movimento della macchina in base alla differenza tra ``dir_angle`` e ``x_angle``:

    * Se ``dir_angle`` è maggiore di ``x_angle``, decrementa ``dir_angle`` di 1 per cambiare gradualmente l'angolo di direzione.
    * Se ``dir_angle`` è minore di ``x_angle``, incrementa ``dir_angle`` di 1.
    * Imposta l'angolo del servo di direzione con ``px.set_dir_servo_angle()`` per sterzare le ruote della macchina di conseguenza.
    * Fai avanzare la macchina alla velocità specificata con ``px.forward(speed)``.
