.. _picarx_skill:

.. start_using_picarx

22. Usar OpenClaw para Controlar el PiCar-X
==============================================


**¿Qué es OpenClaw?**

Considéralo como una versión mejorada de ChatGPT. Mientras que los chatbots tradicionales solo pueden hablar (generar texto), OpenClaw puede actuar. Entiende tus instrucciones en lenguaje natural y puede realizar operaciones en tu ordenador, como ejecutar comandos, gestionar archivos y llamar a diversas herramientas.

Aquí tienes algunos escenarios de aplicación fantásticos:

* **Asistente personal todoterreno:** Deja que te ayude a gestionar tu agenda, establecer recordatorios y hacer seguimiento de tareas. Solo tienes que decírselo en una app de mensajería (como Telegram, WhatsApp), y él lo recordará y ejecutará.
* **Pegamento de automatización:** Puede actuar como aglutinante para tus diversos servicios. Por ejemplo, puedes pedirle que monitorice un sitio web en busca de cambios de precio. Una vez detectada una bajada de precio, puede activar automáticamente un flujo de trabajo n8n para enviarte una notificación por correo electrónico.
* **Asistente de desarrollo dedicado:** Pídele que te ayude a gestionar servidores, ejecutar scripts y revisar logs. Puedes simplemente decir: «Comprueba la carga del sistema», y él puede conectarse por SSH a tu servidor, ejecutar el comando y devolver los resultados.
* **Compañero de hardware:** Este es un caso de uso muy interesante. Puedes hacer que OpenClaw controle el hardware conectado a una Raspberry Pi. Por ejemplo, un desarrollador lo usó para controlar un aspirador robótico con un brazo mecánico, o incluso para analizar datos de un simulador de carreras y mostrarlos en una pantalla LED. ¡El equipo oficial de Raspberry Pi incluso lo usó para construir un fotomatón automático para una boda, simplemente conversando, sin escribir una sola línea de código!


.. important::

   La Raspberry Pi Zero 2W tiene solo 512 MB de RAM, mientras que OpenClaw requiere un mínimo de 1 GB. Por lo tanto, no puede funcionar correctamente. Se recomienda una Raspberry Pi 4/5 o superior.

Inicio Rápido de OpenClaw
-------------------------------

Si quieres experimentar la potencia de OpenClaw lo más rápido posible, usa este método. Instalará y lanzará automáticamente un asistente de configuración interactivo.

1.  Abre el terminal en tu Raspberry Pi y ejecuta directamente el siguiente comando. Este comando descarga el script de instalación desde el sitio oficial y lo ejecuta:

    .. code-block:: bash

       curl -fsSL https://openclaw.ai/install.sh | bash

    .. note:: Dado que las nuevas versiones se actualizan rápidamente, es normal que los pasos de instalación difieran ligeramente.

2.  El script descargará e instalará automáticamente OpenClaw.

    .. image:: /img/openclaw/install_open_claw.png


3.  A continuación verás un aviso de seguridad preguntándote si confías en OpenClaw. Una vez que estés seguro de que es fiable, usa las teclas de flecha para navegar hasta «Yes» y pulsa Enter.

    .. image:: /img/openclaw/security_open_claw.png


4.  Selecciona Quick Start, luego pulsa Enter.

    .. image:: /img/openclaw/quickstart_open_claw.png

5.  Selecciona tu modelo, luego pulsa Enter. Aquí usamos OpenAI como ejemplo.

    .. image:: /img/openclaw/model_provider_open_claw.png

6.  Selecciona OpenAI API Key.

    .. image:: /img/openclaw/api_key_open_claw.png

7.  Pega la clave API ahora.

    .. image:: /img/openclaw/paste_api_key_open_claw.png

8.  Ve a |link_openai_platform| e inicia sesión. En la página **API keys**, haz clic en **Create new secret key**.

    .. image:: /img/openclaw/llm_openai_create.png

