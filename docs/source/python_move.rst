Let PiCar-X Move
========================

PiCar-X的基本功能都已被封装在 ``picarx.py`` 中，主要是控制舵机和车轮的工作。

让PiCar-X往前移动，走个漂亮的S字，然后停下来摇头晃脑。这能让我们掌握驱动马达和车身上3个舵机的方法。

你可以在example文件夹中打开 ``move.py`` 或者直接复制以下代码到Python IDE运行。

**Code**

.. code-block:: python

    import sys
    sys.path.append(r'/home/pi/picar-x/lib')
    from utils import reset_mcu
    reset_mcu()

    from picarx import Picarx
    import time

    if __name__ == "__main__":
        try:
            px = Picarx()
            px.forward(30)
            time.sleep(0.5)
            for angle in range(0,35):
                px.set_dir_servo_angle(angle)
                time.sleep(0.01)
            for angle in range(35,-35,-1):
                px.set_dir_servo_angle(angle)
                time.sleep(0.01)        
            for angle in range(-35,0):
                px.set_dir_servo_angle(angle)
                time.sleep(0.01)
            px.forward(0)
            time.sleep(1)

            for angle in range(0,35):
                px.set_camera_servo1_angle(angle)
                time.sleep(0.01)
            for angle in range(35,-35,-1):
                px.set_camera_servo1_angle(angle)
                time.sleep(0.01)        
            for angle in range(-35,0):
                px.set_camera_servo1_angle(angle)
                time.sleep(0.01)
            for angle in range(0,35):
                px.set_camera_servo2_angle(angle)
                time.sleep(0.01)
            for angle in range(35,-35,-1):
                px.set_camera_servo2_angle(angle)
                time.sleep(0.01)        
            for angle in range(-35,0):
                px.set_camera_servo2_angle(angle)
                time.sleep(0.01)

        finally:
            px.forward(0)

**How it works?**

首先，导入工具函数库，以支持PiCar-X的基本功能。这几行代码将出现在所有让PiCar-X动起来的示例中。

.. code-block:: python
    :emphasize-lines: 0

    import sys
    sys.path.append(r'/home/pi/picar-x/lib')
    from utils import reset_mcu
    reset_mcu()

    from picarx import Picarx
    import time

然后，找到以下几句代码，善用它们将可以顺利让PiCar-X动起来了。

.. code-block:: python
    :emphasize-lines: 0

    px = Picarx()

    speed = 30
    angle = 30

    px.forward(speed)    
    px.set_dir_servo_angle(angle)
    px.set_camera_servo1_angle(angle)
    px.set_camera_servo2_angle(angle)