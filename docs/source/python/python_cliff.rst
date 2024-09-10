.. note::

    Ciao, benvenuto nella community di appassionati di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato ai nuovi annunci di prodotto e anteprime esclusive.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa a promozioni e omaggi durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _py_cliff:

6. Rilevamento del Burrone 
=============================

Diamo al PiCar-X un po' di consapevolezza di autoconservazione e insegniamogli a utilizzare il proprio modulo grayscale per evitare di precipitare da un burrone.

In questo esempio, l'auto rimarrà inattiva. 
Se la spingi verso un burrone, si sveglierà immediatamente, arretrerà e dirà "pericolo".

**Esegui il Codice**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 6.cliff_detection.py
    

**Codice**

.. note::
    Puoi **Modificare/Reset/Scopiare/Eseguire/Fermare** il codice qui sotto. Prima di ciò, devi andare al percorso del codice sorgente come ``picar-x/example``. Dopo aver modificato il codice, puoi eseguirlo direttamente per vedere l'effetto.

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
    # modifica manuale del valore di riferimento
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
                # print("lo stato del burrone è:  %s"%gm_state)

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

**Come funziona?** 

La funzione per rilevare il burrone è simile a questa:

* ``get_grayscale_data()``: Questo metodo restituisce direttamente le letture dei tre sensori, da destra a sinistra. Più luminosa è l'area, maggiore sarà il valore ottenuto.

* ``get_cliff_status(gm_val_list)``: Questo metodo confronta le letture delle tre sonde e restituisce un risultato. Se il risultato è vero, viene rilevato che c'è un burrone davanti all'auto.

