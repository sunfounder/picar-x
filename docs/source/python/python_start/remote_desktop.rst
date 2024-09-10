.. note::

    Ciao, benvenuto nella SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi i problemi post-vendita e le sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e Condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Giveaway Festivi**: Partecipa a promozioni e concorsi durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _remote_desktop:

Accesso Desktop Remoto per Raspberry Pi
==================================================

Per chi preferisce un'interfaccia grafica (GUI) rispetto all'accesso a riga di comando, il Raspberry Pi supporta la funzionalità di desktop remoto. Questa guida ti guiderà nell'impostazione e nell'uso di VNC (Virtual Network Computing) per l'accesso remoto.

Ti consigliamo di utilizzare `VNC® Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ a tale scopo.

**Abilitazione del Servizio VNC su Raspberry Pi**

Il servizio VNC è preinstallato nel sistema operativo Raspberry Pi OS ma è disabilitato per impostazione predefinita. Segui questi passaggi per abilitarlo:

#. Inserisci il seguente comando nel terminale del Raspberry Pi:

    .. raw:: html

        <run></run>

    .. code-block:: 

        sudo raspi-config

#. Naviga fino a **Opzioni di Interfaccia** utilizzando il tasto freccia in basso, quindi premi **Invio**.

    .. image:: img/config_interface.png
        :align: center

#. Seleziona **VNC** dalle opzioni.

    .. image:: img/vnc.png
        :align: center

#. Usa i tasti freccia per scegliere **<Sì>** -> **<OK>** -> **<Fine>** e finalizza l'attivazione del servizio VNC.

    .. image:: img/vnc_yes.png
        :align: center

**Accesso tramite VNC Viewer**

#. Scarica e installa `VNC Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ sul tuo computer personale.

#. Una volta installato, avvia VNC Viewer. Inserisci il nome host o l'indirizzo IP del tuo Raspberry Pi e premi Invio.

    .. image:: img/vnc_viewer1.png
        :align: center

#. Quando richiesto, inserisci nome utente e password del tuo Raspberry Pi, quindi fai clic su **OK**.

    .. image:: img/vnc_viewer2.png
        :align: center

#. Dopo pochi secondi, verrà visualizzato il desktop di Raspberry Pi OS. Ora puoi aprire il Terminale per iniziare a inserire i comandi.

    .. image:: img/bookwarm.png
        :align: center

