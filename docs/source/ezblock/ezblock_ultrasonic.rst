.. note::

    Hola, bienvenido a la Comunidad de Entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirte?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos exclusivos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo!

Prueba del Módulo Ultrasónico
=================================

PiCar-X tiene un módulo de sensor ultrasónico integrado que se puede usar para evitar obstáculos y realizar experimentos de seguimiento automático de objetos. En esta lección, el módulo leerá una distancia en centímetros (24 cm = 1 pulgada) y **imprimirá** los resultados en una ventana de **Depuración**.

**CONSEJOS**

.. image:: img/sp210512_114549.png 

El bloque **Ultrasonic get distance** leerá la distancia entre el PiCar-X y un obstáculo directamente al frente.

.. image:: img/sp210512_114830.png

Este programa se simplifica con una **Variable**. Por ejemplo, cuando hay múltiples funciones en un programa que necesitan utilizar la distancia a un obstáculo, se puede usar una **Variable** para informar el mismo valor de distancia a cada función, en lugar de que cada función lea el valor por separado.

.. image:: img/sp210512_114916.png

Haz clic en el botón **Crear variable...** en la categoría de **Variables** y utiliza la flecha desplegable para seleccionar la variable llamada “distancia”.

.. image:: img/sp210512_114945.png

La función **Imprimir** puede imprimir datos como variables y texto para facilitar la depuración.

.. image:: img/debug_monitor.png

Una vez que el código esté en ejecución, habilita el monitor de depuración haciendo clic en el icono **Depuración** en la esquina inferior izquierda.

**EJEMPLO**

.. note::

    * Puedes escribir el programa según la siguiente imagen, consulta el tutorial: :ref:`ezblock:create_project_latest`.
    * O encuentra el código con el mismo nombre en la página de **Ejemplos** de EzBlock Studio y haz clic en **Ejecutar** o **Editar** directamente.

.. image:: img/sp210512_115125.png
