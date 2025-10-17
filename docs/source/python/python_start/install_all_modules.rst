.. note::

    Ciao, benvenuto nella SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e Condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e alle anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Giveaway Festivi**: Partecipa a promozioni e concorsi durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _install_all_modules:

5. Installare tutti i moduli (Importante)
========================================

Assicurati di essere connesso a Internet e aggiorna il sistema:

.. raw:: html

    <run></run>

.. code-block::

    sudo apt update
    sudo apt upgrade

.. note::

    I pacchetti relativi a Python3 devono essere installati se stai installando la versione Lite del sistema operativo.

    .. raw:: html

        <run></run>

    .. code-block::
    
        sudo apt install git python3-pip python3-setuptools python3-smbus


Installa ``robot-hat``.

.. raw:: html

    <run></run>

.. code-block::

    cd ~/
    git clone -b 2.5.x https://github.com/sunfounder/robot-hat.git --depth 1
    cd robot-hat
    sudo python3 install.py


Quindi scarica e installa il modulo ``vilib``.

.. raw:: html

    <run></run>

.. code-block::

    cd ~/
    git clone -b picamera2 https://github.com/sunfounder/vilib.git --depth 1
    cd vilib
    sudo python3 install.py

Scarica e installa il modulo ``picar-x``.

.. raw:: html

    <run></run>

.. code-block::

    cd ~/
    git clone -b 2.1.x https://github.com/sunfounder/picar-x.git --depth 1
    cd picar-x
    sudo pip3 install . --break

Questo passaggio richiederà un po’ di tempo, quindi sii paziente.

Infine, è necessario eseguire lo script ``i2samp.sh`` per installare i componenti richiesti dall’amplificatore i2s, altrimenti il picar-x non avrà audio.

.. raw:: html

    <run></run>

.. code-block::

    cd ~/robot-hat
    sudo bash i2samp.sh
	
.. image:: img/i2s.png

Digita ``y`` e premi invio per continuare l’esecuzione dello script.

.. image:: img/i2s2.png

Digita ``y`` e premi invio per eseguire ``/dev/zero`` in background.

.. image:: img/i2s3.png

Digita ``y`` e premi invio per riavviare il Picar-X.

.. note::
    Se non c’è audio dopo il riavvio, potrebbe essere necessario eseguire lo script i2samp.sh più volte.
