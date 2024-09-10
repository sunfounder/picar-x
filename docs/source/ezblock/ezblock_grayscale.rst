.. note::

    Ciao, benvenuto nella SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e Condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Giveaway Festivi**: Partecipa a promozioni e concorsi durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _test_grayscale:

Test del Modulo in Scala di Grigi
======================================

Il PiCar-X include un modulo in scala di grigi per implementare il seguimento delle linee, il rilevamento delle scogliere e altri esperimenti divertenti. Il modulo in scala di grigi ha tre sensori di rilevamento che segnalano ciascuno un valore in base alla tonalità del colore rilevata dal sensore. Ad esempio, un sensore che legge una tonalità di nero puro restituirà un valore di “0”.

**CONSIGLI**

.. image:: img/sp210512_115406.png

Utilizza il blocco **Grayscale module** per leggere il valore di uno dei sensori. Nell'esempio sopra, il sensore “A0” è quello più a sinistra del PiCar-X. Utilizza la freccia a tendina per cambiare il sensore in “A1” (sensore centrale) o “A2” (sensore più a destra).

.. image:: img/sp210512_120023.png

Il programma è semplificato con il blocco **create list with**. 
Una **Lista** viene utilizzata nello stesso modo di una singola **Variabile**, 
ma in questo caso una **Lista** è più efficiente di una singola **Variabile** perché il **modulo in scala di grigi** riporterà più di un valore del sensore.
Il blocco **create list with** creerà variabili separate per ogni sensore e le inserirà in una Lista.

**ESEMPIO**

.. note::

    * Puoi scrivere il programma seguendo l'immagine qui sotto, fai riferimento al tutorial: :ref:`ezblock:create_project_latest`.
    * Oppure trova il codice con lo stesso nome nella pagina **Esempi** di EzBlock Studio e clicca direttamente su **Esegui** o **Modifica**.

.. image:: img/sp210512_120508.png
