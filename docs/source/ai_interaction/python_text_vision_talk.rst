.. note::

    Hola, ¡bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook! Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirte?**

    - **Soporte de expertos**: Resuelve problemas post-venta y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y avances exclusivos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

17. Visión y Texto con Ollama
================================

En esta lección, aprenderás a usar **Ollama**, una herramienta para ejecutar modelos de lenguaje y visión de gran tamaño de forma local.  
Te mostraremos cómo instalar Ollama, descargar un modelo y conectar PiCar-X a él.  

Con esta configuración, PiCar-X puede tomar una instantánea con la cámara y el modelo podrá **ver y hablar** —  
podrás hacer cualquier pregunta sobre la imagen, y el modelo responderá en lenguaje natural.

Antes de Empezar
----------------

Asegúrate de haber completado:

* :ref:`install_all_modules` — Instala los módulos ``robot-hat``, ``vilib``, ``picar-x`` y luego ejecuta el script ``i2samp.sh``.

.. _download_ollama:

1. Instalar Ollama (LLM) y Descargar un Modelo
-------------------------------------------------

Puedes elegir dónde instalar **Ollama**: 

* En tu Raspberry Pi (ejecución local)  
* O en otra computadora (Mac/Windows/Linux) en la **misma red local**  

**Modelos recomendados según el hardware**

Puedes elegir cualquier modelo disponible en |link_ollama_hub|.  
Los modelos vienen en diferentes tamaños (3B, 7B, 13B, 70B...).  
Los modelos más pequeños se ejecutan más rápido y requieren menos memoria, mientras que los modelos más grandes ofrecen mejor calidad pero necesitan hardware más potente.

Consulta la tabla siguiente para decidir qué tamaño de modelo se adapta mejor a tu dispositivo.

.. list-table::
   :header-rows: 1
   :widths: 20 20 40

   * - Tamaño del modelo
     - RAM mínima requerida
     - Hardware recomendado
   * - ~3B parámetros
     - 8GB (mejor con 16GB)
     - Raspberry Pi 5 (16GB) o PC/Mac de gama media
   * - ~7B parámetros
     - 16GB+
     - Pi 5 (16GB, justo utilizable) o PC/Mac de gama media
   * - ~13B parámetros
     - 32GB+
     - PC de escritorio / Mac con mucha RAM
   * - 30B+ parámetros
     - 64GB+
     - Estación de trabajo / servidor / GPU recomendado
   * - 70B+ parámetros
     - 128GB+
     - Servidor de gama alta con múltiples GPUs

**Instalar en Raspberry Pi**

Si deseas ejecutar Ollama directamente en tu Raspberry Pi:

* Usa **Raspberry Pi OS de 64 bits**  
* Recomendado: **Raspberry Pi 5 (16GB RAM)**  

Ejecuta los siguientes comandos:

.. code-block:: bash

   # Instalar Ollama
   curl -fsSL https://ollama.com/install.sh | sh

   # Descargar un modelo liviano (bueno para pruebas)
   ollama pull llama3.2:3b

   # Prueba rápida (escribe 'hi' y presiona Enter)
   ollama run llama3.2:3b

   # Servir la API (puerto por defecto 11434)
   # Consejo: configura OLLAMA_HOST=0.0.0.0 para permitir acceso desde la LAN
   OLLAMA_HOST=0.0.0.0 ollama serve

**Instalar en Mac / Windows / Linux (Aplicación de Escritorio)**

1. Descarga e instala Ollama desde |link_ollama|  

   .. image:: img/llm_ollama_download.png

2. Abre la app de Ollama, ve a **Model Selector** y usa la barra de búsqueda para encontrar un modelo.  
   Por ejemplo, escribe ``llama3.2:3b`` (un modelo pequeño y liviano para comenzar).  

   .. image:: img/llm_ollama_choose.png

3. Una vez finalizada la descarga, escribe algo simple como “Hi” en la ventana de chat.  
   Ollama descargará automáticamente el modelo la primera vez que lo uses.

   .. image:: img/llm_olama_llama_download.png

4. Ve a **Settings** → habilita **Expose Ollama to the network**.  
   Esto permite que tu Raspberry Pi se conecte a él a través de la red LAN.  

   .. image:: img/llm_olama_windows_enable.png

.. warning::

   Si ves un error como:

   ``Error: model requires more system memory ...``

   El modelo es demasiado grande para tu máquina.  
   Usa un **modelo más pequeño** o cambia a un equipo con más RAM.

2. Probar Ollama
-------------------

Una vez que Ollama esté instalado y tu modelo esté listo, puedes probarlo rápidamente con un bucle de chat mínimo.

**Pasos**

#. Crea un nuevo archivo:

   .. code-block:: bash
 
      cd ~/picar-x/example
      nano test_llm_ollama.py

#. Pega el siguiente código y guarda (``Ctrl+X`` → ``Y`` → ``Enter``):

   .. code-block:: python
 
      from picarx.llm import Ollama
 
      INSTRUCTIONS = "You are a helpful assistant."
      WELCOME = "Hello, I am a helpful assistant. How can I help you?"
 
      # If Ollama runs on the same Raspberry Pi, use "localhost".
      # If it runs on another computer in your LAN, replace with that computer's IP address.
      llm = Ollama(
          ip="localhost",
          model="llama3.2:3b"   # you can replace with any model
      )
 
      # Basic configuration
      llm.set_max_messages(20)
      llm.set_instructions(INSTRUCTIONS)
      llm.set_welcome(WELCOME)
 
      print(WELCOME)
 
      while True:
          text = input(">>> ")
          if text.strip().lower() in {"exit", "quit"}:
              break
 
          # Response with streaming output
          response = llm.prompt(text, stream=True)
          for token in response:
              if token:
                  print(token, end="", flush=True)
          print("")

