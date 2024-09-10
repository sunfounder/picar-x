.. note::

    Ciao, benvenuto nella SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e Condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Giveaway Festivi**: Partecipa a promozioni e concorsi durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

Rilevamento del Viso
======================

Oltre al rilevamento dei colori, il PiCar-X include anche una funzione di rilevamento del viso. Nell'esempio seguente viene utilizzato il widget Joystick per regolare la direzione della fotocamera, e il numero di volti rilevati verrà visualizzato nel monitor di debug.

Per maggiori informazioni su come utilizzare il widget Video, fai riferimento al tutorial sui video di Ezblock qui: :ref:`ezblock:video_latest`.

.. image:: img/face_detection.PNG


**CONSIGLI**

.. image:: img/sp210512_141947.png

Imposta il widget **face detection** su **on** per abilitare il rilevamento facciale.

.. image:: img/sp210512_142327.png

Questi due blocchi vengono utilizzati per regolare l'orientamento della fotocamera pan-tilt, simili alla guida del PiCar-X nel tutorial :ref:`ezb_remote_control`. Aumentando il valore, la fotocamera ruoterà verso destra o verso l'alto, diminuendo il valore la fotocamera ruoterà verso sinistra o verso il basso.

.. image:: img/sp210512_142407.png

I risultati del rilevamento delle immagini vengono forniti tramite il blocco **detected face**. Utilizza le opzioni del menu a tendina per scegliere se leggere le coordinate, la dimensione o il numero di volti rilevati dalla funzione di rilevamento.

.. image:: img/sp210512_142616.png

Utilizza il blocco **create text with** per stampare la combinazione di **testo** e dei dati del **detected face**.

**ESEMPIO**

.. note::

    * Puoi scrivere il programma seguendo l'immagine qui sotto, fai riferimento al tutorial: :ref:`ezblock:create_project_latest`.
    * Oppure trova il codice con lo stesso nome nella pagina **Esempi** di EzBlock Studio e clicca direttamente su **Esegui** o **Modifica**.

.. image:: img/sp210512_142830.png
