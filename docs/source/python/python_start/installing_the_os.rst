.. note::

    Hola, ¡bienvenido a la Comunidad de Entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook! Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirte?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo!

.. _install_os_sd:

2. Instalación del Sistema Operativo
=========================================


**Componentes necesarios**

* Una computadora personal
* Una tarjeta Micro SD y un lector

1. Instalar Raspberry Pi Imager
-----------------------------------

#. Visita la página de descargas de software de Raspberry Pi en `Raspberry Pi Imager <https://www.raspberrypi.org/software/>`_. Elige la versión del Imager compatible con tu sistema operativo. Descarga y abre el archivo para iniciar la instalación.

    .. image:: img/os_install_imager.png
        :align: center

#. Es posible que aparezca un aviso de seguridad durante la instalación, dependiendo de tu sistema operativo. Por ejemplo, Windows podría mostrar un mensaje de advertencia. En esos casos, selecciona **Más información** y luego **Ejecutar de todos modos**. Sigue las instrucciones en pantalla para completar la instalación de Raspberry Pi Imager.

    .. image:: img/os_info.png
        :align: center

#. Inicia la aplicación Raspberry Pi Imager haciendo clic en su ícono o escribiendo ``rpi-imager`` en tu terminal.

    .. image:: img/os_open_imager.png
        :align: center

2. Instalar el Sistema Operativo en la Tarjeta Micro SD
-----------------------------------------------------------

#. Inserta tu tarjeta SD en tu computadora o portátil utilizando un lector.

#. Dentro de Imager, haz clic en **Raspberry Pi Device** y selecciona el modelo de Raspberry Pi desde el menú desplegable.

    .. image:: img/os_choose_device.png
        :align: center

#. Selecciona **Sistema Operativo** y elige la versión recomendada del sistema operativo.

    .. image:: img/os_choose_os.png
        :align: center

#. Haz clic en **Elegir Almacenamiento** y selecciona el dispositivo de almacenamiento adecuado para la instalación.

    .. note::

        Asegúrate de seleccionar el dispositivo de almacenamiento correcto. Para evitar confusiones, desconecta cualquier otro dispositivo de almacenamiento si hay varios conectados.

    .. image:: img/os_choose_sd.png
        :align: center

#. Haz clic en **SIGUIENTE** y luego en **EDITAR CONFIGURACIÓN** para personalizar los ajustes del sistema operativo.

    .. note::

        Si tienes un monitor para tu Raspberry Pi, puedes omitir los siguientes pasos y hacer clic en 'Sí' para comenzar la instalación. Ajusta otros parámetros más adelante en el monitor.

    .. image:: img/os_enter_setting.png
        :align: center

#. Define un **nombre de host** para tu Raspberry Pi.

    .. note::

        El nombre de host es el identificador de red de tu Raspberry Pi. Puedes acceder a tu Pi usando ``<hostname>.local`` o ``<hostname>.lan``.

    .. image:: img/os_set_hostname.png
        :align: center

#. Crea un **Nombre de usuario** y una **Contraseña** para la cuenta de administrador de la Raspberry Pi.

    .. note::

        Establecer un nombre de usuario y contraseña únicos es vital para asegurar tu Raspberry Pi, que no cuenta con una contraseña predeterminada.

    .. image:: img/os_set_username.png
        :align: center

#. Configura la red Wi-Fi proporcionando el **SSID** y la **Contraseña** de tu red.

    .. note::

        Establece el ``Wireless LAN country`` utilizando el código de dos letras `ISO/IEC alpha2 <https://es.wikipedia.org/wiki/ISO_3166-1_alpha-2>`_ correspondiente a tu ubicación.

    .. image:: img/os_set_wifi.png
        :align: center

#. Para conectarte remotamente a tu Raspberry Pi, habilita SSH en la pestaña de Servicios.

    * Para **autenticación por contraseña**, usa el nombre de usuario y contraseña de la pestaña General.
    * Para la autenticación con clave pública, elige "Permitir solo autenticación con clave pública". Si tienes una clave RSA, se utilizará. De lo contrario, haz clic en "Ejecutar SSH-keygen" para generar un nuevo par de claves.

    .. image:: img/os_enable_ssh.png
        :align: center

#. El menú **Opciones** te permite configurar el comportamiento de Imager durante la escritura, como reproducir sonido al finalizar, expulsar el medio al terminar y habilitar la telemetría.

    .. image:: img/os_options.png
        :align: center

    
#. Cuando hayas terminado de personalizar los ajustes del sistema operativo, haz clic en **Guardar** para guardar tus personalizaciones. Luego, haz clic en **Sí** para aplicarlas cuando se escriba la imagen.

    .. image:: img/os_click_yes.png
        :align: center

#. Si la tarjeta SD contiene datos existentes, asegúrate de hacer una copia de seguridad para evitar la pérdida de datos. Procede haciendo clic en **Sí** si no es necesario hacer una copia de seguridad.

    .. image:: img/os_continue.png
        :align: center

#. Cuando aparezca el mensaje "Escritura exitosa", la imagen habrá sido completamente escrita y verificada. ¡Ya estás listo para iniciar una Raspberry Pi desde la tarjeta Micro SD!

    .. image:: img/os_finish.png
        :align: center

#. Ahora puedes insertar la tarjeta SD configurada con Raspberry Pi OS en la ranura para microSD ubicada en la parte inferior de la Raspberry Pi.

    .. image:: img/os_sd_to_pi.jpg
        :width: 500
        :align: center
