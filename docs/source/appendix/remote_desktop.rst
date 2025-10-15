.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _remote_desktop:

Acceso a Escritorio Remoto para Raspberry Pi
==================================================

Para quienes prefieren una interfaz gráfica de usuario (GUI) en lugar del acceso por línea de comandos, la Raspberry Pi admite funcionalidad de escritorio remoto.  
Esta guía te mostrará cómo configurar y usar **VNC (Virtual Network Computing)** para acceso remoto.

Recomendamos usar `VNC® Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ para este propósito.

**Habilitar el servicio VNC en Raspberry Pi**

El servicio VNC viene preinstalado en Raspberry Pi OS pero está deshabilitado por defecto.  
Sigue estos pasos para habilitarlo:

#. Introduce el siguiente comando en la terminal de Raspberry Pi:

    .. raw:: html

        <run></run>

    .. code-block:: 

        sudo raspi-config

#. Navega a **Interfacing Options** usando la tecla de flecha hacia abajo y presiona **Enter**.

    .. image:: img/config_interface.png
        :align: center

#. Selecciona **VNC** de las opciones.

    .. image:: img/vnc.png
        :align: center

#. Usa las teclas de flecha para elegir **<Yes>** -> **<OK>** -> **<Finish>** y finalizar la activación del servicio VNC.

    .. image:: img/vnc_yes.png
        :align: center

**Iniciar sesión mediante VNC Viewer**

#. Descarga e instala `VNC Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ en tu computadora personal.

#. Una vez instalado, abre VNC Viewer. Introduce el nombre de host o la dirección IP de tu Raspberry Pi y presiona **Enter**.

    .. image:: img/vnc_viewer1.png
        :align: center

#. Cuando se te solicite, ingresa el nombre de usuario y la contraseña de tu Raspberry Pi, luego haz clic en **OK**.

    .. image:: img/vnc_viewer2.png
        :align: center

#. Después de unos segundos, se mostrará el escritorio de Raspberry Pi OS.  
   Ahora puedes abrir la Terminal y comenzar a introducir comandos.

    .. image:: img/bookwarm.png
        :align: center