9.  Rellena los detalles (Owner, Name, Project y permisos si es necesario), luego haz clic en **Create secret key**.

    .. image:: /img/openclaw/llm_openai_create_confirm.png

10. Una vez creada la clave, cópiala inmediatamente — no podrás volver a verla. Si la pierdes, tendrás que generar una nueva.

    .. image:: /img/openclaw/llm_openai_copy.png

11. Pega la clave en la configuración de OpenClaw.

    .. image:: /img/openclaw/paste_api_key_enter_open_claw.png

12. Selecciona el modelo que deseas usar. En este ejemplo, usaremos **Keep current**.

    .. image:: /img/openclaw/model_config_open_claw.png

13. A continuación viene la selección del canal. Los canales se refieren a los servicios de comunicación soportados por OpenClaw, como Telegram, WhatsApp, Discord y más. Usa la flecha hacia abajo para seleccionar la opción «Skip for now», luego pulsa Enter.

    .. image:: /img/openclaw/channel_open_claw.png

14. A continuación, se te pedirá que configures las habilidades inmediatamente. Selecciona «Yes» y pulsa Enter.

    .. image:: /img/openclaw/config_skill_open_claw.png

15. Instala las habilidades que necesites. En el siguiente ejemplo, seleccionamos la opción «Skip for now» (pulsa la barra espaciadora para seleccionar), luego pulsa Enter.

    .. image:: /img/openclaw/install_skill_open_claw.png

16. Luego vienen los Hooks; marcaremos «command-logger» y «session-memory».

    .. image:: /img/openclaw/hooks2_open_claw.png


17. La instalación está completa. Puedes iniciar OpenClaw seleccionando «Hatch in TUI» y pulsando Enter.

   .. image:: /img/openclaw/hatch_open_claw.png


.. note::

   Puedes iniciar OpenClaw introduciendo el siguiente comando:

    .. code-block:: bash

       openclaw tui

   Y puedes pulsar ctrl+c dos veces para salir de la interfaz TUI.

------------------------------------------------------------------------

Hacer que OpenClaw Controle el PiCar-X
----------------------------------------------

**¿Qué es la habilidad PiCar-X?**

La habilidad PiCar-X es una extensión para OpenClaw que te permite controlar tu coche robot SunFounder PiCar-X mediante lenguaje natural. En lugar de escribir scripts de Python o memorizar ángulos de servo, puedes simplemente decirle a OpenClaw lo que quieres que haga el PiCar-X — como «avanza», «comprueba qué hay delante» o «gira a la izquierda» — y OpenClaw ejecutará automáticamente el código Python apropiado.

Aquí tienes algunas cosas que puedes hacer con la habilidad PiCar-X:

* **Conducción:** Avanzar, retroceder, girar a la izquierda/derecha con control del servo de dirección
* **Cámara orientable:** Panorámica izquierda/derecha, inclinación arriba/abajo mediante la cámara de 2 ejes
* **Sensores:** Leer distancia ultrasónica, datos del sensor de escala de grises para seguimiento de línea y detección de precipicios
* **Sonido:** Reproducir efectos de sonido y música a través del altavoz del coche
* **Visión artificial:** Tomar fotos, detectar rostros, seguir colores, reconocer códigos QR, gestos y señales de tráfico

----------------------------------------------------------------

Prerrequisitos
------------------------------

Antes de poder usar la habilidad PiCar-X con OpenClaw, asegúrate de tener:

1. **PiCar-X** correctamente montado y conectado a tu Raspberry Pi
2. **OpenClaw** instalado y en funcionamiento
3. Las siguientes bibliotecas de Python instaladas:

   - ``picarx``
   - ``robot_hat``
   - ``vilib``

Puedes verificar la instalación ejecutando:

.. code-block:: bash

   python3 -c "import picarx"

Si este comando se ejecuta sin errores, estás listo para continuar.

----------------------------------------------------------------

Instalar la Habilidad PiCar-X
------------------------------

