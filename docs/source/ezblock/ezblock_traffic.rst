.. note::

    Hola, bienvenido a la Comunidad de Entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirte?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos exclusivos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo!

Detección de Señales de Tráfico
===============================

Además de la detección de colores y rostros, PiCar-X también puede detectar señales de tráfico.

Ahora combinemos esta función de detección de señales de tráfico con la de seguimiento de línea. Deja que PiCar-X siga la línea y, cuando pongas la señal de "Stop" frente a él, se detendrá. Cuando coloques la señal de "Avanzar" frente a él, continuará moviéndose.


**CONSEJOS**

#. PiCar reconocerá 4 modelos diferentes de señales de tráfico incluidos en el PDF imprimible a continuación.

    .. image:: img/taffics_sign.png

    * :download:`[PDF]Traffic Sign Cards <https://github.com/sunfounder/sf-pdf/raw/master/prop_card/object_detection/traffic-sign-cards.pdf>`

#. El bloque **Set ref to ()** se utiliza para establecer el umbral de escala de grises; debes modificarlo según la situación real. Puedes ejecutar :ref:`test_grayscale` para ver los valores del módulo de escala de grises en superficies blancas y negras, y llenar sus valores medios en este bloque.



**EJEMPLO**

.. note::

    * Puedes escribir el programa según la siguiente imagen, consulta el tutorial: :ref:`ezblock:create_project_latest`.
    * O encuentra el código con el mismo nombre en la página de **Ejemplos** de EzBlock Studio y haz clic en **Ejecutar** o **Editar** directamente.


.. image:: img/sp210513_101526.png

.. image:: img/sp210513_110948.png

.. image:: img/sp210512_171425.png

.. image:: img/sp210512_171454.png