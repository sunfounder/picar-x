.. note::

    Ciao, benvenuto nella community di appassionati di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato ai nuovi annunci di prodotto e anteprime esclusive.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa a promozioni e omaggi durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _install_all_modules:


Installare Tutti i Moduli (Importante)
=========================================

#. **Preparare il sistema**

   Assicurati che il tuo Raspberry Pi sia connesso a Internet, quindi aggiorna il sistema:

   .. raw:: html

      <run></run>

   .. code-block::

      sudo apt update
      sudo apt upgrade

   .. note::
      
      Se stai utilizzando Raspberry Pi OS Lite, installa prima i pacchetti Python 3 richiesti:

   .. raw:: html

      <run></run>

   .. code-block::

         sudo apt install git python3-pip python3-setuptools python3-smbus

#. **Installare robot-hat**

   Scarica e installa il modulo ``robot-hat``:

   .. raw:: html

      <run></run>

   .. code-block::

      cd ~/
      git clone -b 2.5.x https://github.com/sunfounder/robot-hat.git --depth 1
      cd robot-hat
      sudo python3 install.py

#. **Installare vilib**

   Scarica e installa il modulo ``vilib``:

   .. raw:: html

      <run></run>

   .. code-block::

      cd ~/
      git clone https://github.com/sunfounder/vilib.git --depth 1
      cd vilib
      sudo python3 install.py

#. **Installare picar-x**

   Scarica e installa il modulo ``picar-x``:

   .. raw:: html

      <run></run>

   .. code-block::

      cd ~/
      git clone -b 2.1.x https://github.com/sunfounder/picar-x.git --depth 1
      cd picar-x
      sudo pip3 install . --break

   Questo passaggio potrebbe richiedere un po’ di tempo. Ti preghiamo di essere paziente.

#. **Abilitare l’audio (amplificatore I2S)**

   Per abilitare l’uscita audio, esegui lo script ``i2samp.sh`` per installare i componenti necessari dell’amplificatore I2S:

   .. raw:: html

      <run></run>

   .. code-block::

      cd ~/robot-hat
      sudo bash i2samp.sh

   Segui le istruzioni visualizzate sullo schermo digitando ``y`` e premendo Invio per continuare, esegui ``/dev/zero`` in background e riavvia il Picar-X.

   .. note::
      Se dopo il riavvio non c’è alcun suono, prova a eseguire lo script ``i2samp.sh`` più volte.
