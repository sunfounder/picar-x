.. note::

    Hola, ¡bienvenido a la Comunidad de Entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook! Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirte?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos exclusivos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo!

Movimiento
==========

Este primer proyecto enseña cómo programar acciones de movimiento para el PiCar-X. En este proyecto, el programa indicará al PiCar-X que ejecute cinco acciones en el siguiente orden: “avanzar”, “retroceder”, “girar a la izquierda”, “girar a la derecha” y “detenerse”.

Para aprender el uso básico de Ezblock Studio, por favor revisa las siguientes dos secciones:

* :ref:`ezblock:create_project_latest`


.. image:: img/move.png

**CONSEJOS**

.. image:: img/sp210512_113300.png

Este bloque hará que el PiCar-X avance a una velocidad basada en un porcentaje de la potencia disponible. En el ejemplo a continuación, "50" representa el 50% de la potencia, o media velocidad.

.. image:: img/sp210512_113418.png

Este bloque hará que el PiCar-X retroceda a una velocidad basada en un porcentaje de la potencia disponible.

.. image:: img/sp210512_113514.png

Este bloque ajusta la orientación de las ruedas delanteras. El rango es de "-45" a "45". En el ejemplo a continuación, "-30" significa que las ruedas girarán 30° hacia la izquierda.

.. image:: img/BLK_Basic_delay.png
    :width: 200

Este bloque pausará las órdenes durante un tiempo determinado, basado en milisegundos. En el ejemplo a continuación, el PiCar-X esperará 1 segundo (1000 milisegundos) antes de ejecutar el siguiente comando.

.. image:: img/sp210512_113550.png

Este bloque hará que el PiCar-X se detenga por completo.

**EJEMPLO**

.. note::

    * Puedes escribir el programa según la siguiente imagen, por favor revisa el tutorial: :ref:`ezblock:create_project_latest`.
    * O encuentra el código con el mismo nombre en la página de **Ejemplos** de EzBlock Studio y haz clic en **Ejecutar** o **Editar** directamente.


.. image:: img/sp210512_113827.png

