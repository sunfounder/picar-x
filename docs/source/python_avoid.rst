Avoiding Obstacles
=============================

在这个示例中你将使用超声波传感器来检测前方，从而躲避障碍物。

**Code**

.. code-block:: python

    import sys
    sys.path.append(r'/home/pi/picar-x/lib')
    from utils import reset_mcu
    reset_mcu()

    from picarx import Picarx
    from ultrasonic import Ultrasonic
    from pin import Pin

    if __name__ == "__main__":
        try:
            trig_pin = Pin("D2") 
            echo_pin = Pin("D3")
            sonar = Ultrasonic(trig_pin, echo_pin)
            px = Picarx()
            px.forward(30)
            while True:
                distance = sonar.read()
                print("distance: ",distance)
                if distance > 0 and distance < 300:
                    if distance < 25:
                        px.set_dir_servo_angle(-35)
                    else:
                        px.set_dir_servo_angle(0)
        finally:
            px.forward(0)


**How it works?**

你只需要简单的调用Ultrasonic库就可以实现距离获取了。

.. code-block:: python

    from ultrasonic import Ultrasonic

    trig_pin = Pin("D2") 
    echo_pin = Pin("D3")
    sonar = Ultrasonic(trig_pin, echo_pin)    
    
    while True:
        distance = sonar.read()
        print("distance: ",distance)