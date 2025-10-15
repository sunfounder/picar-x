.. note::

    Hola, ¡bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook! Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirte?**

    - **Soporte de expertos**: Resuelve problemas post-venta y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y avances exclusivos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.


.. _ai_voice_assistant_car:

21. Coche Asistente de Voz con IA
===================================

Esta lección convierte tu PiCar-X en un **asistente de voz sobre ruedas impulsado por IA**.  
El robot puede activarse con tu voz, reconocer lo que dices, responder con emoción  
y expresar sus “sentimientos” mediante movimientos, gestos y luces.

Construirás un **coche asistente de voz totalmente interactivo** usando:

* **LLM** - Modelo de Lenguaje Grande (OpenAI GPT o Doubao).  
* **STT** - Reconocimiento de voz a texto (Speech-to-Text).  
* **TTS** - Conversión de texto a voz (Text-to-Speech).  
* **Sensores + Acciones** - Ultrasonido, cámara y acciones expresivas integradas.

----

Antes de Empezar
----------------

Asegúrate de haber completado:

* :ref:`test_piper` — Verifica los idiomas compatibles de **Piper TTS**.  
* :ref:`test_vosk` — Verifica los idiomas compatibles de **Vosk STT**.  
* :ref:`py_online_llm` — Este paso es **muy importante**: obtén tu clave API de **OpenAI** o **Doubao**, o la clave API de cualquier otro LLM compatible.

Ya deberías tener:

* Un **micrófono** y **altavoz** funcionando en tu PiCar-X.  
* Una **clave API válida** guardada en ``secret.py``.  
* Una conexión de red estable (se recomienda **conexión por cable** para mayor estabilidad).

----

Ejecutar el Ejemplo
-------------------

Ambas versiones de idioma están ubicadas en el mismo directorio:

.. code-block:: bash

   cd ~/picar-x/example

**Versión en inglés** (OpenAI GPT, instrucciones en inglés):

.. code-block:: bash

   sudo python3 21.voice_active_car_gpt.py

* LLM: ``OpenAI GPT-4o-mini``  
* TTS: ``en_US-ryan-low`` (Piper)  
* STT: Vosk (``en-us``)

Palabra de activación:

.. code-block::

   "Hey buddy"

---

**Versión en chino** (Doubao, instrucciones en chino):

.. code-block:: bash

   sudo python3 21.voice_active_car_doubao_cn.py

* LLM: ``Doubao-seed-1-6-250615``  
* TTS: ``zh_CN-huayan-x_low`` (Piper)  
* STT: Vosk (``cn``)

Palabra de activación:

.. code-block::

   "你好 滴滴"

.. note::

   Puedes modificar la **palabra de activación** y el **nombre del robot** en el código:  
   ``NAME = "Buddy"`` o ``NAME = "滴滴"``  
   ``WAKE_WORD = ["hey buddy"]`` o ``WAKE_WORD = ["你好 滴滴"]``

----

Qué Sucederá
-----------------

Cuando ejecutes este ejemplo correctamente:

* El robot **esperará la palabra de activación** (por ejemplo, “Hey Buddy” / “你好 滴滴”).  
* Cuando escuche la palabra de activación:

  * Los LED **parpadearán** y permanecerán encendidos.  
  * El robot **te saludará** con una voz alegre.

* Luego comenzará a **escuchar tu voz** en tiempo real.  
* Después de reconocer lo que dijiste:

  * Envía tu voz al **LLM** (OpenAI o Doubao).  
  * **Piensa** y parpadea los LED mientras procesa.  
  * Responde con **voz TTS**.  
  * Ejecuta **acciones correspondientes** (por ejemplo, asentir, girar, celebrar).

* Si te acercas demasiado, el sensor ultrasónico:

  * Activa un movimiento automático **hacia atrás** por seguridad.  
  * Interrumpe la interacción actual con una respuesta de advertencia.

**Ejemplo de interacción**

.. code-block:: text

   Tú: Hey Buddy
   Robot: ¡Hola!

   Tú: Gira a la izquierda y mira alrededor.
   Robot: ¡Recibido, girando mi cabeza a la izquierda como un gato curioso!
   ACCIONES: turn_left, look_left

----

Cambiar a Otros LLM o TTS
------------------------------

Puedes cambiar fácilmente a otros LLM, TTS o idiomas de STT con solo unas pocas ediciones:

* LLM compatibles:

  * OpenAI
  * Doubao
  * Deepseek
  * Gemini
  * Qwen
  * Grok

* :ref:`test_piper` — Verifica los idiomas compatibles de **Piper TTS**.  
* :ref:`test_vosk` — Verifica los idiomas compatibles de **Vosk STT**.  

Para cambiar, simplemente modifica la parte de inicialización en el código:

.. code-block:: python

   from picarx.llm import Gemini as LLM
   llm = LLM(api_key="YOUR_KEY", model="gemini-pro")

   # Establecer modelos e idiomas
   TTS_MODEL = "en_US-ryan-low"
   STT_LANGUAGE = "en-us"


