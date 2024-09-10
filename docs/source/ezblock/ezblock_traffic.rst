.. note::

    Ciao, benvenuto nella SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e Condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Giveaway Festivi**: Partecipa a promozioni e concorsi durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

Rilevamento dei Segnali Stradali
====================================

Oltre al rilevamento dei colori e dei volti, PiCar-X è anche in grado di rilevare i segnali stradali.

Ora combiniamo questa funzione di rilevamento dei segnali stradali con la funzione di seguimento della linea. Lasciamo che PiCar-X segua la linea, e quando metti il segnale di Stop davanti a lui, si fermerà. Quando metti il segnale di Avanti davanti a lui, riprenderà a muoversi in avanti.

**CONSIGLI**

#. PiCar riconoscerà 4 modelli di segnali stradali inclusi nel PDF stampabile qui sotto.

    .. image:: img/taffics_sign.png

    * :download:`[PDF]Traffic Sign Cards <https://github.com/sunfounder/sf-pdf/raw/master/prop_card/object_detection/traffic-sign-cards.pdf>`

#. Il blocco **Set ref to ()** viene utilizzato per impostare la soglia della scala di grigi, che deve essere modificata in base alla situazione reale. Puoi eseguire il test :ref:`test_grayscale` per vedere i valori del modulo in scala di grigi su superfici bianche e nere e inserire i valori medi in questo blocco.


**ESEMPIO**

.. note::

    * Puoi scrivere il programma seguendo l'immagine qui sotto, fai riferimento al tutorial: :ref:`ezblock:create_project_latest`.
    * Oppure trova il codice con lo stesso nome nella pagina **Esempi** di EzBlock Studio e clicca direttamente su **Esegui** o **Modifica**.

.. image:: img/sp210513_101526.png

.. image:: img/sp210513_110948.png

.. image:: img/sp210512_171425.png

.. image:: img/sp210512_171454.png
