.. note::

    Hola, bienvenido a la Comunidad de Entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirte?**

    - **Soporte de expertos**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos exclusivos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _login_windows:

PuTTY
=========================

Si eres usuario de Windows, puedes usar algunas aplicaciones para SSH. Aquí te recomendamos `PuTTY <https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html>`_.

**Paso 1**

Descarga PuTTY.

**Paso 2**

Abre PuTTY y haz clic en **Session** en la estructura de árbol a la izquierda. Ingresa
la dirección IP de la Raspberry Pi en el cuadro de texto bajo **Host Name (or IP
address)** y **22** bajo **Port** (por defecto es 22).

.. image:: img/image25.png
    :align: center

**Paso 3**

Haz clic en **Open**. Ten en cuenta que cuando inicies sesión por primera vez en la Raspberry Pi con
la dirección IP, aparecerá un recordatorio de seguridad. Solo haz clic en **Yes**.

**Paso 4**

Cuando la ventana de PuTTY te pida \"**login as:**\", escribe
\"**pi**\" (el nombre de usuario de la Raspberry Pi), y la **contraseña**: \"raspberry\"
(la predeterminada, si no la has cambiado).

.. note::

    Cuando ingresas la contraseña, los caracteres no se muestran en la ventana, lo cual es normal. Lo que necesitas es ingresar la contraseña correcta.
    
    Si aparece "inactive" junto a PuTTY, significa que la conexión se ha interrumpido y necesita ser reconectada.
    
.. image:: img/image26.png
    :align: center

**Paso 5**


Aquí, hemos conectado la Raspberry Pi y es hora de realizar los siguientes pasos.
