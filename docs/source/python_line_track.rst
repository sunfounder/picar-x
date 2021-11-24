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

.. note::
    您可以 **修改/重置/复制/运行/停止** 下面的代码。 但在此之前，您需要转到像 ``picar-x/example`` 这样的源代码路径。 修改代码后，可以直接运行看看效果。

.. raw:: html

    <run></run>

.. code-block:: python

    import sys
    sys.path.append(r'/home/pi/picar-x/lib')
    from utils import reset_mcu
    reset_mcu()
    from grayscale_module import Grayscale_Module
    from picarx import Picarx

    if __name__=='__main__':
    try:
        gm = Grayscale_Module(500)
        px = Picarx()
        px_power = 10
        while True:
            gm_val_list = gm.get_grayscale_data()
            print("gm_val_list:",gm_val_list)
            gm_status = gm.get_line_status(gm_val_list)
            print("gm_status:",gm_status)

            if gm_status == 'forward':
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

要使用灰度传感器模块，请导入 ``Grayscale_Module`` 库。

``Grayscale_Module`` 库有两种方法：

* ``get_grayscale_data()``：该方法直接输出三个传感器的读数，从右到左。区域越亮，获得的值越大。

* ``get_line_status()``: 该方法将根据三个探测器检测到的值生成一个动作。有四种类型的动作： forward 、 left 、 right 和 stop 。

这些动作的触发条件如下：
生成对象时，会分配一个数字作为阈值。
例如， ``gm = Grayscale_Module(500)`` 将生成一个阈值为 500 的 ``gm`` 对象。
当三个探针的检测值均大于阈值时，
表示探头感应到的是白色，没有检测到黑线，
这使得 ``get_line_status()`` 生成 ``stop`` 的返回值。


* 如果右侧（也是第一个）探针检测到黑线，则返回 ``right`` 。
* 如果中间探针检测到黑线，则返回 ``forward`` ;
* 如果左探针检测到黑线，则返回 ``left`` 。