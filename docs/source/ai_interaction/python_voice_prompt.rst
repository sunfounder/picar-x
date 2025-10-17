.. note::

    Hola, ¡bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook! Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirte?**

    - **Soporte de expertos**: Resuelve problemas post-venta y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y avances exclusivos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

14. Coche con Indicaciones de Voz usando Espeak y Pico2Wave
=============================================================

En esta lección usaremos dos motores de texto a voz (TTS) integrados en Raspberry Pi — **Espeak** y **Pico2Wave** — para hacer que el PiCar-X hable.  

Estos dos motores son sencillos y funcionan sin conexión, pero suenan bastante diferentes:

* **Espeak**: muy ligero y rápido, pero con voz robótica. Puedes ajustar la velocidad, el tono y el volumen.  
* **Pico2Wave**: produce una voz más suave y natural que Espeak, pero con menos opciones de configuración.  

Escucharás la diferencia en **calidad de voz** y **funcionalidades**, y luego construirás un “coche con indicaciones de voz” que anuncia sus acciones antes de moverse.  

----

1. Probar Espeak
--------------------

Espeak es un motor TTS ligero incluido en Raspberry Pi OS.  
Su voz suena robótica, pero es altamente configurable: puedes ajustar el volumen, el tono, la velocidad y más.  

**Pasos para probarlo**:

* Crea un nuevo archivo con el comando:

  .. code-block:: bash
  
      cd ~/picar-x/example
      sudo nano test_tts_espeak.py

* Luego copia el código de ejemplo en él. Pulsa ``Ctrl+X``, luego ``Y`` y finalmente ``Enter`` para guardar y salir.

  .. code-block:: python
  
      from picarx.tts import Espeak

      tts = Espeak()
  
      # Quick hello (sanity check)
      tts.say("Hello! I'm Espeak TTS.")
  
      # Optional voice tuning
      # tts.set_amp(100)   # 0 to 200
      # tts.set_speed(150) # 80 to 260
      # tts.set_gap(5)     # 0 to 200
      # tts.set_pitch(50)  # 0 to 99
* Ejecuta el programa con:

  .. code-block:: bash

     sudo python3 test_tts_espeak.py

* Deberías escuchar al PiCar-X decir: “Hello! I'm Espeak TTS.”  
* Descomenta las líneas de ajuste de voz en el código para experimentar cómo ``amp``, ``speed``, ``gap`` y ``pitch`` afectan al sonido.

----

2. Probar Pico2Wave
---------------------

Pico2Wave produce una voz más natural y humana que Espeak.  
Es más sencillo de usar pero menos flexible: solo puedes cambiar el idioma, no el tono ni la velocidad.

**Pasos para probarlo**:

* Crea un nuevo archivo con el comando:

  .. code-block:: bash

      cd ~/picar-x/example
      sudo nano test_tts_pico2wave.py

* Luego copia el código de ejemplo en él. Pulsa ``Ctrl+X``, luego ``Y`` y finalmente ``Enter`` para guardar y salir.

  .. code-block:: python
  
      from picarx.tts import Pico2Wave

      tts = Pico2Wave()
  
      tts.set_lang('en-US')  # en-US, en-GB, de-DE, es-ES, fr-FR, it-IT
  
      # Saludo rápido (prueba básica)
      tts.say("Hello! I'm Pico2Wave TTS.")

* Ejecuta el programa con:

  .. code-block:: bash

     sudo python3 test_tts_pico2wave.py

* Deberías escuchar al PiCar-X decir: “Hello! I'm Pico2Wave TTS.”  
* Prueba cambiando el idioma (por ejemplo, ``es-ES`` para español) y escucha la diferencia.

----

3. Coche con Indicaciones de Voz
--------------------------------------

Ahora combinemos **Pico2Wave** o **Espeak** con el código de conducción de PiCar-X para crear un “coche con indicaciones de voz”:  
antes de cada acción, el coche anunciará lo que está a punto de hacer.

**Ejecutar el Código**

.. code-block:: bash

    cd ~/picar-x/example
    sudo python3 14.voice_promt_car.py

Ejecuta este código y verás que tu PiCar-X avanza, retrocede y gira, anunciando cada movimiento antes de hacerlo.  
Esto hace que tu coche sea más seguro, amigable e interactivo.

**Código**

.. code-block:: python

  from picarx import Picarx
  from picarx.tts import Espeak
  import time

  # If you want to try Pico2Wave instead of Espeak, uncomment below:
  # from picarx.tts import Pico2Wave
  # tts = Pico2Wave()
  # tts.set_lang('en-US')  # Options: en-US, en-GB, de-DE, es-ES, fr-FR, it-IT

  px = Picarx()
  tts = Espeak()

  # Quick hello (test)
  tts.say("Hello! I'm PiCar-X.")

  def main():
      try:
          # Forward
          tts.say("Moving forward")
          px.forward(30)
          time.sleep(2)
          px.stop()

          # Backward
          tts.say("Moving backward")
          px.backward(30)
          time.sleep(2)
          px.stop()

          # Turn left
          tts.say("Turning left")
          px.set_dir_servo_angle(-20)
          px.forward(30)
          time.sleep(2)
          px.stop()
          px.set_dir_servo_angle(0)

          # Turn right
          tts.say("Turning right")
          px.set_dir_servo_angle(20)
          px.forward(30)
          time.sleep(2)
          px.stop()
          px.set_dir_servo_angle(0)

      except KeyboardInterrupt:
          # Stop if interrupted
          px.stop()
      finally:
          # Reset to safe state
          px.stop()
          px.set_dir_servo_angle(0)

  if __name__ == "__main__":
      main()

----

Solución de Problemas
--------------------------------

* **Sin sonido al ejecutar Espeak o Pico2Wave**

  * Verifica que tus altavoces/auriculares estén conectados y que el volumen no esté silenciado.  
  * Ejecuta una prueba rápida en la terminal:

    .. code-block:: bash

       espeak "Hello world"
       pico2wave -w test.wav "Hello world" && aplay test.wav

  Si no escuchas nada, el problema está en la salida de audio, no en tu código Python.

* **La voz de Espeak suena demasiado rápida o robótica**

  * Prueba ajustando los parámetros en tu código:

    .. code-block:: python

       tts.set_speed(120)   # más lento
       tts.set_pitch(60)    # diferente tono

* **Permiso denegado al ejecutar el código**

  * Prueba ejecutar con ``sudo``:

    .. code-block:: bash

       sudo python3 test_tts_espeak.py


Comparación: Espeak vs Pico2Wave
-------------------------------------

.. list-table::
   :widths: 20 40 40
   :header-rows: 1

   * - Característica
     - Espeak
     - Pico2Wave
   * - Calidad de voz
     - Robótica, sintética
     - Más natural, parecida a la humana
   * - Idiomas
     - Inglés por defecto
     - Menos, pero comunes
   * - Ajustable
     - Sí (velocidad, tono, etc.)
     - No (solo idioma)
   * - Rendimiento
     - Muy rápido y ligero
     - Un poco más lento y pesado


