.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirte?**

    - **Soporte experto**: Resuelve problemas técnicos y de posventa con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos.
    - **Descuentos exclusivos**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _py_calibrate:

1. Calibración del PiCar-X
==========================

Calibrar Motores y Servos
-------------------------

Algunos ángulos de los servos pueden estar ligeramente desalineados debido a posibles desviaciones durante la instalación del PiCar-X o limitaciones de los propios servos, por lo que puedes calibrarlos.

Por supuesto, puedes omitir este capítulo si consideras que el montaje es perfecto y no requiere calibración.

#. Ejecuta el archivo ``calibration.py``.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/picar-x/example
        sudo python3 1.cali_servo_motor.py

#. Después de ejecutar el código, verás la siguiente interfaz mostrada en el terminal.

    .. image:: img/calibrate1.png

#. La tecla ``R`` se utiliza para probar si los 3 servos funcionan correctamente.

#. Presiona la tecla numérica ``1`` para seleccionar el servo de la rueda delantera, y luego presiona las teclas ``W/S`` para que la rueda delantera mire lo más hacia adelante posible sin desviarse a la izquierda ni a la derecha.

    .. image:: img/calibrate2.png

#. Presiona la tecla numérica ``2`` para seleccionar el **servo Pan**, luego presiona las teclas ``W/S`` para que la plataforma de la cámara mire al frente sin inclinarse a la izquierda ni a la derecha.

    .. image:: img/calibrate3.png

#. Presiona la tecla numérica ``3`` para seleccionar el **servo de inclinación**, luego presiona las teclas ``W/S`` para que la plataforma de la cámara no se incline hacia arriba ni hacia abajo.

    .. image:: img/calibrate4.png

#. Dado que los cables de los motores pueden haberse invertido durante la instalación, puedes presionar la tecla ``E`` para probar si el coche puede avanzar normalmente. Si no es así, utiliza las teclas numéricas ``4`` y ``5`` para seleccionar los motores izquierdo y derecho, luego presiona la tecla ``Q`` para calibrar la dirección de rotación.

    .. image:: img/calibrate6.png

#. Cuando la calibración esté completa, presiona la tecla ``Barra Espaciadora`` para guardar los parámetros de calibración. Aparecerá un mensaje pidiéndote que ingreses ``y`` para confirmar, y luego presiona ``Ctrl+C`` para salir del programa y completar la calibración.

    .. image:: img/calibrate5.png


Calibrar el Módulo de Escala de Grises
--------------------------------------

Debido a las condiciones ambientales variables y a las situaciones de iluminación,
los parámetros predeterminados para el módulo de escala de grises podrían no ser óptimos.
Puedes ajustar estos valores con este programa para lograr mejores resultados.


#. Coloca una tira de cinta adhesiva negra, de aproximadamente 15 cm de largo, en un suelo de color claro. Centra tu PiCar-X de manera que quede sobre la cinta. En esta configuración, el sensor central del módulo de escala de grises debe estar directamente sobre la cinta, mientras que los dos sensores laterales deben estar sobre la superficie clara.


#. Ejecuta el código.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/picar-x/example
        sudo python3 1.cali_grayscale.py

#. Después de ejecutar el código, verás la siguiente interfaz mostrada en el terminal.

    .. image:: img/calibrate_g1.png

#. Presiona la tecla "Q" para iniciar la calibración de escala de grises. Luego observarás que el PiCar-X realiza pequeños movimientos hacia la izquierda y hacia la derecha. Durante este proceso, cada uno de los tres sensores debería cruzar la cinta adhesiva al menos una vez.

#. Además, notarás que aparecen tres pares de valores significativamente diferentes en la sección de "valor de umbral", mientras que la "referencia de línea" mostrará dos valores intermedios, representando el promedio de cada uno de estos pares.

    .. image:: img/calibrate_g2.png

#. A continuación, suspende el PiCar-X en el aire (o colócalo sobre el borde de un acantilado) y presiona la tecla "E". Observarás que los valores de la "referencia de acantilado" también se actualizan en consecuencia.

    .. image:: img/calibrate_g3.png

#. Una vez que hayas verificado que todos los valores son precisos, presiona la tecla "Barra Espaciadora" para guardar los datos. Luego puedes salir del programa presionando Ctrl+C.