Sigue estos pasos para instalar la habilidad PiCar-X para OpenClaw:

1. **Copia los archivos de la habilidad PiCar-X** al directorio de habilidades de OpenClaw:

   .. code-block:: bash

      cp -r ~/picar-x/picarx-control ~/.openclaw/workspace/skills/

2. **Verifica la instalación** comprobando los archivos de la habilidad:

   .. code-block:: bash

      ls ~/.openclaw/workspace/skills/picarx-control/

   Deberías ver ``SKILL.md``, ``install.sh``, ``scripts/`` y ``references/`` en la salida.

El archivo ``SKILL.md`` de la habilidad contiene todas las instrucciones que OpenClaw necesita — reglas de seguridad, plantillas de código para cada capacidad y un mapeo de solicitudes en lenguaje natural a código Python. OpenClaw lee este archivo y lo usa para decidir qué código ejecutar en tu PiCar-X.

----------------------------------------------------------------

Probar la Habilidad PiCar-X desde la CLI
----------------------------------------------

Antes de usar la habilidad con OpenClaw, puede que quieras probar la funcionalidad básica directamente desde el terminal usando la herramienta CLI incluida.

**Comprobar la distancia ultrasónica:**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/picarx-control/scripts/pc.py sensor distance

**Avanzar:**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/picarx-control/scripts/pc.py move forward --speed 60

**Retroceder:**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/picarx-control/scripts/pc.py move backward --speed 60

**Girar a la izquierda:**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/picarx-control/scripts/pc.py turn left --angle 30

**Girar a la derecha:**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/picarx-control/scripts/pc.py turn right --angle 30

**Establecer ángulo de panorámica de la cámara:**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/picarx-control/scripts/pc.py cam pan --angle 30

**Establecer ángulo de inclinación de la cámara:**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/picarx-control/scripts/pc.py cam tilt --angle 20

**Reproducir un efecto de sonido:**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/picarx-control/scripts/pc.py sound play /path/to/sound.wav --volume 80

**Leer datos del sensor de escala de grises (seguimiento de línea):**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/picarx-control/scripts/pc.py sensor grayscale

**Ejecutar calibración de servos:**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/picarx-control/scripts/pc.py calibrate

----------------------------------------------------------------

Usar la Habilidad PiCar-X en OpenClaw
----------------------------------------------------

Una vez que hayas verificado que la habilidad PiCar-X funciona desde la línea de comandos, puedes empezar a usarla dentro de OpenClaw.

1. **Inicia OpenClaw TUI**:

   .. code-block:: bash

      openclaw tui

2. **Envía comandos en lenguaje natural** para controlar el PiCar-X. Aquí tienes algunos ejemplos:

   * «Avanza»
   * «Retrocede»
   * «Gira a la izquierda»
   * «Gira a la derecha»
   * «Comprueba si hay algo delante»
   * «Mira a la izquierda»
   * «Mira hacia arriba»
   * «Mira hacia abajo»
   * «Toma una foto»
   * «Detecta rostros»
   * «Encuentra el color rojo»
   * «Sigue la línea»
   * «Comprueba si hay un precipicio delante»

3. **OpenClaw traducirá automáticamente** tu solicitud al código Python apropiado y lo ejecutará en el PiCar-X.

----------------------------------------------------------------

Acciones y Comandos Disponibles
-------------------------------------------

Aquí está la lista completa de capacidades soportadas por la habilidad PiCar-X:

