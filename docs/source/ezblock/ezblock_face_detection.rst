.. note::

    Hola, bienvenido a la Comunidad de Entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirse?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos exclusivos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo!

Detección de rostros
=========================

Además de la detección de colores, PiCar-X también incluye una función de detección de rostros. En el siguiente ejemplo, el widget de Joystick se utiliza para ajustar la dirección de la cámara, y el número de rostros detectados se mostrará en el monitor de depuración.

Para obtener más información sobre cómo usar el widget de Video, consulta el tutorial de video de Ezblock aquí: :ref:`ezblock:video_latest`.

.. image:: img/face_detection.PNG


**CONSEJOS**

.. image:: img/sp210512_141947.png

Configura el widget de **detección de rostros** en **activado** para habilitar la detección facial.

.. image:: img/sp210512_142327.png

Estos dos bloques se utilizan para ajustar la orientación de la cámara pan-tilt, de forma similar a conducir el PiCar-X en el tutorial :ref:`ezb_remote_control`. A medida que el valor aumenta, la cámara rotará hacia la derecha o hacia arriba; si el valor disminuye, rotará hacia la izquierda o hacia abajo.

.. image:: img/sp210512_142407.png

Los resultados de la detección de imagen se proporcionan a través del bloque **rostro detectado**. Utiliza las opciones del menú desplegable para elegir entre leer las coordenadas, el tamaño o el número de resultados de la función de detección de imágenes.

.. image:: img/sp210512_142616.png

Usa el bloque **crear texto con** para imprimir la combinación de **texto** y los datos de **rostro detectado**.

**EJEMPLO**

.. note::

    * Puedes escribir el programa según la imagen a continuación, consulta el tutorial: :ref:`ezblock:create_project_latest`.
    * O encuentra el código con el mismo nombre en la página de **Ejemplos** de EzBlock Studio y haz clic en **Ejecutar** o **Editar** directamente.

.. image:: img/sp210512_142830.png
