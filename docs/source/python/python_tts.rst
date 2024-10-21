.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti?**

    - **Supporto Esperti**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara & Condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato ai nuovi annunci di prodotti e anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a concorsi e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi!

.. _py_tts:

3. Sintesi Vocale & Effetti Sonori
=========================================

In questo esempio utilizziamo gli effetti sonori di PiCar-X (più precisamente del Robot HAT).
È composto da tre parti: Musica, Suoni, Sintesi Vocale.


**Installa i2samp**

Prima di utilizzare le funzioni di Sintesi Vocale (TTS) e degli Effetti Sonori,
attiva l'altoparlante in modo che possa emettere suoni.

Esegui ``i2samp.sh`` nella cartella **picar-x**,
questo script installerà tutto il necessario per usare l'amplificatore i2s.

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x
    sudo bash i2samp.sh 

.. image:: img/tt_bash.png

Ci saranno diversi messaggi che chiederanno di confermare le richieste. Rispondi a tutti con **Y**. Dopo aver apportato le modifiche al sistema Raspberry Pi, sarà necessario riavviare il computer affinché le modifiche abbiano effetto.

Dopo il riavvio, esegui nuovamente lo script ``i2samp.sh`` per testare l'amplificatore. Se un suono viene riprodotto con successo dall'altoparlante, la configurazione è completata.

**Esegui il Codice**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 3.tts_example.py
    
Dopo l'esecuzione del codice, segui le istruzioni stampate nel terminale.

Input da tastiera per richiamare la funzione!

    * space: Riproduci effetto sonoro (Clacson dell'auto)
    * c: Riproduci effetto sonoro in thread
    * t: Sintesi vocale (Di' Ciao)
    * q: Riproduci/Interrompi Musica

**Codice**

.. code-block:: python

    from time import sleep
    from robot_hat import Music,TTS
    import readchar

    music = Music()
    tts = TTS()

    manual = '''
    Input key to call the function!
        space: Play sound effect (Car horn)
        c: Play sound effect with threads
        t: Text to speak
        q: Play/Stop Music
    '''

    def main():
        print(manual)

        flag_bgm = False
        music.music_set_volume(20)
        tts.lang("en-US")

        while True:
            key = readchar.readkey()
            key = key.lower()
            if key == "q":
                flag_bgm = not flag_bgm
                if flag_bgm is True:
                    music.music_play('../musics/slow-trail-Ahjay_Stelino.mp3')
                else:
                    music.music_stop()

            elif key == readchar.key.SPACE:
                music.sound_play('../sounds/car-double-horn.wav')
                sleep(0.05)

            elif key == "c":
                music.sound_play_threading('../sounds/car-double-horn.wav')
                sleep(0.05)

            elif key == "t":
                words = "Hello"
                tts.say(words)

    if __name__ == "__main__":
        main()

**Come funziona?**

Le funzioni relative alla musica di sottofondo includono:

* ``music = Music()`` : Dichiara l'oggetto.
* ``music.music_set_volume(20)`` : Imposta il volume, il range è 0~100.
* ``music.music_play('../musics/slow-trail-Ahjay_Stelino.mp3')`` : Riproduci il file musicale, in questo caso il file **slow-trail-Ahjay_Stelino.mp3** nella cartella ``../musics``.
* ``music.music_stop()`` : Interrompi la riproduzione della musica di sottofondo.

.. note::

    Puoi aggiungere diversi effetti sonori o musica nella cartella ``musics`` o ``sounds`` tramite :ref:`filezilla`.

Le funzioni relative agli effetti sonori includono:

* ``music = Music()``
* ``music.sound_play('../sounds/car-double-horn.wav')`` : Riproduci il file degli effetti sonori.
* ``music.sound_play_threading('../sounds/car-double-horn.wav')`` : Riproduci il file degli effetti sonori in modalità threading senza sospendere il thread principale.

Il software `eSpeak <http://espeak.sourceforge.net/>`_ è utilizzato per implementare le funzioni di Sintesi Vocale (TTS).

Importa il modulo TTS in robot_hat, che incapsula le funzioni per convertire il testo in voce.

Le funzioni relative alla Sintesi Vocale includono:

* ``tts = TTS()``
* ``tts.say(words)`` : Sintesi vocale del testo.
* ``tts.lang("en-US")`` : Imposta la lingua.

.. note:: 

    Imposta la lingua con i parametri di ``lang("")`` usando i seguenti caratteri.

.. list-table:: Language
    :widths: 15 50

    *   - zh-CN 
        - Mandarino (Cinese)
    *   - en-US 
        - Inglese-Stati Uniti
    *   - en-GB     
        - Inglese-Regno Unito
    *   - de-DE     
        - Tedesco-Deutsch
    *   - es-ES     
        - Spagna-Spagnolo
    *   - fr-FR  
        - Francia-Francese
    *   - it-IT  
        - Italia-Italiano
