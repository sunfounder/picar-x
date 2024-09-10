.. note::

    Ciao, benvenuto nella SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e Condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Giveaway Festivi**: Partecipa a promozioni e concorsi durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _ezb_minecart:

Minecart
=====================

Realizziamo un progetto con un carrello da miniera! Questo progetto utilizzerà il modulo in scala di grigi per far muovere il PiCar-X lungo una pista. 
Utilizza del nastro di colore scuro per creare una pista sul pavimento il più dritta possibile e non troppo curva. Potrebbe essere necessario fare qualche esperimento se il PiCar-X deraglia.

Durante il movimento lungo la pista, le sonde sui lati sinistro e destro del modulo in scala di grigi rileveranno il terreno di colore chiaro, mentre la sonda centrale rileverà la pista. Se la pista ha un arco, la sonda sul lato sinistro o destro del sensore rileverà il nastro di colore scuro e girerà le ruote in quella direzione. Se il carrello della miniera raggiunge la fine della pista o deraglia, il modulo in scala di grigi non rileverà più il nastro della pista e il PiCar-X si fermerà.


**CONSIGLI**

* Il blocco **Set ref to ()** viene utilizzato per impostare la soglia della scala di grigi, che deve essere modificata in base alla situazione reale. Puoi eseguire il test :ref:`test_grayscale` per vedere i valori del modulo in scala di grigi su superfici bianche e nere e inserire i valori medi in questo blocco.


**ESEMPIO**

.. note::

    * Puoi scrivere il programma seguendo l'immagine qui sotto, fai riferimento al tutorial: :ref:`ezblock:create_project_latest`.
    * Oppure trova il codice con lo stesso nome nella pagina **Esempi** di EzBlock Studio e clicca direttamente su **Esegui** o **Modifica**.

.. image:: img/sp210512_170342.png

.. image:: img/sp210512_171425.png

.. image:: img/sp210512_171454.png
