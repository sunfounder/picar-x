.. note::

    ¡Hola, bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook! Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirte?**

    - **Soporte experto**: Resuelve problemas técnicos y de posventa con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos.
    - **Descuentos exclusivos**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _py_bull_fight:

10. Lucha de Toros
=============================

¡Convierte a PiCar-X en un toro enfurecido! Usa su cámara para detectar y embestir un paño rojo.


**Ejecutar el Código**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 10.bull_fight.py


**Ver la Imagen**

Después de ejecutar el código, el terminal mostrará el siguiente mensaje:

.. code-block::

    ¡No hay escritorio!
    * Sirviendo la aplicación Flask "vilib.vilib" (carga perezosa)
    * Entorno: producción
    ADVERTENCIA: No uses el servidor de desarrollo en un entorno de producción.
    Utiliza un servidor WSGI de producción en su lugar.
    * Modo de depuración: apagado
    * Corriendo en http://0.0.0.0:9000/ (Presiona CTRL+C para salir)

Luego puedes ingresar ``http://<tu IP>:9000/mjpg`` en el navegador para ver la transmisión de video, por ejemplo: ``https://192.168.18.113:9000/mjpg``.

.. image:: img/display.png

**Código**

.. note::
    Puedes **Modificar/Restablecer/Copiar/Ejecutar/Detener** el código a continuación. Pero antes de eso, debes ir a la ruta del código fuente como ``picar-x\examples``. Después de modificar el código, puedes ejecutarlo directamente para ver el efecto.

.. raw:: html

    <run></run>

.. code-block:: python

    from picarx import Picarx
    from time import sleep
    from vilib import Vilib

    px = Picarx()

    def clamp_number(num,a,b):
        return max(min(num, max(a, b)), min(a, b))

    def main():
        Vilib.camera_start()
        Vilib.display()
        Vilib.color_detect("red")
        speed = 50
        dir_angle=0
        x_angle =0
        y_angle =0
        while True:
            if Vilib.detect_obj_parameter['color_n']!=0:
                coordinate_x = Vilib.detect_obj_parameter['color_x']
                coordinate_y = Vilib.detect_obj_parameter['color_y']
                
                # change the pan-tilt angle for track the object
                x_angle +=(coordinate_x*10/640)-5
                x_angle = clamp_number(x_angle,-35,35)
                px.set_cam_pan_angle(x_angle)

                y_angle -=(coordinate_y*10/480)-5
                y_angle = clamp_number(y_angle,-35,35)
                px.set_cam_tilt_angle(y_angle)

                # Movimiento
                # El ángulo de movimiento cambiará más lento que el ángulo de la cámara para evitar confusiones cuando la imagen cambie a alta velocidad.
                if dir_angle > x_angle:
                    dir_angle -= 1
                elif dir_angle < x_angle:
                    dir_angle += 1
                px.set_dir_servo_angle(x_angle)
                px.forward(speed)
                sleep(0.05)

            else:
                px.forward(0)
                sleep(0.05)

    if __name__ == "__main__":
        try:
            main()
        finally:
            px.stop()
            print("stop and exit")
            sleep(0.1)

**¿Cómo funciona?**

Debes prestar atención a las siguientes tres partes de este ejemplo:

1. Definir la función principal:

    * Inicia la cámara usando ``Vilib.camera_start()``.
    * Muestra la transmisión de la cámara con ``Vilib.display()``.
    * Activa la detección de color y especifica el color objetivo como "rojo" con ``Vilib.color_detect("red")``.
    * Inicializa variables: ``speed`` para la velocidad de movimiento del coche, ``dir_angle`` para el ángulo de dirección del movimiento del coche, ``x_angle`` para el ángulo horizontal de la cámara, y ``y_angle`` para el ángulo vertical de la cámara.

2. Ingresar en un bucle continuo (while True) para seguir el objeto de color rojo:

    * Verifica si hay un objeto de color rojo detectado (``Vilib.detect_obj_parameter['color_n'] != 0``).
    * Si se detecta un objeto de color rojo, obtén sus coordenadas (``coordinate_x`` y ``coordinate_y``).
    * Calcula nuevos ángulos de giro y elevación (``x_angle`` y ``y_angle``) según la posición del objeto detectado y ajústalos para seguir el objeto.
    * Limita los ángulos de giro y elevación dentro del rango especificado usando la función ``clamp_number``.
    * Ajusta los ángulos de giro y elevación de la cámara con ``px.set_cam_pan_angle()`` y ``px.set_cam_tilt_angle()`` para mantener el objeto en la vista.

3. Controlar el movimiento del coche en función de la diferencia entre ``dir_angle`` y ``x_angle``:

    * Si ``dir_angle`` es mayor que ``x_angle``, disminuye ``dir_angle`` en 1 para cambiar gradualmente el ángulo de dirección.
    * Si ``dir_angle`` es menor que ``x_angle``, aumenta ``dir_angle`` en 1.
    * Ajusta el ángulo del servo de dirección usando ``px.set_dir_servo_angle()`` para dirigir las ruedas del coche en consecuencia.
    * Mueve el coche hacia adelante a la velocidad especificada usando ``px.forward(speed)``.

