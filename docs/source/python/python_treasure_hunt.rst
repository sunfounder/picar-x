.. note::

    Ciao, benvenuto nella community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto Esperti**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara & Condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato a nuovi annunci di prodotti e anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a concorsi e promozioni durante le festività.

    👉 Pronto per esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _py_treasure:

12. Caccia al Tesoro
============================

Organizza un labirinto nella tua stanza e posiziona sei carte di colori diversi in sei angoli. Poi controlla PiCar-X per cercare queste carte una alla volta!

.. note:: Puoi scaricare e stampare le :download:`PDF Color Cards <https://github.com/sunfounder/sf-pdf/raw/master/prop_card/object_detection/color-cards.pdf>` for color detection.

**Esegui il Codice**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 12.treasure_hunt.py

**Visualizza l'Immagine**

Dopo l'esecuzione del codice, il terminale mostrerà il seguente messaggio:

.. code-block::

    No desktop !
    * Serving Flask app "vilib.vilib" (lazy loading)
    * Environment: production
    WARNING: Do not use the development server in a production environment.
    Use a production WSGI server instead.
    * Debug mode: off
    * Running on http://0.0.0.0:9000/ (Press CTRL+C to quit)

Poi puoi inserire ``http://<your IP>:9000/mjpg`` nel browser per visualizzare il video, ad esempio:  ``http://192.168.18.113:9000/mjpg``

.. image:: img/display.png

**Codice**

.. code-block:: python

    from picarx import Picarx
    from time import sleep
    from robot_hat import Music,TTS
    from vilib import Vilib
    import readchar
    import random
    import threading
    
    px = Picarx()
    
    music = Music()
    tts = TTS()
    
    manual = '''
    Press keys on keyboard to control Picar-X!
        w: Forward
        a: Turn left
        s: Backward
        d: Turn right
        space: Say the target again
        ctrl+c: Quit
    '''
    
    color = "red"
    color_list=["red","orange","yellow","green","blue","purple"]
    
    def renew_color_detect():
        global color
        color = random.choice(color_list)
        Vilib.color_detect(color)
        tts.say("Look for " + color)
    
    key = None
    lock = threading.Lock()
    
    def key_scan_thread():
        global key
        while True:
            key_temp = readchar.readkey()
            print('\r',end='')
            with lock:
                key = key_temp.lower()
                if key == readchar.key.SPACE:
                    key = 'space'
                elif key == readchar.key.CTRL_C:
                    key = 'quit'
                    break
            sleep(0.01)
    
    def car_move(key):
        if 'w' == key:
            px.set_dir_servo_angle(0)
            px.forward(80)
        elif 's' == key:
            px.set_dir_servo_angle(0)
            px.backward(80)
        elif 'a' == key:
            px.set_dir_servo_angle(-30)
            px.forward(80)
        elif 'd' == key:
            px.set_dir_servo_angle(30)
            px.forward(80)
    
    def main():
        global key
        Vilib.camera_start(vflip=False,hflip=False)
        Vilib.display(local=False,web=True)
        sleep(0.8)
        print(manual)
    
        sleep(1)
        _key_t = threading.Thread(target=key_scan_thread)
        _key_t.setDaemon(True)
        _key_t.start()
    
        tts.say("game start")
        sleep(0.05)
        renew_color_detect()
        while True:
    
            if Vilib.detect_obj_parameter['color_n']!=0 and Vilib.detect_obj_parameter['color_w']>100:
                tts.say("will done")
                sleep(0.05)
                renew_color_detect()
    
            with lock:
                if key != None and key in ('wsad'):
                    car_move(key)
                    sleep(0.5)
                    px.stop()
                    key =  None
                elif key == 'space':
                    tts.say("Look for " + color)
                    key =  None
                elif key == 'quit':
                    _key_t.join()
                    print("\n\rQuit")
                    break
    
            sleep(0.05)
    
    if __name__ == "__main__":
        try:
            main()
        except KeyboardInterrupt:
            pass
        except Exception as e:
            print(f"ERROR: {e}")
        finally:
            Vilib.camera_close()
            px.stop()
            sleep(.2)


**Come funziona?**

Per comprendere la logica di base di questo codice, puoi concentrarti sulle seguenti parti chiave:

1. **Inizializzazione e Importazioni:**
   Le dichiarazioni di importazione all'inizio del codice mostrano le librerie utilizzate.

2. **Variabili Globali:**
   Le definizioni delle variabili globali, come ``color`` e ``key``, utilizzate per tracciare il colore target e l'input della tastiera.

3. ``renew_color_detect()`` :
   Questa funzione seleziona un colore casuale da una lista e lo imposta come colore target per il rilevamento. Utilizza anche il text-to-speech per annunciare il colore selezionato.

4. ``key_scan_thread()`` :
   Funzione eseguita in un thread separato per scansionare continuamente l'input della tastiera, aggiornando la variabile ``key`` con il tasto premuto.

5. ``car_move(key)`` :
   Funzione che controlla il movimento di PiCar-X in base all'input della tastiera (``key``). Imposta la direzione e la velocità del movimento del robot.

6. ``main()`` : Funzione principale che coordina la logica generale del codice. Include:

    * Inizializza la telecamera e avvia la visualizzazione.
    * Crea un thread separato per l'input della tastiera.
    * Annuncia l'inizio del gioco tramite text-to-speech.
    * Entra in un ciclo continuo per:

        * Controllare gli oggetti colorati rilevati e avviare azioni quando viene rilevato un oggetto valido.
        * Gestire l'input della tastiera per controllare il robot e interagire con il gioco.
    * Gestisce l'uscita dal gioco e le eccezioni come KeyboardInterrupt.
    * Assicura che la telecamera venga chiusa e che PiCar-X si fermi all'uscita.

Comprendendo queste parti chiave del codice, puoi capire come il robot PiCar-X 
risponde all'input della tastiera e rileva e interagisce con oggetti di un colore 
specifico utilizzando la telecamera e le capacità audio.
