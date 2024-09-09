.. note::

    Hola, bienvenido a la Comunidad de Entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. ¡Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 con otros entusiastas!

    **¿Por qué unirte?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo!

7. Ajuste del Servomotor (Importante)
======================================

El rango de ángulo del servomotor es de -90° a 90°, pero el ángulo configurado en la fábrica es aleatorio, puede ser 0° o 45°. Si ensamblamos el servomotor con ese ángulo directamente, provocará un estado caótico cuando el robot ejecute el código, o peor aún, el servomotor podría bloquearse y quemarse.

Por eso, es necesario configurar todos los ángulos de los servomotores a 0° antes de instalarlos, de manera que el ángulo del servomotor quede centrado, sin importar en qué dirección gire.

#. Para asegurarte de que el servomotor esté correctamente ajustado a 0°, primero inserta el brazo del servomotor en el eje del servo y luego gira suavemente el brazo a diferentes ángulos. Este brazo solo te permitirá ver claramente que el servomotor está rotando.

    .. image:: img/servo_arm.png

#. Ahora, ejecuta ``servo_zeroing.py`` en la carpeta ``example/``.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/picar-x/example
        sudo python3 servo_zeroing.py

#. A continuación, conecta el cable del servomotor en el puerto P11 como se muestra a continuación. Al mismo tiempo, verás que el brazo del servo gira a una posición (esta es la posición de 0°, que puede no estar vertical o paralela).

    .. image:: img/Z_P11.JPG

#. Ahora, retira el brazo del servomotor, asegurándote de que el cable permanezca conectado, y no apagues el sistema. Luego, continúa el ensamblaje siguiendo las instrucciones en papel.

.. note::

    * No desconectes este cable del servomotor antes de fijarlo con el tornillo del servo; puedes desconectarlo después de fijarlo.
    * No gires el servomotor mientras esté encendido para evitar daños; si el eje del servomotor no está insertado en el ángulo correcto, retira el servomotor y vuelve a insertarlo.
    * Antes de ensamblar cada servomotor, debes conectar el cable del servo en el puerto P11 y encender el sistema para configurar su ángulo a 0°.

