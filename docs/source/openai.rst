.. note::

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. ¡Profundiza en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas!

    **¿Por qué unirte?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones especiales.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.


Interacción con IA Usando GPT-4O
=====================================================
En nuestros proyectos anteriores, usamos la programación para dirigir a PiCar-X en tareas predeterminadas, lo que podría parecer un poco tedioso. Este proyecto introduce un emocionante salto hacia una interacción dinámica. ¡Cuidado con tratar de burlar a nuestro coche, ya que ahora está equipado para entender mucho más que nunca!

Este proyecto detalla todos los pasos técnicos necesarios para integrar GPT-4O en tu sistema, incluyendo la configuración de los entornos virtuales necesarios, la instalación de librerías esenciales y la configuración de claves API e ID de asistente.

.. note::

   Este proyecto requiere el uso de |link_openai_platform|, y es necesario pagar por OpenAI. Además, la API de OpenAI se factura por separado de ChatGPT, con su propio precio disponible en https://openai.com/api/pricing/.

   Por lo tanto, debes decidir si deseas continuar con este proyecto o asegurarte de haber financiado la API de OpenAI.

Ya sea que tengas un micrófono para comunicarte directamente o prefieras escribir en una ventana de comandos, ¡las respuestas de PiCar-X potenciadas por GPT-4O seguramente te sorprenderán!

¡Vamos a sumergirnos en este proyecto y liberar un nuevo nivel de interacción con PiCar-X!

1. Instalación de Paquetes y Dependencias Requeridos
--------------------------------------------------------------
.. note::

   Primero debes instalar los módulos necesarios para PiCar-X. Para más detalles, consulta: :ref:`install_all_modules`.
   
En esta sección, crearemos y activaremos un entorno virtual, instalando los paquetes y dependencias necesarios dentro de él. Esto asegura que los paquetes instalados no interfieran con el resto del sistema, manteniendo el aislamiento de las dependencias del proyecto y evitando conflictos con otros proyectos o paquetes del sistema.

#. Usa el comando ``python -m venv`` para crear un entorno virtual llamado ``my_venv``, incluyendo paquetes a nivel del sistema. La opción ``--system-site-packages`` permite que el entorno virtual acceda a los paquetes instalados a nivel del sistema, lo cual es útil cuando se necesitan librerías a nivel del sistema.

   .. code-block:: shell

      python -m venv --system-site-packages my_venv

#. Cambia al directorio ``my_venv`` y activa el entorno virtual utilizando el comando ``source bin/activate``. El indicador del comando cambiará para indicar que el entorno virtual está activo.

   .. code-block:: shell

      cd my_venv
      source bin/activate

#. Ahora, instala los paquetes de Python requeridos dentro del entorno virtual activado. Estos paquetes estarán aislados al entorno virtual y no afectarán a otros paquetes del sistema.

   .. code-block:: shell

      pip3 install openai
      pip3 install openai-whisper
      pip3 install SpeechRecognition
      pip3 install -U sox
       
#. Finalmente, usa el comando ``apt`` para instalar las dependencias a nivel del sistema, que requieren privilegios de administrador.

   .. code-block:: shell

      sudo apt install python3-pyaudio
      sudo apt install sox


2. Obtener Clave API e ID de Asistente
-----------------------------------------

**Obtener Clave API**

#. Visita |link_openai_platform| y haz clic en el botón **Create new secret key** en la esquina superior derecha.

   .. image:: img/apt_create_api_key.png
      :width: 700
      :align: center

#. Selecciona el Propietario, Nombre, Proyecto y permisos según sea necesario, y luego haz clic en **Create secret key**.

   .. image:: img/apt_create_api_key2.png
      :width: 700
      :align: center

#. Una vez generada, guarda esta clave secreta en un lugar seguro y accesible. Por razones de seguridad, no podrás verla nuevamente a través de tu cuenta de OpenAI. Si pierdes esta clave secreta, tendrás que generar una nueva.

   .. image:: img/apt_create_api_key_copy.png
      :width: 700
      :align: center

**Obtener ID de Asistente**

#. Luego, haz clic en **Assistants**, y luego en **Create**, asegurándote de estar en la página **Dashboard**.

   .. image:: img/apt_create_assistant.png
      :width: 700
      :align: center

#. Mueve tu cursor aquí para copiar el **ID de asistente**, luego pégalo en un cuadro de texto o en otro lugar. Este es el identificador único para este Asistente.

   .. image:: img/apt_create_assistant_id.png
      :width: 700
      :align: center

