.. note::

    Ciao, benvenuto nella community di appassionati di SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Ottieni accesso anticipato ai nuovi annunci di prodotto e anteprime esclusive.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa a promozioni e omaggi durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _py_computer_vision:

7. Visione artificiale
=========================

Questo progetto ci introduce ufficialmente nel campo della visione artificiale!

**Esegui il Codice**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 7.display.py

**Visualizza l'immagine**

Dopo l'esecuzione del codice, il terminale visualizzerà il seguente messaggio:

.. code-block::

    No desktop !
    * Serving Flask app "vilib.vilib" (lazy loading)
    * Environment: production
    WARNING: Do not use the development server in a production environment.
    Use a production WSGI server instead.
    * Debug mode: off
    * Running on http://0.0.0.0:9000/ (Press CTRL+C to quit)

A questo punto puoi inserire ``http://<your IP>:9000/mjpg`` nel browser per visualizzare lo streaming video, ad esempio: ``https://192.168.18.113:9000/mjpg``

.. image:: img/display.png

Dopo l'esecuzione del programma, vedrai le seguenti informazioni finali:

* Digita un tasto per richiamare la funzione!
* q: Scatta foto
* 1: Rilevamento colore: rosso
* 2: Rilevamento colore: arancione
* 3: Rilevamento colore: giallo
* 4: Rilevamento colore: verde
* 5: Rilevamento colore: blu
* 6: Rilevamento colore: viola
* 0: Disattiva rilevamento colore
* r: Scansiona il codice QR
* f: Attiva/Disattiva rilevamento facciale
* s: Visualizza informazioni sull'oggetto rilevato

Segui le istruzioni per attivare le funzioni corrispondenti.

    *  **Scatta Foto**

        Digita ``q`` nel terminale e premi Invio. L'immagine attualmente visualizzata dalla fotocamera verrà salvata (se il rilevamento del colore è attivato, il riquadro di rilevamento apparirà anche nell'immagine salvata).
        Puoi visualizzare queste foto nella directory ``/home/{username}/Pictures/`` del Raspberry Pi.
        Puoi utilizzare strumenti come :ref:`filezilla` per trasferire le foto sul tuo PC.

    *  **Rilevamento Colore**

        Inserire un numero compreso tra ``1~6`` rileverà uno dei colori tra "rosso, arancione, giallo, verde, blu, viola". Inserisci ``0`` per disattivare il rilevamento del colore.

        .. image:: img/DTC2.png

        .. note:: You can download and print the :download:`PDF Color Cards <https://github.com/sunfounder/sf-pdf/raw/master/prop_card/object_detection/color-cards.pdf>` for color detection.

    *  **Rilevamento Facciale**

        Digita ``f`` per attivare il rilevamento facciale.

        .. image:: img/DTC5.png

    *  **Rilevamento Codice QR**

        Inserisci ``r`` per avviare il riconoscimento del codice QR. Non sarà possibile eseguire altre operazioni prima che il codice QR sia stato riconosciuto. Le informazioni decodificate del codice QR verranno stampate nel terminale.

        .. image:: img/DTC4.png

    *  **Visualizza Informazioni**

        Inserendo ``s`` verranno visualizzate le informazioni sul target del rilevamento facciale (e del rilevamento del colore) nel terminale. Inclusi le coordinate centrali (X, Y) e le dimensioni (larghezza, altezza) dell'oggetto rilevato.

**Codice** 

.. code-block:: python

    from pydoc import text
    from vilib import Vilib
    from time import sleep, time, strftime, localtime
    import threading
    import readchar
    import os

    flag_face = False
    flag_color = False
    qr_code_flag = False

    manual = '''
    Input key to call the function!
        q: Take photo
        1: Color detect : red
        2: Color detect : orange
        3: Color detect : yellow
        4: Color detect : green
        5: Color detect : blue
        6: Color detect : purple
        0: Switch off Color detect
        r: Scan the QR code
        f: Switch ON/OFF face detect
        s: Display detected object information
    '''

    color_list = ['close', 'red', 'orange', 'yellow',
            'green', 'blue', 'purple',
    ]

    def face_detect(flag):
        print("Face Detect:" + str(flag))
        Vilib.face_detect_switch(flag)


    def qrcode_detect():
        global qr_code_flag
        if qr_code_flag == True:
            Vilib.qrcode_detect_switch(True)
            print("Waitting for QR code")

        text = None
        while True:
            temp = Vilib.detect_obj_parameter['qr_data']
            if temp != "None" and temp != text:
                text = temp
                print('QR code:%s'%text)
            if qr_code_flag == False:
                break
            sleep(0.5)
        Vilib.qrcode_detect_switch(False)


    def take_photo():
        _time = strftime('%Y-%m-%d-%H-%M-%S',localtime(time()))
        name = 'photo_%s'%_time
        username = os.getlogin()

        path = f"/home/{username}/Pictures/"
        Vilib.take_photo(name, path)
        print('photo save as %s%s.jpg'%(path,name))


    def object_show():
        global flag_color, flag_face

        if flag_color is True:
            if Vilib.detect_obj_parameter['color_n'] == 0:
                print('Color Detect: None')
            else:
                color_coodinate = (Vilib.detect_obj_parameter['color_x'],Vilib.detect_obj_parameter['color_y'])
                color_size = (Vilib.detect_obj_parameter['color_w'],Vilib.detect_obj_parameter['color_h'])
                print("[Color Detect] ","Coordinate:",color_coodinate,"Size",color_size)

        if flag_face is True:
            if Vilib.detect_obj_parameter['human_n'] == 0:
                print('Face Detect: None')
            else:
                human_coodinate = (Vilib.detect_obj_parameter['human_x'],Vilib.detect_obj_parameter['human_y'])
                human_size = (Vilib.detect_obj_parameter['human_w'],Vilib.detect_obj_parameter['human_h'])
                print("[Face Detect] ","Coordinate:",human_coodinate,"Size",human_size)


    def main():
        global flag_face, flag_color, qr_code_flag
        qrcode_thread = None

        Vilib.camera_start(vflip=False,hflip=False)
        Vilib.display(local=True,web=True)
        print(manual)

        while True:
            # lettura tasto
            key = readchar.readkey()
            key = key.lower()
            # scatta foto
            if key == 'q':
                take_photo()
            # rilevamento colore
            elif key != '' and key in ('0123456'):  # '' in ('0123') -> True
                index = int(key)
                if index == 0:
                    flag_color = False
                    Vilib.color_detect('close')
                else:
                    flag_color = True
                    Vilib.color_detect(color_list[index]) # rileva_colore(colore:str -> nome_colore/chiudi)
                print('Color detect : %s'%color_list[index])
            # rilevamento facciale
            elif key =="f":
                flag_face = not flag_face
                face_detect(flag_face)
            # rilevamento QR code
            elif key =="r":
                qr_code_flag = not qr_code_flag
                if qr_code_flag == True:
                    if qrcode_thread == None o non qrcode_thread.is_alive():
                        qrcode_thread = threading.Thread(target=qrcode_detect)
                        qrcode_thread.setDaemon(True)
                        qrcode_thread.start()
                else:
                    if qrcode_thread != None e qrcode_thread.is_alive():
                    # attende la fine del thread
                        qrcode_thread.join()
                        print('QRcode Detect: close')
            # mostra informazioni sull'oggetto rilevato
            elif key == "s":
                object_show()

            sleep(0.5)


    if __name__ == "__main__":
        main()

