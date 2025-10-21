.. note::

    Hola, ¡bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook! Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirte?**

    - **Soporte de expertos**: Resuelve problemas post-venta y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y avances exclusivos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

15. Robot Narrador con IA usando Piper y OpenAI
========================================================

En la lección anterior, probamos dos motores TTS integrados en Raspberry Pi (**Espeak** y **Pico2Wave**).  
Ahora exploraremos dos opciones más potentes: **Piper** (offline, basado en redes neuronales) y **OpenAI TTS** (online, basado en la nube).

* **Piper**: un motor TTS local que funciona sin conexión en Raspberry Pi.  
* **OpenAI TTS**: un servicio en línea que proporciona voces muy naturales y parecidas a las humanas.  

Al final, tu PiCar-X conducirá y contará chistes como un pequeño narrador.  

Antes de Empezar
----------------

Asegúrate de haber completado:

* :ref:`install_all_modules` — Instala los módulos ``robot-hat``, ``vilib``, ``picar-x`` y luego ejecuta el script ``i2samp.sh``.

.. _test_piper:

1. Probar Piper
------------------

**Pasos para probarlo**:

#. Crea un nuevo archivo:

   .. code-block:: bash

      cd ~/picar-x/example
      sudo nano test_tts_piper.py

#. Copia el siguiente código de ejemplo en el archivo. Presiona ``Ctrl+X``, luego ``Y`` y finalmente ``Enter`` para guardar y salir.

   .. code-block:: python

       from picarx.tts import Piper

       tts = Piper()

       # Listar idiomas compatibles
       print(tts.available_countrys())

       # Listar modelos para inglés (en_us)
       print(tts.available_models('en_us'))

       # Establecer un modelo de voz (se descarga automáticamente si no está presente)
       tts.set_model("en_US-amy-low")

       # Decir algo
       tts.say("Hello! I'm Piper TTS.")

   * ``available_countrys()``: imprime los idiomas compatibles.  
   * ``available_models()``: lista los modelos disponibles para ese idioma.  
   * ``set_model()``: establece el modelo de voz (lo descarga automáticamente si falta).  
   * ``say()``: convierte texto a voz y lo reproduce.

#. Ejecuta el programa:

   .. code-block:: bash

      sudo python3 test_tts_piper.py

#. La primera vez que lo ejecutes, el modelo de voz seleccionado se descargará automáticamente. 

   * Luego deberías escuchar al PiCar-X decir: ``Hello! I'm Piper TTS.``

   * Puedes cambiar a otro modelo de idioma llamando a ``set_model()`` con un nombre diferente.

2. Probar OpenAI TTS
-------------------------------

**Obtener y guardar tu clave API**

#. Ve a |link_openai_platform| e inicia sesión. En la página de **API keys**, haz clic en **Create new secret key**.

   .. image:: img/llm_openai_create.png

#. Rellena los detalles (Owner, Name, Project y permisos si es necesario), luego haz clic en **Create secret key**.

   .. image:: img/llm_openai_create_confirm.png

#. Una vez creada la clave, cópiala de inmediato — no podrás verla nuevamente. Si la pierdes, deberás generar una nueva.

   .. image:: img/llm_openai_copy.png

#. En tu carpeta de proyecto (por ejemplo: ``/picar-x/example``), crea un archivo llamado ``secret.py``:

   .. code-block:: bash

       cd ~/picar-x/example
       sudo nano secret.py

#. Pega tu clave en el archivo de esta forma:

   .. code-block:: python

       # secret.py
       # Guarda secretos aquí. Nunca subas este archivo a Git.
       OPENAI_API_KEY = "sk-xxx"

**Escribir y ejecutar un programa de prueba**

#. Crea un nuevo archivo:

   .. code-block:: bash

       cd ~/picar-x/example
       sudo nano test_tts_openai.py

#. Copia el siguiente código de ejemplo en el archivo. Presiona ``Ctrl+X``, luego ``Y`` y finalmente ``Enter`` para guardar y salir.

   .. code-block:: python

      from picarx.tts import OpenAI_TTS
      from secret import OPENAI_API_KEY   # o usa la versión try/except mostrada arriba

      # Inicializar OpenAI TTS
      tts = OpenAI_TTS(api_key=OPENAI_API_KEY)
      tts.set_model('gpt-4o-mini-tts')  # modelo TTS de baja latencia
      tts.set_voice('alloy')            # seleccionar una voz

      # Saludo rápido (prueba de funcionamiento)
      tts.say("Hello! I'm OpenAI TTS.")

#. Ejecuta el programa:

   .. code-block:: bash

       sudo python3 test_tts_openai.py

#. Deberías escuchar al PiCar-X decir:  

   ``Hello! I'm OpenAI TTS.``

.. **Modelos y Voces Disponibles**

.. .. list-table::
..    :header-rows: 1
..    :widths: 20 80

..    * - Categoría
..      - Opciones
..    * - Modelos
..      - 
..        - ``tts-1``  
..        - ``tts-1-hd``  
..        - ``gpt-4o-mini-tts``  
..        - ``accent``  
..        - ``emotional-range``  
..        - ``intonation``  
..        - ``impressions``  
..        - ``speed-of-speech``  
..        - ``tone``  
..        - ``whispering``
..    * - Voces
..      - 
..        - ``alloy``  
..        - ``ash``  
..        - ``ballad``  
..        - ``coral``  
..        - ``echo``  
..        - ``fable``  
..        - ``nova``  
..        - ``onyx``  
..        - ``sage``  
..        - ``shimmer``


3. Robot Narrador
------------------------

