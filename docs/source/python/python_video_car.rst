.. note::

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. ¡Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 junto con otros entusiastas!

    **¿Por qué unirte?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones especiales.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy.

.. _video_car:

11. Coche con Video
==========================================

¡Este programa te proporcionará una Vista en Primera Persona desde el PiCar-X! 
Usa las teclas WSAD del teclado para controlar la dirección del movimiento, 
y las teclas O y P para ajustar la velocidad.

**Ejecutar el Código**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 11.video_car.py

Una vez que el código esté en ejecución, podrás ver lo que PiCar-X está grabando y controlarlo presionando las siguientes teclas.

* O: aumentar velocidad
* P: disminuir velocidad
* W: avanzar  
* S: retroceder
* A: girar a la izquierda
* D: girar a la derecha
* F: detenerse
* T: tomar foto
* Ctrl+C: salir

**Ver la Imagen**

Después de ejecutar el código, el terminal mostrará el siguiente mensaje:

.. code-block::

    ¡No hay escritorio!
    * Sirviendo la aplicación Flask "vilib.vilib" (carga perezosa)
    * Entorno: producción
    ADVERTENCIA: No utilices el servidor de desarrollo en un entorno de producción.
    Usa un servidor WSGI de producción.
    * Modo de depuración: desactivado
    * Ejecutando en http://0.0.0.0:9000/ (Presiona CTRL+C para salir)

Luego puedes ingresar ``http://<tu IP>:9000/mjpg`` en el navegador para ver la pantalla de video, por ejemplo:  ``https://192.168.18.113:9000/mjpg``

.. image:: img/display.png


**Código**

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
        sleep(2)  # espera a que arranque
        print(manual)
        
        while True:
             print("\rstatus: %s , speed: %s    "%(status, speed), end='', flush=True)
            # leer tecla
            key = readchar.readkey().lower()
            # operación 
            if key in ('wsadfop'):
                # aceleración
                if key == 'o':
                    if speed <=90:
                        speed += 10           
                elif key == 'p':
                    if speed >=10:
                        speed -= 10
                    if speed == 0:
                        status = 'stop'
                # dirección
                elif key in ('wsad'):
                    if speed == 0:
                        speed = 10
                    if key == 'w':
                        # Límite de velocidad al retroceder, evitar corrientes instantáneas demasiado altas
                        if status != 'forward' and speed > 60:  
                            speed = 60
                        status = 'forward'
                    elif key == 'a':
                        status = 'turn left'
                    elif key == 's':
                        if status != 'backward' and speed > 60: # Límite de velocidad al retroceder
                            speed = 60
                        status = 'backward'
                    elif key == 'd':
                        status = 'turn right' 
                # detener
                elif key == 'f':
                    status = 'stop'
                # mover
                move(status, speed)  
            # tomar foto
            elif key == 't':
                take_photo()
            # salir
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

