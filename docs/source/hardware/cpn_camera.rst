.. note::

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. ¡Profundiza en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas!

    **¿Por qué unirte?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones especiales.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

Módulo de Cámara
================


**Descripción**

.. image:: img/camera_module_pic.png
   :width: 200
   :align: center

Este es un módulo de cámara Raspberry Pi de 5MP con sensor OV5647. Es plug and play, conecta el cable de cinta incluido al puerto CSI (Interfaz Serial de Cámara) en tu Raspberry Pi y estará listo para usar.

La placa es pequeña, mide aproximadamente 25mm x 23mm x 9mm y pesa 3g, lo que la hace ideal para aplicaciones móviles u otras aplicaciones donde el tamaño y el peso son críticos. El módulo de cámara tiene una resolución nativa de 5 megapíxeles y cuenta con una lente de enfoque fijo integrada que captura imágenes fijas a 2592 x 1944 píxeles y también admite video 1080p30, 720p60 y 640x480p90.

.. note:: 

   El módulo solo puede capturar imágenes y videos, no sonido.



**Especificaciones**

* **Resolución de Imágenes Estáticas**: 2592×1944 
* **Resolución de Video Compatible**: 1080p/30 fps, 720p/ 60fps y 640 x 480p 60/90 grabación de video 
* **Apertura (F)**: 1.8 
* **Ángulo de Visión**: 65 grados 
* **Dimensiones**: 24mmx23.5mmx8mm 
* **Peso**: 3g 
* **Interfaz**: Conector CSI 
* **Sistema Operativo Compatible**: Raspberry Pi OS (se recomienda la versión más reciente)



**Montar el Módulo de Cámara**


En el módulo de cámara o Raspberry Pi, encontrarás un conector de plástico plano. Tire suavemente del interruptor de fijación negro hasta que esté parcialmente extraído. Inserte el cable FFC en el conector de plástico en la dirección mostrada y empuje el interruptor de fijación de nuevo en su lugar.

Si el cable FFC está instalado correctamente, estará recto y no se saldrá cuando lo tire suavemente. Si no, vuelva a instalarlo.


.. image:: img/connect_ffc.png
.. image:: img/1.10_camera.png
   :width: 700

.. warning::

   No instale la cámara con la alimentación encendida, ya que puede dañarla.

.. **Enable the Camera Interface**

.. Run the following command to enable the camera interface of your Raspberry Pi. If you have enabled it, skip this; if you do not know whether you have done that or not, please continue.

.. .. raw:: html

..    <run></run>

.. .. code-block:: 

..    sudo raspi-config

.. **3 Interfacing options**

.. .. image:: img/image282.png
..    :align: center

.. **P1 Camera**

.. .. image:: img/camera_config1.png
..    :align: center

.. **<Yes>, then <Ok> -> <Finish>**

.. .. image:: img/camera_config2.png
..    :align: center

.. After the configuration is complete, it is recommended to reboot the Raspberry Pi.

.. .. raw:: html

..    <run></run>

.. .. code-block:: 

..    sudo reboot