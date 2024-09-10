.. note::

    Ciao, benvenuto nella SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e Condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Giveaway Festivi**: Partecipa a promozioni e concorsi durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

Test del Modulo Ultrasonico
===============================

Il PiCar-X ha un modulo sensore a ultrasuoni integrato che può essere utilizzato per esperimenti di evitamento ostacoli e inseguimento automatico di oggetti. In questa lezione, il modulo leggerà una distanza in centimetri (24 cm = 1 pollice) e stamperà i risultati in una finestra di **Debug**.

**CONSIGLI**

.. image:: img/sp210512_114549.png 

Il blocco **Ultrasonic get distance** leggerà la distanza tra il PiCar-X e un ostacolo direttamente di fronte.

.. image:: img/sp210512_114830.png

Questo programma è semplificato con una **Variabile**. Ad esempio, quando ci sono più funzioni in un programma che devono utilizzare la distanza da un ostacolo, una **Variabile** può essere utilizzata per riportare lo stesso valore di distanza a ciascuna funzione, invece che ogni funzione legga il valore separatamente.

.. image:: img/sp210512_114916.png

Clicca sul pulsante **Create variable...** nella categoria **Variables** e utilizza la freccia a tendina per selezionare la variabile chiamata “distance”.

.. image:: img/sp210512_114945.png

La funzione **Print** può stampare dati come variabili e testo per facilitare il debug.

.. image:: img/debug_monitor.png

Una volta eseguito il codice, abilita il monitor di debug cliccando sull'icona **Debug** nell'angolo in basso a sinistra.

**ESEMPIO**

.. note::

    * Puoi scrivere il programma seguendo l'immagine qui sotto, fai riferimento al tutorial: :ref:`ezblock:create_project_latest`.
    * Oppure trova il codice con lo stesso nome nella pagina **Esempi** di EzBlock Studio e clicca direttamente su **Esegui** o **Modifica**.

.. image:: img/sp210512_115125.png
