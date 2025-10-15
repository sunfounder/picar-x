.. note::

    Ciao, benvenuto nella Community SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia suggerimenti e tutorial per migliorare le tue abilità.
    - **Anteprime Esclusive**: Ottieni accesso anticipato ai nuovi annunci di prodotto e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Giveaway Festivi**: Partecipa a promozioni e omaggi festivi.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _setup_pi:

4. Configurare il tuo Raspberry Pi
===================================

Per iniziare a programmare e controllare il tuo PiCar-X, devi prima accedere al tuo Raspberry Pi.  
Questa sezione ti guiderà attraverso due metodi comuni: utilizzare un monitor, una tastiera e un mouse, oppure configurare una connessione headless per accedere da remoto da un altro computer.

Se hai uno schermo
-------------------------

.. note:: Il Raspberry Pi Zero 2W installato sul robot non è facile da collegare a uno schermo. Si consiglia il metodo **headless (senza schermo)**.

**Componenti necessari**

* Raspberry Pi
* Alimentatore
* Scheda Micro SD
* Cavo HDMI
* Schermo
* Mouse
* Tastiera

#. Inserisci la scheda microSD nel tuo Raspberry Pi.
#. Collega mouse, tastiera e schermo (per Pi 4/5 utilizza **HDMI0**, la porta più vicina all’alimentazione).
#. Accendi il Raspberry Pi.
#. Dopo pochi istanti, apparirà il desktop di Raspberry Pi OS e potrai aprire un Terminale per inserire comandi.

    .. image:: img/bookwarm.png
        :align: center


Se non hai uno schermo (Configurazione Headless)
----------------------------------------------------

Senza un monitor, puoi configurare e accedere al tuo Raspberry Pi da remoto. Questo è il modo più comodo per iniziare.

**Componenti necessari**

* Raspberry Pi
* Alimentatore
* Scheda Micro SD
* Un computer sulla stessa rete

**Suggerimenti**

* Imposta correttamente il **paese della LAN wireless** utilizzando il codice ISO/IEC alpha-2 (es. ``US``, ``UK``, ``CN``); altrimenti il Wi-Fi non funzionerà.  
* Assicurati che il tuo Raspberry Pi e il tuo computer siano sulla stessa rete locale.  
* Per una connessione più stabile, utilizza una connessione di rete diretta (Ethernet) quando possibile.  


**Connessione tramite SSH**

1. Sul tuo computer, apri un terminale (Windows: **PowerShell**, macOS/Linux: **Terminale**) e digita:

   .. code-block::

      ssh <username>@<hostname>.local
      # Esempio:
      ssh daisy@picarx.local

#. In alternativa, controlla la lista DHCP/client del tuo router, trova l’indirizzo IP del Pi e connettiti utilizzando:

   .. code-block::

      ssh <username>@<IP>
      
      # Esempio:

      ssh daisy@192.xxx.xx.xx

#. Al primo accesso, vedrai un messaggio di sicurezza. Digita ``yes`` per continuare:

#. Inserisci la password impostata in Raspberry Pi Imager. (I caratteri non verranno visualizzati durante la digitazione; è normale.)

   .. note::
      L’assenza di caratteri visibili durante l’inserimento della password è una normale misura di sicurezza. Digita con attenzione.

#. Una volta connesso, il tuo Raspberry Pi è pronto per le operazioni da remoto.

   .. image:: img/ssh_login.png
      :align: center

**Risoluzione dei problemi**

* **ssh: Could not resolve hostname ...**  

  * Controlla che l’hostname sia corretto.  
  * Se non funziona, usa l’indirizzo IP del Pi invece di ``<hostname>.local``.

* **The term 'ssh' is not recognized... (Windows)**  

  * Il tuo sistema non ha OpenSSH installato. Installa OpenSSH manualmente (vedi :ref:`openssh_powershell`), oppure usa un client SSH di terze parti (vedi :ref:`login_windows`).  

* **Permission denied (publickey,password)**  

  * Assicurati di utilizzare il nome utente e la password configurati in Raspberry Pi Imager.  

* **Connection refused**  

  * Attendi 1–2 minuti dopo l’accensione.  
  * Conferma che SSH sia stato abilitato in Raspberry Pi Imager.

**Opzioni di accesso grafico**

Se preferisci un’interfaccia grafica invece della riga di comando, hai due opzioni:

    .. image:: img/bookwarm.png
        :align: center

* :ref:`remote_desktop`: Abilita **VNC (Virtual Network Computing)** per un’esperienza desktop completa sul tuo Pi.  
* |link_rpi_connect|: Usa **Raspberry Pi Connect** per un accesso remoto sicuro da qualsiasi luogo, direttamente da un browser.  

Ora puoi controllare il tuo Raspberry Pi senza monitor, tramite SSH per operazioni da riga di comando oppure con VNC / Raspberry Pi Connect per un’esperienza desktop grafica.
