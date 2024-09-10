.. note::

    Ciao, benvenuto nella Community SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia suggerimenti e tutorial per migliorare le tue abilità.
    - **Anteprime Esclusive**: Ottieni accesso anticipato ai nuovi annunci di prodotto e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Giveaway Festivi**: Partecipa a promozioni e omaggi festivi.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

4. Configura il tuo Raspberry Pi
==================================
Se hai uno schermo
---------------------

.. note:: Il Raspberry Pi ZERO installato sul robot non è facile da collegare allo schermo, ti consigliamo di utilizzare il metodo senza schermo per configurarlo.

Se disponi di uno schermo, sarà facile operare sul Raspberry Pi.

**Componenti Necessari**

* Raspberry Pi
* Alimentatore
* Scheda Micro SD
* Alimentatore per lo schermo
* Cavo HDMI
* Schermo
* Mouse
* Tastiera

#. Collega il mouse e la tastiera.

#. Collega lo schermo alla porta HDMI del Raspberry Pi e assicurati che lo schermo sia collegato alla presa a muro e acceso.

    .. note::

        Se utilizzi un Raspberry Pi 4, devi collegare lo schermo alla porta HDMI0 (quella più vicina alla porta di alimentazione).

#. Usa l'alimentatore per alimentare il Raspberry Pi.

#. Dopo pochi secondi, verrà visualizzato il desktop del sistema operativo Raspberry Pi. Ora puoi aprire il Terminale per iniziare a inserire i comandi.

    .. image:: img/bookwarm.png
        :align: center

Se non hai uno schermo
------------------------

Se non disponi di un monitor, puoi accedere al tuo Raspberry Pi da remoto.

**Componenti Necessari**

* Raspberry Pi
* Alimentatore
* Scheda Micro SD

Puoi utilizzare il comando SSH per aprire la shell Bash del Raspberry Pi. Bash è la shell standard predefinita per Linux. La shell stessa è un comando (istruzione) utilizzato dall'utente su Unix/Linux. La maggior parte delle operazioni può essere eseguita tramite la shell.

Se non sei soddisfatto dell'utilizzo della finestra dei comandi per accedere al tuo Raspberry Pi, puoi anche utilizzare la funzione di desktop remoto per gestire facilmente i file sul tuo Raspberry Pi tramite un'interfaccia grafica (GUI).

Consulta i tutorial dettagliati per ciascun sistema operativo riportati qui sotto.

.. toctree::

    remote_macosx
    remote_windows
    remote_linux
    remote_desktop
