.. note::

    ¡Hola! Bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. ¡Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 junto con otros entusiastas!

    **¿Por qué unirte?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y adelantos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones especiales.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy.

.. _py_stare:

8. Te Observa
==========================================

Este proyecto también se basa en el proyecto :ref:`py_computer_vision`, 
con la incorporación de algoritmos de detección facial.

Cuando aparezcas frente a la cámara, reconocerá tu rostro y ajustará su soporte para mantener tu cara en el centro de la imagen.

Puedes ver la transmisión en ``http://<your IP>:9000/mjpg``.

**Ejecutar el Código**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 8.stare_at_you.py

Cuando el código se ejecute, la cámara del coche seguirá enfocando tu rostro.

**Código**

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
        Vilib.face_detect_switch(True)
        x_angle =0
        y_angle =0
        while True:
            if Vilib.detect_obj_parameter['human_n']!=0:
                coordinate_x = Vilib.detect_obj_parameter['human_x']
                coordinate_y = Vilib.detect_obj_parameter['human_y']
                
                # ajustar el ángulo del soporte para seguir el rostro
                x_angle +=(coordinate_x*10/640)-5
                x_angle = clamp_number(x_angle,-35,35)
                px.set_cam_pan_angle(x_angle)

                y_angle -=(coordinate_y*10/480)-5
                y_angle = clamp_number(y_angle,-35,35)
                px.set_cam_tilt_angle(y_angle)

                sleep(0.05)

            else:
                pass
                sleep(0.05)

    if __name__ == "__main__":
        try:
            main()
        finally:
            px.stop()
            print("stop and exit")
            sleep(0.1)

**¿Cómo funciona?**

Estas líneas de código en el bucle ``while True`` permiten que la cámara siga el rostro.

.. code-block:: python

    while True:
        if Vilib.detect_obj_parameter['human_n']!=0:
            coordinate_x = Vilib.detect_obj_parameter['human_x']
            coordinate_y = Vilib.detect_obj_parameter['human_y']
            
            # ajustar el ángulo del soporte para seguir el rostro
            x_angle +=(coordinate_x*10/640)-5
            x_angle = clamp_number(x_angle,-35,35)
            px.set_cam_pan_angle(x_angle)

            y_angle -=(coordinate_y*10/480)-5
            y_angle = clamp_number(y_angle,-35,35)
            px.set_cam_tilt_angle(y_angle)

1. Verifica si se ha detectado un rostro humano.

    .. code-block:: python

        Vilib.detect_obj_parameter['human_n'] != 0

2. Si se detecta un rostro, obtén las coordenadas ( ``coordinate_x`` y ``coordinate_y`` ) del rostro detectado.

3. Calcula los nuevos ángulos de paneo e inclinación ( ``x_angle`` y ``y_angle`` ) basados en la posición del rostro y ajústalos para seguirlo.

4. Limita los ángulos de paneo e inclinación dentro del rango especificado usando la función ``clamp_number``.

5. Configura los ángulos de paneo e inclinación de la cámara utilizando ``px.set_cam_pan_angle()`` y ``px.set_cam_tilt_angle()``.

