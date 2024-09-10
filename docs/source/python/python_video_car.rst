.. note::

    Ciao, benvenuto nella Community di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti?**

    - **Supporto Esperti**: Risolvi i problemi post-vendita e le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara & Condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato ai nuovi annunci di prodotti e anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a concorsi e promozioni durante le festività.

    👉 Pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi!

.. _video_car:

11. Video Car
==========================================

Questo programma ti offrirà una visione in prima persona dal PiCar-X! 
Usa i tasti WSAD della tastiera per controllare la direzione di movimento, 
e i tasti O e P per regolare la velocità.

**Esegui il Codice**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 11.video_car.py

Una volta eseguito il codice, puoi vedere cosa sta riprendendo PiCar-X e controllarlo premendo i seguenti tasti:

* O: aumenta la velocità
* P: diminuisci la velocità
* W: avanti  
* S: indietro
* A: gira a sinistra
* D: gira a destra
* F: ferma
* T: scatta foto
* Ctrl+C: esci

**Visualizza l'Immagine**

Dopo l'esecuzione del codice, il terminale mostrerà il seguente prompt:

.. code-block::

    No desktop !
    * Serving Flask app "vilib.vilib" (lazy loading)
    * Environment: production
    WARNING: Do not use the development server in a production environment.
    Use a production WSGI server instead.
    * Debug mode: off
    * Running on http://0.0.0.0:9000/ (Press CTRL+C to quit)

Puoi quindi inserire ``http://<your IP>:9000/mjpg`` nel browser per visualizzare lo schermo video, ad esempio:  ``https://192.168.18.113:9000/mjpg``

.. image:: img/display.png


**Codice**

.. code-block:: python
    
    #!/usr/bin/env python3

    from robot_hat.utils import reset_mcu
    from picarx import Picarx
    from vilib import Vilib
    from time import sleep, time, strftime, localtime
    import readchar

    import os
    user = os.getlogin()
    user_home = os.path.expanduser(f'~{user}')

    reset_mcu()
    sleep(0.2)

    manual = '''
    Press key to call the function(non-case sensitive):

        O: speed up
        P: speed down
        W: forward  
        S: backward
        A: turn left
        D: turn right
        F: stop
        T: take photo

        Ctrl+C: quit
    '''


    px = Picarx()

    def take_photo():
        _time = strftime('%Y-%m-%d-%H-%M-%S',localtime(time()))
        name = 'photo_%s'%_time
        path = f"{user_home}/Pictures/picar-x/"
        Vilib.take_photo(name, path)
        print('\nphoto save as %s%s.jpg'%(path,name))


    def move(operate:str, speed):

        if operate == 'stop':
            px.stop()  
        else:
            if operate == 'forward':
                px.set_dir_servo_angle(0)
                px.forward(speed)
            elif operate == 'backward':
                px.set_dir_servo_angle(0)
                px.backward(speed)
            elif operate == 'turn left':
                px.set_dir_servo_angle(-30)
                px.forward(speed)
            elif operate == 'turn right':
                px.set_dir_servo_angle(30)
                px.forward(speed)
            


    def main():
        speed = 0
        status = 'stop'

        Vilib.camera_start(vflip=False,hflip=False)
        Vilib.display(local=True,web=True)
        sleep(2)  # attendi l'avvio
        print(manual)
        
        while True:
            print("\rstatus: %s , speed: %s    "%(status, speed), end='', flush=True)
            # readkey
            key = readchar.readkey().lower()
            # operazione 
            if key in ('wsadfop'):
                # accelerazione
                if key == 'o':
                    if speed <=90:
                        speed += 10           
                elif key == 'p':
                    if speed >=10:
                        speed -= 10
                    if speed == 0:
                        status = 'stop'
                # direzione
                elif key in ('wsad'):
                    if speed == 0:
                        speed = 10
                    if key == 'w':
                        # Limite di velocità in retromarcia, per evitare un corrente eccessivo
                        if status != 'forward' and speed > 60:  
                            speed = 60
                        status = 'forward'
                    elif key == 'a':
                        status = 'turn left'
                    elif key == 's':
                        if status != 'backward' and speed > 60: # Speed limit when reversing
                            speed = 60
                        status = 'backward'
                    elif key == 'd':
                        status = 'turn right' 
                # stop
                elif key == 'f':
                    status = 'stop'
                # move 
                move(status, speed)  
            # take photo
            elif key == 't':
                take_photo()
            # quit
            elif key == readchar.key.CTRL_C:
                print('\nquit ...')
                px.stop()
                Vilib.camera_close()
                break 

            sleep(0.1)


    if __name__ == "__main__":
        try:
            main()
        except Exception as e:    
            print("error:%s"%e)
        finally:
            px.stop()
            Vilib.camera_close()

