.. note::

    Ciao, benvenuto nella SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi i problemi post-vendita e le sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e Condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Giveaway Festivi**: Partecipa a promozioni e concorsi durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

7. Regolazione del Servo (Importante)
=========================================

.. note::

    Se il tuo Robot HAT è della versione V44 o superiore (con l'altoparlante posizionato nella parte superiore della scheda) e include un pulsante Zero integrato, puoi saltare questo passaggio e semplicemente premere il pulsante Zero per attivare il programma di azzeramento dei servomotori.

    .. image:: img/robot_hat_v44.png
        :width: 500
        :align: center

L'angolo di rotazione del servo varia da -90° a 90°, ma l'angolo impostato in fabbrica è casuale, potrebbe essere 0°, oppure 45°; se montiamo il servo con un angolo casuale, il robot potrebbe non funzionare correttamente, o peggio, il servo potrebbe bloccarsi o surriscaldarsi.

Pertanto, è necessario impostare tutti i servo a 0° prima di assemblarli, in modo che l'angolo sia centrato, indipendentemente dalla direzione di rotazione.

#. Per garantire che il servo sia impostato correttamente su 0°, inserisci prima il braccio del servo nell'asse del servo e ruota delicatamente il braccio in un'angolazione diversa. Questo ti permetterà di vedere chiaramente la rotazione del servo.

    .. image:: img/servo_arm.png

#. Ora, esegui ``servo_zeroing.py`` nella cartella ``example/``.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/picar-x/example
        sudo python3 servo_zeroing.py

#. Successivamente, collega il cavo del servo alla porta P11 come segue, e vedrai che il braccio del servo si muoverà in una posizione. (Questa è la posizione 0°, che può non essere verticale o parallela).

    .. image:: img/Z_P11.JPG

#. Ora, rimuovi il braccio del servo, assicurandoti che il cavo del servo rimanga collegato, e non spegnere l'alimentazione. Continua con l'assemblaggio seguendo le istruzioni cartacee.

.. note::

    * Non scollegare il cavo del servo prima di fissarlo con la vite del servo, puoi scollegarlo solo dopo averlo fissato.
    * Non ruotare il servo mentre è alimentato per evitare danni; se l'albero del servo non è inserito nell'angolo corretto, estrai il servo e reinseriscilo.
    * Prima di assemblare ogni servo, è necessario collegare il cavo del servo a P11 e accendere l'alimentazione per impostare il suo angolo su 0°.
