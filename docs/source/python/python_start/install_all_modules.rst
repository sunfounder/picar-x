.. note::

    ¡Hola, bienvenido a la Comunidad de Entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook! Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirte?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos exclusivos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo!

.. _install_all_modules:


5. Instalar Todos los Módulos (Importante)
=============================================

Asegúrate de estar conectado a Internet y actualiza tu sistema:

.. raw:: html

    <run></run>

.. code-block::

    sudo apt update
    sudo apt upgrade

.. note::

    Los paquetes relacionados con Python3 deben estar instalados si estás utilizando la versión Lite del sistema operativo.

    .. raw:: html

        <run></run>

    .. code-block::
    
        sudo apt install git python3-pip python3-setuptools python3-smbus


Instala ``robot-hat``.

.. raw:: html

    <run></run>

.. code-block::

    cd ~/
    git clone -b v2.0 https://github.com/sunfounder/robot-hat.git
    cd robot-hat
    sudo python3 setup.py install


Luego descarga e instala el módulo ``vilib``.

.. raw:: html

    <run></run>

.. code-block::

    cd ~/
    git clone -b picamera2 https://github.com/sunfounder/vilib.git
    cd vilib
    sudo python3 install.py

Descarga e instala el módulo ``picar-x``.

.. raw:: html

    <run></run>

.. code-block::

    cd ~/
    git clone -b v2.0 https://github.com/sunfounder/picar-x.git
    cd picar-x
    sudo python3 setup.py install

Este paso tomará un poco de tiempo, así que por favor ten paciencia.

Finalmente, necesitas ejecutar el script ``i2samp.sh`` para instalar los componentes requeridos por el amplificador i2s, de lo contrario el picar-x no tendrá sonido.

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x
    sudo bash i2samp.sh
	
.. image:: img/i2s.png

Escribe ``y`` y presiona enter para continuar ejecutando el script.

.. image:: img/i2s2.png

Escribe ``y`` y presiona enter para ejecutar ``/dev/zero`` en segundo plano.

.. image:: img/i2s3.png

Escribe ``y`` y presiona enter para reiniciar el Picar-X.

.. note::
    Si no hay sonido después de reiniciar, es posible que necesites ejecutar el script i2samp.sh varias veces.
