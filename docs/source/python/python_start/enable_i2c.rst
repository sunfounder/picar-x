.. note::

    Ciao, benvenuto nella SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e Condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Giveaway Festivi**: Partecipa a promozioni e concorsi durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

6. Abilitare l'Interfaccia I2C (Importante)
===============================================

Utilizzeremo l'interfaccia I2C del Raspberry Pi. Questa interfaccia dovrebbe essere stata abilitata durante l'installazione del modulo ``robot-hat``. Per assicurarci che tutto sia corretto, verifichiamo se è effettivamente abilitata.

#. Inserisci il seguente comando:

    .. raw:: html

        <run></run>

    .. code-block:: 

        sudo raspi-config

#. Scegli **Interfacing Options** premendo la freccia verso il basso sulla tastiera, quindi premi il tasto **Enter**.

    .. image:: img/image282.png
        :align: center

#. Poi seleziona **I2C**.

    .. image:: img/image283.png
        :align: center

#. Usa i tasti freccia della tastiera per selezionare **<Yes>** -> **<OK>** per completare la configurazione dell'I2C.

    .. image:: img/image284.png
        :align: center

#. Dopo aver selezionato **<Finish>**, apparirà un pop-up che ti ricorderà che è necessario riavviare per rendere effettive le impostazioni; seleziona **<Yes>**.

    .. image:: img/camera_enable2.png
        :align: center
