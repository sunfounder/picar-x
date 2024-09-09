.. note::

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. ¡Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 junto con otros entusiastas!

    **¿Por qué unirte?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones especiales.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy.

.. _py_treasure:

12. Búsqueda del Tesoro
============================

Organiza un laberinto en tu habitación y coloca seis tarjetas de colores diferentes en seis esquinas. ¡Luego controla el PiCar-X para buscar estas tarjetas de colores una por una!

.. note:: Puedes descargar e imprimir las :download:`Tarjetas de Colores en PDF <https://github.com/sunfounder/sf-pdf/raw/master/prop_card/object_detection/color-cards.pdf>` para la detección de colores.

**Ejecutar el Código**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 12.treasure_hunt.py

**Ver la Imagen**

Después de ejecutar el código, el terminal mostrará el siguiente mensaje:

.. code-block::

    ¡No hay escritorio!
    * Sirviendo la aplicación Flask "vilib.vilib" (carga perezosa)
    * Entorno: producción
    ADVERTENCIA: No utilices el servidor de desarrollo en un entorno de producción.
    Usa un servidor WSGI de producción en su lugar.
    * Modo de depuración: desactivado
    * Ejecutando en http://0.0.0.0:9000/ (Presiona CTRL+C para salir)

Luego puedes ingresar ``http://<your IP>:9000/mjpg`` en el navegador para ver la pantalla de video, por ejemplo:  ``http://192.168.18.113:9000/mjpg``

.. image:: img/display.png

**Código**

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

**¿Cómo funciona?**

Para entender la lógica básica de este código, puedes concentrarte en las siguientes partes clave:

1. **Inicialización e Importaciones:**
   Las declaraciones de importación al comienzo del código te permiten entender las bibliotecas que se están utilizando.

2. **Variables globales:**
   Definiciones de variables globales, como ``color`` y ``key``, que se utilizan a lo largo del código para rastrear el color objetivo y la entrada del teclado.

3. ``renew_color_detect()`` :
   Esta función selecciona un color aleatorio de una lista y lo establece como el color objetivo para la detección. También utiliza la conversión de texto a voz para anunciar el color seleccionado.

4. ``key_scan_thread()`` :
   Esta función se ejecuta en un hilo separado y escanea continuamente la entrada del teclado, actualizando la variable ``key`` con la tecla presionada. Utiliza un bloqueo para garantizar el acceso seguro entre hilos.

5. ``car_move(key)`` :
   Esta función controla el movimiento del PiCar-X basado en la entrada del teclado (``key``). Establece la dirección y la velocidad del movimiento del robot.

6. ``main()`` : La función principal que organiza la lógica general del código. Realiza las siguientes acciones:

    * Inicializa la cámara y comienza a mostrar la transmisión de la cámara.
    * Crea un hilo separado para escanear la entrada del teclado.
    * Anuncia el inicio del juego utilizando la conversión de texto a voz.
    * Entra en un bucle continuo para:

        * Verificar si se han detectado objetos de color y activar acciones cuando se detecta un objeto válido.
        * Manejar la entrada del teclado para controlar el robot e interactuar con el juego.
    * Gestiona la salida del juego y las excepciones, como KeyboardInterrupt.
    * Asegura que la cámara se cierre y el PiCar-X se detenga al salir.

Al comprender estas partes clave del código, 
puedes captar la lógica fundamental de cómo el robot PiCar-X responde a la entrada del teclado y detecta e interactúa con objetos de un color específico usando la cámara y las capacidades de salida de audio.
