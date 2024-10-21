.. note::

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. ¡Profundiza en el mundo de Raspberry Pi, Arduino y ESP32 junto con otros entusiastas!

    **¿Por qué unirte?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones especiales.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy.

.. _py_tts:

3. Texto a Voz y Efectos de Sonido
=========================================

En este ejemplo, usamos los efectos de sonido de PiCar-X (o más específicamente, de Robot HAT). 
Consiste en tres partes: Música, Sonido y Texto a Voz.


**Instalar i2samp**

Antes de usar las funciones de Texto a Voz (TTS) y los Efectos de Sonido, 
primero activa el altavoz para que esté habilitado y pueda emitir sonidos.

Ejecuta ``i2samp.sh`` en la carpeta **picar-x**, 
y este script instalará todo lo necesario para usar el amplificador i2s.

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x
    sudo bash i2samp.sh 

.. image:: img/tt_bash.png

Habrá varios mensajes pidiendo confirmar la solicitud. Responde a todos los mensajes con un **Y**. Después de que se hayan realizado los cambios en el sistema de Raspberry Pi, será necesario reiniciar el equipo para que los cambios surtan efecto.

Después de reiniciar, ejecuta nuevamente el script ``i2samp.sh`` para probar el amplificador. Si se reproduce sonido correctamente desde el altavoz, la configuración estará completa.

**Ejecutar el Código**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 3.tts_example.py
    
Después de ejecutar el código, sigue las instrucciones que se imprimirán en el terminal.

¡Introduce una tecla para llamar a la función!

    * espacio: Reproducir efecto de sonido (Bocina de coche)
    * c: Reproducir efecto de sonido con hilos
    * t: Texto a decir (Decir Hola)
    * q: Reproducir/Detener música

**Código**

.. code-block:: python

    from time import sleep
    from robot_hat import Music,TTS
    import readchar

    music = Music()
    tts = TTS()

    manual = '''
    Introduce una tecla para llamar a la función:
        espacio: Reproducir efecto de sonido (Bocina de coche)
        c: Reproducir efecto de sonido con hilos
        t: Texto a decir
        q: Reproducir/Detener música
    '''

    def main():
        print(manual)

        flag_bgm = False
        music.music_set_volume(20)
        tts.lang("en-US")


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

            elif key == "t":
                words = "Hello"
                tts.say(words)

    if __name__ == "__main__":
        main()

**¿Cómo funciona?**

Las funciones relacionadas con la música de fondo incluyen:

* ``music = Music()`` : Declara el objeto.
* ``music.music_set_volume(20)`` : Ajusta el volumen, el rango es de 0~100.
* ``music.music_play('../musics/slow-trail-Ahjay_Stelino.mp3')`` : Reproduce archivos de música, en este caso el archivo **slow-trail-Ahjay_Stelino.mp3** que está en la ruta ``../musics``.
* ``music.music_stop()`` : Detiene la música de fondo.

.. note::

    Puedes agregar diferentes efectos de sonido o música a la carpeta ``musics`` o ``sounds`` mediante :ref:`filezilla`.

Las funciones relacionadas con los efectos de sonido incluyen:

* ``music = Music()``
* ``music.sound_play('../sounds/car-double-horn.wav')`` : Reproduce el archivo de efecto de sonido.
* ``music.sound_play_threading('../sounds/car-double-horn.wav')`` : Reproduce el archivo de efecto de sonido en un nuevo hilo sin suspender el hilo principal.

El software `eSpeak <http://espeak.sourceforge.net/>`_ se utiliza para implementar las funciones de TTS.

Importa el módulo TTS en robot_hat, que encapsula funciones que convierten texto en voz.

Las funciones relacionadas con Texto a Voz incluyen:

* ``tts = TTS()``
* ``tts.say(words)`` : Reproducción de texto en audio.
* ``tts.lang("en-US")`` :  Configura el idioma.

.. note:: 

    Configura el idioma utilizando los parámetros de ``lang("")`` con los siguientes caracteres.

.. list-table:: Idioma
    :widths: 15 50

    *   - zh-CN 
        - Mandarín (Chino)
    *   - en-US 
        - Inglés-Estados Unidos
    *   - en-GB     
        - Inglés-Reino Unido
    *   - de-DE     
        - Alemán-Deutsch
    *   - es-ES     
        - España-Español
    *   - fr-FR  
        - Francia-Francés
    *   - it-IT  
        - Italia-Italiano
