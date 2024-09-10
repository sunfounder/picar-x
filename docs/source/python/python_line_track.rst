.. note::

    Ciao, benvenuto nella SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto Esperti**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara & Condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato a nuovi annunci di prodotti e anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a promozioni festive e concorsi.

    👉 Pronto per esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _py_line_tracking:

5. Tracciamento della Linea
====================================

In questo progetto, useremo il modulo Grayscale per far muovere il PiCar-X lungo una linea. 
Utilizza del nastro adesivo scuro per tracciare una linea il più possibile diritta, senza troppe curve. 
Potrebbe essere necessario fare alcuni esperimenti se il PiCar-X si discosta dalla linea.

**Esegui il Codice**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 5.minecart_plus.py
    
Dopo aver eseguito il codice, il PiCar-X si muoverà lungo la linea.

**Codice**

.. note::
    Puoi **Modificare/Resettare/Copiare/Eseguire/Interrompere** il codice qui sotto. Prima di farlo, devi andare nel percorso del codice sorgente come ``picar-x/example``. Dopo aver modificato il codice, puoi eseguirlo direttamente per vedere l'effetto.

.. raw:: html

    <run></run>

.. code-block:: python

    from picarx import Picarx
    from time import sleep

    px = Picarx()
    # px = Picarx(grayscale_pins=['A0', 'A1', 'A2'])

    # Esegui ./calibration/grayscale_calibration.py per calibrare automaticamente i valori grayscale
    # oppure modifica manualmente i valori di riferimento con il seguente codice
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
        _state = px.get_line_status(val_list)  # [bool, bool, bool], 0 significa linea, 1 significa sfondo
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
       

**Come funziona?** 

Questo script Python controlla un robot Picarx utilizzando sensori di scala di grigi per la navigazione. Ecco una suddivisione delle sue componenti principali:

* Importazione e Inizializzazione:

    Lo script importa la classe Picarx per il controllo del robot e la funzione sleep dal modulo time per aggiungere dei ritardi.

    Viene creata un'istanza di Picarx, e c'è una linea commentata che mostra un'inizializzazione alternativa con pin specifici per i sensori di scala di grigi.

    .. code-block:: python
        
        from picarx import Picarx
        from time import sleep

        px = Picarx()

* Configurazione e Variabili Globali:

    ``current_state``, ``px_power``, ``offset`` e ``last_state`` sono variabili globali utilizzate per tracciare e controllare i movimenti del robot. ``px_power`` imposta la potenza del motore, e ``offset`` viene utilizzato per regolare l'angolo di sterzata.

    .. code-block:: python

        current_state = None
        px_power = 10
        offset = 20
        last_state = "stop"

* Funzione ``outHandle``:

    Questa funzione viene chiamata quando il robot deve gestire uno scenario "fuori linea".

    Regola la direzione del robot in base a ``last_state`` e controlla i valori del sensore di scala di grigi per determinare il nuovo stato.

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

* Funzione ``get_status``:

    Interpreta i dati del sensore di scala di grigi (``val_list``) per determinare lo stato di navigazione del robot.

    Lo stato del robot può essere 'forward', 'left', 'right' o 'stop', a seconda di quale sensore rileva la linea.

    .. code-block:: python
        
        def get_status(val_list):
            _state = px.get_line_status(val_list)  # [bool, bool, bool], 0 significa linea, 1 significa sfondo
            if _state == [0, 0, 0]:
                return 'stop'
            elif _state[1] == 1:
                return 'forward'
            elif _state[0] == 1:
                return 'right'
            elif _state[2] == 1:
                return 'left'

* Ciclo Principale:

    Il ciclo ``while True`` controlla continuamente i dati del sensore di scala di grigi e regola di conseguenza i movimenti del robot.

    A seconda dello ``gm_state``, imposta l'angolo di sterzata e la direzione del movimento.

    .. code-block:: python

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

* Sicurezza e Chiusura:

    Il blocco ``try...finally`` garantisce che il robot si fermi quando lo script viene interrotto o completato.

    .. code-block:: python
        
        finally:
        px.stop()
        print("stop and exit")
        sleep(0.1)

In sintesi, lo script utilizza i sensori di scala di grigi per navigare il robot Picarx. Legge continuamente i dati del sensore per determinare la direzione e regola il movimento e la sterzata del robot di conseguenza. La funzione ``outHandle`` fornisce logica aggiuntiva per situazioni in cui il robot deve correggere significativamente il proprio percorso.
