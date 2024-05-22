.. note::

    你好，欢迎来到 SunFounder 树莓派、Arduino 和 ESP32 爱好者社区的 Facebook 页面！与其他爱好者一起深入探讨树莓派、Arduino 和 ESP32。

    **为什么加入？**

    - **专家支持**: 通过我们的社区和团队的帮助解决售后问题和技术挑战。
    - **学习与分享**: 交流技巧和教程，提升你的技能。
    - **独家预览**: 提前了解新产品发布和预告。
    - **特别折扣**: 尊享我们最新产品的专属折扣。
    - **节日促销和赠品**: 参与赠品活动和节日促销。

    👉 准备好与我们一起探索和创造了吗？点击 [|link_sf_facebook|] 加入我们吧！

让帕克动起来
========================

这是第一个项目，让我们测试一下帕克的基本运动。

**运行代码**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/picar-x/example
    sudo python3 move.py

运行代码后，帕克会向前移动，S形转弯，停下来摇头。

**代码**

.. .. note::
..     您可以 **修改/重置/复制/运行/停止** 下面的代码。 但在此之前，您需要转到像 ``picar-x/example`` 这样的源代码路径。 修改代码后，可以直接运行看看效果。

.. raw:: html

    <run></run>

.. code-block:: python

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

**这个怎么运作？**

帕克的基本功能在 ``picarx`` 模块中，
可以用来控制舵机和车轮，
并使帕克向前移动、S 形转弯或摇头。

现在，导入了支持帕克基本功能的库。 这些线条将出现在所有涉及帕克运动的示例中。

.. code-block:: python
    :emphasize-lines: 0

    from picarx import Picarx
    import time

然后使用带有 ``for`` 循环的以下函数使帕克向前移动、改变方向和移动相机的平移/倾斜。

.. code-block:: python

    px.forward(speed)    
    px.set_dir_servo_angle(angle)
    px.set_camera_servo1_angle(angle)
    px.set_camera_servo2_angle(angle)

* ``forward()``：命令帕克以给定的速度前进。
* ``set_dir_servo_angle()``：将转向舵机转向特定的角度。
* ``set_camera_servo1_angle()``：将平移伺服器转到特定的角度。
* ``set_camera_servo2_angle()``：将倾斜伺服转向特定的角度。

.. image:: img/pan_tilt_servo.png
    :width: 300