#. Ejecuta el programa:

   .. code-block:: bash
 
      python3 test_llm_ollama.py
 
#. Ahora puedes chatear con PiCar-X directamente desde la terminal.

   * Puedes elegir **cualquier modelo** disponible en |link_ollama_hub|, pero se recomiendan modelos pequeños (por ejemplo, ``moondream:1.8b``, ``phi3:mini``) si solo tienes 8–16GB de RAM.  
   * Asegúrate de que el modelo que especifiques en el código coincida con el que ya descargaste en Ollama.  
   * Escribe ``exit`` o ``quit`` para detener el programa.  
   * Si no puedes conectarte, asegúrate de que Ollama esté en ejecución y que ambos dispositivos estén en la misma red LAN si estás usando un host remoto.



3. Visión y Texto con Ollama
--------------------------------

En esta demostración, la cámara Pi toma una fotografía **cada vez que escribes una pregunta**.  
El programa envía **tu texto + la nueva foto** a un modelo de visión local a través de Ollama  
y luego transmite la respuesta del modelo en inglés simple.  
Este es un punto de partida mínimo de “ver y contar” que luego puedes ampliar con detección de colores, rostros o códigos QR.

**Antes de comenzar**

#. Abre la aplicación **Ollama** (o ejecuta el servicio) y asegúrate de haber descargado un **modelo con capacidad de visión**.

   * Si tienes suficiente memoria (≥16GB RAM), puedes probar ``llava:7b``.
   * Si solo tienes **8GB RAM**, utiliza un modelo más pequeño como ``moondream:1.8b`` o ``granite3.2-vision:2b``.

   .. image:: img/llm_ollama_image_model.png

**Ejecutar la Demo**

#. Ve a la carpeta de ejemplos y ejecuta el script:

   .. code-block:: bash

      cd ~/picar-x/example
      python3 17.text_vision_talk.py

#. Lo que sucede cuando se ejecuta:

   * El programa imprime un mensaje de bienvenida y espera tu entrada (``>>>``).
   * **Cada vez que escribes algo** (por ejemplo, “hello”, “¿Hay algo amarillo?”, “¿Hay rostros?”, “¿Qué hay en el escritorio?”), este:

     * **captura una foto** con la cámara Pi (guardada en ``/tmp/llm-img.jpg``),  
     * **envía tu texto + la foto** al modelo de visión mediante Ollama,  
     * **transmite** la respuesta del modelo en la terminal.

   * Escribe ``exit`` o ``quit`` para finalizar el programa.

**Código**

.. code-block:: python

   from picarx.llm import Ollama
   from picamera2 import Picamera2
   import time

   """
   You need to set up Ollama first.

   Note: At least 8GB RAM is recommended for small vision models (e.g., moondream:1.8b).
         For llava:7b, more memory is preferred (≥16GB).
   """

   INSTRUCTIONS = "You are a helpful assistant."
   WELCOME = "Hello, I am a helpful assistant. How can I help you?"

   # If Ollama runs on the same Pi, use "localhost".
   # If it runs on another computer in your LAN, replace with that computer's IP.
   llm = Ollama(
       ip="localhost",          # e.g., "192.168.100.145" if remote
       model="llava:7b"         # change to "moondream:1.8b" or "granite3.2-vision:2b" for 8GB RAM
   )

   # Basic configuration
   llm.set_max_messages(20)
   llm.set_instructions(INSTRUCTIONS)
   llm.set_welcome(WELCOME)

   # Init camera
   camera = Picamera2()
   config = camera.create_still_configuration(
       main={"size": (1280, 720)},
   )
   camera.configure(config)
   camera.start()
   time.sleep(2)

   print(WELCOME)

   while True:
       input_text = input(">>> ")
       if input_text.strip().lower() in {"exit", "quit"}:
           break

       # Capture image
       img_path = "/tmp/llm-img.jpg"
       camera.capture_file(img_path)

       # Response with stream (text + image)
       response = llm.prompt(input_text, stream=True, image_path=img_path)
       for next_word in response:
           if next_word:
               print(next_word, end="", flush=True)
       print("")

Solución de Problemas
-----------------------------


* **Recibo un error como: `model requires more system memory ...`.**

  * Esto significa que el modelo es demasiado grande para tu dispositivo.  
  * Usa un modelo más pequeño como ``moondream:1.8b`` o ``granite3.2-vision:2b``.  
  * O cambia a una máquina con más RAM y expón Ollama a la red.

* **El código no puede conectarse a Ollama (connection refused).** 

  Verifica lo siguiente:
  
  * Asegúrate de que Ollama esté en ejecución (``ollama serve`` o que la aplicación de escritorio esté abierta).  
  * Si usas una computadora remota, habilita **Expose to network** en la configuración de Ollama.  
  * Revisa que el ``ip="..."`` en tu código coincida con la IP LAN correcta.  
  * Confirma que ambos dispositivos estén en la misma red local.

* **Mi cámara de la Pi no captura nada.**

  * Verifica que ``Picamera2`` esté instalada y funcione con un script de prueba sencillo.  
  * Comprueba que el cable de la cámara esté bien conectado y habilitado en ``raspi-config``.  
  * Asegúrate de que tu script tenga permiso para escribir en la ruta de destino (``/tmp/llm-img.jpg``).

* **La salida es demasiado lenta.**  

  * Los modelos más pequeños responden más rápido, pero con respuestas más simples.  
  * Puedes bajar la resolución de la cámara (por ejemplo, 640×480 en lugar de 1280×720) para acelerar el procesamiento de imágenes.  
  * Cierra otros programas en tu Pi para liberar CPU y RAM.
