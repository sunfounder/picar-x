.. note::

    Hola, ¡bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook! Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirte?**

    - **Soporte de expertos**: Resuelve problemas post-venta y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y avances exclusivos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.


16. Coche Controlado por Voz con Vosk (Sin conexión)
===========================================================

Vosk es un motor ligero de reconocimiento de voz a texto (STT) que admite muchos idiomas y funciona completamente **sin conexión** en Raspberry Pi.  
Solo necesitas acceso a Internet una vez para descargar un modelo de idioma. Después de eso, todo funciona sin conexión de red.  

En esta lección vamos a:  

* Comprobar el micrófono en Raspberry Pi.  
* Instalar y probar Vosk con un modelo de idioma elegido.  
* Construir un **PiCar-X controlado por voz** que escuche una palabra de activación y luego responda a comandos como **adelante**, **atrás**, **izquierda** y **derecha**.  

1. Comprobar tu micrófono
--------------------------

Antes de usar el reconocimiento de voz, asegúrate de que tu micrófono USB funcione correctamente.

#. Lista de dispositivos de grabación disponibles:

   .. code-block:: bash

      arecord -l

   Busca una línea como ``card 1: ... device 0``.  

#. Graba una muestra corta (reemplaza ``1,0`` con los números que encontraste):

   .. code-block:: bash

      arecord -D plughw:1,0 -f S16_LE -r 16000 -d 3 test.wav

   * Ejemplo: si tu dispositivo es ``card 2, device 0``, usa:

   .. code-block:: bash

      arecord -D plughw:2,0 -f S16_LE -r 16000 -d 3 test.wav

#. Reprodúcela para confirmar la grabación:

   .. code-block:: bash

      aplay test.wav

#. Ajusta el volumen del micrófono si es necesario:

   .. code-block:: bash

      alsamixer

   * Presiona **F6** para seleccionar tu micrófono USB.  
   * Busca el canal **Mic** o **Capture**.  
   * Asegúrate de que no esté silenciado (**[MM]** significa silenciado; presiona ``M`` para activar → debe mostrar **[OO]**).  
   * Usa las flechas ↑ / ↓ para cambiar el volumen de grabación.


.. _test_vosk:

2. Probar Vosk
--------------------------

**Pasos para probarlo**:

#. Crea un nuevo archivo:

   .. code-block:: bash

      cd ~/picar-x/example
      sudo nano test_stt_vosk.py

#. Copia el código de ejemplo en él. Pulsa ``Ctrl+X``, luego ``Y``, y ``Enter`` para guardar y salir.

   .. code-block:: python

      from picarx.stt import Vosk

      vosk = Vosk(language="en-us")

      print(vosk.available_languages)

      while True:
          print("Say something")
          result = vosk.listen(stream=False)
          print(result)

#. Ejecuta el programa:

   .. code-block:: bash

      sudo python3 test_stt_vosk.py

#. La primera vez que ejecutes este código con un nuevo idioma, Vosk **descargará automáticamente el modelo de idioma** (por defecto descargará la versión **pequeña**).  
   Al mismo tiempo, también mostrará la lista de idiomas admitidos. Luego verás:

   .. code-block:: text

        vosk-model-small-en-us-0.15.zip: 100%|███████████████████| 39.3M/39.3M [00:05<00:00, 7.85MB/s]
        ['ar', 'ar-tn', 'ca', 'cn', 'cs', 'de', 'en-gb', 'en-in', 'en-us', 'eo', 'es', 'fa', 'fr', 'gu', 'hi', 'it', 'ja', 'ko', 'kz', 'nl', 'pl', 'pt', 'ru', 'sv', 'te', 'tg', 'tr', 'ua', 'uz', 'vn']
        Say something

   Esto significa:

   * El archivo del modelo (``vosk-model-small-en-us-0.15``) se ha descargado.  
   * Se ha mostrado la lista de idiomas admitidos.  
   * El sistema ahora está escuchando — di algo al micrófono de PiCar-X y el texto reconocido aparecerá en la terminal.

   **Consejos**:

   * Mantén el micrófono a unos 15–30 cm de distancia.  
   * Elige un modelo que coincida con tu idioma y acento.  

**Modo de Transmisión (opcional)**

También puedes transmitir audio de forma continua para ver resultados parciales mientras hablas:

