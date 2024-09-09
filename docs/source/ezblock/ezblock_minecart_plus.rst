.. note::

    Hola, bienvenido a la Comunidad de Entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos exclusivos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo!

Minecart Plus
=======================

En este proyecto, se ha agregado la recuperación de descarrilamiento al proyecto :ref:`ezb_minecart` para permitir que el PiCar-X se adapte y recupere de una curva más pronunciada.

.. image:: img/minec.png


**CONSEJOS**

#. Usa otro bloque **para hacer algo** para permitir que el PiCar-X retroceda y se recupere de una curva cerrada. Ten en cuenta que la nueva función **para hacer algo** no devuelve ningún valor, pero se utiliza solo para reorientar el PiCar-X.

    .. image:: img/sp210512_171727.png

#. El bloque **Establecer ref a ()** se utiliza para configurar el umbral de escala de grises, y debes modificarlo de acuerdo con la situación real. Puedes ejecutar :ref:`test_grayscale` para ver los valores del módulo de escala de grises en superficies blancas y negras, y completar los valores intermedios en este bloque.


**EJEMPLO**

.. note::

    * Puedes escribir el programa según la siguiente imagen, consulta el tutorial: :ref:`ezblock:create_project_latest`.
    * O encuentra el código con el mismo nombre en la página de **Ejemplos** de EzBlock Studio y haz clic en **Ejecutar** o **Editar** directamente.

.. image:: img/sp210512_171914.png

.. image:: img/sp210512_171932.png

.. image:: img/sp210512_171425.png

.. image:: img/sp210512_171454.png
