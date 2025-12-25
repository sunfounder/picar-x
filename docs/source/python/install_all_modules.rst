.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirte?**

    - **Soporte experto**: Resuelve problemas técnicos y de posventa con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos.
    - **Descuentos exclusivos**: Disfruta de descuentos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _install_all_modules:


Instalar Todos los Módulos (Importante)
=========================================

#. **Preparar el sistema**

   Asegúrate de que tu Raspberry Pi esté conectada a Internet y luego actualiza el sistema:

   .. raw:: html

      <run></run>

   .. code-block::

      sudo apt update
      sudo apt upgrade

   .. note::
      Si estás utilizando Raspberry Pi OS Lite, instala primero los paquetes necesarios de Python 3:

   .. raw:: html

      <run></run>

   .. code-block::

         sudo apt install git python3-pip python3-setuptools python3-smbus

#. **Instalar robot-hat**

   Descarga e instala el módulo ``robot-hat``:

   .. raw:: html

      <run></run>

   .. code-block::

      cd ~/
      git clone -b 2.5.x https://github.com/sunfounder/robot-hat.git --depth 1
      cd robot-hat
      sudo python3 install.py

#. **Instalar vilib**

   Descarga e instala el módulo ``vilib``:

   .. raw:: html

      <run></run>

   .. code-block::

      cd ~/
      git clone https://github.com/sunfounder/vilib.git --depth 1
      cd vilib
      sudo python3 install.py

#. **Instalar picar-x**

   Descarga e instala el módulo ``picar-x``:

   .. raw:: html

      <run></run>

   .. code-block::

      cd ~/
      git clone -b 2.1.x https://github.com/sunfounder/picar-x.git --depth 1
      cd picar-x
      sudo pip3 install . --break

   Este paso puede tardar un poco. Por favor, ten paciencia.

#. **Habilitar sonido (amplificador I2S)**

   Para habilitar la salida de audio, ejecuta el script ``i2samp.sh`` para instalar los componentes necesarios del amplificador I2S:

   .. raw:: html

      <run></run>

   .. code-block::

      cd ~/robot-hat
      sudo bash i2samp.sh

   Sigue las instrucciones que aparecen en pantalla escribiendo ``y`` y presionando Enter para continuar, ejecuta ``/dev/zero`` en segundo plano y reinicia el PiCar-X.

   .. note::
      Si no hay sonido después de reiniciar, intenta ejecutar el script ``i2samp.sh`` varias veces.
