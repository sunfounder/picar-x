.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Profundiza más en Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirte?**

    - **Soporte Experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y Comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos Exclusivos**: Accede anticipadamente a anuncios de nuevos productos y adelantos.
    - **Descuentos Especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones Festivas y Sorteos**: Participa en sorteos y promociones de temporada.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy.

.. _py_computer_vision:

7. Visión por Computadora
=========================

¡Este proyecto te introducirá oficialmente en el campo de la visión por computadora!

**Ejecuta el Código**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 7.computer_vision.py

**Ver la Imagen**

Después de ejecutar el código, el terminal mostrará el siguiente mensaje:

.. code-block::

    No desktop !
    * Serving Flask app "vilib.vilib" (lazy loading)
    * Environment: production
    WARNING: Do not use the development server in a production environment.
    Use a production WSGI server instead.
    * Debug mode: off
    * Running on http://0.0.0.0:9000/ (Press CTRL+C to quit)

Luego puedes ingresar ``http://<your IP>:9000/mjpg`` en el navegador para ver la pantalla de video, por ejemplo: ``https://192.168.18.113:9000/mjpg``

.. image:: img/display.png


Al finalizar el programa, verás la siguiente información:


* ¡Presiona una tecla para activar la función!
* q: Tomar foto
* 1: Detectar color: rojo
* 2: Detectar color: naranja
* 3: Detectar color: amarillo
* 4: Detectar color: verde
* 5: Detectar color: azul
* 6: Detectar color: púrpura
* 0: Apagar detección de color
* r: Escanear código QR
* f: Activar/Desactivar detección facial
* s: Mostrar información del objeto detectado

Sigue las indicaciones para activar las funciones correspondientes.

    *  **Tomar Foto**

        Escribe ``q`` en el terminal y presiona Enter. La imagen actual vista por la cámara se guardará (si la función de detección de color está activada, también aparecerá el cuadro de marca en la imagen guardada). 
        Puedes ver estas fotos en el directorio ``/home/{username}/Pictures/`` de tu Raspberry Pi.
        Puedes usar herramientas como :ref:`filezilla` para transferir las fotos a tu PC.
        

    *  **Detección de Color**

        Ingresar un número entre ``1~6`` detectará uno de los colores: "rojo, naranja, amarillo, verde, azul, púrpura". Ingresar ``0`` apagará la detección de color.

        .. image:: img/DTC2.png

        .. note:: Puedes descargar e imprimir las :download:`Tarjetas de Colores en PDF <https://github.com/sunfounder/sf-pdf/raw/master/prop_card/object_detection/color-cards.pdf>` para la detección de colores.


    *  **Detección Facial**

        Escribe ``f`` para activar la detección facial.

        .. image:: img/DTC5.png

    *  **Detección de Código QR**

        Ingresar ``r`` abrirá el reconocimiento del código QR. No se podrán realizar otras operaciones antes de que el código QR sea reconocido. La información decodificada del código QR se imprimirá en el terminal.

        .. image:: img/DTC4.png

    *  **Mostrar Información**

        Ingresar ``s`` imprimirá la información del objetivo detectado (detección facial y detección de color) en el terminal, incluyendo las coordenadas del centro (X, Y) y el tamaño (Ancho, Alto) del objeto detectado.


**Código**

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
            # leer tecla
            key = readchar.readkey()
            key = key.lower()
            # tomar foto
            if key == 'q':
                take_photo()
            # detección de color
            elif key != '' and key in ('0123456'):
                index = int(key)
                if index == 0:
                    flag_color = False
                    Vilib.color_detect('close')
                else:
                    flag_color = True
                    Vilib.color_detect(color_list[index])
                print('Color detect : %s'%color_list[index])
            # detección facial
            elif key =="f":
                flag_face = not flag_face
                face_detect(flag_face)
            # detección de código QR
            elif key =="r":
                qr_code_flag = not qr_code_flag
                if qr_code_flag == True:
                    if qrcode_thread == None or not qrcode_thread.is_alive():
                        qrcode_thread = threading.Thread(target=qrcode_detect)
                        qrcode_thread.setDaemon(True)
                        qrcode_thread.start()
                else:
                    if qrcode_thread != None and qrcode_thread.is_alive():
                        qrcode_thread.join()
                        print('QRcode Detect: close')
            # mostrar información del objeto detectado
            elif key == "s":
                object_show()

            sleep(0.5)


    if __name__ == "__main__":
        main()