Conducción (``pc.py move``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Acción
     - Descripción
   * - ``forward``
     - Avanzar
   * - ``backward``
     - Retroceder

Dirección (``pc.py turn``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Acción
     - Descripción
   * - ``left``
     - Girar a la izquierda ajustando el ángulo de dirección
   * - ``right``
     - Girar a la derecha ajustando el ángulo de dirección

Cámara orientable (``pc.py cam``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Capacidad
     - Descripción
   * - Panorámica
     - Rotar la cámara horizontalmente (de -90° a 90°)
   * - Inclinación
     - Inclinar la cámara verticalmente (de -35° a 65°)

Sensores
^^^^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Comando
     - Descripción
   * - ``sensor distance``
     - Leer el sensor de distancia ultrasónico (devuelve cm)
   * - ``sensor grayscale``
     - Leer los valores del módulo de escala de grises de 3 canales (para seguimiento de línea y detección de precipicios)

Sonido (``pc.py sound``)
^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Comando
     - Descripción
   * - ``sound play <archivo>``
     - Reproducir un archivo de efecto de sonido
   * - ``sound music <archivo>``
     - Reproducir música de fondo
   * - ``sound volume <0-100>``
     - Establecer el volumen del altavoz
   * - ``sound stop``
     - Detener la reproducción

.. note::

   Los archivos de sonido pueden ser cualquier archivo de audio en formato ``.wav`` accesible en tu Raspberry Pi. También puedes usar ``sound music`` para reproducir archivos de música de fondo.

Cámara y Visión (vía lenguaje natural / exec)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Capacidad
     - Descripción
   * - Tomar foto
     - Capturar y guardar una foto en ``~/Pictures/``
   * - Detección de rostros
     - Detectar rostros humanos e informar de la posición
   * - Detección de color
     - Localizar objetos por color (rojo, azul, verde, etc.)
   * - Reconocimiento de gestos
     - Reconocer gestos de piedra/papel/tijera
   * - Detección de señales de tráfico
     - Reconocer señales de stop/izquierda/derecha/adelante
   * - Escaneo de códigos QR
     - Leer datos y posición de códigos QR

Seguimiento de Línea y Detección de Precipicios
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Capacidad
     - Descripción
   * - Seguimiento de línea
     - Seguir una línea negra sobre una superficie clara usando el sensor de escala de grises de 3 canales
   * - Detección de precipicios
     - Detectar bordes/caídas usando los valores de umbral del sensor de escala de grises

----------------------------------------------------------------

Solución de Problemas
------------------------------

Problemas con OpenClaw
^^^^^^^^^^^^^^^^^^^^^^^^

P. Durante la instalación, obtengo el error ``Error: systemctl is-enabled unavailable: Command failed: systemctl --user is-enabled openclaw-gateway.service``. ¿Qué debo hacer?

   Puedes ignorarlo por ahora, pero podrías encontrar problemas en los siguientes pasos. Por favor, consúltalos uno por uno en ese momento.


P. Cuando ejecuto ``openclaw tui``, obtengo el error ``-bash: openclaw: command not found``. ¿Qué debo hacer?

   Ejecuta el siguiente comando:

   .. code-block:: bash

      echo 'export PATH="$HOME/.npm-global/bin:$PATH"' >> ~/.bashrc
      source ~/.bashrc

   Ahora deberías poder iniciar la interfaz TUI con ``openclaw tui``.



P. En ``openclaw tui``, me encuentro con ``not connected to gateway — message not sent`` o el mensaje ``gateway disconnected: closed``.

   Esto se debe a que tu servicio OpenClaw Gateway no está iniciado. Abre otro terminal y ejecuta el siguiente comando para iniciar el OpenClaw Gateway:

   .. code-block:: bash

      openclaw gateway

   Luego reinicia ``openclaw tui``, y podrás usarlo directamente.


P. Quiero configurar el servicio OpenClaw Gateway para que se ejecute en segundo plano / se inicie automáticamente al arrancar. ¿Cómo lo hago?

   Normalmente, tu servicio OpenClaw Gateway debería iniciarse automáticamente al arrancar. Si no lo hace, puedes iniciarlo manualmente con el siguiente comando.

   1. Crea el directorio ``~/.config/systemd/user``:

   .. code-block:: bash

      mkdir -p ~/.config/systemd/user


   2. Crea el archivo ``openclaw-gateway.service``:

   .. code-block:: bash

      cat > ~/.config/systemd/user/openclaw-gateway.service << EOF
      [Unit]
      Description=OpenClaw Gateway
      After=network.target

      [Service]
      Type=simple
      ExecStart=$HOME/.npm-global/bin/openclaw gateway run
      Restart=on-failure
      RestartSec=10
      Environment="PATH=$HOME/.npm-global/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin"
      Environment="NODE_ENV=production"

      [Install]
      WantedBy=default.target
      EOF


   3. Luego recarga la configuración de systemd:

   .. code-block:: bash

      systemctl --user daemon-reload

   4. Inicia el servicio:

   .. code-block:: bash

      systemctl --user start openclaw-gateway

   En este punto, reinicia ``openclaw tui``, y podrás usarlo directamente.

   5. Actívalo para que se inicie al arrancar:

   .. code-block:: bash

      systemctl --user enable openclaw-gateway


P. Mi OpenClaw no puede interactuar con el sistema, ¿qué debo hacer?

   Un OpenClaw recién instalado puede no tener permiso para interactuar con tu sistema Raspberry Pi por defecto; solo puede chatear. Necesitamos configurar manualmente los permisos.

   1.  Abre el archivo de configuración de OpenClaw:

      .. code-block:: bash

         nano ~/.openclaw/openclaw.json

   2.  Encuentra la opción ``tools`` y modifica ``profile`` y ``exec`` como se muestra.

      .. code-block:: json

        "tools": {
            "profile": "coding",
            "exec": {
                "secrity": "full"
            }
        },

   3.  Guarda y sale.

   4.  Introduce el siguiente comando en el terminal para reiniciar el OpenClaw Gateway:

      .. code-block:: bash

         openclaw gateway restart

   Ahora, OpenClaw debería tener permisos de lectura y escritura y poder interactuar con tu sistema Raspberry Pi.

Problemas con el PiCar-X
^^^^^^^^^^^^^^^^^^^^^^^^


P. El PiCar-X no responde a los comandos. ¿Qué debo hacer?

   Primero, verifica que el PiCar-X esté correctamente conectado y encendido. Luego prueba la funcionalidad básica:

   .. code-block:: bash

      python3 ~/.openclaw/workspace/skills/picarx-control/scripts/pc.py sensor distance

   Si esto falla, asegúrate de que las bibliotecas Python requeridas estén instaladas:

   .. code-block:: bash

      python3 -c "import picarx; import robot_hat; import vilib"

P. La prueba ``import picarx`` falla.

   Esto significa que la biblioteca Python de PiCar-X no está instalada correctamente. Consulta la guía oficial de instalación de PiCar-X para instalar las bibliotecas necesarias. También puedes ejecutar el script de instalación incluido:

   .. code-block:: bash

      bash ~/.openclaw/workspace/skills/picarx-control/install.sh

P. OpenClaw no reconoce la habilidad PiCar-X.

   Recuerda a OpenClaw que sincronice las habilidades diciendo en el TUI: *«Please rsync my skills»* o reinicia el OpenClaw Gateway:

   .. code-block:: bash

      openclaw gateway restart

P. Los movimientos del PiCar-X parecen bruscos o la dirección está descentrada.

   Esto suele deberse a valores de calibración de los servos incorrectos. Ejecuta el script de calibración para ajustar el servo de dirección y la cámara orientable:

   .. code-block:: bash

      python3 ~/.openclaw/workspace/skills/picarx-control/scripts/pc.py calibrate

   También puedes ajustar el parámetro de velocidad (por ejemplo, usa ``--speed 40``) para un movimiento más suave, o añadir pausas cortas entre comandos consecutivos.

P. El seguimiento de línea o la escala de grises no funciona correctamente.

   Asegúrate de que el módulo de escala de grises esté correctamente calibrado para tu superficie. Puedes establecer los valores de referencia de línea usando la configuración. Consulta la documentación principal de PiCar-X para los procedimientos de calibración de escala de grises.

----------------------------------------------------------------

.. end_using_picarx
