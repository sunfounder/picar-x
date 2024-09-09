.. note::

    Hola, bienvenido a la Comunidad de Entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. ¡Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 con otros entusiastas!

    **¿Por qué unirte?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo!

.. _remote_desktop:

Acceso remoto al escritorio para Raspberry Pi
==================================================

Para aquellos que prefieren una interfaz gráfica de usuario (GUI) en lugar del acceso por línea de comandos, Raspberry Pi admite la funcionalidad de escritorio remoto. Esta guía te enseñará cómo configurar y usar VNC (Virtual Network Computing) para acceso remoto.

Recomendamos usar `VNC® Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ para este propósito.

**Habilitando el servicio VNC en Raspberry Pi**

El servicio VNC viene preinstalado en Raspberry Pi OS, pero está deshabilitado por defecto. Sigue estos pasos para habilitarlo:

#. Ingresa el siguiente comando en la terminal de Raspberry Pi:

    .. raw:: html

        <run></run>

    .. code-block:: 

        sudo raspi-config

#. Navega hasta **Opciones de Interfaz** usando la tecla de flecha hacia abajo, luego presiona **Enter**.

    .. image:: img/config_interface.png
        :align: center

#. Selecciona **VNC** entre las opciones.

    .. image:: img/vnc.png
        :align: center

#. Usa las teclas de flecha para elegir **<Sí>** -> **<OK>** -> **<Finalizar** y activa el servicio VNC.

    .. image:: img/vnc_yes.png
        :align: center

**Iniciar sesión a través de VNC Viewer**

#. Descarga e instala `VNC Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ en tu computadora personal.

#. Una vez instalado, abre VNC Viewer. Ingresa el nombre de host o la dirección IP de tu Raspberry Pi y presiona Enter.

    .. image:: img/vnc_viewer1.png
        :align: center

#. Cuando se te solicite, introduce el nombre de usuario y la contraseña de tu Raspberry Pi, luego haz clic en **OK**.

    .. image:: img/vnc_viewer2.png
        :align: center

#. Después de unos segundos, se mostrará el escritorio de Raspberry Pi OS. Ahora puedes abrir la Terminal para comenzar a ingresar comandos.

    .. image:: img/bookwarm.png
        :align: center
