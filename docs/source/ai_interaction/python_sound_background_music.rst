.. note::

    Ciao, benvenuto nella SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community su Facebook! Scopri di più su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e Condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Accedi in anteprima agli annunci di nuovi prodotti e alle anticipazioni.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Giveaway Festivi**: Partecipa a giveaway e promozioni in occasione delle festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _py_tts:

13. Riprodurre Musica ed Effetti Sonori
===============================================

In questo progetto imparerai a far riprodurre al PiCar-X musica di sottofondo o effetti sonori. Puoi anche riprodurre file musicali che hai già salvato.


**Esegui il Codice**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 13.sound_background_music.py
    
Dopo l’avvio del codice, segui le istruzioni visualizzate nel terminale.

Premi un tasto per richiamare la funzione!

    * space: Riproduci effetto sonoro (Clacson auto)
    * c: Riproduci effetto sonoro con thread
    * q: Avvia/Arresta Musica

**Codice**

.. code-block:: python

    from time import sleep
    from picarx.music import Music
    import readchar

    music = Music()

    manual = '''
    Input key to call the function!
        space: Play sound effect (Car horn)
        c: Play sound effect with threads
        q: Play/Stop Music
    '''

    def main():
        print(manual)

        flag_bgm = False
        music.music_set_volume(20)


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


    if __name__ == "__main__":
        main()

**Come funziona?**

Le funzioni relative alla musica di sottofondo includono:

* ``music = Music()`` : Dichiara l’oggetto.
* ``music.music_set_volume(20)`` : Imposta il volume, con un intervallo da 0 a 100.
* ``music.music_play('../musics/slow-trail-Ahjay_Stelino.mp3')`` : Riproduce un file musicale, in questo caso **slow-trail-Ahjay_Stelino.mp3** nella cartella ``../musics``.
* ``music.music_stop()`` : Interrompe la riproduzione della musica di sottofondo.

.. note::

    Puoi aggiungere diversi effetti sonori o file musicali nelle cartelle ``musics`` o ``sounds`` tramite :ref:`filezilla`.
