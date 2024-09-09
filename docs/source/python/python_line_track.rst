.. note::

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. ¡Profundiza en el mundo de Raspberry Pi, Arduino y ESP32 con otros entusiastas!

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones especiales en días festivos.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy.

.. _py_line_tracking:

5. Seguimiento de Línea
====================================

Este proyecto usará el módulo de escala de grises para hacer que el PiCar-X avance siguiendo una línea. 
Usa cinta de color oscuro para hacer una línea lo más recta posible y con pocas curvas. 
Puede que necesites experimentar un poco si el PiCar-X se sale de la línea.

**Ejecutar el Código**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 5.minecart_plus.py
    
Después de ejecutar el código, el PiCar-X se moverá hacia adelante siguiendo una línea.

**Código**

.. note::
    Puedes **Modificar/Restablecer/Copiar/Ejecutar/Detener** el código a continuación. Pero antes de eso, debes ir a la ruta del código fuente como ``picar-x/example``. Después de modificar el código, puedes ejecutarlo directamente para ver el efecto.

.. raw:: html

    <run></run>

.. code-block:: python

    from picarx import Picarx
    from time import sleep

    px = Picarx()
    # px = Picarx(grayscale_pins=['A0', 'A1', 'A2'])

    # Por favor, ejecuta ./calibration/grayscale_calibration.py para calibrar automáticamente los valores de escala de grises
    # o modifica manualmente los valores de referencia con el siguiente código
    # px.set_line_reference([1400, 1400, 1400])

    current_state = None
    px_power = 10
    offset = 20
    last_state = "stop"

    def outHandle():
        global last_state, current_state
        if last_state == 'left':
            px.set_dir_servo_angle(-30)
            px.backward(10)
        elif last_state == 'right':
            px.set_dir_servo_angle(30)
            px.backward(10)
        while True:
            gm_val_list = px.get_grayscale_data()
            gm_state = get_status(gm_val_list)
            print("outHandle gm_val_list: %s, %s"%(gm_val_list, gm_state))
            currentSta = gm_state
            if currentSta != last_state:
                break
        sleep(0.001)

    def get_status(val_list):
        _state = px.get_line_status(val_list)  # [bool, bool, bool], 0 significa línea, 1 significa fondo
        if _state == [0, 0, 0]:
            return 'stop'
        elif _state[1] == 1:
            return 'forward'
        elif _state[0] == 1:
            return 'right'
        elif _state[2] == 1:
            return 'left'

    if __name__=='__main__':
        try:
            while True:
                gm_val_list = px.get_grayscale_data()
                gm_state = get_status(gm_val_list)
                print("gm_val_list: %s, %s"%(gm_val_list, gm_state))

                if gm_state != "stop":
                    last_state = gm_state

                if gm_state == 'forward':
                    px.set_dir_servo_angle(0)
                    px.forward(px_power) 
                elif gm_state == 'left':
                    px.set_dir_servo_angle(offset)
                    px.forward(px_power) 
                elif gm_state == 'right':
                    px.set_dir_servo_angle(-offset)
                    px.forward(px_power) 
                else:
                    outHandle()
        finally:
            px.stop()
            print("stop and exit")
            sleep(0.1)
       

**¿Cómo funciona?** 

Este script de Python controla un coche robótico PiCarX utilizando sensores de escala de grises para la navegación. Aquí tienes un desglose de sus componentes principales:

* Importación e inicialización:

    El script importa la clase Picarx para controlar el coche robótico y la función sleep del módulo time para añadir retrasos.

    Se crea una instancia de Picarx, y hay una línea comentada que muestra una inicialización alternativa con pines específicos de sensores de escala de grises.

    .. code-block:: python
        
        from picarx import Picarx
        from time import sleep

        px = Picarx()

* Configuración y variables globales:

    ``current_state``, ``px_power``, ``offset`` y ``last_state`` son variables globales utilizadas para rastrear y controlar el movimiento del coche. ``px_power`` establece la potencia del motor, y ``offset`` se usa para ajustar el ángulo de dirección.

    .. code-block:: python

        current_state = None
        px_power = 10
        offset = 20
        last_state = "stop"

* Función ``outHandle``:

    Esta función se llama cuando el coche necesita manejar un escenario "fuera de la línea".

    Ajusta la dirección del coche según ``last_state`` y verifica los valores del sensor de escala de grises para determinar el nuevo estado.

    .. code-block:: python

        def outHandle():
            global last_state, current_state
            if last_state == 'left':
                px.set_dir_servo_angle(-30)
                px.backward(10)
            elif last_state == 'right':
                px.set_dir_servo_angle(30)
                px.backward(10)
            while True:
                gm_val_list = px.get_grayscale_data()
                gm_state = get_status(gm_val_list)
                print("outHandle gm_val_list: %s, %s"%(gm_val_list, gm_state))
                currentSta = gm_state
                if currentSta != last_state:
                    break
            sleep(0.001)

* Función ``get_status``:

    Interpreta los datos del sensor de escala de grises (``val_list``) para determinar el estado de navegación del coche.

    El estado del coche puede ser 'forward', 'left', 'right' o 'stop', dependiendo de qué sensor detecte la línea.

    .. code-block:: python
        
        def get_status(val_list):
            _state = px.get_line_status(val_list)  # [bool, bool, bool], 0 significa línea, 1 significa fondo
            if _state == [0, 0, 0]:
                return 'stop'
            elif _state[1] == 1:
                return 'forward'
            elif _state[0] == 1:
                return 'right'
            elif _state[2] == 1:
                return 'left'

* Bucle principal:

    El bucle ``while True`` verifica continuamente los datos de escala de grises y ajusta el movimiento del coche en consecuencia.

    Dependiendo del ``gm_state``, ajusta el ángulo de dirección y la dirección de movimiento.

    .. code-block:: python

        if __name__=='__main__':
            try:
                while True:
                    gm_val_list = px.get_grayscale_data()
                    gm_state = get_status(gm_val_list)
                    print("gm_val_list: %s, %s"%(gm_val_list, gm_state))

                    if gm_state != "stop":
                        last_state = gm_state

                    if gm_state == 'forward':
                        px.set_dir_servo_angle(0)
                        px.forward(px_power) 
                    elif gm_state == 'left':
                        px.set_dir_servo_angle(offset)
                        px.forward(px_power) 
                    elif gm_state == 'right':
                        px.set_dir_servo_angle(-offset)
                        px.forward(px_power) 
                    else:
                        outHandle()

* Seguridad y limpieza:

    El bloque ``try...finally`` asegura que el coche se detenga cuando el script sea interrumpido o finalizado.

    .. code-block:: python
        
        finally:
        px.stop()
        print("stop and exit")
        sleep(0.1)

En resumen, el script utiliza sensores de escala de grises para navegar el coche robótico PiCarX. Lee continuamente los datos del sensor para determinar la dirección y ajusta el movimiento y la dirección del coche en consecuencia. La función outHandle proporciona lógica adicional para situaciones en las que el coche necesita ajustar significativamente su ruta.
