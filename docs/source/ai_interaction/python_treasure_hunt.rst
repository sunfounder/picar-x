.. note::

    Hola, ¡bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook! Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirte?**

    - **Soporte de expertos**: Resuelve problemas post-venta y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y avances exclusivos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _py_treasure:

20. Búsqueda del Tesoro
============================

En esta lección, convertirás tu PiCar-X en un **robot cazatesoros**.  
Organiza un laberinto en tu habitación y coloca seis tarjetas de diferentes colores en distintas esquinas.  
Tu PiCar-X **buscará, reconocerá y celebrará** cuando encuentre el color objetivo.  

Este proyecto combina tres habilidades que has aprendido hasta ahora:

* **Visión por Computador** – detección de tarjetas de color con la cámara Pi.  
* **Control por Teclado** – conducción manual del robot a través del laberinto.  
* **Retroalimentación por Voz** – Pico2Wave anuncia el color objetivo y el éxito.  

¡Es un juego divertido que muestra cómo los robots pueden **ver, pensar y actuar** como cazatesoros!

   
Antes de Empezar
----------------

Asegúrate de haber completado:

* :ref:`install_all_modules` — Instala los módulos ``robot-hat``, ``vilib``, ``picar-x`` y luego ejecuta el script ``i2samp.sh``.
* Puedes descargar e imprimir las :download:`Tarjetas de Color en PDF <https://github.com/sunfounder/sf-pdf/raw/master/prop_card/object_detection/color-cards.pdf>` para una detección de color fiable.  

Ejecutar el Código
----------------------------

.. raw:: html

    <run></run>

.. code-block:: bash

    cd ~/picar-x/example
    sudo python3 20.treasure_hunt.py

Después de ejecutar, verás un mensaje como este:

.. code-block:: text

    * Running on http://0.0.0.0:9000/ (Press CTRL+C to quit)

Luego, abre ``http://<your IP>:9000/mjpg`` en tu navegador para ver el video en vivo.  
Ejemplo: ``http://192.168.18.113:9000/mjpg``  

.. image:: img/display.png

Reglas del Juego
--------------------

1. El robot selecciona aleatoriamente un **color objetivo** y dice: **“¡Busca rojo!”**  
2. Conduces el PiCar-X con el teclado:  

   * ``w`` = avanzar  
   * ``a`` = girar a la izquierda  
   * ``s`` = retroceder  
   * ``d`` = girar a la derecha  
   * ``space`` = repetir objetivo  
   * ``Ctrl+C`` = salir  

3. Cuando la cámara ve la tarjeta del color objetivo, el PiCar-X dice **“¡Bien hecho!”**  
4. Se elige un nuevo color objetivo y ¡la búsqueda continúa!  

Código
-----------

