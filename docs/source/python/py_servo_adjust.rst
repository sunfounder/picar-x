.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirte?**

    - **Soporte experto**: Resuelve problemas técnicos y de posventa con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos.
    - **Descuentos exclusivos**: Disfruta de descuentos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

Ajuste del Servo (Importante)
=============================

.. note::

    Si tu Robot HAT es versión V44 o superior (con el altavoz ubicado en la parte superior de la placa) e incluye un botón **Zero** integrado, puedes omitir este paso y simplemente presionar el botón **Zero** para activar el programa de centrado del servo.

    .. image:: img/robot_hat_v44.png
        :width: 500
        :align: center

El rango de ángulo del servo es de -90 a 90, pero el ángulo configurado de fábrica es aleatorio: puede ser 0°, 45° u otro valor.  
Si lo ensamblamos directamente con ese ángulo, provocará un estado caótico cuando el robot ejecute el código o, peor aún, hará que el servo se bloquee y se queme.

Por lo tanto, es necesario configurar todos los servos a 0° antes de instalarlos, de modo que el ángulo del servo quede en el punto medio, independientemente de la dirección en la que gire.

#. Para asegurarte de que el servo se haya configurado correctamente en 0°, primero inserta el brazo del servo en el eje y luego gira suavemente el brazo a un ángulo diferente.  
   Este brazo del servo es solo para que puedas ver claramente que el servo está girando.

    .. image:: img/servo_arm.png

#. Ahora, ejecuta ``servo_zeroing.py`` en la carpeta ``example/``.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/picar-x/example
        sudo python3 servo_zeroing.py

#. A continuación, conecta el cable del servo al puerto P11 como se muestra a continuación. Al mismo tiempo, verás que el brazo del servo gira a una posición (esta es la posición de 0°, que es una ubicación aleatoria y puede no ser vertical ni paralela).


    .. image:: img/Z_P11.jpg

#. Ahora, retira el brazo del servo asegurándote de que el cable del servo permanezca conectado y no apagues la alimentación. Luego continúa con el ensamblaje siguiendo las instrucciones en papel.

.. note::

    * No desconectes el cable del servo antes de fijarlo con el tornillo del servo; puedes desconectarlo después de fijarlo.
    * No gires el servo mientras esté encendido para evitar daños; si el eje del servo no está insertado en el ángulo correcto, retira el servo y vuelve a insertarlo.
    * Antes de ensamblar cada servo, debes conectar el cable del servo al P11 y encender la alimentación para ajustar su ángulo a 0°.

