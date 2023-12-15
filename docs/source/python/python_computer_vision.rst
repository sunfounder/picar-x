.. _py_computer_vision:

7. Computervision
=======================

Dieses Projekt wird offiziell in das Feld der Computervision eintreten!

**Code ausführen**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 7.display.py

**Das Bild betrachten**

Nachdem der Code ausgeführt wurde, wird im Terminal folgende Aufforderung angezeigt:

.. code-block::

    No desktop !
    * Serving Flask app "vilib.vilib" (lazy loading)
    * Environment: production
    WARNING: Do not use the development server in a production environment.
    Use a production WSGI server instead.
    * Debug mode: off
    * Running on http://0.0.0.0:9000/ (Press CTRL+C to quit)

Dann können Sie ``http://<Ihre IP>:9000/mjpg`` im Browser eingeben, um den Videobildschirm zu betrachten, wie z. B.:  ``https://192.168.18.113:9000/mjpg``

.. image:: img/display.png


Nachdem das Programm ausgeführt wurde, sehen Sie folgende Informationen am Ende:


* Taste drücken, um die Funktion aufzurufen!
* q: Foto machen
* 1: Farberkennung : rot
* 2: Farberkennung : orange
* 3: Farberkennung : gelb
* 4: Farberkennung : grün
* 5: Farberkennung : blau
* 6: Farberkennung : lila
* 0: Farberkennung ausschalten
* r: QR-Code scannen
* f: Gesichtserkennung EIN/AUS schalten
* s: Informationen über erkannte Objekte anzeigen

Bitte folgen Sie den Aufforderungen, um die entsprechenden Funktionen zu aktivieren.

    *  **Foto machen**

        Geben Sie im Terminal ``q`` ein und drücken Sie Enter. Das von der Kamera aktuell gesehene Bild wird gespeichert (wenn die Farberkennungsfunktion eingeschaltet ist, wird auch die Markierungsbox im gespeicherten Bild angezeigt). 
        Diese Fotos können Sie im Verzeichnis ``/home/{username}/Pictures/`` des Raspberry Pi sehen.
        Sie können Tools wie :ref:`filezilla` verwenden, um Fotos auf Ihren PC zu übertragen.
        

    *  **Farberkennung**

        Durch Eingabe einer Zahl zwischen ``1~6`` wird eine der Farben „rot, orange, gelb, grün, blau, lila“ erkannt. Geben Sie ``0`` ein, um die Farberkennung auszuschalten.

        .. image:: img/DTC2.png

        .. note:: Sie können die :download:`PDF-Farbkarten <https://github.com/sunfounder/sf-pdf/raw/master/prop_card/object_detection/color-cards.pdf>` für die Farberkennung herunterladen und ausdrucken.


    *  **Gesichtserkennung**

        Geben Sie ``f`` ein, um die Gesichtserkennung einzuschalten.

        .. image:: img/DTC5.png

    *  **QR-Code-Erkennung**

        Geben Sie ``r`` ein, um die QR-Code-Erkennung zu öffnen. Vor der Erkennung des QR-Codes können keine anderen Operationen durchgeführt werden. Die Dekodierungsinformationen des QR-Codes werden im Terminal gedruckt.

        .. image:: img/DTC4.png

    *  **Informationen anzeigen**

        Durch Eingabe von ``s`` werden die Informationen des Gesichtserkennungs- (und Farberkennungs-) Ziels im Terminal gedruckt. Einschließlich der Mittelkoordinaten (X, Y) und Größe (Breite, Höhe) des gemessenen Objekts.


**Code** 

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
            # readkey
            key = readchar.readkey()
            key = key.lower()
            # take photo
            if key == 'q':
                take_photo()
            # color detect
            elif key != '' and key in ('0123456'):  # '' in ('0123') -> True
                index = int(key)
                if index == 0:
                    flag_color = False
                    Vilib.color_detect('close')
                else:
                    flag_color = True
                    Vilib.color_detect(color_list[index]) # color_detect(color:str -> color_name/close)
                print('Color detect : %s'%color_list[index])
            # face detection
            elif key =="f":
                flag_face = not flag_face
                face_detect(flag_face)
            # qrcode detection
            elif key =="r":
                qr_code_flag = not qr_code_flag
                if qr_code_flag == True:
                    if qrcode_thread == None or not qrcode_thread.is_alive():
                        qrcode_thread = threading.Thread(target=qrcode_detect)
                        qrcode_thread.setDaemon(True)
                        qrcode_thread.start()
                else:
                    if qrcode_thread != None and qrcode_thread.is_alive():
                    # wait for thread to end
                        qrcode_thread.join()
                        print('QRcode Detect: close')
            # show detected object information
            elif key == "s":
                object_show()

            sleep(0.5)


    if __name__ == "__main__":
        main()

