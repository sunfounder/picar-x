.. note::

    Ciao, benvenuto nella community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto Esperti**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara & Condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato a nuovi annunci di prodotti e anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a concorsi e promozioni durante le festività.

    👉 Pronto per esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _py_video:

9. Registra Video
==================

Questo esempio ti guiderà nell'utilizzo della funzione di registrazione.

**Esegui il Codice**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 9.record_video.py


Dopo aver eseguito il codice, puoi inserire ``http://<tuo IP>:9000/mjpg`` nel browser per visualizzare lo schermo video. Ad esempio:  ``http://192.168.18.113:9000/mjpg``

.. image:: img/display.png

La registrazione può essere avviata o interrotta premendo i tasti sulla tastiera.

* Premi ``q`` per avviare la registrazione o mettere in pausa/continuare, ``e`` per fermare o salvare la registrazione.
* Se desideri uscire dal programma, premi ``ctrl+c``.


**Codice** 

.. code-block:: python

    from time import sleep,strftime,localtime
    from vilib import Vilib
    import readchar
    import os

    manual = '''
    Press keys on keyboard to control recording:
        Q: record/pause/continue
        E: stop
        Ctrl + C: Quit
    '''

    def print_overwrite(msg,  end='', flush=True):
        print('\r\033[2K', end='',flush=True)
        print(msg, end=end, flush=True)

    def main():
        rec_flag = 'stop' # start,pause,stop
        vname = None
        username = os.getlogin()
        
        Vilib.rec_video_set["path"] = f"/home/{username}/Videos/" # imposta il percorso

        Vilib.camera_start(vflip=False,hflip=False)
        Vilib.display(local=True,web=True)
        sleep(0.8)  # attesa avvio

        print(manual)
        while True:
            # leggi la tastiera
            key = readchar.readkey()
            key = key.lower()
            # avvia/pausa
            if key == 'q':
                key = None
                if rec_flag == 'stop':
                    rec_flag = 'start'
                    # imposta nome
                    vname = strftime("%Y-%m-%d-%H.%M.%S", localtime())
                    Vilib.rec_video_set["name"] = vname
                    # avvia registrazione
                    Vilib.rec_video_run()
                    Vilib.rec_video_start()
                    print_overwrite('rec start ...')
                elif rec_flag == 'start':
                    rec_flag = 'pause'
                    Vilib.rec_video_pause()
                    print_overwrite('pause')
                elif rec_flag == 'pause':
                    rec_flag = 'start'
                    Vilib.rec_video_start()
                    print_overwrite('continue')
            # ferma
            elif key == 'e' and rec_flag != 'stop':
                key = None
                rec_flag = 'stop'
                Vilib.rec_video_stop()
                print_overwrite("The video saved as %s%s.avi"%(Vilib.rec_video_set["path"],vname),end='\n')
            # esci
            elif key == readchar.key.CTRL_C:
                Vilib.camera_close()
                print('\nquit')
                break

            sleep(0.1)

    if __name__ == "__main__":
        main()

**Come funziona?**


Le funzioni relative alla registrazione includono quanto segue:


* ``Vilib.rec_video_run(video_name)`` : Avvia il thread per registrare il video. ``video_name`` è il nome del file video, deve essere una stringa.
* ``Vilib.rec_video_start()``: Avvia o continua la registrazione video.
* ``Vilib.rec_video_pause()``: Mette in pausa la registrazione.
* ``Vilib.rec_video_stop()``: Interrompe la registrazione.

``Vilib.rec_video_set["path"] = f"/home/{username}/Videos/"`` imposta la posizione di archiviazione dei file video.
