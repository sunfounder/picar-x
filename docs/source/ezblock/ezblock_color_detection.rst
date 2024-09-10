.. note::

    Ciao, benvenuto nella SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e Condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Giveaway Festivi**: Partecipa a promozioni e concorsi durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

Rilevamento dei Colori
===========================

Il PiCar-X è un'auto a guida autonoma dotata di una fotocamera integrata, che consente ai programmi Ezblock di utilizzare il codice per il rilevamento degli oggetti e il riconoscimento dei colori. In questa sezione, Ezblock verrà utilizzato per creare un programma di rilevamento dei colori.

.. note::

    Prima di iniziare questa sezione, assicurati che il cavo FFC della fotocamera Raspberry Pi sia collegato correttamente e in modo sicuro. Per istruzioni dettagliate su come collegare correttamente il cavo FCC, fai riferimento a: :ref:`assembly_instructions`.

In questo programma, Ezblock riceverà prima l'intervallo di spazio di Tonalità-Saturazione-Valore (HSV) del colore da rilevare, quindi utilizzerà OpenCV per elaborare i colori nell'intervallo HSV per eliminare il rumore di fondo e, infine, inquadrare il colore corrispondente.

Ezblock include 6 modelli di colore per il PiCar-X: "rosso", "arancione", "giallo", "verde", "blu" e "viola". Le schede colore sono state preparate nel PDF seguente e dovranno essere stampate con una stampante a colori.

* :download:`[PDF]Color Cards <https://github.com/sunfounder/sf-pdf/raw/master/prop_card/object_detection/color-cards.pdf>`

.. image:: img/color_card.png
    :width: 600

.. note::

    I colori stampati possono avere una tonalità leggermente diversa rispetto ai modelli di colore di Ezblock a causa delle differenze nel toner della stampante o del supporto di stampa, come una carta di colore marrone chiaro. Questo può causare un riconoscimento dei colori meno preciso.

.. image:: img/ezblock_color_detect.PNG

**CONSIGLI**

.. image:: img/sp210512_121105.png

Trascina il widget Video dalla pagina di Controllo Remoto, e verrà generato un monitor video. Per maggiori informazioni su come utilizzare il widget Video, fai riferimento al tutorial sui video Ezblock qui: :ref:`ezblock:video_latest`.

.. image:: img/sp210512_121125.png

Abilita il monitor video impostando il blocco **camera monitor** su **on**. Nota: impostando il **camera monitor** su **off** si chiuderà il monitor, ma il rilevamento degli oggetti sarà comunque disponibile.

.. image:: img/sp210512_134133.png

Usa il blocco **color detection** per abilitare il rilevamento dei colori. Nota: può essere rilevato solo un colore alla volta.

**ESEMPIO**

.. note::

    * Puoi scrivere il programma seguendo l'immagine qui sotto, fai riferimento al tutorial: :ref:`ezblock:create_project_latest`.
    * Oppure trova il codice con lo stesso nome nella pagina **Esempi** di EzBlock Studio e clicca direttamente su **Esegui** o **Modifica**.

.. image:: img/sp210512_134636.png
