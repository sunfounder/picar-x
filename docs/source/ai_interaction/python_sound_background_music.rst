.. note::

    Hola, ¡bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook! Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirte?**

    - **Soporte de expertos**: Resuelve problemas post-venta y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y avances exclusivos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _py_tts:

13. Reproducir Música y Efectos de Sonido
===========================================

En este proyecto, aprenderás a hacer que el PiCar-X reproduzca música de fondo o efectos de sonido. También puedes reproducir archivos de música que hayas almacenado.


**Ejecutar el Código**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 13.sound_background_music.py
    
Después de que el código se ejecute, por favor opera según el mensaje que se imprime en la terminal.

¡Presiona una tecla para llamar a la función!

    * space: Reproducir efecto de sonido (Bocina de coche)
    * c: Reproducir efecto de sonido con hilos
    * q: Reproducir/Detener música

**Código**


.. code-block:: python

    from time import sleep
    from picarx.music import Music
    import readchar

    music = Music()

    manual = '''
    Input key to call the function!
        space: Play sound effect (Car horn)
        c: Play sound effect with threads
        q: Play/Stop Music
    '''

    def main():
        print(manual)

        flag_bgm = False
        music.music_set_volume(20)


        while True:
            key = readchar.readkey()
            key = key.lower()
            if key == "q":
                flag_bgm = not flag_bgm
                if flag_bgm is True:
                    music.music_play('../musics/slow-trail-Ahjay_Stelino.mp3')
                else:
                    music.music_stop()

            elif key == readchar.key.SPACE:
                music.sound_play('../sounds/car-double-horn.wav')
                sleep(0.05)

            elif key == "c":
                music.sound_play_threading('../sounds/car-double-horn.wav')
                sleep(0.05)


    if __name__ == "__main__":
        main()
        
**¿Cómo funciona?**

Las funciones relacionadas con la música de fondo incluyen lo siguiente:

* ``music = Music()`` : Declara el objeto.
* ``music.music_set_volume(20)`` : Ajusta el volumen, el rango es de 0 a 100.
* ``music.music_play('../musics/slow-trail-Ahjay_Stelino.mp3')`` : Reproduce archivos de música, en este caso el archivo **slow-trail-Ahjay_Stelino.mp3** ubicado en la carpeta ``../musics``.
* ``music.music_stop()`` : Detiene la reproducción de la música de fondo.

.. note::

    Puedes agregar diferentes efectos de sonido o música a las carpetas ``musics`` o ``sounds`` mediante :ref:`filezilla`.
