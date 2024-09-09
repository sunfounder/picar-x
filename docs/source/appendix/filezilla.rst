.. note::

    Hola, bienvenido a la Comunidad de Entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirte?**

    - **Soporte de expertos**: Resuelve problemas post-venta y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y avances exclusivos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo!

.. _filezilla:

Software Filezilla
==========================

.. image:: img/filezilla_icon.png

El Protocolo de Transferencia de Archivos (FTP) es un protocolo de comunicación estándar utilizado para transferir archivos de un servidor a un cliente en una red informática.

Filezilla es un software de código abierto que no solo soporta FTP, sino también FTP sobre TLS (FTPS) y SFTP. Podemos utilizar Filezilla para subir archivos locales (como imágenes y audios, etc.) a la Raspberry Pi, o descargar archivos desde la Raspberry Pi a la computadora local.

**Paso 1**: Descargar Filezilla.

Descarga el cliente desde el `Filezilla’s official website <https://filezilla-project.org/>`_. Filezilla ofrece un excelente tutorial, por favor consulta: `Documentation - Filezilla <https://wiki.filezilla-project.org/Documentation>`_.

**Paso 2**: Conectar a Raspberry Pi.

Después de una rápida instalación, ábrelo y ahora `connect it to an FTP server <https://wiki.filezilla-project.org/Using#Connecting_to_an_FTP_server>`_. Existen 3 formas de conectar, aquí utilizamos la barra de **Conexión Rápida**. Introduce el **nombre del host/IP**, **usuario**, **contraseña** y **puerto (22)**, luego haz clic en **Conexión Rápida** o presiona **Enter** para conectarte al servidor.

.. image:: img/filezilla_connect.png

.. note::

    La Conexión Rápida es una buena manera de probar tu información de inicio de sesión. Si deseas crear una entrada permanente, puedes seleccionar **Archivo** -> **Copiar la Conexión Actual al Administrador de Sitios** después de una Conexión Rápida exitosa, introduce el nombre y haz clic en **OK**. La próxima vez podrás conectarte seleccionando el sitio guardado anteriormente dentro de **Archivo** -> **Administrador de Sitios**.
    
    .. image:: img/ftp_site.png

**Paso 3**: Subir/descargar archivos.

Puedes subir archivos locales a la Raspberry Pi arrastrándolos y soltándolos, o descargar archivos de la Raspberry Pi a tu computadora local.

.. image:: img/upload_ftp.png

