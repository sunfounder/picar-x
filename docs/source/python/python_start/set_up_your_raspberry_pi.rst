.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete más en Raspberry Pi, Arduino y ESP32 junto con otros entusiastas.

    **¿Por qué unirte?**

    - **Soporte experto**: Resuelve problemas técnicos y de posventa con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Accede anticipadamente a anuncios de nuevos productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones especiales en días festivos.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _setup_pi:

4. Configurar Tu Raspberry Pi
=============================

Para comenzar a programar y controlar tu PiCar-X, primero necesitas acceder a tu Raspberry Pi.  
Esta sección te guiará a través de dos métodos comunes: usar un monitor, teclado y ratón, o configurar una conexión **sin pantalla (headless)** para iniciar sesión de forma remota desde otro ordenador.

Si Tienes una Pantalla
-------------------------

.. note:: La Raspberry Pi Zero 2W instalada en el robot no es fácil de conectar a una pantalla. Recomendamos el método **headless (sin pantalla)**.

**Componentes Necesarios**

* Raspberry Pi  
* Adaptador de corriente  
* Tarjeta Micro SD  
* Cable HDMI  
* Pantalla  
* Ratón  
* Teclado

#. Inserta la tarjeta microSD en tu Raspberry Pi.  
#. Conecta el ratón, teclado y pantalla (para Pi 4/5 usa **HDMI0**, el puerto más cercano a la entrada de alimentación).  
#. Enciende la Raspberry Pi.  
#. Después de unos segundos, aparecerá el escritorio de Raspberry Pi OS y podrás abrir una Terminal para introducir comandos.

    .. image:: img/bookwarm.png
        :align: center


Si No Tienes Pantalla (Configuración Headless)
-----------------------------------------------

Sin un monitor, puedes configurar e iniciar sesión en tu Raspberry Pi de forma remota.  
Este es el método más práctico para empezar.

**Componentes Necesarios**

* Raspberry Pi  
* Adaptador de corriente  
* Tarjeta Micro SD  
* Un ordenador en la misma red

**Consejos**

* Configura correctamente el **país de la red inalámbrica (Wireless LAN)** usando el código ISO/IEC alfa-2 (por ejemplo, ``US``, ``UK``, ``CN``); de lo contrario, el Wi-Fi no funcionará.  
* Asegúrate de que tu Raspberry Pi y tu ordenador estén en la misma red local.  
* Para una conexión más estable, utiliza una conexión directa por cable Ethernet cuando sea posible.  


**Conectarse por SSH**

1. En tu ordenador, abre una terminal (Windows: **PowerShell**, macOS/Linux: **Terminal**) y escribe:

   .. code-block::

      ssh <usuario>@<hostname>.local
      # Ejemplo:
      ssh daisy@picarx.local

#. Alternativamente, revisa la lista DHCP/clientes de tu router, encuentra la IP de la Pi y conéctate usando:

   .. code-block::

      ssh <usuario>@<IP>
      
      # Ejemplo:

      ssh daisy@192.xxx.xx.xx

#. En el primer inicio de sesión, aparecerá un mensaje de seguridad. Escribe ``yes`` para continuar.

#. Ingresa la contraseña que configuraste en Raspberry Pi Imager. (Los caracteres no aparecerán mientras escribes; esto es normal).

   .. note::
      La ausencia de caracteres visibles al escribir la contraseña es una medida de seguridad estándar. Solo escribe con cuidado.

#. Una vez conectado, tu Raspberry Pi estará lista para operaciones remotas.

   .. image:: img/ssh_login.png
      :align: center

**Solución de Problemas**

* **ssh: Could not resolve hostname ...**  

  * Verifica que el nombre del host sea correcto.  
  * Si aún falla, usa la dirección IP de la Pi en lugar de ``<hostname>.local``.

* **The term 'ssh' is not recognized... (Windows)**  

  * Tu sistema no tiene OpenSSH instalado. Instálalo manualmente (ver :ref:`openssh_powershell`) o usa un cliente SSH de terceros (ver :ref:`login_windows`).  

* **Permission denied (publickey,password)**  

  * Asegúrate de usar el nombre de usuario y contraseña que configuraste en Raspberry Pi Imager.  

* **Connection refused**  

  * Espera 1–2 minutos después de encender la Pi.  
  * Confirma que SSH fue habilitado en Raspberry Pi Imager.

**Opciones de Acceso Gráfico**

Si prefieres una interfaz gráfica en lugar de la línea de comandos, tienes dos opciones:

    .. image:: img/bookwarm.png
        :align: center

* :ref:`remote_desktop`: Habilita **VNC (Virtual Network Computing)** para una experiencia completa de escritorio en tu Pi.  
* |link_rpi_connect|: Usa **Raspberry Pi Connect** para acceso remoto seguro desde cualquier lugar, directamente en un navegador.

Ahora puedes controlar tu Raspberry Pi sin un monitor, ya sea mediante SSH para operaciones por línea de comandos o con VNC / Raspberry Pi Connect para una experiencia gráfica de escritorio.

