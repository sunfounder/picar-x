.. note::

    Ciao, benvenuto nella SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e Condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Giveaway Festivi**: Partecipa a promozioni e concorsi durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

Minecart Plus
=======================

In questo progetto è stato aggiunto il recupero dal deragliamento al progetto :ref:`ezb_minecart`, per permettere al PiCar-X di adattarsi e riprendersi da curve più strette.

.. image:: img/minec.png


**CONSIGLI**

#. Usa un altro blocco **to do something** per permettere al PiCar-X di fare retromarcia e recuperare da una curva stretta. Nota che la nuova funzione **to do something** non restituisce alcun valore, ma viene utilizzata solo per riorientare il PiCar-X.

    .. image:: img/sp210512_171727.png

#. Il blocco **Set ref to ()** viene utilizzato per impostare la soglia della scala di grigi, che deve essere modificata in base alla situazione reale. Puoi eseguire il test :ref:`test_grayscale` per vedere i valori del modulo in scala di grigi su superfici bianche e nere e inserire i valori medi in questo blocco.


**ESEMPIO**

.. note::

    * Puoi scrivere il programma seguendo l'immagine qui sotto, fai riferimento al tutorial: :ref:`ezblock:create_project_latest`.
    * Oppure trova il codice con lo stesso nome nella pagina **Esempi** di EzBlock Studio e clicca direttamente su **Esegui** o **Modifica**.

.. image:: img/sp210512_171914.png

.. image:: img/sp210512_171932.png

.. image:: img/sp210512_171425.png

.. image:: img/sp210512_171454.png
