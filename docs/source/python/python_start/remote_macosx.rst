Para Usuarios de Mac OS X
=============================

Para los usuarios de Mac OS X, SSH (Secure Shell) ofrece un método seguro y conveniente para acceder y controlar remotamente una Raspberry Pi. Esto es especialmente útil cuando se trabaja con la Raspberry Pi de forma remota o cuando no está conectada a un monitor. Usando la aplicación Terminal en un Mac, puedes establecer esta conexión segura. El proceso implica un comando SSH que incorpora el nombre de usuario y el nombre del host de la Raspberry Pi. Durante la conexión inicial, aparecerá un mensaje de seguridad solicitando la confirmación de la autenticidad de la Raspberry Pi.

#. Para conectarte a la Raspberry Pi, escribe el siguiente comando SSH:

    .. code-block::

        ssh pi@raspberrypi.local

    .. image:: img/mac-ping.png

#. Aparecerá un mensaje de seguridad durante tu primer inicio de sesión. Responde con **yes** para continuar.

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. Introduce la contraseña de la Raspberry Pi. Ten en cuenta que la contraseña no se mostrará en la pantalla mientras la escribes, lo cual es una característica estándar de seguridad.

    .. code-block::

        pi@raspberrypi.local's password: 
        Linux raspberrypi 5.15.61-v8+ #1579 SMP PREEMPT Fri Aug 26 11:16:44 BST 2022 aarch64

        The programs included with the Debian GNU/Linux system are free software;
        the exact distribution terms for each program are described in the
        individual files in /usr/share/doc/*/copyright.

        Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
        permitted by applicable law.
        Last login: Thu Sep 22 12:18:22 2022
        pi@raspberrypi:~ $ 

