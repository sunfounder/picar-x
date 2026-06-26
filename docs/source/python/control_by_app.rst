.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 junto con otros entusiastas.

    **¿Por qué unirte?**

    - **Soporte experto**: Resuelve problemas técnicos y de posventa con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _control_by_app:

12. Controlado por la APP
=========================

El controlador de SunFounder se utiliza para controlar robots basados en Raspberry Pi/Pico.

La APP integra widgets como Botón, Interruptor, Joystick, D-pad, Deslizador y Deslizador de Aceleración; widgets de entrada como Pantalla Digital, Radar Ultrasónico, Detección de Escala de Grises y Velocímetro.

Hay 17 áreas de A a Q donde puedes colocar diferentes widgets para personalizar tu propio controlador.

Además, esta aplicación proporciona un servicio de transmisión de video en vivo.

Vamos a personalizar un controlador de PiCar-X usando esta aplicación.

**¿Cómo hacerlo?**

#. Instala el módulo ``sunfounder-controller``.

    Los módulos ``robot-hat``, ``vilib`` y ``picar-x`` deben estar instalados primero, para más detalles consulta: :ref:`install_all_modules`.


    .. raw:: html

        <run></run>

    .. code-block::

        cd ~
        git clone https://github.com/sunfounder/sunfounder-controller.git
        cd ~/sunfounder-controller
        sudo python3 setup.py install

#. Ejecuta el código.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/picar-x/example
        sudo python3 12.app_control.py

#. Install `SunFounder Controller <https://docs.sunfounder.com/projects/sf-controller/en/latest/>`_ from **APP Store(iOS)** or **Google Play(Android)**.


#. Abre y crea un nuevo controlador.

    Crea un nuevo controlador haciendo clic en el signo + en la APP SunFounder Controller.

    .. image:: img/app1.PNG

    Hay controladores predefinidos para algunos productos en la sección de Predefinidos, que puedes usar según sea necesario. Aquí, seleccionamos **PiCar-X**.

    .. image:: img/app_control_preset.jpg

#. Conecta a PiCar-X.

    Cuando hagas clic en el botón **Conectar**, buscará automáticamente robots cercanos. Su nombre está definido en ``picarx_control.py`` y debe estar ejecutándose en todo momento.

    .. image:: img/app9.PNG
    
    Una vez que hagas clic en el nombre del producto, aparecerá el mensaje "Conectado correctamente" y el nombre del producto aparecerá en la esquina superior derecha.

    .. image:: img/app10.PNG

    .. note::

        * Debes asegurarte de que tu dispositivo móvil esté conectado a la misma LAN que PiCar-X.
        * Si no se busca automáticamente, también puedes ingresar manualmente la IP para conectarte.

        .. image:: img/app11.PNG

#. Ejecuta este controlador.

    Haz clic en el botón **Ejecutar** para iniciar el controlador, verás la transmisión de video del coche y ahora podrás controlar tu PiCar-X con estos widgets.

    .. image:: img/app12.PNG
    
    Aquí están las funciones de los widgets.

    * **A**: Muestra la velocidad actual del coche.
    * **E**: Enciende la función de evasión de obstáculos.
    * **I**: Activa la función de seguimiento de línea.
    * **J**: Reconocimiento de voz, mantén presionado este widget para comenzar a hablar, y mostrará la voz reconocida cuando lo sueltes. Hemos configurado 4 comandos en el código para controlar el coche: ``forward``, ``backward``, ``left`` y ``right``.
    * **K**: Controla los movimientos de avance, retroceso, izquierda y derecha del coche.
    * **Q**: Mueve la cabeza (Cámara) hacia arriba, abajo, izquierda y derecha.
    * **N**: Activa la función de reconocimiento de color.
    * **O**: Activa la función de reconocimiento facial.
    * **P**: Activa la función de reconocimiento de objetos, puede reconocer casi 90 tipos de objetos. Para la lista de modelos, consulta: https://github.com/sunfounder/vilib/blob/master/workspace/coco_labels.txt.


