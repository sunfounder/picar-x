.. note::

    Ciao, benvenuto nella SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi i problemi post-vendita e le sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e Condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Giveaway Festivi**: Partecipa a promozioni e concorsi durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

Per Utenti Mac OS X
==========================

Per gli utenti Mac OS X, SSH (Secure Shell) offre un metodo sicuro e comodo per accedere e controllare in remoto un Raspberry Pi. Questo è particolarmente utile per lavorare con il Raspberry Pi a distanza o quando non è collegato a un monitor. Utilizzando l'applicazione Terminale su un Mac, è possibile stabilire questa connessione sicura. Il processo prevede l'uso di un comando SSH che incorpora il nome utente e il nome host del Raspberry Pi. Durante la connessione iniziale, verrà visualizzato un prompt di sicurezza che richiede la conferma dell'autenticità del Raspberry Pi.

#. Per connettersi al Raspberry Pi, digita il seguente comando SSH:

    .. code-block::

        ssh pi@raspberrypi.local

    .. image:: img/mac-ping.png

#. Al primo accesso apparirà un messaggio di sicurezza. Rispondi con **yes** per procedere.

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. Inserisci la password per il Raspberry Pi. Ricorda che la password non verrà visualizzata sullo schermo mentre la digiti, una misura di sicurezza standard.

    .. code-block::

        pi@raspberrypi.local's password: 
        Linux raspberrypi 5.15.61-v8+ #1579 SMP PREEMPT Fri Aug 26 11:16:44 BST 2022 aarch64

        The programs included with the Debian GNU/Linux system are free software;
        the exact distribution terms for each program are described in the
        individual files in /usr/share/doc/*/copyright.

        Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
        permitted by applicable law.
        Last login: Thu Sep 22 12:18:22 2022
        pi@raspberrypi:~ $ 
