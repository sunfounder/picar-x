.. note::

    你好，欢迎来到 SunFounder 树莓派、Arduino 和 ESP32 爱好者社区的 Facebook 页面！与其他爱好者一起深入探讨树莓派、Arduino 和 ESP32。

    **为什么加入？**

    - **专家支持**: 通过我们的社区和团队的帮助解决售后问题和技术挑战。
    - **学习与分享**: 交流技巧和教程，提升你的技能。
    - **独家预览**: 提前了解新产品发布和预告。
    - **特别折扣**: 尊享我们最新产品的专属折扣。
    - **节日促销和赠品**: 参与赠品活动和节日促销。

    👉 准备好与我们一起探索和创造了吗？点击 [|link_sf_facebook|] 加入我们吧！

避障
==============================

在这个项目中，帕克会在前进的同时检测前方的障碍物，当障碍物太近时，它会改变前进的方向。

**运行代码**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/picar-x/example
    sudo python3 avoiding_obstacles.py
    
运行代码后，帕克会向前走。

如果检测到前方障碍物的距离小于25cm，则向左转。

若左转后方向无障碍物或障碍物距离大于25cm，则继续前进。

**代码**

.. .. note::

..     您可以 **修改/重置/复制/运行/停止** 下面的代码。 但在此之前，您需要转到像 ``picar-x/example`` 这样的源代码路径。 修改代码后，可以直接运行看看效果。

.. raw:: html

    <run></run>

.. code-block:: python

    from picarx import Picarx


    def main():
        try:
            px = Picarx()
            # px = Picarx(ultrasonic_pins=['D2','D3']) # tring, echo
            px.forward(30)
            while True:
                distance = px.ultrasonic.read()
                print("distance: ",distance)
                if distance > 0 and distance < 300:
                    if distance < 25:
                        px.set_dir_servo_angle(-35)
                    else:
                        px.set_dir_servo_angle(0)
        finally:
            px.forward(0)


    if __name__ == "__main__":
        main()


**这个怎么运作？**

picarx 模块中还导入了 ultrasonic 模块，我们可以用其封装的一些功能来检测距离。

.. code-block:: python

    from picarx import Picarx

因为 picarx 模块中导入了 ultrasonic 模块，我们可以直接用 ``px.ultrasonic.read()`` 来获取距离。

.. code-block:: python

    px = Picarx()
    px.forward(30)
    while True:
        distance = px.ultrasonic.read() 

下面的代码片段读取超声波模块报告的距离值，如果距离低于 25 厘米（10 英寸），它将把转向伺服从 0°（直线）设置为 -35°（左转）。

.. code-block:: python

    while True:
        distance = px.ultrasonic.read()
        print("distance: ",distance)
        if distance > 0 and distance < 300:
            if distance < 25:
                px.set_dir_servo_angle(-35)
            else:
                px.set_dir_servo_angle(0)