Ahora que hemos probado tanto **Piper** como **OpenAI TTS**, usémoslos en un proyecto real:  
un **robot narrador sobre ruedas** que se desplaza mientras cuenta chistes.  

En este programa, el PiCar-X:

* Te saludará con TTS al iniciar.  
* Avanzará y contará un primer chiste.  
* Avanzará de nuevo y contará un segundo chiste.  
* Finalmente retrocederá, regresará a “casa” y se despedirá.  

¡Es como tener un pequeño robot narrador sobre ruedas!

**Ejecutar el código**

.. code-block:: bash

    cd ~/picar-x/example
    sudo python3 15.storytelling_robot.py

**Código**

.. code-block:: python

   from picarx import Picarx
   import time

   # === TTS Configuration ===
   # Default: Piper
   from picarx.tts import Piper
   tts = Piper()
   tts.set_model("en_US-amy-low")  # use the voice model you installed

   # Optional: switch to OpenAI TTS
   # from picarx.tts import OpenAI_TTS
   # from secret import OPENAI_API_KEY
   # tts = OpenAI_TTS(api_key=OPENAI_API_KEY)
   # tts.set_model("gpt-4o-mini-tts")  # low-latency TTS model
   # tts.set_voice("alloy")            # choose a voice

   # === PiCar-X Setup ===
   px = Picarx()

   # Quick hello (sanity check)
   tts.say("Hello! I'm PiCar-X speaking with Piper.")

   def main():
       try:
           # Leg 1
           px.forward(30)
           time.sleep(3)
           px.stop()
           tts.say("Why can't your nose be twelve inches long? Because then it would be a foot!")

           # Leg 2
           px.forward(30)
           time.sleep(3)
           px.stop()
           tts.say("Why did the cow go to outer space? To see the moooon!")

           # Wrap-up
           tts.say("That's all for today. Goodbye, let's go home and sleep.")
           px.backward(30)
           time.sleep(6)
           px.stop()

       except KeyboardInterrupt:
           px.stop()
       finally:
           px.stop()
           px.set_dir_servo_angle(0)

   if __name__ == "__main__":
       main()

----

Solución de Problemas
---------------------------

* **No module named 'secret'**

  Esto significa que ``secret.py`` no está en la misma carpeta que tu archivo de Python.
  Mueve ``secret.py`` al mismo directorio donde ejecutas el script, por ejemplo:

  .. code-block:: bash

     ls ~/picar-x/example
     # Asegúrate de ver ambos: secret.py y tu archivo .py

* **OpenAI: Invalid API key / 401**

  * Verifica que pegaste la clave completa (empieza con ``sk-``) y que no haya espacios/saltos de línea extra.
  * Asegúrate de importarla correctamente en tu código:

    .. code-block:: python

       from secret import OPENAI_API_KEY

  * Confirma el acceso a la red en tu Pi (prueba ``ping api.openai.com``).  

* **OpenAI: Quota exceeded / billing error**

  * Puede que necesites agregar facturación o aumentar la cuota en el panel de OpenAI.
  * Intenta de nuevo después de resolver el problema de cuenta/facturación.

* **Piper: tts.say() se ejecuta pero no hay sonido**

  * Asegúrate de que realmente haya un modelo de voz:

    .. code-block:: bash

       ls ~/.local/share/piper/voices

  * Confirma que el nombre del modelo coincida exactamente en el código:

    .. code-block:: python

       tts.set_model("en_US-amy-low")

  * Revisa el dispositivo/salida de audio y volumen en tu Pi (``alsamixer``), y que los altavoces estén conectados y alimentados.

* **ALSA / errores de dispositivo de sonido (p. ej., “Audio device busy” o “No such file or directory”)**

  * Cierra otros programas que usen audio.
  * Reinicia la Pi si el dispositivo permanece ocupado.
  * Para salida por HDMI vs. jack de auriculares, selecciona el dispositivo correcto en la configuración de audio de Raspberry Pi OS.

* **Permission denied al ejecutar Python**

  * Prueba con ``sudo`` si tu entorno lo requiere:

    .. code-block:: bash

       sudo python3 test_tts_piper.py



Comparación de Motores TTS
------------------------------

.. list-table:: Comparación de características: Espeak vs Pico2Wave vs Piper vs OpenAI TTS
   :header-rows: 1
   :widths: 18 18 20 22 22

   * - Elemento
     - Espeak
     - Pico2Wave
     - Piper
     - OpenAI TTS
   * - Se ejecuta en
     - Integrado en Raspberry Pi (offline)
     - Integrado en Raspberry Pi (offline)
     - Raspberry Pi / PC (offline, necesita modelo)
     - Nube (online, necesita clave API)
   * - Calidad de voz
     - Robótica
     - Más natural que Espeak
     - Natural (TTS neuronal)
     - Muy natural / similar a humana
   * - Controles
     - Velocidad, tono, volumen
     - Controles limitados
     - Elegir diferentes voces/modelos
     - Elegir modelo y voces
   * - Idiomas
     - Muchos (la calidad varía)
     - Conjunto limitado
     - Muchas voces/idiomas disponibles
     - Mejor en inglés (otros varían según disponibilidad)
   * - Latencia / velocidad
     - Muy rápida
     - Rápida
     - En tiempo real en Pi 4/5 con modelos “low”
     - Dependiente de la red (normalmente baja latencia)
   * - Configuración
     - Mínima
     - Mínima
     - Descargar modelos ``.onnx`` + ``.onnx.json``
     - Crear clave API, instalar cliente
   * - Mejor para
     - Pruebas rápidas, prompts básicos
     - Voz offline ligeramente mejor
     - Proyectos locales con mejor calidad
     - Máxima calidad, opciones de voz ricas
