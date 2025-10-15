.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 junto con otros entusiastas.

    **¿Por qué unirte?**

    - **Soporte experto**: Resuelve problemas técnicos y de posventa con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

1. ¿Qué Más Necesitas?
===============================

Antes de comenzar a jugar con PiCar-X, vamos a preparar el hardware esencial.  
Piensa en estos componentes como el **cerebro, corazón y sentidos** de PiCar-X — sin ellos, el coche no puede funcionar correctamente.

Componentes Requeridos
------------------------------

* **Raspberry Pi**

  La Raspberry Pi actúa como el **cerebro** de PiCar-X, encargándose de todas las tareas de cálculo, sensado y control.  
  
  .. image:: img/need_pi.jpg

  * **Modelos compatibles**: Raspberry Pi 5, 4, 3 y Raspberry Pi Zero 2 W (mejor en Pi 5 o Pi 4).  
  * **Mínimo**: **2GB de RAM** — suficiente para todas las funciones estándar de PiCar-X (movimiento, sensores, transmisión de cámara) y para usar **servicios de IA en línea** como OpenAI Whisper, TTS o LLMs.  
  * **Recomendado**: **4GB de RAM o más** — garantiza un mejor rendimiento al ejecutar **modelos de IA locales** (por ejemplo, reconocimiento de voz con Vosk, TTS con Piper o LLMs ligeros) junto con transmisión de cámara y tareas de control.  
  

* **Adaptador de Corriente**

  PiCar-X viene con un **paquete de baterías 18650** y una placa **Robot HAT** con un circuito de carga incorporado.
  
  .. image:: img/need_power.png
    :width: 400

  * Para cargarlo, se recomienda usar una **fuente de alimentación de 5V 3A**, como el **adaptador USB-C oficial de 15W de Raspberry Pi**.  
  * También puedes usar un cargador **USB-C Power Delivery (PD)** o un cargador rápido **QC 2.0**.  
  * Una carga completa suele tardar unos **2 horas** (de 0 % a 100 %).  


* **Tarjeta Micro SD**

  La Raspberry Pi no tiene disco duro incorporado. Arranca y almacena todos los archivos en una **tarjeta Micro SD**.  
  
  .. image:: img/need_sd.jpg
    :width: 200

  * Mínimo: **16GB**  
  * Recomendado: **32GB** para mayor estabilidad  
  * Marca: Usa opciones confiables como **SanDisk** o **Samsung** para evitar errores de lectura/escritura  
  

Componentes Opcionales
------------------------

Aunque no son estrictamente necesarios, los siguientes periféricos mejorarán mucho tu experiencia de aprendizaje y depuración:

* **Monitor (HDMI o TV)** 

  Para principiantes, recomendamos usar una pantalla con entrada HDMI, ya que facilita la configuración del sistema operativo Raspberry Pi y la ejecución de programas gráficos.  

  .. image:: img/need_screen.png
    :width: 400

* **Cable HDMI (Estándar / Mini / Micro)**
 
  Los distintos modelos de Raspberry Pi usan diferentes conectores HDMI, asegúrate de revisar tu modelo y preparar el cable correcto. 
  
  * **Raspberry Pi 4 / 5**: Micro HDMI  
  * **Raspberry Pi 3**: HDMI estándar  
  * **Raspberry Pi Zero 2W**: Mini HDMI 

  .. image:: img/need_hdmi.png
    :width: 400

* **Teclado y Ratón**

  Muy útiles durante la configuración inicial de Raspberry Pi OS.  
  Más adelante, podrás usar acceso remoto (SSH/VNC), pero para principiantes recomendamos preparar un set USB o inalámbrico básico.  

  .. image:: img/need_keyboard_mouse.png
    :width: 500
 

**Consejos para la Preparación**

* Si compraste el **kit PiCar-X**, la mayoría de los accesorios ya están incluidos, pero **debes preparar la placa Raspberry Pi, la tarjeta Micro SD y el adaptador de corriente por separado**.  
* ¿No sabes qué comprar? 👉 La opción más estable y universal es:  
  **Raspberry Pi 4 (2GB) + Fuente de alimentación oficial + Tarjeta Micro SD de 32GB**.
