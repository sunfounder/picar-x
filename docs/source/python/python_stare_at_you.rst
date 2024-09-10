.. note::

    Ciao, benvenuto nella community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto Esperti**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara & Condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato a nuovi annunci di prodotti e anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a concorsi e promozioni durante le festività.

    👉 Pronto per esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _py_stare:

8. Ti Fissa
==========================================

Questo progetto è basato sul progetto :ref:`py_computer_vision`, 
con l'aggiunta di algoritmi di rilevamento facciale.

Quando ti presenti davanti alla telecamera, essa riconoscerà il tuo volto e regolerà il suo giunto cardanico per mantenere il viso al centro dell'inquadratura.

Puoi visualizzare lo schermo su ``http://<your IP>:9000/mjpg``.

**Esegui il Codice**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 8.stare_at_you.py

Quando il codice viene eseguito, la telecamera del veicolo fisserà sempre il tuo volto.

**Codice**

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
        Vilib.face_detect_switch(True)
        x_angle =0
        y_angle =0
        while True:
            if Vilib.detect_obj_parameter['human_n']!=0:
                coordinate_x = Vilib.detect_obj_parameter['human_x']
                coordinate_y = Vilib.detect_obj_parameter['human_y']
                
                # cambia l'angolo del pan-tilt per seguire l'oggetto
                x_angle +=(coordinate_x*10/640)-5
                x_angle = clamp_number(x_angle,-35,35)
                px.set_cam_pan_angle(x_angle)

                y_angle -=(coordinate_y*10/480)-5
                y_angle = clamp_number(y_angle,-35,35)
                px.set_cam_tilt_angle(y_angle)

                sleep(0.05)

            else :
                pass
                sleep(0.05)

    if __name__ == "__main__":
        try:
        main()
        
        finally:
            px.stop()
            print("stop and exit")
            sleep(0.1)

**Come funziona?**

Queste righe di codice nel ciclo ``while True`` fanno sì che la telecamera segua il volto.

.. code-block:: python

    while True:
        if Vilib.detect_obj_parameter['human_n']!=0:
            coordinate_x = Vilib.detect_obj_parameter['human_x']
            coordinate_y = Vilib.detect_obj_parameter['human_y']
            
            # cambia l'angolo del pan-tilt per seguire l'oggetto
            x_angle +=(coordinate_x*10/640)-5
            x_angle = clamp_number(x_angle,-35,35)
            px.set_cam_pan_angle(x_angle)

            y_angle -=(coordinate_y*10/480)-5
            y_angle = clamp_number(y_angle,-35,35)
            px.set_cam_tilt_angle(y_angle)

1. Verifica se viene rilevato un volto umano

    .. code-block:: python

        Vilib.detect_obj_parameter['human_n'] != 0

2. Se viene rilevato un volto, ottieni le coordinate ( ``coordinate_x`` e ``coordinate_y`` ) del volto rilevato.

3. Calcola nuovi angoli di pan e tilt ( ``x_angle`` e ``y_angle`` ) in base alla posizione del volto e regolali per seguirlo.

4. Limita gli angoli di pan e tilt entro l'intervallo specificato utilizzando la funzione ``clamp_number``.

5. Imposta gli angoli di pan e tilt della telecamera utilizzando ``px.set_cam_pan_angle()`` e ``px.set_cam_tilt_angle()``.
