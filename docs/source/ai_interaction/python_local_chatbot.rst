.. note::

    Hola, ¡bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook! Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirte?**

    - **Soporte de expertos**: Resuelve problemas post-venta y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y avances exclusivos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

19. Chatbot de Voz Local
===========================

En esta lección, combinarás todo lo que has aprendido — **reconocimiento de voz (STT)**,  
**texto a voz (TTS)** y un **LLM local (Ollama)** — para crear un **chatbot de voz** totalmente sin conexión  
que se ejecuta en tu sistema PiCar-X.

El flujo de trabajo es simple:

#. **Escuchar** — El micrófono captura tu voz y la transcribe con **Vosk**.  
#. **Pensar** — El texto se envía a un **LLM** local que se ejecuta en Ollama (p. ej., ``llama3.2:3b``).  
#. **Hablar** — El chatbot responde en voz alta usando **Piper TTS**.  

Esto crea un **robot conversacional manos libres** que puede entender y responder en tiempo real.

----

Antes de Empezar
----------------

Asegúrate de haber preparado lo siguiente:

* Haber probado **Piper TTS** (:ref:`test_piper`) y elegido un modelo de voz funcional.  
* Haber probado **Vosk STT** (:ref:`test_vosk`) y elegido el paquete de idioma correcto (p. ej., ``en-us``).  
* Haber instalado **Ollama** (:ref:`download_ollama`) en tu Pi u otro ordenador, y descargado un modelo como ``llama3.2:3b`` (o uno más pequeño como ``moondream:1.8b`` si la memoria es limitada).

----

Ejecutar el Código
-------------------------

#. Abre el script de ejemplo:

   .. code-block:: bash

      cd ~/picar-x/example
      sudo nano 19.local_voice_chatbot.py

#. Actualiza los parámetros según sea necesario:

   * ``stt = Vosk(language="en-us")``: Cámbialo para que coincida con tu acento/paquete de idioma (p. ej., ``en-us``, ``zh-cn``, ``es``).  
   * ``tts.set_model("en_US-amy-low")``: Sustituye por el modelo de voz de Piper que verificaste en :ref:`test_piper`.  
   * ``llm = Ollama(ip="localhost", model="llama3.2:3b")``: Actualiza tanto ``ip`` como ``model`` a tu propia configuración.  

     * ``ip``: Si Ollama se ejecuta en el **mismo Pi**, usa ``localhost``. Si Ollama se ejecuta en otro ordenador de tu LAN, habilita **Expose to network** en Ollama y establece ``ip`` en la IP LAN de ese ordenador.  
     * ``model``: Debe coincidir exactamente con el nombre del modelo que descargaste/activaste en Ollama.  

#. Ejecuta el script:

   .. code-block:: bash

      cd ~/picar-x/example
      sudo python3 19.local_voice_chatbot.py

#. Después de ejecutarlo, deberías ver:

   * El bot te saluda con un mensaje de bienvenida hablado.  
   * Espera entrada de voz.  
   * Vosk transcribe tu voz a texto.  
   * El texto se envía a Ollama, que devuelve una respuesta por streaming.  
   * La respuesta se limpia (eliminando el razonamiento oculto) y Piper la pronuncia.  
   * Detén el programa en cualquier momento con ``Ctrl+C``.

----

Código
-------------------------

