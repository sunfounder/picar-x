.. note::

    ¡Hola, bienvenido a la Comunidad de Entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook! Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirte?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos exclusivos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo!

6. Habilitar la Interfaz I2C (Importante)
==============================================

Vamos a utilizar la interfaz I2C de Raspberry Pi. Esta interfaz debería haber sido habilitada al instalar el módulo ``robot-hat`` anteriormente. Para asegurarnos de que todo esté en orden, revisemos si está efectivamente habilitada.

#. Introduce el siguiente comando:

    .. raw:: html

        <run></run>

    .. code-block:: 

        sudo raspi-config

#. Elige **Interfacing Options** presionando la tecla de flecha hacia abajo en tu teclado y luego presiona la tecla **Enter**.

    .. image:: img/image282.png
        :align: center

#. Luego selecciona **I2C**.

    .. image:: img/image283.png
        :align: center

#. Usa las teclas de flecha del teclado para seleccionar **<Yes>** -> **<OK>** para completar la configuración de I2C.

    .. image:: img/image284.png
        :align: center

#. Después de seleccionar **<Finish>**, aparecerá un recordatorio indicando que necesitas reiniciar para que los cambios surtan efecto, selecciona **<Yes>**.

    .. image:: img/camera_enable2.png
        :align: center
