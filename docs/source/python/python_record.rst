.. note::

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. ¡Profundiza en el mundo de Raspberry Pi, Arduino y ESP32 junto con otros entusiastas!

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones especiales.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy.

.. _py_video:

9. Grabar Video
===============

Este ejemplo te guiará en cómo utilizar la función de grabación.

**Ejecutar el Código**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 9.record_video.py


Después de ejecutar el código, puedes ingresar ``http://<your IP>:9000/mjpg`` en el navegador para ver la pantalla de video, por ejemplo: ``http://192.168.18.113:9000/mjpg``

.. image:: img/display.png

La grabación se puede detener o iniciar presionando las teclas en el teclado.

* Presiona ``q`` para comenzar a grabar o pausar/continuar, y ``e`` para detener la grabación o guardar.
* Si deseas salir del programa, presiona ``ctrl+c``.


**Código** 

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
        
        Vilib.rec_video_set["path"] = f"/home/{username}/Videos/" # establecer la ruta

        Vilib.camera_start(vflip=False,hflip=False)
        Vilib.display(local=True,web=True)
        sleep(0.8)  # esperar el arranque

        print(manual)
        while True:
            # leer el teclado
            key = readchar.readkey()
            key = key.lower()
            # iniciar/pausar
            if key == 'q':
                key = None
                if rec_flag == 'stop':
                    rec_flag = 'start'
                    # establecer nombre
                    vname = strftime("%Y-%m-%d-%H.%M.%S", localtime())
                    Vilib.rec_video_set["name"] = vname
                    # iniciar grabación
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
            # detener
            elif key == 'e' and rec_flag != 'stop':
                key = None
                rec_flag = 'stop'
                Vilib.rec_video_stop()
                print_overwrite("The video saved as %s%s.avi"%(Vilib.rec_video_set["path"],vname),end='\n')
            # salir
            elif key == readchar.key.CTRL_C:
                Vilib.camera_close()
                print('\nquit')
                break

            sleep(0.1)

    if __name__ == "__main__":
        main()

**¿Cómo funciona?**

Las funciones relacionadas con la grabación incluyen las siguientes:

* ``Vilib.rec_video_run(video_name)`` : Inicia el hilo para grabar el video. ``video_name`` es el nombre del archivo de video, debe ser una cadena de texto.
* ``Vilib.rec_video_start()``: Iniciar o continuar la grabación de video.
* ``Vilib.rec_video_pause()``: Pausar la grabación.
* ``Vilib.rec_video_stop()``: Detener la grabación.

``Vilib.rec_video_set["path"] = f"/home/{username}/Videos/"`` establece la ubicación de almacenamiento de los archivos de video.