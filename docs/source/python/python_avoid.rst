.. note::

    Ciao, benvenuto nella community di appassionati di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato ai nuovi annunci di prodotto e anteprime esclusive.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa a promozioni e omaggi durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _py_avoid:

4. Evitamento Ostacoli
=============================

In questo progetto, PiCar-X rileverà ostacoli davanti a sé mentre si muove 
in avanti, e quando gli ostacoli sono troppo vicini, cambierà direzione.

**Esegui il codice**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 4.avoiding_obstacles.py
    
Dopo aver eseguito il codice, PiCar-X si muoverà in avanti.

Se rileva che la distanza dell'ostacolo davanti è inferiore a 20 cm, si sposterà all'indietro.

Se c'è un ostacolo tra 20 e 40 cm, girerà a sinistra.

Se non ci sono ostacoli nella direzione dopo aver girato a sinistra o la distanza dell'ostacolo è superiore a 25 cm, continuerà a muoversi in avanti.

**Codice**

.. note::
    Puoi **Modificare/Reimpostare/Copiare/Eseguire/Interrompere** il codice seguente. Ma prima devi andare nel percorso del codice sorgente come ``picar-x/example``. Dopo aver modificato il codice, puoi eseguirlo direttamente per vedere l'effetto.

.. raw:: html

    <run></run>

.. code-block:: python

    from picarx import Picarx
    import time
    
    POWER = 50
    SafeDistance = 40   # > 40 sicuro
    DangerDistance = 20 # > 20 && < 40 girare, 
                        # < 20 indietro
    
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

**Come funziona?**

* Importazione del Modulo Picarx e Inizializzazione delle Costanti:

    Questa parte del codice importa la classe ``Picarx`` dal modulo ``picarx``, essenziale per controllare il robot Picarx. Sono definite costanti come ``POWER``, ``SafeDistance`` e ``DangerDistance``, che verranno utilizzate successivamente per controllare il movimento del robot in base alle misurazioni della distanza.

    .. code-block:: python

        from picarx import Picarx
        import time

        POWER = 50
        SafeDistance = 40 # > 40 sicuro
        DangerDistance = 20 # > 20 && < 40 girare,
        # < 20 indietro

* Definizione della Funzione Principale e Lettura del Sensore Ultrasonico:

    La funzione ``main`` è il punto in cui viene controllato il robot Picarx. Viene creata un'istanza di ``Picarx``, che attiva le funzionalità del robot. Il codice entra in un ciclo infinito, leggendo costantemente la distanza dal sensore ultrasonico. Questa distanza viene utilizzata per determinare il movimento del robot.

    .. code-block:: python
        
        def main():
        try:
        px = Picarx()

            while True:
                distance = round(px.ultrasonic.read(), 2)
                # [Resto della logica]

* Logica del Movimento Basata sulla Distanza:

    Il movimento del robot è controllato in base alla ``distanza`` letta dal sensore ultrasonico. Se la ``distanza`` è maggiore di ``SafeDistance``, il robot si muove in avanti. Se la distanza è compresa tra ``DangerDistance`` e ``SafeDistance``, gira leggermente e continua a muoversi in avanti. Se la ``distanza`` è inferiore a ``DangerDistance``, il robot si muove all'indietro girando in direzione opposta.

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

* Sicurezza e Pulizia con il Blocco 'finally':

    Il blocco ``try...finally`` garantisce la sicurezza fermando il movimento del robot in caso di interruzione o errore. Questo è un passaggio cruciale per prevenire comportamenti incontrollabili del robot.

    .. code-block:: python
        
        try:
        # [Logica di controllo]
        finally:
        px.forward(0)

* Punto di Ingresso dell'Esecuzione:

    Il classico punto di ingresso Python ``if __name__ == "__main__":`` viene utilizzato per eseguire la funzione principale quando lo script viene eseguito come programma autonomo.

    .. code-block:: python
        
        if name == "main":
            main()

In sintesi, lo script utilizza il modulo Picarx per controllare un robot, utilizzando un sensore ultrasonico per la misurazione della distanza. Il movimento del robot viene adattato in base a queste misurazioni, garantendo un funzionamento sicuro attraverso un attento controllo e un meccanismo di sicurezza nel blocco finally.

