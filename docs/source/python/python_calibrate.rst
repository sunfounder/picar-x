.. note::

    Ciao, benvenuto nella community di appassionati di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato ai nuovi annunci di prodotto e anteprime esclusive.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa a promozioni e omaggi durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _py_calibrate:

0. Calibrazione del PiCar-X
==================================

Calibrazione Motori e Servo
------------------------------

Alcuni angoli dei servo potrebbero essere leggermente inclinati a causa di possibili deviazioni durante l'installazione del PiCar-X o per limitazioni dei servo stessi, quindi puoi calibrarli.

Naturalmente, puoi saltare questo capitolo se ritieni che il montaggio sia perfetto e non richieda calibrazione.

#. Esegui il file ``calibration.py``.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/picar-x/example/calibration
        sudo python3 calibration.py

#. Dopo aver eseguito il codice, vedrai la seguente interfaccia visualizzata nel terminale.

    .. image:: img/calibrate1.png

#. Il tasto ``R`` viene utilizzato per testare se i 3 servo funzionano correttamente. Dopo aver selezionato un servo con i tasti ``1``, ``2`` o ``3``, premi il tasto ``R`` per testare quel servo.

#. Premi il tasto numero ``1`` per selezionare il servo della ruota anteriore, poi premi il tasto ``W/S`` per fare in modo che la ruota anteriore guardi il più possibile avanti senza inclinarsi a destra o sinistra.

    .. image:: img/calibrate2.png

#. Premi il tasto numero ``2`` per selezionare il **servo Pan**, poi premi il tasto ``W/S`` per fare in modo che la piattaforma pan/tilt guardi dritto senza inclinarsi a destra o sinistra.

    .. image:: img/calibrate3.png

#. Premi il tasto numero ``3`` per selezionare il **servo Tilt**, poi premi il tasto ``W/S`` per fare in modo che la piattaforma pan/tilt guardi dritto senza inclinarsi su e giù.

    .. image:: img/calibrate4.png

#. Poiché i collegamenti dei motori potrebbero essere invertiti durante l'installazione, puoi premere ``E`` per testare se la macchina può muoversi in avanti normalmente. Se così non fosse, usa i tasti numerici ``4`` e ``5`` per selezionare i motori sinistro e destro, poi premi il tasto ``Q`` per calibrare la direzione di rotazione.

    .. image:: img/calibrate6.png

#. Quando la calibrazione è completata, premi la ``Barra Spaziatrice`` per salvare i parametri di calibrazione. Apparirà un messaggio per inserire ``y`` per confermare, quindi premi ``Ctrl+C`` per uscire dal programma e completare la calibrazione.

    .. image:: img/calibrate5.png

Calibrazione del Modulo Grayscale
------------------------------------

A causa delle diverse condizioni ambientali e situazioni di illuminazione, 
i parametri preimpostati per il modulo grayscale potrebbero non essere ottimali. 
Puoi perfezionare queste impostazioni tramite questo programma per ottenere risultati migliori.

#. Stendi una striscia di nastro isolante nero, lunga circa 15 cm, su un pavimento di colore chiaro. Centra il tuo PiCar-X in modo che si posizioni sopra il nastro. In questo assetto, il sensore centrale del modulo grayscale dovrebbe trovarsi direttamente sopra il nastro, mentre i due sensori laterali dovrebbero trovarsi sulla superficie più chiara.

#. Esegui il file ``grayscale_calibration.py``.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/picar-x/example/calibration
        sudo python3 grayscale_calibration.py

#. Dopo aver eseguito il codice, vedrai la seguente interfaccia visualizzata nel terminale.

    .. image:: img/calibrate_g1.png

#. Premi il tasto "Q" per avviare la calibrazione grayscale. Vedrai il PiCar-X effettuare piccoli movimenti sia a sinistra che a destra. Durante questo processo, ciascuno dei tre sensori dovrebbe passare almeno una volta sul nastro isolante.

#. Inoltre, noterai tre coppie di valori significativamente diversi che appariranno nella sezione "valori di soglia", mentre la "linea di riferimento" mostrerà due valori intermedi, ciascuno rappresentante la media di una di queste coppie.

    .. image:: img/calibrate_g2.png

#. Successivamente, sospendi il PiCar-X a mezz'aria (o posizionalo sopra un bordo) e premi il tasto "E". Vedrai che anche i valori di "riferimento scogliera" verranno aggiornati di conseguenza.

    .. image:: img/calibrate_g3.png

#. Una volta verificato che tutti i valori siano corretti, premi il tasto "spazio" per salvare i dati. Puoi quindi uscire dal programma premendo Ctrl+C.