.. code-block:: python

    #!/usr/bin/env python3

    from picarx import Picarx
    from vilib import Vilib
    from picarx.tts import Pico2Wave

    from time import sleep
    import threading
    import readchar
    import random

    # -----------------------
    # Settings
    # -----------------------
    COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
    DETECTION_WIDTH_THRESHOLD = 100  # how wide the color blob must be
    DRIVE_SPEED = 80
    TURN_ANGLE = 30

    MANUAL = """
    Press keys to control PiCar-X:
      w: forward    a: turn left    s: backward    d: turn right
      space: repeat target          Ctrl+C: quit
    """

    # -----------------------
    # Init
    # -----------------------
    px = Picarx()

    tts = Pico2Wave()
    tts.set_lang("en-US")

    current_color = "red"
    key = None
    lock = threading.Lock()

    def say(line: str):
        print(f"[SAY] {line}")
        tts.say(line)

    def renew_color_detect():
        """Choose a new target color and start detection."""
        global current_color
        current_color = random.choice(COLORS)
        Vilib.color_detect(current_color)
        say(f"Look for {current_color}!")

    def key_scan_thread():
        """Background thread reading keys."""
        global key
        while True:
            k = readchar.readkey()
            # Map special keys before lowercasing
            if k == readchar.key.SPACE:
                mapped = "space"
            elif k == readchar.key.CTRL_C:
                mapped = "quit"
            else:
                mapped = k.lower()

            with lock:
                key = mapped

            if mapped == "quit":
                return
            sleep(0.01)

    def car_move(k: str):
        if k == "w":
            px.set_dir_servo_angle(0)
            px.forward(DRIVE_SPEED)
        elif k == "s":
            px.set_dir_servo_angle(0)
            px.backward(DRIVE_SPEED)
        elif k == "a":
            px.set_dir_servo_angle(-TURN_ANGLE)
            px.forward(DRIVE_SPEED)
        elif k == "d":
            px.set_dir_servo_angle(TURN_ANGLE)
            px.forward(DRIVE_SPEED)

    def main():
        global key

        # Start camera and web preview
        Vilib.camera_start(vflip=False, hflip=False)
        Vilib.display(local=False, web=True)
        sleep(0.8)

        print(MANUAL.strip())
        say("Game start!")
        sleep(0.1)
        renew_color_detect()

        # Start keyboard thread (modern style)
        key_thread = threading.Thread(target=key_scan_thread, daemon=True)
        key_thread.start()

        try:
            while True:
                # Check detection: if target color present and wide enough
                if (Vilib.detect_obj_parameter.get("color_n", 0) != 0 and
                    Vilib.detect_obj_parameter.get("color_w", 0) > DETECTION_WIDTH_THRESHOLD):
                    say("Well done!")
                    sleep(0.1)
                    renew_color_detect()

                # Take a snapshot of the last key (and clear it)
                with lock:
                    k = key
                    key = None

                # Handle movement / actions
                if k in ("w", "a", "s", "d"):
                    car_move(k)
                    sleep(0.5)
                    px.stop()
                elif k == "space":
                    say(f"Look for {current_color}!")
                elif k == "quit":
                    print("\n[INFO] Quit requested.")
                    break

                sleep(0.05)

        except KeyboardInterrupt:
            print("\n[INFO] Stopped by user.")
        finally:
            try:
                Vilib.camera_close()
            except Exception:
                pass
            px.stop()
            say("Goodbye!")
            sleep(0.2)

    if __name__ == "__main__":
        main()

Cómo Funciona
----------------------------

1. **Inicialización** 

   * Importa los módulos y configura PiCar-X, la cámara y TTS.  
   * Define la lista de colores, la velocidad y el ángulo de dirección.  

2. **Selección del Objetivo**

   * ``renew_color_detect()`` elige aleatoriamente un color objetivo.  
   * El robot anuncia el objetivo con Pico2Wave.  

3. **Control por Teclado** 

   * ``key_scan_thread()`` se ejecuta en segundo plano para capturar las teclas.  
   * Las teclas ``w, a, s, d`` controlan el movimiento; ``space`` repite el objetivo.  

4. **Detección de Color**  

   * La cámara verifica constantemente si el color objetivo es visible.  
   * Si el área detectada es lo suficientemente grande, PiCar-X celebra.  

5. **Bucle Principal**

   * Gestiona continuamente el movimiento, la detección y la retroalimentación.  
   * Detiene el robot y la cámara de forma limpia al salir.  

Solución de Problemas
-------------------------

* **¿La cámara no transmite imagen?**  

  Ejecuta ``libcamera-hello`` para comprobar si la cámara Pi está correctamente conectada.  

* **¿El robot no detecta colores?** 

  Asegúrate de que las tarjetas estén impresas con claridad y colocadas con buena iluminación. Prueba ajustando ``DETECTION_WIDTH_THRESHOLD``.  

* **¿Sin retroalimentación de voz?**  

  Verifica que ``pico2wave`` esté instalado y que tu salida de audio esté configurada correctamente.  

* **¿El coche no se mueve?**  

  Confirma que la PiCar-X esté encendida y que la calibración del motor sea correcta.  

----

Al completar esta lección, habrás creado un **mini juego de búsqueda del tesoro** con PiCar-X,  
combinando **visión, control e interacción** en un solo proyecto.