.. code-block:: python

   import re
   import time
   from picarx.llm import Ollama
   from picarx.stt import Vosk
   from picarx.tts import Piper

   # Initialize speech recognition
   stt = Vosk(language="en-us")

   # Initialize TTS
   tts = Piper()
   tts.set_model("en_US-amy-low")

   # Instructions for the LLM
   INSTRUCTIONS = (
       "You are a helpful assistant. Answer directly in plain English. "
       "Do NOT include any hidden thinking, analysis, or tags like <think>."
   )
   WELCOME = "Hello! I'm your voice chatbot. Speak when you're ready."

   # Initialize Ollama connection
   llm = Ollama(ip="localhost", model="llama3.2:3b")
   llm.set_max_messages(20)
   llm.set_instructions(INSTRUCTIONS)

   # Utility: clean hidden reasoning
   def strip_thinking(text: str) -> str:
       if not text:
           return ""
       text = re.sub(r"<\s*think[^>]*>.*?<\s*/\s*think\s*>", "", text, flags=re.DOTALL|re.IGNORECASE)
       text = re.sub(r"<\s*thinking[^>]*>.*?<\s*/\s*thinking\s*>", "", text, flags=re.DOTALL|re.IGNORECASE)
       text = re.sub(r"```(?:\s*thinking)?\s*.*?```", "", text, flags=re.DOTALL|re.IGNORECASE)
       text = re.sub(r"\[/?thinking\]", "", text, flags=re.IGNORECASE)
       return re.sub(r"\s+\n", "\n", text).strip()

   def main():
       print(WELCOME)
       tts.say(WELCOME)

       try:
           while True:
               print("\n🎤 Listening... (Press Ctrl+C to stop)")

               # Collect final transcript from Vosk
               text = ""
               for result in stt.listen(stream=True):
                   if result["done"]:
                       text = result["final"].strip()
                       print(f"[YOU] {text}")
                   else:
                       print(f"[YOU] {result['partial']}", end="\r", flush=True)

               if not text:
                   print("[INFO] Nothing recognized. Try again.")
                   time.sleep(0.1)
                   continue

               # Query Ollama with streaming
               reply_accum = ""
               response = llm.prompt(text, stream=True)
               for next_word in response:
                   if next_word:
                       print(next_word, end="", flush=True)
                       reply_accum += next_word
               print("")

               # Clean and speak
               clean = strip_thinking(reply_accum)
               if clean:
                   tts.say(clean)
               else:
                   tts.say("Sorry, I didn't catch that.")

               time.sleep(0.05)

       except KeyboardInterrupt:
           print("\n[INFO] Stopping...")
       finally:
           tts.say("Goodbye!")
           print("Bye.")

   if __name__ == "__main__":
       main()

----

Análisis del Código
---------------------------

**Importaciones y configuración global**

.. code-block:: python

   import re
   import time
   from picarx.llm import Ollama
   from picarx.stt import Vosk
   from picarx.tts import Piper

Incluye los tres subsistemas que construiste antes:
**Vosk** para reconocimiento de voz a texto (STT), **Ollama** para el LLM y **Piper** para texto a voz (TTS).



**Inicializar STT (Vosk)**

.. code-block:: python

   stt = Vosk(language="en-us")

Carga el modelo de Vosk para inglés de EE. UU.  
Cambia el código de idioma (p. ej., ``zh-cn``, ``es``) para que coincida con tu paquete de voz y mejorar la precisión.



**Inicializar TTS (Piper)**

.. code-block:: python

   tts = Piper()
   tts.set_model("en_US-amy-low")

Crea un motor Piper y selecciona una voz específica.  
Elige un modelo que hayas probado en :ref:`test_piper`. Las voces de menor calidad son más rápidas y usan menos CPU.



**Instrucciones del LLM y línea de bienvenida**

.. code-block:: python

   INSTRUCTIONS = (
       "You are a helpful assistant. Answer directly in plain English. "
       "Do NOT include any hidden thinking, analysis, or tags like <think>."
   )
   WELCOME = "Hello! I'm your voice chatbot. Speak when you're ready."

Dos decisiones clave de UX:

* Mantén las **respuestas cortas y directas** (ayuda a la claridad del TTS).
* Prohíbe explícitamente las etiquetas de “cadena de pensamiento” ocultas para reducir salidas ruidosas.



**Conectar a Ollama y definir el alcance de la conversación**

.. code-block:: python

   llm = Ollama(ip="localhost", model="llama3.2:3b")
   llm.set_max_messages(20)
   llm.set_instructions(INSTRUCTIONS)

* ``ip="localhost"`` asume que el servidor de Ollama se ejecuta en el mismo Pi. Si se ejecuta en otra máquina de la LAN, coloca la **IP LAN** de ese equipo y habilita *Expose to network* en Ollama.
* ``set_max_messages(20)`` mantiene un historial de conversación corto. Reduce esto si la memoria/latencia es ajustada.

**Eliminar razonamientos/etiquetas ocultas antes de hablar**