**Come funziona?**

La prima cosa a cui devi prestare attenzione è la seguente funzione. Queste due funzioni permettono di avviare la fotocamera.

.. code-block:: python

    Vilib.camera_start()
    Vilib.display()

Funzioni relative al "rilevamento degli oggetti":

* ``Vilib.face_detect_switch(True)`` : Attiva/Disattiva il rilevamento facciale
* ``Vilib.color_detect(color)`` : Per il rilevamento del colore, può essere eseguito un solo rilevamento colore alla volta. I parametri che possono essere inseriti sono: ``"red"``, ``"orange"``, ``"yellow"``, ``"green"``, ``"blue"``, ``"purple"``
* ``Vilib.color_detect_switch(False)`` : Disattiva il rilevamento del colore
* ``Vilib.qrcode_detect_switch(False)`` : Attiva/Disattiva il rilevamento dei codici QR, restituendo i dati decodificati del QR code.
* ``Vilib.gesture_detect_switch(False)`` : Attiva/Disattiva il rilevamento dei gesti
* ``Vilib.traffic_sign_detect_switch(False)`` : Attiva/Disattiva il rilevamento dei segnali stradali

Le informazioni rilevate dall'oggetto saranno memorizzate nel dizionario ``detect_obj_parameter = Manager().dict()``.

Nel programma principale, puoi usarlo così:

.. code-block:: python

    Vilib.detect_obj_parameter['color_x']

Le chiavi del dizionario e i loro utilizzi sono mostrati nella seguente lista:

* ``color_x``: il valore x della coordinata centrale del blocco di colore rilevato, l'intervallo è 0~320
* ``color_y``: il valore y della coordinata centrale del blocco di colore rilevato, l'intervallo è 0~240
* ``color_w``: la larghezza del blocco di colore rilevato, l'intervallo è 0~320
* ``color_h``: l'altezza del blocco di colore rilevato, l'intervallo è 0~240
* ``color_n``: il numero di blocchi di colore rilevati
* ``human_x``: il valore x della coordinata centrale del volto umano rilevato, l'intervallo è 0~320
* ``human_y``: il valore y della coordinata centrale del volto rilevato, l'intervallo è 0~240
* ``human_w``: la larghezza del volto umano rilevato, l'intervallo è 0~320
* ``human_h``: l'altezza del volto umano rilevato, l'intervallo è 0~240
* ``human_n``: il numero di volti rilevati
* ``traffic_sign_x``: il valore della coordinata x del segnale stradale rilevato, l'intervallo è 0~320
* ``traffic_sign_y``: il valore della coordinata y del segnale stradale rilevato, l'intervallo è 0~240
* ``traffic_sign_w``: la larghezza del segnale stradale rilevato, l'intervallo è 0~320
* ``traffic_sign_h``: l'altezza del segnale stradale rilevato, l'intervallo è 0~240
* ``traffic_sign_t``: il contenuto del segnale stradale rilevato, la lista dei valori è `['stop','right','left','forward']`
* ``gesture_x``: Il valore della coordinata x del gesto rilevato, l'intervallo è 0~320
* ``gesture_y``: Il valore della coordinata y del gesto rilevato, l'intervallo è 0~240
* ``gesture_w``: La larghezza del gesto rilevato, l'intervallo è 0~320
* ``gesture_h``: L'altezza del gesto rilevato, l'intervallo è 0~240
* ``gesture_t``: Il contenuto del gesto rilevato, la lista dei valori è `["paper","scissor","rock"]`
* ``qr_date``: il contenuto del codice QR rilevato
* ``qr_x``: il valore della coordinata x del codice QR da rilevare, l'intervallo è 0~320
* ``qr_y``: il valore della coordinata y del codice QR da rilevare, l'intervallo è 0~240
* ``qr_w``: la larghezza del codice QR da rilevare, l'intervallo è 0~320
* ``qr_h``: l'altezza del codice QR da rilevare, l'intervallo è 0~320
