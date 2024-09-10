.. note::

    Ciao, benvenuto nella SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi i problemi post-vendita e le sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e Condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Giveaway Festivi**: Partecipa a promozioni e concorsi durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

Per Utenti Linux/Unix
==========================

#. Trova e apri il **Terminale** sul tuo sistema Linux/Unix.

#. Assicurati che il tuo Raspberry Pi sia connesso alla stessa rete. Verificalo digitando ``ping <hostname>.local``. Ad esempio:

    .. code-block::

        ping raspberrypi.local

    Dovresti vedere l'indirizzo IP del Raspberry Pi se è connesso alla rete.

    * Se il terminale mostra un messaggio come ``Ping request could not find host pi.local. Please check the name and try again.``, verifica nuovamente il nome host che hai inserito.
    * Se non riesci a recuperare l'indirizzo IP, controlla le impostazioni di rete o Wi-Fi sul Raspberry Pi.

#. Avvia una connessione SSH digitando ``ssh <username>@<hostname>.local`` o ``ssh <username>@<IP address>``. Ad esempio:

    .. code-block::

        ssh pi@raspberrypi.local

#. Al primo accesso, vedrai un messaggio di sicurezza. Digita ``yes`` per procedere.

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. Inserisci la password che hai impostato in precedenza. Nota che, per motivi di sicurezza, la password non sarà visibile mentre la digiti.

    .. note::
        È normale che i caratteri della password non vengano visualizzati nel terminale. Assicurati semplicemente di digitare la password corretta.

#. Una volta effettuato correttamente l'accesso, il tuo Raspberry Pi sarà connesso e potrai procedere con il passo successivo.