.. code-block:: python

   def strip_thinking(text: str) -> str:
       if not text:
           return ""
       text = re.sub(r"<\s*think[^>]*>.*?<\s*/\s*think\s*>", "", text, flags=re.DOTALL|re.IGNORECASE)
       text = re.sub(r"<\s*thinking[^>]*>.*?<\s*/\s*thinking\s*>", "", text, flags=re.DOTALL|re.IGNORECASE)
       text = re.sub(r"```(?:\s*thinking)?\s*.*?```", "", text, flags=re.DOTALL|re.IGNORECASE)
       text = re.sub(r"\[/?thinking\]", "", text, flags=re.IGNORECASE)
       return re.sub(r"\s+\n", "\n", text).strip()

Algunos modelos pueden emitir etiquetas de estilo interno (p. ej., ``<think>…``).  
Esta función las elimina para que tu TTS **solo** lea la respuesta final.

**Consejo:** Si ves otros artefactos en pantalla (porque transmites tokens en bruto), esta función ya garantiza que la salida **hablada** esté limpia.

**Bucle principal: saluda una vez, luego escuchar → pensar → hablar**

.. code-block:: python

   print(WELCOME)
   tts.say(WELCOME)

Saluda al usuario por terminal y por altavoz. Ocurre una sola vez al inicio.

**Escuchar (STT en streaming con parciales en vivo)**

.. code-block:: python

   print("\n🎤 Escuchando... (Pulsa Ctrl+C para detener)")

   text = ""
   for result in stt.listen(stream=True):
       if result["done"]:
           text = result["final"].strip()
           print(f"[TÚ] {text}")
       else:
           print(f"[TÚ] {result['partial']}", end="\r", flush=True)

* ``stream=True`` produce transcripciones **parciales** para retroalimentación inmediata y una transcripción **final** cuando termina el enunciado.
* El texto final reconocido se guarda en ``text`` y se imprime una vez.

**Protección:** Si no se reconoció nada, se omite la llamada al LLM:

.. code-block:: python

   if not text:
       print("[INFO] No se reconoció nada. Intenta de nuevo.")
       time.sleep(0.1)
       continue

Evita enviar prompts vacíos al modelo (ahorra tiempo y tokens).

**Pensar (LLM) con impresión en streaming**

.. code-block:: python

   reply_accum = ""
   response = llm.prompt(text, stream=True)
   for next_word in response:
       if next_word:
           print(next_word, end="", flush=True)
           reply_accum += next_word
   print("")

* Envía la transcripción final al LLM local y **muestra los tokens a medida que llegan** para baja latencia.
* Mientras tanto, acumulas la respuesta completa en ``reply_accum`` para el postprocesamiento.

**Nota:** Si prefieres **no** mostrar tokens en bruto, establece ``stream=False`` y simplemente imprime la cadena final.

**Hablar (limpiar primero, luego TTS una vez)**

.. code-block:: python

   clean = strip_thinking(reply_accum)
   if clean:
       tts.say(clean)
   else:
       tts.say("Sorry, I didn't catch that.")

* Limpia el texto final para eliminar etiquetas ocultas y luego **lo habla una sola vez**.  
* Mantener el TTS en una sola pasada evita mensajes repetidos como “[LLM] / [SAY]”.


**Salida y cierre**

.. code-block:: python

   except KeyboardInterrupt:
       print("\n[INFO] Stopping...")
   finally:
       tts.say("Goodbye!")
       print("Bye.")

Usa **Ctrl+C** para detener. El bot dice una breve despedida para indicar un cierre limpio.


----

Solución de Problemas y Preguntas Frecuentes (FAQ)
--------------------------------------------------

* **El modelo es demasiado grande (error de memoria)**

  Usa un modelo más pequeño como ``moondream:1.8b`` o ejecuta Ollama en un ordenador más potente.  

* **No hay respuesta de Ollama**

  Asegúrate de que Ollama esté en ejecución (``ollama serve`` o la aplicación de escritorio abierta).  
  Si es remoto, habilita **Expose to network** y verifica la dirección IP.  

* **Vosk no reconoce la voz** 

  Verifica que el micrófono funcione correctamente.  
  Si es necesario, prueba con otro paquete de idioma (``zh-cn``, ``es``, etc.).  

* **Piper sin sonido o con errores**  

  Confirma que el modelo de voz elegido esté descargado y probado en :ref:`test_piper`.  

* **Las respuestas son demasiado largas o fuera de tema**

  Edita ``INSTRUCTIONS`` y agrega: **“Mantén las respuestas cortas y directas.”**




