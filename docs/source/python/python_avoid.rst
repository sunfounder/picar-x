.. note::

    ¡Hola! Bienvenido a la Comunidad de Entusiastas de SunFounder para Raspberry Pi, Arduino y ESP32 en Facebook. Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 junto a otros entusiastas.

    **¿Por qué unirte?**

    - **Soporte experto**: Resuelve problemas técnicos y de posventa con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos.
    - **Descuentos exclusivos**: Disfruta de descuentos en nuestros productos más recientes.
    - **Promociones y sorteos festivos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _py_avoid:

4. Evitación de Obstáculos
==========================

En este proyecto, PiCar-X detectará obstáculos frente a él mientras avanza, 
y cuando los obstáculos estén demasiado cerca, cambiará la dirección de avance.

**Ejecutar el Código**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 4.avoiding_obstacles.py
    
Después de ejecutar el código, PiCar-X comenzará a avanzar.

Si detecta que la distancia del obstáculo delante es inferior a 20 cm, retrocederá.

Si hay un obstáculo entre 20 y 40 cm, girará a la izquierda.

Si no hay obstáculos en la dirección tras girar a la izquierda o la distancia del obstáculo es mayor a 25 cm, 
seguirá avanzando.

**Código**

.. note::
    Puedes **Modificar/Restablecer/Copiar/Ejecutar/Detener** el código a continuación. Pero antes de eso, necesitas ir a la ruta del código fuente como ``picar-x/example``. Después de modificar el código, puedes ejecutarlo directamente para ver el efecto.

.. raw:: html

    <run></run>

.. code-block:: python

    from picarx import Picarx
    import time
    
    POWER = 50
    SafeDistance = 40   # > 40 seguro
    DangerDistance = 20 # > 20 && < 40 gira, 
                        # < 20 retrocede
    
    def main():
        try:
            px = Picarx()
            # px = Picarx(ultrasonic_pins=['D2','D3']) # tring, echo
           
            while True:
                distance = round(px.ultrasonic.read(), 2)
                print("distance: ",distance)
                if distance >= SafeDistance:
                    px.set_dir_servo_angle(0)
                    px.forward(POWER)
                elif distance >= DangerDistance:
                    px.set_dir_servo_angle(30)
                    px.forward(POWER)
                    time.sleep(0.1)
                else:
                    px.set_dir_servo_angle(-30)
                    px.backward(POWER)
                    time.sleep(0.5)
    
        finally:
            px.forward(0)
    
    
    if __name__ == "__main__":
        main()

**¿Cómo funciona?**

* Importación del Módulo Picarx e Inicialización de Constantes: 

    Esta sección del código importa la clase ``Picarx`` del módulo ``picarx``, que es esencial para controlar el robot Picarx. Se definen constantes como ``POWER``, ``SafeDistance`` y ``DangerDistance``, que se utilizarán más adelante en el script para controlar el movimiento del robot en función de las mediciones de distancia.

    .. code-block:: python

        from picarx import Picarx
        import time

        POWER = 50
        SafeDistance = 40 # > 40 seguro
        DangerDistance = 20 # > 20 && < 40 gira,
        # < 20 retrocede

* Definición de la Función Principal y Lectura del Sensor Ultrasónico:

    La función ``main`` es donde se controla el robot Picarx. Se crea una instancia de ``Picarx``, que activa las funcionalidades del robot. El código entra en un bucle infinito, leyendo constantemente la distancia del sensor ultrasónico. Esta distancia se utiliza para determinar el movimiento del robot.

    .. code-block:: python
        
        def main():
        try:
        px = Picarx()

            while True:
                distance = round(px.ultrasonic.read(), 2)
                # [Rest of the logic]

* Lógica de Movimiento Basada en la Distancia:

    El movimiento del robot se controla en función de la ``distance`` leída desde el sensor ultrasónico. Si la ``distance`` es mayor que la ``SafeDistance``, el robot avanza. Si la distancia está entre ``DangerDistance`` y ``SafeDistance``, gira levemente y avanza. Si la ``distance`` es menor que ``DangerDistance``, el robot retrocede mientras gira en la dirección opuesta.

    .. code-block:: python

        if distance >= SafeDistance:
            px.set_dir_servo_angle(0)
            px.forward(POWER)
        elif distance >= DangerDistance:
            px.set_dir_servo_angle(30)
            px.forward(POWER)
            time.sleep(0.1)
        else:
            px.set_dir_servo_angle(-30)
            px.backward(POWER)
            time.sleep(0.5)

* Seguridad y Limpieza con el Bloque 'finally':

    El bloque ``try...finally`` garantiza la seguridad deteniendo el movimiento del robot en caso de una interrupción o error. Esta es una parte crucial para evitar comportamientos incontrolables del robot.

    .. code-block:: python
        
        try:
        # [Lógica de control]
        finally:
        px.forward(0)

* Punto de Entrada de Ejecución:

    El punto de entrada estándar de Python ``if __name__ == "__main__":`` se utiliza para ejecutar la función principal cuando el script se ejecuta como un programa independiente.

    .. code-block:: python
        
        if name == "main":
            main()

En resumen, el script utiliza el módulo Picarx para controlar un robot, utilizando un sensor ultrasónico para medir distancias. El movimiento del robot se adapta en función de estas mediciones, garantizando una operación segura a través de un control cuidadoso y un mecanismo de seguridad en el bloque finally.
