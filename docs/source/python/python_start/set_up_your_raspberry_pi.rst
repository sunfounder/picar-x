.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete más en Raspberry Pi, Arduino y ESP32 junto con otros entusiastas.

    **¿Por qué unirte?**

    - **Soporte experto**: Resuelve problemas técnicos y de posventa con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Accede anticipadamente a anuncios de nuevos productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones especiales en días festivos.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

4. Configura tu Raspberry Pi
===============================
Si tienes una pantalla
----------------------

.. note:: La Raspberry Pi ZERO instalada en el Robot no es fácil de conectar a la pantalla, por favor usa el método sin pantalla para configurarla.


Si tienes una pantalla, te resultará fácil operar la Raspberry Pi.

**Componentes requeridos**

* Raspberry Pi
* Adaptador de corriente
* Tarjeta Micro SD
* Adaptador de corriente de la pantalla
* Cable HDMI
* Pantalla
* Ratón
* Teclado

#. Conecta el ratón y el teclado.

#. Conecta la pantalla al puerto HDMI de la Raspberry Pi y asegúrate de que tu pantalla esté conectada a la toma de corriente y encendida.

    .. note::

        Si utilizas una Raspberry Pi 4, debes conectar la pantalla al puerto HDMI0 (el más cercano al puerto de alimentación).

#. Utiliza el adaptador de corriente para encender la Raspberry Pi.

#. Después de unos segundos, se mostrará el escritorio del sistema operativo de Raspberry Pi. Ahora puedes abrir el terminal para empezar a introducir comandos.

    .. image:: img/bookwarm.png
        :align: center

Si no tienes pantalla
-------------------------

Si no tienes un monitor, puedes iniciar sesión de forma remota en tu Raspberry Pi.

**Componentes requeridos**

* Raspberry Pi
* Adaptador de corriente
* Tarjeta Micro SD

Puedes utilizar el comando SSH para abrir la terminal Bash de la Raspberry Pi. Bash es el shell estándar por defecto para Linux. El shell en sí es un comando (instrucción) cuando el usuario utiliza Unix/Linux. La mayoría de lo que necesitas hacer se puede realizar a través del shell.

Si no estás satisfecho con usar la ventana de comandos para acceder a tu Raspberry Pi, también puedes utilizar la función de escritorio remoto para gestionar fácilmente los archivos en tu Raspberry Pi usando una interfaz gráfica.

Consulta a continuación los tutoriales detallados para cada sistema.


.. toctree::

    remote_macosx
    remote_windows
    remote_linux
    remote_desktop

