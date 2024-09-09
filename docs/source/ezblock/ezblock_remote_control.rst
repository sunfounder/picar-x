.. note::

    Hola, bienvenido a la Comunidad de Entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirte?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos exclusivos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo!

.. _ezb_remote_control:

Control Remoto
=======================

Este proyecto te enseñará cómo controlar remotamente el PiCar-X con el widget de Joystick.
Nota: Después de arrastrar y soltar el widget de Joystick desde la página de Control Remoto, utiliza la función “Map” para calibrar las lecturas del eje X y del eje Y de los Joysticks. Para más información sobre la función de Control Remoto, consulta el siguiente enlace:

* :ref:`ezblock:remote_control_latest`

.. image:: img/remote_control23.png

**CONSEJOS**

.. image:: img/sp210512_114004.png

Para utilizar la función de control remoto, abre la página de Control Remoto desde el lado izquierdo de la página principal.

.. image:: img/sp210512_114042.png

Arrastra un Joystick al área central de la página de Control Remoto. Moviendo el punto blanco en el centro y arrastrándolo suavemente en cualquier dirección producirá una coordenada (X,Y). El rango del eje X o el eje Y está predeterminado en “-100” a “100”. Mover el punto blanco y arrastrarlo directamente hacia el extremo izquierdo del Joystick resultará en un valor de X de “-100” y un valor de Y de “0”.

.. image:: img/sp210512_114136.png

Después de arrastrar y soltar un widget en la página de control remoto, aparecerá una nueva categoría llamada Remote con el bloque anterior.
Este bloque lee el valor del Joystick en la página de Control Remoto. Puedes hacer clic en el menú desplegable para cambiar a la lectura del eje Y.

.. image:: img/sp210512_114235.png

El bloque de valor de mapeo puede volver a asignar un número de un rango a otro. Si el rango está configurado de 0 a 100, y el número del valor de mapeo es 50, entonces está en una posición del 50% del rango, o “50”. Si el rango está configurado de 0 a 255 y el número del valor de mapeo es 50, entonces está en una posición del 50% del rango, o “127.5”.

**EJEMPLO**

.. note::

    * Puedes escribir el programa según la siguiente imagen, por favor revisa el tutorial: :ref:`ezblock:create_project_latest`.
    * O encuentra el código con el mismo nombre en la página de **Ejemplos** de EzBlock Studio y haz clic en **Ejecutar** o **Editar** directamente.

.. image:: img/sp210512_114416.png

