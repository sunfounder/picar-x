.. note::

    你好，欢迎来到 SunFounder 树莓派、Arduino 和 ESP32 爱好者社区的 Facebook 页面！与其他爱好者一起深入探讨树莓派、Arduino 和 ESP32。

    **为什么加入？**

    - **专家支持**: 通过我们的社区和团队的帮助解决售后问题和技术挑战。
    - **学习与分享**: 交流技巧和教程，提升你的技能。
    - **独家预览**: 提前了解新产品发布和预告。
    - **特别折扣**: 尊享我们最新产品的专属折扣。
    - **节日促销和赠品**: 参与赠品活动和节日促销。

    👉 准备好与我们一起探索和创造了吗？点击 [|link_sf_facebook|] 加入我们吧！

线路跟踪
====================================

本项目将使用灰度模块使帕克沿线向前移动。
使用深色胶带使线条尽可能平滑，转弯幅度不要太大，避免帕克脱轨。

**运行代码**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/picar-x/example
    sudo python3 minecart_plus.py
    
运行代码后，帕克会沿着线向前移动。

**代码**

.. .. note::
..     您可以 **修改/重置/复制/运行/停止** 下面的代码。 但在此之前，您需要转到像 ``picar-x/example`` 这样的源代码路径。 修改代码后，可以直接运行看看效果。

.. raw:: html

    <run></run>

.. code-block:: python

    from picarx import Picarx

    if __name__=='__main__':
    try:
        px = Picarx()
        px_power = 10
        while True:
            gm_val_list = px.get_grayscale_data()
            print("gm_val_list:",gm_val_list)
            gm_status = px.get_line_status(gm_val_list)
            print("gm_status:",gm_status)

            if gm_status == 'forward':
                print(1)
                px.forward(px_power) 

            elif gm_status == 'left':
                px.set_dir_servo_angle(12)
                px.forward(px_power) 

            elif gm_status == 'right':
                px.set_dir_servo_angle(-12)
                px.forward(px_power) 
            else:
                px.set_dir_servo_angle(0)
                px.stop()
    finally:
        px.stop()

**这个怎么运作？**

picarx 模块中也导入了灰度传感器模块 grayscale_module ，我们可以用其中的一些方法来检测黑线。

检测黑线的函数如下所示：

* ``get_grayscale_data()``：该函数直接输出三个传感器的读数，从右到左。区域越亮，获得的值越大。

* ``get_line_status()``: 该函数将根据三个探测器检测到的值生成一个动作。有四种类型的动作： forward 、 left 、 right 和 stop 。

这些动作的触发条件如下：
模块中默认分配了一个数值作为检测到黑色还是白色的阈值。
当三个探针的检测值均大于阈值时，
表示探头感应到的是白色，没有检测到则为黑线，
检测到黑线会使 ``get_line_status()`` 返回一个 ``stop`` 参数。


* 如果右侧（也是第一个）探针检测到黑线，则返回 ``right`` 。
* 如果中间探针检测到黑线，则返回 ``forward`` ;
* 如果左探针检测到黑线，则返回 ``left`` 。