**¿Cómo funciona?**

Lo primero a lo que debes prestar atención es a la siguiente función. Estas dos funciones te permiten iniciar la cámara.

.. code-block:: python

    Vilib.camera_start()
    Vilib.display()

Funciones relacionadas con "detección de objetos":

* ``Vilib.face_detect_switch(True)`` : Activar/Desactivar detección facial
* ``Vilib.color_detect(color)`` : Para la detección de colores, solo se puede realizar una detección a la vez. Los parámetros que se pueden ingresar son: ``"red"``, ``"orange"``, ``"yellow"``, ``"green"``, ``"blue"``, ``"purple"``
* ``Vilib.color_detect_switch(False)`` : Apagar la detección de color
* ``Vilib.qrcode_detect_switch(False)`` : Activar/Desactivar la detección de códigos QR, devuelve los datos decodificados del código QR.
* ``Vilib.gesture_detect_switch(False)`` : Activar/Desactivar la detección de gestos
* ``Vilib.traffic_sign_detect_switch(False)`` : Activar/Desactivar la detección de señales de tráfico

La información detectada por el objetivo se almacenará en el diccionario ``detect_obj_parameter = Manager().dict()``.

En el programa principal, puedes usarlo de esta manera:

.. code-block:: python

    Vilib.detect_obj_parameter['color_x']

Las claves del diccionario y sus usos se muestran en la siguiente lista:

* ``color_x``: el valor x de la coordenada central del bloque de color detectado, el rango es 0~320
* ``color_y``: el valor y de la coordenada central del bloque de color detectado, el rango es 0~240
* ``color_w``: el ancho del bloque de color detectado, el rango es 0~320
* ``color_h``: la altura del bloque de color detectado, el rango es 0~240
* ``color_n``: el número de parches de color detectados
* ``human_x``: el valor x de la coordenada central del rostro humano detectado, el rango es 0~320
* ``human_y``: el valor y de la coordenada central del rostro detectado, el rango es 0~240
* ``human_w``: el ancho del rostro humano detectado, el rango es 0~320
* ``human_h``: la altura del rostro humano detectado, el rango es 0~240
* ``human_n``: el número de rostros detectados
* ``traffic_sign_x``: el valor x de la coordenada central de la señal de tráfico detectada, el rango es 0~320
* ``traffic_sign_y``: el valor y de la coordenada central de la señal de tráfico detectada, el rango es 0~240
* ``traffic_sign_w``: el ancho de la señal de tráfico detectada, el rango es 0~320
* ``traffic_sign_h``: la altura de la señal de tráfico detectada, el rango es 0~240
* ``traffic_sign_t``: el contenido de la señal de tráfico detectada, la lista de valores es `['stop','right','left','forward']`
* ``gesture_x``: el valor x de la coordenada central del gesto detectado, el rango es 0~320
* ``gesture_y``: el valor y de la coordenada central del gesto detectado, el rango es 0~240
* ``gesture_w``: el ancho del gesto detectado, el rango es 0~320
* ``gesture_h``: la altura del gesto detectado, el rango es 0~240
* ``gesture_t``: el contenido del gesto detectado, la lista de valores es `["paper","scissor","rock"]`
* ``qr_date``: el contenido del código QR detectado
* ``qr_x``: el valor x de la coordenada central del código QR detectado, el rango es 0~320
* ``qr_y``: el valor y de la coordenada central del código QR detectado, el rango es 0~240
* ``qr_w``: el ancho del código QR detectado, el rango es 0~320
* ``qr_h``: la altura del código QR detectado, el rango es 0~320