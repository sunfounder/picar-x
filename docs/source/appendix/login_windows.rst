.. note::

    Ciao, benvenuto nella SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue abilità.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Giveaway Festivi**: Partecipa a promozioni e concorsi durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _login_windows:

PuTTY
=========================

Se sei un utente Windows, puoi utilizzare alcune applicazioni per SSH. Qui ti consigliamo `PuTTY <https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html>`_.

**Passo 1**

Scarica PuTTY.

**Passo 2**

Apri PuTTY e clicca su **Session** nella struttura ad albero a sinistra. 
Inserisci l'indirizzo IP del Raspberry Pi nella casella di testo sotto 
**Host Name (or IP address)** e **22** sotto **Port** (di default è 22).

.. image:: img/image25.png
    :align: center

**Passo 3**

Clicca su **Open**. Nota che, quando accedi per la prima volta al Raspberry Pi 
utilizzando l'indirizzo IP, comparirà un promemoria di sicurezza. Clicca 
semplicemente su **Yes**.

**Passo 4**

Quando nella finestra di PuTTY compare \"**login as:**\", digita \"**pi**\" 
(il nome utente del Raspberry Pi) e come **password** inserisci: \"raspberry\" 
(quella predefinita, se non l'hai cambiata).

.. note::

    Quando inserisci la password, i caratteri non verranno visualizzati nella finestra, il che è normale. Devi solo inserire correttamente la password.
    
    Se accanto a PuTTY compare "inactive", significa che la connessione è stata interrotta e deve essere ristabilita.

.. image:: img/image26.png
    :align: center

**Passo 5**

A questo punto, siamo collegati al Raspberry Pi ed è il momento di procedere con i passaggi successivi.
