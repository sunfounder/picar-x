.. note::

    Ciao, benvenuto nella SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e Condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Giveaway Festivi**: Partecipa a promozioni e concorsi durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

Attenzione ai Pedoni
=============================

Questo progetto farà sì che il PiCar-X adotti le misure appropriate in base alle condizioni della strada. Durante la guida, il PiCar-X si fermerà completamente se rileva un pedone sul suo percorso.

Una volta avviato il programma, tieni una foto di una persona davanti al PiCar-X. Il Video Monitor rileverà il volto della persona e il PiCar-X si fermerà automaticamente.

Per simulare i protocolli di sicurezza stradale, viene creato un processo di giudizio che invierà un valore **[count]** a un blocco **if do else**. Questo processo controllerà 10 volte se appare un volto umano, e se viene rilevato incrementerà **[count]** di +1. Quando **[count]** supera 3, il PiCar-X smetterà di muoversi.

* :ref:`ezblock:remote_control_latest`

.. image:: img/face_detection.PNG


**ESEMPIO**

.. note::

    * Puoi scrivere il programma seguendo l'immagine qui sotto, fai riferimento al tutorial: :ref:`ezblock:create_project_latest`.
    * Oppure trova il codice con lo stesso nome nella pagina **Esempi** di EzBlock Studio e clicca direttamente su **Esegui** o **Modifica**.

.. image:: img/sp210512_185509.png