.. code-block:: python

   from picarx.stt import Vosk

   vosk = Vosk(language="en-us")

   while True:
       print("Say something")
       for result in vosk.listen(stream=True):
           if result["done"]:
               print(f"final:   {result['final']}")
           else:
               print(f"partial: {result['partial']}", end="\r", flush=True)

3. Coche Controlado por Voz
---------------------------------------

¡Ahora conectemos el reconocimiento de voz al PiCar-X!  

Usaremos una **palabra de activación** ("hey robot") para que el coche solo escuche comandos después de ser activado. Esto ahorra CPU y evita activaciones no deseadas.  


**Ejecutar el código**

.. code-block:: bash

   cd ~/picar-x/example
   sudo python3 16.voice_controlled_car.py

En este programa, el coche:

* Espera la palabra de activación **"hey robot"**.  
* Después de eso, puedes hablar de forma natural — siempre que tu frase incluya una de las palabras clave (**forward**, **backward**, **left**, **right**), el coche responderá.  
  
  Por ejemplo:

  * “Can you move forward a little?” → el coche avanza.  
  * “Please turn left now.” → el coche gira a la izquierda. 
 
* El comando **"sleep"** detiene el bucle de control y pone al coche nuevamente en modo de espera.  

**Código**

.. code-block:: python

   from picarx import Picarx
   from picarx.stt import Vosk
   import time

   px = Picarx()
   stt = Vosk(language="en-us")

   WAKE_WORDS = ["hey robot"]

   print('Say "hey robot" to wake me up! Then say: forward / backward / left / right. Say "sleep" to stop listening.')

   try:
       while True:
           # --- wait for wake word once ---
           stt.wait_until_heard(WAKE_WORDS)
           print("Wake word detected. Listening for commands... (say 'sleep' to pause)")

           # --- command loop: multiple commands after one wake ---
           while True:
               res = stt.listen(stream=False)
               text = res.get("text", "") if isinstance(res, dict) else str(res)
               text = text.lower().strip()
               if not text:
                   continue

               print("Heard:", text)

               if "sleep" in text:
                   # pause command mode; go back to wait for wake word
                   px.stop(); px.set_dir_servo_angle(0)
                   print("Sleeping. Say 'hey robot' to wake me again.")
                   break

               elif "forward" in text:
                   px.set_dir_servo_angle(0)
                   px.forward(30); time.sleep(1); px.stop()

               elif "backward" in text:
                   px.set_dir_servo_angle(0)
                   px.backward(30); time.sleep(1); px.stop()

               elif "left" in text:
                   px.set_dir_servo_angle(-25)
                   px.forward(30); time.sleep(1)
                   px.stop(); px.set_dir_servo_angle(0)

               elif "right" in text:
                   px.set_dir_servo_angle(25)
                   px.forward(30); time.sleep(1)
                   px.stop(); px.set_dir_servo_angle(0)
               # (ignore other words)

   except KeyboardInterrupt:
       pass
   finally:
       px.stop(); px.set_dir_servo_angle(0)
       print("Stopped and centered. Bye.")


Solución de Problemas
-----------------------------

* **No such file or directory (al ejecutar `arecord`)**

  Puede que estés usando el número de tarjeta/dispositivo incorrecto.  
  Ejecuta:

  .. code-block:: bash

     arecord -l

  y reemplaza ``1,0`` con los números que aparezcan para tu micrófono USB.

* **El archivo grabado no tiene sonido**

  Abre el mezclador y revisa el volumen del micrófono:

  .. code-block:: bash

     alsamixer

  * Presiona **F6** para seleccionar tu micrófono USB.  
  * Asegúrate de que **Mic/Capture** no esté silenciado (**[OO]** en lugar de **[MM]**).  
  * Sube el nivel con la tecla ↑.

* **Vosk no reconoce la voz**

  * Asegúrate de que el **código de idioma** coincida con tu modelo (por ejemplo, ``en-us`` para inglés, ``zh-cn`` para chino).  
  * Mantén el micrófono a 15–30 cm de distancia y evita ruidos de fondo.  
  * Habla con claridad y lentamente.

* **La palabra de activación (“hey robot”) nunca se activa**

  * Dila en un tono natural, no demasiado rápido.  
  * Verifica que el programa imprima el texto reconocido. Si no lo hace, el micrófono no está funcionando.  

* **Alta latencia / reconocimiento lento**

  * La descarga automática por defecto es un **modelo pequeño** (más rápido pero menos preciso).  
  * Si sigue lento, cierra otros programas para liberar CPU.  
