.. note::

    Ciao, benvenuto nella SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue abilità.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Giveaway Festivi**: Partecipa a promozioni e concorsi durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _remote_desktop:

Accesso Desktop Remoto per Raspberry Pi
=======================================

Per chi preferisce un’interfaccia grafica (GUI) invece dell’accesso tramite riga di comando, Raspberry Pi supporta la funzionalità di desktop remoto.  
Questa guida ti guiderà nella configurazione e nell’uso di VNC (Virtual Network Computing) per l’accesso remoto.

Si consiglia di utilizzare `VNC® Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ per questo scopo.

**Abilitare il Servizio VNC su Raspberry Pi**

Il servizio VNC è preinstallato in Raspberry Pi OS ma è disabilitato per impostazione predefinita. Segui questi passaggi per abilitarlo:

#. Inserisci il seguente comando nel terminale del Raspberry Pi:

    .. raw:: html

        <run></run>

    .. code-block:: 

        sudo raspi-config

#. Naviga su **Interfacing Options** usando la freccia giù e premi **Enter**.

    .. image:: img/config_interface.png
        :align: center

#. Seleziona **VNC** tra le opzioni.

    .. image:: img/vnc.png
        :align: center

#. Usa le frecce per scegliere **<Yes>** -> **<OK>** -> **<Finish>** per completare l’attivazione del servizio VNC.

    .. image:: img/vnc_yes.png
        :align: center

**Accesso tramite VNC Viewer**

#. Scarica e installa `VNC Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ sul tuo computer personale.

#. Una volta installato, avvia VNC Viewer. Inserisci l’hostname o l’indirizzo IP del tuo Raspberry Pi e premi Invio.

    .. image:: img/vnc_viewer1.png
        :align: center

#. Quando richiesto, inserisci nome utente e password del tuo Raspberry Pi e clicca su **OK**.

    .. image:: img/vnc_viewer2.png
        :align: center

#. Dopo alcuni secondi verrà visualizzato il desktop di Raspberry Pi OS. Ora puoi aprire il Terminale e iniziare a inserire comandi.

    .. image:: img/bookwarm.png
        :align: center
