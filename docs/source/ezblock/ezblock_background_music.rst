.. note::

    Ciao, benvenuto nella SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e Condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Giveaway Festivi**: Partecipa a promozioni e concorsi durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

Musica di Sottofondo
======================

Oltre a programmare il PiCar-X per riprodurre effetti sonori o text-to-speech (TTS), il PiCar-X può anche riprodurre musica di sottofondo. Questo progetto utilizzerà un widget **Slider** per regolare il volume della musica.

* :ref:`ezblock:remote_control_latest`

Per un tutorial dettagliato sulle funzioni di controllo remoto di Ezblocks, fai riferimento al tutorial :ref:`ezb_remote_control`.

**CONSIGLI**

.. image:: img/sp210512_152803.png

Il blocco **play background music** dovrà essere aggiunto alla funzione **Start**. Utilizza il menu a tendina per scegliere la musica di sottofondo che il PiCar-X riprodurrà.

.. image:: img/sp210512_153123.png

Il blocco **set background music volume to** regolerà il volume in un intervallo da 0 a 100.

.. image:: img/sp210512_154708.png

Trascina una barra **Slider** dalla pagina **Remote Control** per regolare il volume della musica.

.. image:: img/sp210512_154259.png

Il blocco **slider [A] get value** leggerà il valore dello slider. Nell'esempio sopra è stato selezionato lo slider ‘A’. Se ci sono più slider, usa il menu a tendina per selezionare quello corretto.

**ESEMPIO**

.. note::

    * Puoi scrivere il programma seguendo l'immagine seguente, fai riferimento al tutorial: :ref:`ezblock:create_project_latest`.
    * Oppure trova il codice con lo stesso nome nella pagina **Esempi** di EzBlock Studio e clicca direttamente su **Esegui** o **Modifica**.

.. image:: img/sp210512_155406.png
