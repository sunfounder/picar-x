.. note::

    Ciao, benvenuto nella SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi i problemi post-vendita e le sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e Condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Giveaway Festivi**: Partecipa a promozioni e concorsi durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _install_os_sd:

2. Installazione del Sistema Operativo
============================================================


**Componenti Necessari**

* Un Computer
* Una scheda Micro SD e un Lettore

1. Installare Raspberry Pi Imager
-------------------------------------

#. Visita la pagina di download del software Raspberry Pi su `Raspberry Pi Imager <https://www.raspberrypi.org/software/>`_. Seleziona la versione di Imager compatibile con il tuo sistema operativo. Scarica e apri il file per avviare l'installazione.

    .. image:: img/os_install_imager.png
        :align: center

#. Durante l'installazione potrebbe apparire un avviso di sicurezza, a seconda del tuo sistema operativo. Ad esempio, su Windows potrebbe comparire un messaggio di avviso. In tal caso, seleziona **Maggiori informazioni** e poi **Esegui comunque**. Segui le istruzioni sullo schermo per completare l'installazione di Raspberry Pi Imager.

    .. image:: img/os_info.png
        :align: center

#. Avvia l'applicazione Raspberry Pi Imager facendo clic sulla sua icona o digitando ``rpi-imager`` nel terminale.

    .. image:: img/os_open_imager.png
        :align: center

2. Installare il Sistema Operativo sulla Micro SD
------------------------------------------------------

#. Inserisci la tua scheda SD nel computer o nel portatile utilizzando un lettore.

#. Nell'Imager, clicca su **Dispositivo Raspberry Pi** e seleziona il modello di Raspberry Pi dal menu a discesa.

    .. image:: img/os_choose_device.png
        :align: center

#. Seleziona **Sistema Operativo** e scegli la versione del sistema operativo raccomandata.

    .. image:: img/os_choose_os.png
        :align: center

#. Clicca su **Scegli Storage** e seleziona il dispositivo di archiviazione corretto per l'installazione.

    .. note::

        Assicurati di selezionare il dispositivo di archiviazione corretto. Per evitare confusione, disconnetti eventuali dispositivi di archiviazione aggiuntivi se ne hai collegati più di uno.

    .. image:: img/os_choose_sd.png
        :align: center

#. Clicca su **AVANTI** e poi su **MODIFICA IMPOSTAZIONI** per personalizzare le impostazioni del sistema operativo.

    .. note::

        Se hai un monitor per il tuo Raspberry Pi, puoi saltare i prossimi passaggi e cliccare 'Sì' per iniziare l'installazione. Puoi regolare altre impostazioni successivamente sul monitor.

    .. image:: img/os_enter_setting.png
        :align: center

#. Definisci un **hostname** per il tuo Raspberry Pi.

    .. note::

        L'hostname è l'identificativo di rete del tuo Raspberry Pi. Puoi accedere al tuo Pi utilizzando ``<hostname>.local`` o ``<hostname>.lan``.

    .. image:: img/os_set_hostname.png
        :align: center

#. Crea un **Nome Utente** e una **Password** per l'account amministratore del Raspberry Pi.

    .. note::

        È essenziale stabilire un nome utente e una password unici per proteggere il tuo Raspberry Pi, che non ha una password predefinita.

    .. image:: img/os_set_username.png
        :align: center

#. Configura la LAN wireless fornendo il **SSID** e la **Password** della tua rete.

    .. note::

        Imposta il ``Paese LAN Wireless`` al codice `ISO/IEC alpha2 a due lettere <https://it.wikipedia.org/wiki/ISO_3166-1_alpha-2#Codici_alpha-2_ufficialmente_assegnati>`_ corrispondente alla tua posizione.

    .. image:: img/os_set_wifi.png
        :align: center


#. Per connetterti da remoto al tuo Raspberry Pi, abilita SSH nella scheda Servizi.

    * Per l'autenticazione tramite password, utilizza il nome utente e la password dalla scheda Generale.
    * Per l'autenticazione tramite chiave pubblica, scegli "Consenti solo autenticazione tramite chiave pubblica". Se hai una chiave RSA, verrà utilizzata. In caso contrario, clicca su "Esegui SSH-keygen" per generare una nuova coppia di chiavi.

    .. image:: img/os_enable_ssh.png
        :align: center

#. Il menu **Opzioni** ti permette di configurare il comportamento dell'Imager durante la scrittura, inclusa la possibilità di riprodurre un suono alla fine, espellere il supporto al termine e abilitare la telemetria.

    .. image:: img/os_options.png
        :align: center

    
#. Una volta terminate le impostazioni di personalizzazione del sistema operativo, clicca su **Salva** per salvare le modifiche. Poi, clicca su **Sì** per applicarle quando scrivi l'immagine.

    .. image:: img/os_click_yes.png
        :align: center

#. Se la scheda SD contiene dati esistenti, assicurati di eseguire un backup per evitare la perdita di dati. Procedi cliccando su **Sì** se non è necessario alcun backup.

    .. image:: img/os_continue.png
        :align: center

#. Quando appare il popup "Scrittura completata con successo", la tua immagine è stata scritta e verificata completamente. Ora sei pronto per avviare un Raspberry Pi dalla Micro SD Card!

    .. image:: img/os_finish.png
        :align: center

#. Ora puoi inserire la scheda SD configurata con il Raspberry Pi OS nello slot microSD situato sul lato inferiore del Raspberry Pi.

    .. image:: img/insert_sd_card.png
        :width: 500
        :align: center