#. Asigna un nombre al azar, luego copia el siguiente contenido en el cuadro **Instructions** para describir tu Asistente.

   .. image:: img/apt_create_assistant_instructions.png
      :width: 700
      :align: center

   .. code-block::

         You are a small car with AI capabilities named PaiCar-X. You can engage in conversations with people and react accordingly to different situations with actions or sounds. You are driven by two rear wheels, with two front wheels that can turn left and right, and equipped with a camera mounted on a 2-axis gimbal.

         ## Response with Json Format, eg:
         {"actions": ["start engine", "honking", "wave hands"], "answer": "Hello, I am PaiCar-X, your good friend."}

         ## Response Style
         Tone: Cheerful, optimistic, humorous, childlike
         Preferred Style: Enjoys incorporating jokes, metaphors, and playful banter; prefers responding from a robotic perspective
         Answer Elaboration: Moderately detailed

         ## Actions you can do:
         ["shake head", "nod", "wave hands", "resist", "act cute", "rub hands", "think", "twist body", "celebrate, "depressed"]
         ## Sound effects:
         ["honking", "start engine"]


#. PiCar-X está equipado con un módulo de cámara que puedes habilitar para capturar imágenes de lo que ve y subirlas a GPT usando nuestro código de ejemplo. Por lo tanto, recomendamos elegir GPT-4O, que tiene capacidades de análisis de imágenes. Por supuesto, también puedes elegir gpt-3.5-turbo u otros modelos.

   .. image:: img/apt_create_assistant_model.png
      :width: 700
      :align: center

#. Ahora, haz clic en **Playground** para ver si tu cuenta funciona correctamente.

   .. image:: img/apt_playground.png

#. Si tus mensajes o imágenes subidas se envían con éxito y recibes respuestas, significa que tu cuenta no ha alcanzado el límite de uso.


   .. image:: img/apt_playground_40.png
      :width: 700
      :align: center

#. Si recibes un mensaje de error después de ingresar información, es posible que hayas alcanzado tu límite de uso. Verifica el panel de uso o la configuración de facturación.

   .. image:: img/apt_playground_40mini_3.5.png
      :width: 700
      :align: center

3. Completar la Clave API y el ID de Asistente
--------------------------------------------------

#. Usa el comando para abrir el archivo ``keys.py``.

   .. code-block:: shell

      nano ~/picar-x/gpt_examples/keys.py

#. Completa la Clave API y el ID de Asistente que acabas de copiar.

   .. code-block:: shell

      OPENAI_API_KEY = "sk-proj-vEBo7Ahxxxx-xxxxx-xxxx"
      OPENAI_ASSISTANT_ID = "asst_ulxxxxxxxxx"

#. Presiona ``Ctrl + X``, ``Y``, y luego ``Enter`` para guardar el archivo y salir.

4. Ejecución del Ejemplo
----------------------------------
Comunicación por Texto
^^^^^^^^^^^^^^^^^^^^^^^^^^

Si tu PiCar-X no tiene un micrófono, puedes usar la entrada de texto del teclado para interactuar con él ejecutando los siguientes comandos.

#. Ahora, ejecuta los siguientes comandos usando sudo, ya que el altavoz de PiCar-X no funcionará sin él. El proceso tomará un poco de tiempo para completarse.

   .. code-block:: shell

      cd ~/picar-x/gpt_examples/
      sudo ~/my_venv/bin/python3 gpt_car.py --keyboard

#. Una vez que los comandos se hayan ejecutado correctamente, verás la siguiente salida, lo que indica que todos los componentes de PiCar-X están listos.

   .. code-block:: shell

      vilib 0.3.8 launching ...
      picamera2 0.3.19

      Web display on:
         http://rpi_ip:9000/mjpg

      Starting web streaming ...
      * Serving Flask app 'vilib.vilib'
      * Debug mode: off

      input:

#. También se te proporcionará un enlace para ver el feed de la cámara de PiCar-X en tu navegador web: ``http://rpi_ip:9000/mjpg``.

   .. image:: img/apt_ip_camera.png
      :width: 700
      :align: center

#. Ahora puedes escribir tus comandos en la ventana del terminal y presionar Enter para enviarlos. Las respuestas de PiCar-X podrían sorprenderte.

   .. note::
      
      PiCar-X necesita recibir tu entrada, enviarla a GPT para su procesamiento, recibir la respuesta y luego reproducirla mediante síntesis de voz. Todo este proceso toma un poco de tiempo, así que por favor, sé paciente.

   .. image:: img/apt_keyboard_input.png
      :width: 700
      :align: center

#. Si estás usando el modelo GPT-4O, también puedes hacer preguntas basadas en lo que ve PiCar-X.

Comunicación por Voz
^^^^^^^^^^^^^^^^^^^^^^^^

Si tu PiCar-X está equipado con un micrófono, o puedes comprar uno haciendo clic en |link_microphone|, puedes interactuar con PiCar-X usando comandos de voz.

#. Primero, verifica que el Raspberry Pi haya detectado el micrófono.

   .. code-block:: shell

      arecord -l

   Si tiene éxito, recibirás la siguiente información, indicando que tu micrófono ha sido detectado.

   .. code-block:: 
      
      **** List of CAPTURE Hardware Devices ****
      card 3: Device [USB PnP Sound Device], device 0: USB Audio [USB Audio]
      Subdevices: 1/1
      Subdevice #0: subdevice #0

#. Ejecuta el siguiente comando, luego habla con PiCar-X o haz algunos sonidos. El micrófono grabará los sonidos en el archivo ``op.wav``. Presiona ``Ctrl + C`` para detener la grabación.

   .. code-block:: shell

      rec op.wav

#. Finalmente, usa el siguiente comando para reproducir el sonido grabado, confirmando que el micrófono funciona correctamente.

   .. code-block:: shell

      sudo play op.wav

#. Ahora, ejecuta los siguientes comandos usando sudo, ya que el altavoz de PiCar-X no funcionará sin él. El proceso tomará un poco de tiempo para completarse.

   .. code-block:: shell

      cd ~/picar-x/gpt_examples/
      sudo ~/my_venv/bin/python3 gpt_car.py

#. Una vez que los comandos se hayan ejecutado correctamente, verás la siguiente salida, lo que indica que todos los componentes de PiCar-X están listos.

   .. code-block:: shell
      
      vilib 0.3.8 launching ...
      picamera2 0.3.19

      Web display on:
         http://rpi_ip:9000/mjpg

      Starting web streaming ...
      * Serving Flask app 'vilib.vilib'
      * Debug mode: off

      listening ...

#. También se te proporcionará un enlace para ver el feed de la cámara de PiCar-X en tu navegador web: ``http://rpi_ip:9000/mjpg``.

   .. image:: img/apt_ip_camera.png
      :width: 700
      :align: center

#. Ahora puedes hablar con PiCar-X, y sus respuestas podrían sorprenderte.

   .. note::
      
      PiCar-X necesita recibir tu entrada, convertirla a texto, enviarla a GPT para su procesamiento, recibir la respuesta y luego reproducirla mediante síntesis de voz. Todo este proceso toma un poco de tiempo, así que por favor, sé paciente.

   .. image:: img/apt_speech_input.png
      :width: 700
      :align: center

#. Si estás usando el modelo GPT-4O, también puedes hacer preguntas basadas en lo que ve PiCar-X.


5. Modificar parámetros [opcional]
-------------------------------------------

En el archivo ``gpt_car.py``, localiza las siguientes líneas. Puedes modificar estos parámetros para configurar el idioma STT, el volumen de TTS y el rol de la voz.

* **STT (Speech to Text)** se refiere al proceso en el que el micrófono de PiCar-X captura la voz y la convierte en texto para ser enviado a GPT. Puedes especificar el idioma para una mayor precisión y menor latencia en esta conversión.

* **TTS (Text to Speech)** es el proceso de convertir las respuestas de texto de GPT en voz, que se reproduce a través del altavoz de PiCar-X. Puedes ajustar el volumen y seleccionar un rol de voz para la salida TTS.

.. code-block:: python

   # openai assistant init
   # =================================================================
   openai_helper = OpenAiHelper(OPENAI_API_KEY, OPENAI_ASSISTANT_ID, 'picrawler')

   # LANGUAGE = ['zh', 'en'] # config stt language code, https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes
   LANGUAGE = []

   VOLUME_DB = 3 # tts volume gain, preferably less than 5db

   # select tts voice role, could be "alloy, echo, fable, onyx, nova, and shimmer"
   # https://platform.openai.com/docs/guides/text-to-speech/supported-languages
   TTS_VOICE = 'nova'


* Variable ``LANGUAGE``: 

  * Mejora la precisión y el tiempo de respuesta del Speech-to-Text (STT).
  * ``LANGUAGE = []`` significa que se admiten todos los idiomas, pero esto puede reducir la precisión del STT y aumentar la latencia.
  * Se recomienda establecer uno o más idiomas específicos utilizando los códigos de idioma |link_iso_language_code| para mejorar el rendimiento.

* Variable ``VOLUME_DB``:

  * Controla la ganancia aplicada a la salida de Text-to-Speech (TTS).
  * Aumentar el valor aumentará el volumen, pero es mejor mantener el valor por debajo de 5dB para evitar distorsiones de audio.

* Variable ``TTS_VOICE``:

  * Selecciona el rol de voz para la salida de Text-to-Speech (TTS).
  * Opciones disponibles: ``alloy, echo, fable, onyx, nova, shimmer``.
  * Puedes experimentar con diferentes voces de |link_voice_options| para encontrar la que mejor se adapte al tono y al público deseado. Las voces disponibles están actualmente optimizadas para inglés.
