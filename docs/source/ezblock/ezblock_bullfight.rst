.. note::

    Ciao, benvenuto nella SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e Condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Giveaway Festivi**: Partecipa a promozioni e concorsi durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

Corrida
==============

Trasforma il PiCar-X in un toro furioso! Prepara un panno rosso, come un fazzoletto, e diventa un torero. Quando il PiCar-X insegue il panno rosso, fai attenzione a non farti colpire!

.. note::

    Questo progetto è più avanzato rispetto ai precedenti. Il PiCar-X dovrà utilizzare la funzione di rilevamento del colore per mantenere la fotocamera rivolta verso il panno rosso, e l'orientamento del corpo si regolerà automaticamente in base alla direzione in cui è rivolta la fotocamera.

**CONSIGLI**

.. image:: img/sp210512_174650.png

Inizia aggiungendo il blocco **color detection [red]** al widget **Start** per far sì che il PiCar-X cerchi un oggetto di colore rosso. Nel ciclo infinito, aggiungi il blocco **[width] of detected color** per trasformare l'ingresso in una griglia di "rilevamento oggetti".

.. image:: img/sp210512_174807.png

Il "rilevamento oggetti" restituirà le coordinate rilevate in valori (x, y), 
basate sul punto centrale dell'immagine della fotocamera. 
Lo schermo è suddiviso in una griglia 3x3, come mostrato di seguito, quindi 
se il panno rosso viene mantenuto in alto a sinistra nell'immagine della 
fotocamera, le coordinate (x, y) saranno (-1, 1).

.. image:: img/sp210512_174956.png

Il "rilevamento oggetti" rileverà la larghezza e l'altezza del grafico. Se vengono 
identificati più obiettivi, verranno registrate le dimensioni dell'obiettivo più grande.

**ESEMPIO**

.. note::

    * Puoi scrivere il programma seguendo l'immagine sottostante, fai riferimento al tutorial: :ref:`ezblock:create_project_latest`.
    * Oppure trova il codice con lo stesso nome nella pagina **Esempi** di EzBlock Studio e clicca direttamente su **Esegui** o **Modifica**.

.. image:: img/sp210512_175519.png
    :width: 800