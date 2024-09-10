.. note::

    Ciao, benvenuto nella SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community su Facebook! Approfondisci Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirsi?**

    - **Supporto Esperti**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara & Condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato a nuove annunci di prodotti e anteprime.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Giveaway**: Partecipa a promozioni festive e concorsi.

    👉 Pronto per esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _py_keyboard_control:

2. Controllo tramite Tastiera
================================


In questo progetto, impareremo come utilizzare la tastiera per controllare da remoto il PiCar-X. 
Puoi controllare PiCar-X per avanzare, retrocedere, girare a sinistra e a destra.

**Esegui il Codice**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 2.keyboard_control.py

Premi i tasti sulla tastiera per controllare PiCar-X!

    * w: Avanti 
    * a: Gira a sinistra 
    * s: Indietro 
    * d: Gira a destra
    * i: Alza la testa
    * k: Abbassa la testa
    * j: Gira la testa a sinistra
    * l: Gira la testa a destra     
    * ctrl + c: Premilo due volte per uscire dal programma

**Codice**

.. code-block:: python

    from picarx import Picarx
    from time import sleep
    import readchar

    manual = '''
    Press keys on keyboard to control PiCar-X!
        w: Forward
        a: Turn left
        s: Backward
        d: Turn right
        i: Head up
        k: Head down
        j: Turn head left
        l: Turn head right
        ctrl+c: Quit
    '''

    def show_info():
        print("\033[H\033[J",end='')  # clear terminal windows
        print(manual)


    if __name__ == "__main__":
        try:
            pan_angle = 0
            tilt_angle = 0
            px = Picarx()
            show_info()
            while True:
                key = readchar.readkey()
                key = key.lower()
                if key in('wsadikjl'): 
                    if 'w' == key:
                        px.set_dir_servo_angle(0)
                        px.forward(80)
                    elif 's' == key:
                        px.set_dir_servo_angle(0)
                        px.backward(80)
                    elif 'a' == key:
                        px.set_dir_servo_angle(-35)
                        px.forward(80)
                    elif 'd' == key:
                        px.set_dir_servo_angle(35)
                        px.forward(80)
                    elif 'i' == key:
                        tilt_angle+=5
                        if tilt_angle>35:
                            tilt_angle=35
                    elif 'k' == key:
                        tilt_angle-=5
                        if tilt_angle<-35:
                            tilt_angle=-35
                    elif 'l' == key:
                        pan_angle+=5
                        if pan_angle>35:
                            pan_angle=35
                    elif 'j' == key:
                        pan_angle-=5
                        if pan_angle<-35:
                            pan_angle=-35                 

                    px.set_cam_tilt_angle(tilt_angle)
                    px.set_cam_pan_angle(pan_angle)      
                    show_info()                     
                    sleep(0.5)
                    px.forward(0)
            
                elif key == readchar.key.CTRL_C:
                    print("\n Quit")
                    break

        finally:
            px.set_cam_tilt_angle(0)
            px.set_cam_pan_angle(0)  
            px.set_dir_servo_angle(0)  
            px.stop()
            sleep(.2)


**Come funziona?**

PiCar-X dovrebbe eseguire azioni appropriate in base ai caratteri letti dalla tastiera.
La funzione ``lower()`` converte i caratteri maiuscoli in minuscoli, in modo che la 
lettera resti valida indipendentemente dal caso.

.. code-block:: python

    while True:
        key = readchar.readkey()
        key = key.lower()
        if key in('wsadikjl'): 
            if 'w' == key:
                pass
            elif 's' == key:
                pass
            elif 'a' == key:
                pass
            elif 'd' == key:
                pass
            elif 'i' == key:
                pass
            elif 'k' == key:
                pass
            elif 'l' == key:
                pass
            elif 'j' == key:
                pass             
    
        elif key == readchar.key.CTRL_C:
            print("\n Quit")
            break