**Wie funktioniert des?**

Das Erste, worauf Sie hier achten müssen, ist die folgende Funktion. Diese beiden Funktionen ermöglichen es Ihnen, die Kamera zu starten.

.. code-block:: python

    Vilib.camera_start()
    Vilib.display()

Funktionen, die mit „Objekterkennung“ zusammenhängen:

* ``Vilib.face_detect_switch(True)`` : Gesichtserkennung EIN/AUS schalten
* ``Vilib.color_detect(color)`` : Für die Farberkennung, es kann nur eine Farberkennung gleichzeitig durchgeführt werden. Die einführbaren Parameter sind: ``"rot"``, ``"orange"``, ``"gelb"``, ``"grün"``, ``"blau"``, ``"lila"``
* ``Vilib.color_detect_switch(False)`` : Farberkennung ausschalten
* ``Vilib.qrcode_detect_switch(False)`` : QR-Code-Erkennung EIN/AUS schalten, gibt die dekodierten Daten des QR-Codes zurück.
* ``Vilib.gesture_detect_switch(False)`` : Gestenerkennung EIN/AUS schalten
* ``Vilib.traffic_sign_detect_switch(False)`` : Verkehrszeichenerkennung EIN/AUS schalten

Die von dem Ziel erkannten Informationen werden im Wörterbuch ``detect_obj_parameter = Manager().dict()`` gespeichert.

Im Hauptprogramm können Sie es so verwenden:

.. code-block:: python

    Vilib.detect_obj_parameter['color_x']

Die Schlüssel des Wörterbuchs und deren Verwendungen werden in der folgenden Liste gezeigt:

* ``color_x``: der x-Wert der Mittelkoordinate des erkannten Farbblocks, der Bereich ist 0~320
* ``color_y``: der y-Wert der Mittelkoordinate des erkannten Farbblocks, der Bereich ist 0~240
* ``color_w``: die Breite des erkannten Farbblocks, der Bereich ist 0~320
* ``color_h``: die Höhe des erkannten Farbblocks, der Bereich ist 0~240
* ``color_n``: die Anzahl der erkannten Farbflecken
* ``human_x``: der x-Wert der Mittelkoordinate des erkannten menschlichen Gesichts, der Bereich ist 0~320
* ``human_y``: der y-Wert der Mittelkoordinate des erkannten Gesichts, der Bereich ist 0~240
* ``human_w``: die Breite des erkannten menschlichen Gesichts, der Bereich ist 0~320
* ``human_h``: die Höhe des erkannten Gesichts, der Bereich ist 0~240
* ``human_n``: die Anzahl der erkannten Gesichter
* ``traffic_sign_x``: der Mittelkoordinaten-x-Wert des erkannten Verkehrszeichens, der Bereich ist 0~320
* ``traffic_sign_y``: der Mittelkoordinaten-y-Wert des erkannten Verkehrszeichens, der Bereich ist 0~240
* ``traffic_sign_w``: die Breite des erkannten Verkehrszeichens, der Bereich ist 0~320
* ``traffic_sign_h``: die Höhe des erkannten Verkehrszeichens, der Bereich ist 0~240
* ``traffic_sign_t``: der Inhalt des erkannten Verkehrszeichens, die Werteliste ist `['stop','right','left','forward']`
* ``gesture_x``: Der Mittelkoordinaten-x-Wert der erkannten Geste, der Bereich ist 0~320
* ``gesture_y``: Der Mittelkoordinaten-y-Wert der erkannten Geste, der Bereich ist 0~240
* ``gesture_w``: Die Breite der erkannten Geste, der Bereich ist 0~320
* ``gesture_h``: Die Höhe der erkannten Geste, der Bereich ist 0~240
* ``gesture_t``: Der Inhalt der erkannten Geste, die Werteliste ist `["paper","scissor","rock"]`
* ``qr_date``: der Inhalt des erkannten QR-Codes
* ``qr_x``: der Mittelkoordinaten-x-Wert des zu erkennenden QR-Codes, der Bereich ist 0~320
* ``qr_y``: der Mittelkoordinaten-y-Wert des zu erkennenden QR-Codes, der Bereich ist 0~240
* ``qr_w``: die Breite des zu erkennenden QR-Codes, der Bereich ist 0~320
* ``qr_h``: die Höhe des zu erkennenden QR-Codes, der Bereich ist 0~320
