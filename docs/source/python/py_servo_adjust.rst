.. note::

    Ciao, benvenuto nella community di appassionati di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato ai nuovi annunci di prodotto e anteprime esclusive.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa a promozioni e omaggi durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

Regolazione del Servo (Importante)
====================================

.. note::

    Se il tuo Robot HAT è la versione V44 o superiore (con l’altoparlante posizionato nella parte superiore della scheda) e include un pulsante **Zero** integrato, puoi saltare questo passaggio e premere semplicemente il pulsante **Zero** per attivare il programma di azzeramento del servo.

    .. image:: img/robot_hat_v44.png
        :width: 500
        :align: center

L’intervallo di angolazione del servo è -90~90, ma l’angolo impostato in fabbrica è casuale: potrebbe essere 0°, oppure 45°. Se lo assembliamo direttamente con un angolo di questo tipo, dopo l’esecuzione del codice del robot si verificherà uno stato caotico o, peggio ancora, il servo potrebbe bloccarsi e bruciarsi.

Per questo motivo è necessario impostare tutti i servi a 0° prima di installarli, in modo che l’angolo del servo sia centrato, indipendentemente dalla direzione di rotazione.

#. Per assicurarti che il servo sia stato correttamente impostato a 0°, inserisci prima il braccio del servo sull’albero del servo e poi ruota delicatamente il braccio oscillante verso un angolo diverso. Questo braccio del servo serve solo a permetterti di vedere chiaramente che il servo sta ruotando.

    .. image:: img/servo_arm.png

#. Ora esegui ``servo_zeroing.py`` nella cartella ``example/``.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/picar-x/example
        sudo python3 servo_zeroing.py

#. Successivamente, collega il cavo del servo alla porta P11 come mostrato di seguito; allo stesso tempo vedrai il braccio del servo ruotare in una posizione (questa è la posizione 0°, che è casuale e potrebbe non essere verticale o parallela).

    .. image:: img/Z_P11.jpg

#. Ora rimuovi il braccio del servo, assicurandoti che il cavo del servo rimanga collegato e senza spegnere l’alimentazione. Quindi continua l’assemblaggio seguendo le istruzioni cartacee.

.. note::

    * Non scollegare il cavo del servo prima di fissarlo con la vite del servo; puoi scollegarlo dopo averlo fissato.
    * Non ruotare il servo mentre è alimentato per evitare danni; se l’albero del servo non è inserito con l’angolazione corretta, estrai il servo e reinseriscilo.
    * Prima di assemblare ciascun servo, è necessario collegare il cavo del servo alla porta P11 e accendere l’alimentazione per impostare il suo angolo a 0°.
