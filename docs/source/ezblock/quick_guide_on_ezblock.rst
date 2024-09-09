.. note::

    Hola, ¡bienvenido a la Comunidad de Entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook! Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirte?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos exclusivos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo!

.. _ezb_servo_adjust:

Guía rápida sobre EzBlock
===========================

.. note::

    Si estás utilizando una Raspberry Pi 5, no podrás usar nuestro software de programación gráfica, EzBlock, para programar el PiCrawler.


El rango de ángulo del servo es de -90 a 90°, pero el ángulo establecido en la fábrica es aleatorio, podría ser 0°, 45°, o cualquier otro; si lo ensamblamos con un ángulo así, esto puede provocar un estado caótico cuando el robot ejecute el código, o peor aún, el servo podría bloquearse y quemarse.

Por lo tanto, es necesario establecer todos los ángulos de los servos en 0° antes de instalarlos, de modo que el ángulo del servo esté centrado, independientemente de la dirección en la que se gire.

#. En primer lugar, :ref:`ezblock:install_ezblock_os_latest` (los tutoriales de EzBlock) en una tarjeta Micro SD, una vez que se complete la instalación, insértala en la Raspberry Pi.

    .. note::
        Después de completar la instalación, por favor regresa a esta página.

    .. image:: img/insert_sd_card.png
        :width: 500
        :align: center

#. Para asegurarte de que el servo se ha ajustado correctamente a 0°, primero inserta el brazo del servo en el eje del servo y luego gira suavemente el brazo de la palanca a un ángulo diferente. Este brazo es solo para que puedas ver claramente que el servo está girando.

    .. image:: img/servo_arm.png

#. Sigue las instrucciones del folleto de ensamblaje, inserta el cable de la batería y enciende el interruptor de encendido. Luego conecta un cable USB-C con corriente para activar la batería. Espera de 1 a 2 minutos, y escucharás un sonido que indicará que la Raspberry Pi se ha iniciado correctamente.

    .. image:: img/Z_BTR.JPG
        :width: 800
        :align: center

#. A continuación, conecta el cable del servo al puerto P11 como se muestra.

    .. image:: img/Z_P11.JPG

#. Mantén presionada la tecla **USR** y luego presiona la tecla **RST** para ejecutar el script de puesta a cero del servo dentro del sistema. Cuando veas que el brazo del servo gira a una posición (esta es la posición 0°, que es aleatoria y puede no ser vertical o paralela), indica que el programa ha funcionado.

    .. note::

        Este paso solo necesita hacerse una vez; luego, simplemente inserta otros cables de servos y se pondrán a cero automáticamente.

    .. image:: img/Z_P11_BT.png
        :width: 400
        :align: center
    
#. Ahora, retira el brazo del servo, asegurándote de que el cable del servo permanezca conectado, y no apagues la alimentación. Luego continúa con el ensamblaje siguiendo las instrucciones del papel.

.. note::

    * No desenchufes este cable del servo antes de asegurar este servo con el tornillo, puedes desenchufarlo después de asegurar.
    * No gires el servo mientras esté encendido para evitar daños; si el eje del servo se inserta en el ángulo incorrecto, retira el servo y vuelve a insertarlo.
    * Antes de ensamblar cada servo, necesitas conectar el cable del servo al P11 y encender el dispositivo para establecer su ángulo en 0°.
    * Esta función de puesta a cero se desactivará si luego descargas un programa en el robot con la APP de EzBlock.
