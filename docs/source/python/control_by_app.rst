.. note::

    Ciao, benvenuto nella Community SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato ai nuovi annunci di prodotto e alle anteprime esclusive.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Giveaway Festivi**: Partecipa a promozioni e omaggi durante le festività.

    👉 Sei pronto per esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _control_by_app:

13. Controllato tramite APP
==================================

Il controller SunFounder viene utilizzato per controllare robot basati su Raspberry Pi/Pico.

L'APP integra widget come Pulsanti, Interruttori, Joystick, D-pad, Slider e Slider per la velocità; widget di input come Display Digitale, Radar Ultrasonico, Rilevamento Grigio e Tachimetro.

Ci sono 17 aree A-Q, dove puoi posizionare diversi widget per personalizzare il tuo controller.

Inoltre, questa applicazione fornisce un servizio di streaming video in tempo reale.

Personalizziamo un controller PiCar-X usando questa app.

**Come fare?**

#. Installa il modulo ``sunfounder-controller``.

    I moduli ``robot-hat``, ``vilib`` e ``picar-x`` devono essere installati prima, per i dettagli vedi: :ref:`install_all_modules`.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~
        git clone https://github.com/sunfounder/sunfounder-controller.git
        cd ~/sunfounder-controller
        sudo python3 setup.py install

#. Esegui il codice.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/picar-x/example
        sudo python3 13.app_control.py

#. Installa `SunFounder Controller <https://docs.sunfounder.com/projects/sf-controller/en/latest/>`_ da **APP Store(iOS)** o **Google Play(Android)**.

#. Apri l'app e crea un nuovo controller.

    Crea un nuovo controller cliccando sul simbolo + nell'APP SunFounder Controller.

    .. image:: img/app1.PNG

    Ci sono controller preimpostati per alcuni prodotti nella sezione Preset, che puoi utilizzare se necessario. Qui, selezioniamo **PiCar-X**.

    .. image:: img/app_control_preset.jpg

#. Connettiti a PiCar-X.

    Quando clicchi sul pulsante **Connect**, verranno cercati automaticamente i robot nelle vicinanze. Il suo nome è definito in ``picarx_control.py`` e deve essere sempre in esecuzione.

    .. image:: img/app9.PNG
    
    Una volta cliccato sul nome del prodotto, apparirà il messaggio "Connessione riuscita" e il nome del prodotto apparirà nell'angolo in alto a destra.
    .. image:: img/app10.PNG

    .. note::

        * Assicurati che il tuo dispositivo mobile sia connesso alla stessa LAN del PiCar-X.
        * Se non viene cercato automaticamente, puoi anche inserire manualmente l'IP per connetterti.

        .. image:: img/app11.PNG

#. Esegui questo controller.

    Clicca sul pulsante **Run** per avviare il controller, vedrai le immagini riprese dall'auto e potrai controllare il tuo PiCar-X con questi widget.

    .. image:: img/app12.PNG
    
    Ecco le funzioni dei widget.

    * **A**: Mostra la velocità attuale dell'auto.
    * **E**: Attiva la funzione di evitamento ostacoli.
    * **I**: Attiva la funzione di seguire la linea.
    * **J**: Riconoscimento vocale, tieni premuto questo widget per iniziare a parlare, e mostrerà la voce riconosciuta quando lo rilasci. Nel codice abbiamo impostato i comandi ``forward``, ``backward``, ``left`` e ``right`` per controllare l'auto.
    * **K**: Controlla i movimenti avanti, indietro, sinistra e destra dell'auto.
    * **Q**: Ruota la testa (Telecamera) su, giù, sinistra e destra.
    * **N**: Attiva la funzione di riconoscimento dei colori.
    * **O**: Attiva la funzione di riconoscimento facciale.
    * **P**: Attiva la funzione di riconoscimento degli oggetti, può riconoscere quasi 90 tipi di oggetti, per l'elenco dei modelli, fai riferimento a: https://github.com/sunfounder/vilib/blob/master/workspace/coco_labels.txt.
