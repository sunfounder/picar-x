Line Track
====================================

Use 1cm of black insulating tape to paste a track on a light-colored ground (or desktop). 
Run this program, and you will see PiCar-X sprinting into the track.

.. warning::
    In sharp bend will cause derailment!

**code**

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

**How it works?** 

在这里我们调用了 ``Grayscale_Module`` 库。

这个库有两个调用函数：

1. ``get_grayscale_data()`` :它会直接输出三个探测头的读数（从右侧到左侧牌序），通常，越明亮的地方获取到的值越大。

2. ``get_line_status()`` :它会根据三个探测头检测到的值生成小车的应对策略。分为 ``forward`` , ``left`` , ``right`` , ``stop`` 四种。

这些应对应策略的产生条件如下：在生成对象时，我们会传进一个数字作为阈值（如 ``gm = Grayscale_Module(500)`` 就是生成一个阈值为500的gm对象）。
当，三个探测头的检测值都大于阈值，则说明探测头下都是白色，没有黑线， ``get_line_status()`` 产生返回值 ``stop`` 。
如果右侧（也是第一个）探测头检测到黑线，则生成 ``right`` ; 中间探测头检测到黑线则返回 ``forward`` ; 左侧探测头检测到黑线则返回 ``left`` 。

