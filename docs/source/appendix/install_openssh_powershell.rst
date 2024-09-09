.. note::

    Hola, bienvenido a la Comunidad de Entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirte?**

    - **Soporte de expertos**: Resuelve problemas post-venta y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos exclusivos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _openssh_powershell:

Instalar OpenSSH a través de Powershell
===========================================

Cuando intentas conectar a tu Raspberry Pi usando ``ssh <username>@<hostname>.local`` (o ``ssh <username>@<IP address>``), pero aparece el siguiente mensaje de error:

    .. code-block::

        ssh: El término 'ssh' no se reconoce como el nombre de un cmdlet, función, archivo de script o programa ejecutable. Verifica la
        ortografía del nombre, o si se incluyó una ruta, verifica que la ruta sea correcta y vuelve a intentarlo.


Esto significa que tu sistema operativo es demasiado antiguo y no tiene `OpenSSH <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui>`_ preinstalado, por lo que necesitas seguir el tutorial a continuación para instalarlo manualmente.

#. Escribe ``powershell`` en el cuadro de búsqueda de tu escritorio de Windows, haz clic derecho en ``Windows PowerShell`` y selecciona ``Ejecutar como administrador`` en el menú que aparece.

    .. image:: img/powershell_ssh.png
        :align: center

#. Usa el siguiente comando para instalar ``OpenSSH.Client``.

    .. code-block::

        Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

#. Después de la instalación, se mostrará la siguiente salida.

    .. code-block::

        Path          :
        Online        : True
        RestartNeeded : False

#. Verifica la instalación utilizando el siguiente comando.

    .. code-block::

        Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

#. Ahora te indicará que ``OpenSSH.Client`` se ha instalado correctamente.

    .. code-block::

        Name  : OpenSSH.Client~~~~0.0.1.0
        State : Installed

        Name  : OpenSSH.Server~~~~0.0.1.0
        State : NotPresent

    .. warning:: 
        Si no aparece el mensaje anterior, significa que tu sistema Windows sigue siendo demasiado antiguo y se te recomienda instalar una herramienta SSH de terceros, como :ref:`login_windows`.

#. Ahora reinicia PowerShell y vuelve a ejecutarlo como administrador. En este punto, podrás iniciar sesión en tu Raspberry Pi usando el comando ``ssh``, donde se te pedirá que ingreses la contraseña que configuraste anteriormente.

    .. image:: img/powershell_login.png