----

Referencia de Acciones y Sonidos
-----------------------------------

A continuación se muestran las **palabras clave de acción** que el LLM puede devolver (después de la línea ``ACTIONS:``) y lo que hacen en el robot.

.. list-table::
   :header-rows: 1
   :widths: 20 55 25

   * - **Acción**
     - **Qué hace (según preset_actions.py)**
     - **Efecto / Notas**
   * - ``shake head``
     - Mueve rápidamente el ángulo de la cámara de derecha↔izquierda en pasos decrecientes y luego se centra.
     - Gesto de “No”; las ruedas permanecen detenidas.
   * - ``nod``
     - Inclina la cámara arriba↔abajo dos veces y luego se centra.
     - Gesto de “Sí”; las ruedas permanecen detenidas.
   * - ``wave hands``
     - Inclina la cámara y luego gira la dirección izquierda/derecha dos veces (±25°) y centra.
     - Saludo juguetón (usa el servo de dirección como “brazos”).
   * - ``resist``
     - Pequeña inclinación; alterna (giro ±15°, paneo ±15°) 3 veces; se detiene y centra.
     - Movimiento de “rechazo” o defensa.
   * - ``act cute``
     - Cabeza inclinada hacia abajo; pequeños movimientos hacia adelante y atrás (pulsos cortos de motor), luego restablece.
     - Movimiento “tierno” y alegre; movimientos muy cortos.
   * - ``rub hands``
     - Oscilación pequeña de la dirección (±6°) repetida cinco veces; restablece.
     - Imita “frotarse las manos”.
   * - ``think``
     - Paneo suave a la derecha + inclinación hacia abajo + giro a la derecha; breve pausa; pose pensativa; restablece.
     - Usado como animación de “pensar”.
   * - ``twist body``
     - Tres ciclos de avanzar corto/parar/pan-izquierda/giro-izquierda, luego retroceder corto/parar/pan-derecha/giro-derecha.
     - Da una sensación de “giro de cuerpo”.
   * - ``celebrate``
     - Inclina hacia arriba; dos florituras a la derecha (paneo/giro), luego dos a la izquierda; vuelve al centro.
     - Floritura festiva y simétrica.
   * - ``depressed``
     - Serie de inclinaciones descendentes con ángulos y pausas variables; termina tras una pausa larga y restablece.
     - Secuencia de “postura triste”.

Movimiento y Utilidades
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 22 58 20

   * - **Acción**
     - **Qué hace**
     - **Notas**
   * - ``forward``
     - Avanza a baja velocidad durante ~1 segundo, luego se detiene.
     - Implementado por ``forward(car)`` (5% de velocidad + 1 s).
   * - ``backward``
     - Retrocede a baja velocidad durante ~1 segundo, luego se detiene.
     - Implementado por ``backward(car)`` (5% de velocidad + 1 s).

Efectos de Sonido
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 24 56 20

   * - **Sonido**
     - **Qué hace**
     - **Notas**
   * - ``honking``
     - Reproduce ``car-double-horn.wav`` de forma asíncrona (volumen ~100).
     - Activado mediante ``Music.sound_play_threading``.
   * - ``start engine``
     - Reproduce ``car-start-engine.wav`` de forma asíncrona (volumen ~50).
     - Señal de inicio/listo.

Disparadores de Sensores (Automático)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Proximidad ultrasónica**

  * Disparador: distancia < 10 cm  
  * Efecto secundario: ``backward`` automático + desactivar imagen para esta ronda  
  * Mensaje inyectado: ``<<<Ultrasonic sense too close: {distance}cm>>>``

Ciclos de Vida (Indicadores LED)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ``before_listen`` → parpadea dos veces (listo para escuchar)  
* ``before_think`` → parpadeando (pensando)  
* ``before_say`` → LED encendido (hablando)  
* ``after_say`` → espera acciones → LED apagado  
* ``on_stop`` → detener acciones, cerrar dispositivos


----

Solución de Problemas
----------------------------

* **El robot no responde a la palabra de activación**  

  * Verifica si el micrófono funciona.  
  * Asegúrate de que ``WAKE_ENABLE = True``.  
  * Ajusta la palabra de activación para que coincida con tu pronunciación.

* **No sale sonido por el altavoz**
 
  * Verifica la configuración del modelo TTS.  
  * Prueba Piper o Espeak manualmente.  
  * Revisa la conexión del altavoz y el volumen.

* **Error de clave API o tiempo de espera agotado** 
 
  * Revisa tu clave en ``secret.py``.  
  * Asegura la conexión de red.  
  * Confirma que el LLM sea compatible.

* **Picar-X no se mueve ni actúa**
 
  * Comprueba que el nombre de la acción coincida con ``actions_dict``.  
  * Verifica las conexiones de los motores y servos.

* **El sensor ultrasónico se activa inesperadamente.**  

  * Revisa la altura y el ángulo de instalación del sensor.  
  * Ajusta el umbral de distancia ``TOO_CLOSE`` en el código.
