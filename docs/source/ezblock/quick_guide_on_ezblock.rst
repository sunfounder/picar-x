.. note::

    Ciao, benvenuto nella SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e Condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Giveaway Festivi**: Partecipa a promozioni e concorsi durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _ezb_servo_adjust:

Guida Rapida su EzBlock
===========================

.. note::

    Se stai usando un Raspberry Pi 5, il nostro software di programmazione grafica, EzBlock, non è supportato.

L'intervallo dell'angolo del servo è -90~90 gradi, ma l'angolo impostato in fabbrica è casuale, potrebbe essere 0°, potrebbe essere 45°; se lo assembliamo con questo angolo direttamente, si verificherà uno stato caotico dopo che il robot esegue il codice, o peggio, il servo potrebbe bloccarsi e bruciarsi.

Quindi, qui dobbiamo impostare tutti gli angoli del servo a 0° e poi montarli, in modo che l'angolo del servo sia al centro, indipendentemente dalla direzione di rotazione.

#. Prima di tutto, :ref:`ezblock:install_ezblock_os_latest` (i tutorial di EzBlock) su una scheda Micro SD, una volta completata l'installazione, inseriscila nel Raspberry Pi.

    .. note::
        Dopo aver completato l'installazione, torna a questa pagina.

    .. image:: img/insert_sd_card.png
        :width: 500
        :align: center

#. Per assicurarti che il servo sia stato correttamente impostato su 0°, inserisci prima il braccio del servo nell'asse del servo e poi ruota delicatamente il braccio oscillante a un angolo diverso. Questo braccio del servo serve solo per permetterti di vedere chiaramente che il servo ruota.

    .. image:: img/servo_arm.png

#. Segui le istruzioni sull'opuscolo di montaggio, inserisci il cavo della batteria e accendi l'interruttore di alimentazione. Collega poi un cavo USB-C alimentato per attivare la batteria. Aspetta 1-2 minuti, ci sarà un suono che indicherà l'avvio corretto del Raspberry Pi.

    .. image:: img/Z_BTR.JPG
        :width: 800
        :align: center

#. Successivamente, collega il cavo del servo alla porta P11 come mostrato.

    .. image:: img/Z_P11.JPG

#. Tieni premuto il tasto **USR**, quindi premi il tasto **RST** per eseguire lo script di azzeramento del servo all'interno del sistema. Quando vedi che il braccio del servo ruota in una posizione (Questa è la posizione 0°, che è casuale e potrebbe non essere verticale o parallela.), significa che il programma è stato eseguito.

    .. note::

        Questo passaggio deve essere eseguito solo una volta; successivamente, basta inserire gli altri cavi del servo, e si azzereranno automaticamente.

    .. image:: img/Z_P11_BT.png
        :width: 400
        :align: center
    
#. Ora, rimuovi il braccio del servo, assicurandoti che il cavo del servo rimanga collegato, e non spegnere l'alimentazione. Quindi continua il montaggio seguendo le istruzioni cartacee.

.. note::

    * Non scollegare questo cavo del servo prima di fissarlo con la vite del servo; puoi scollegarlo dopo averlo fissato.
    * Non ruotare il servo mentre è acceso per evitare danni; se l'asse del servo è inserito con l'angolazione sbagliata, estrai il servo e reinseriscilo.
    * Prima di montare ogni servo, è necessario collegare il cavo del servo alla porta P11 e accendere l'alimentazione per impostare il suo angolo su 0°.
    * Questa funzione di azzeramento sarà disabilitata se scarichi un programma sul robot successivamente tramite l'app EzBlock.
