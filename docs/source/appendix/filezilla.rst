.. note::

    Ciao, benvenuto nella SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community su Facebook! Scopri di più su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e Condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Accedi in anteprima agli annunci di nuovi prodotti e alle anticipazioni.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Giveaway Festivi**: Partecipa a giveaway e promozioni in occasione delle festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _filezilla:

Software Filezilla
==========================

.. image:: img/filezilla_icon.png

Il File Transfer Protocol (FTP) è un protocollo di comunicazione standard utilizzato per il trasferimento di file da un server a un client su una rete informatica.

Filezilla è un software open source che supporta non solo FTP, ma anche FTP su TLS (FTPS) e SFTP. Possiamo utilizzare Filezilla per caricare file locali (come immagini e audio, ecc.) sul Raspberry Pi, o scaricare file dal Raspberry Pi al computer locale.

**Passo 1**: Scarica Filezilla.

Scarica il client dal `Filezilla’s official website <https://filezilla-project.org/>`_, Filezilla ha un ottimo tutorial, fai riferimento a: `Documentazione - Filezilla <https://wiki.filezilla-project.org/Documentation>`_.

**Passo 2**: Connetti al Raspberry Pi

Dopo una rapida installazione, apri il programma e `connect it to an FTP server <https://wiki.filezilla-project.org/Using#Connecting_to_an_FTP_server>`_. Esistono 3 modi per connettersi, qui utilizziamo la barra **Connessione Rapida**. Inserisci il **nome host/IP**, **nome utente**, **password** e **porta (22)**, quindi clicca su **Connessione Rapida** o premi **Invio** per connetterti al server.

.. image:: img/filezilla_connect.png

.. note::

    Connessione Rapida è un buon modo per testare le tue credenziali di accesso. Se vuoi creare una connessione permanente, puoi selezionare **File**-> **Copia Connessione Corrente nel Gestore Siti** dopo una Connessione Rapida riuscita, inserisci il nome e clicca **OK**. La prossima volta potrai connetterti selezionando il sito salvato in precedenza all'interno di **File** -> **Gestore Siti**.

    .. image:: img/ftp_site.png

**Passo 3**: Carica/scarica file.

Puoi caricare file locali sul Raspberry Pi trascinandoli e rilasciandoli, o scaricare i file dal Raspberry Pi al tuo computer locale.

.. image:: img/upload_ftp.png

