.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 con otros apasionados.

    **¿Por qué unirte?**

    - **Soporte experto**: Resuelve problemas técnicos y posventa con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos exclusivos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _py_cliff:

6. Detección de acantilados 
===============================

Vamos a dotar al PiCar-X de un poco de conciencia de autoprotección y enseñarle a usar su propio módulo de escala de grises para evitar caer por un acantilado.

En este ejemplo, el coche estará en reposo. 
Si lo empujas hacia un acantilado, se activará de inmediato, retrocederá y dirá "peligro".

**Ejecutar el código**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 6.cliff_detection.py
    

**Código**

.. note::
    Puedes **Modificar/Restablecer/Copiar/Ejecutar/Detener** el código a continuación. Pero antes de eso, debes ir a la ruta del código fuente como ``picar-x/example``. Después de modificar el código, puedes ejecutarlo directamente para ver el efecto.

.. raw:: html

    <run></run>

.. code-block:: python

    from picarx import Picarx
    from time import sleep
    from robot_hat import TTS

    tts = TTS()
    tts.lang("en-US")

    px = Picarx()
    # px = Picarx(grayscale_pins=['A0', 'A1', 'A2'])
    # modificar manualmente el valor de referencia
    px.set_cliff_reference([200, 200, 200])

    current_state = None
    px_power = 10
    offset = 20
    last_state = "safe"

    if __name__=='__main__':
        try:
            while True:
                gm_val_list = px.get_grayscale_data()
                gm_state = px.get_cliff_status(gm_val_list)
                # print("El estado del acantilado es:  %s"%gm_state)

                if gm_state is False:
                    state = "safe"
                    px.stop()
                else:
                    state = "danger"   
                    px.backward(80)
                    if last_state == "safe":
                        tts.say("danger")
                        sleep(0.1)
                last_state = state

        finally:
            px.stop()
            print("stop and exit")
            sleep(0.1)

**¿Cómo funciona?** 

La función para detectar acantilados funciona así:

* ``get_grayscale_data()``: Este método proporciona directamente las lecturas de los tres sensores, de derecha a izquierda. Cuanto más brillante sea la zona, mayor será el valor obtenido.

* ``get_cliff_status(gm_val_list)``: Este método compara las lecturas de las tres sondas y da un resultado. Si el resultado es verdadero, se detecta que hay un acantilado delante del coche.

