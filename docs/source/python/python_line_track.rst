.. _py_line_tracking:

6. 线路追踪
====================================

本项目将使用灰度模块让 PiCar-X 沿着一条线向前移动。使用深色胶带制作一条尽可能直且
不太弯曲的线路。若 PiCar-X 偏离线路，可能需要进行一些实验调整。

**运行代码**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 6.minecart_plus.py

运行代码后，PiCar-X 将沿着线路向前移动。

**代码**

.. note::
    您可以 **修改/重置/复制/运行/停止** 以下代码。但在此之前，需进入源码路径，例如 ``picar-x/example``。修改代码后，您可以直接运行以查看效果。

.. raw:: html

    <run></run>

.. code-block:: python

    from picarx import Picarx
    from time import sleep

    px = Picarx()
    # px = Picarx(grayscale_pins=['A0', 'A1', 'A2'])

    # 请运行 ./calibration/grayscale_calibration.py 自动校准灰度值
    # 或者通过以下代码手动修改参考值
    # px.set_line_reference([1400, 1400, 1400])

    current_state = None
    px_power = 10
    offset = 20
    last_state = "stop"

    def outHandle():
        global last_state, current_state
        if last_state == 'left':
            px.set_dir_servo_angle(-30)
            px.backward(10)
        elif last_state == 'right':
            px.set_dir_servo_angle(30)
            px.backward(10)
        while True:
            gm_val_list = px.get_grayscale_data()
            gm_state = get_status(gm_val_list)
            print("outHandle gm_val_list: %s, %s"%(gm_val_list, gm_state))
            currentSta = gm_state
            if currentSta != last_state:
                break
        sleep(0.001)

    def get_status(val_list):
        _state = px.get_line_status(val_list)  # [bool, bool, bool], 0 表示线路，1 表示背景
        if _state == [0, 0, 0]:
            return 'stop'
        elif _state[1] == 1:
            return 'forward'
        elif _state[0] == 1:
            return 'right'
        elif _state[2] == 1:
            return 'left'

    if __name__=='__main__':
        try:
            while True:
                gm_val_list = px.get_grayscale_data()
                gm_state = get_status(gm_val_list)
                print("gm_val_list: %s, %s"%(gm_val_list, gm_state))

                if gm_state != "stop":
                    last_state = gm_state

                if gm_state == 'forward':
                    px.set_dir_servo_angle(0)
                    px.forward(px_power)
                elif gm_state == 'left':
                    px.set_dir_servo_angle(offset)
                    px.forward(px_power)
                elif gm_state == 'right':
                    px.set_dir_servo_angle(-offset)
                    px.forward(px_power)
                else:
                    outHandle()

        except KeyboardInterrupt:
            print("\nKeyboardInterrupt: stop and exit")

        finally:
            px.stop()
            print("stop and exit")
            sleep(0.1)


**工作原理**

该 Python 脚本使用灰度传感器控制 Picarx 机器人小车的导航。以下是其主要组成部分的说明：

* 导入与初始化：

    脚本导入了控制机器人小车的 Picarx 类以及 time 模块中的 sleep 函数，用于添加延时操作。

    创建了 Picarx 的实例，注释行显示了一个使用特定灰度传感器引脚的初始化方法。

    .. code-block:: python

        from picarx import Picarx
        from time import sleep

        px = Picarx()

* 配置与全局变量：

    ``current_state`` 、 ``px_power`` 、 ``offset`` 和 ``last_state`` 是用于跟踪和控制小车运动的全局变量。 ``px_power`` 设置电机功率， ``offset`` 用于调整转向角度。

    .. code-block:: python

        current_state = None
        px_power = 10
        offset = 20
        last_state = "stop"

* ``outHandle`` 函数：

    当小车需要处理“脱线”情况时调用此函数。

    它根据 ``last_state`` 调整小车的方向，并检查灰度传感器值以确定新状态。

    .. code-block:: python

        def outHandle():
            global last_state, current_state
            if last_state == 'left':
                px.set_dir_servo_angle(-30)
                px.backward(10)
            elif last_state == 'right':
                px.set_dir_servo_angle(30)
                px.backward(10)
            while True:
                gm_val_list = px.get_grayscale_data()
                gm_state = get_status(gm_val_list)
                print("outHandle gm_val_list: %s, %s"%(gm_val_list, gm_state))
                currentSta = gm_state
                if currentSta != last_state:
                    break
            sleep(0.001)

* ``get_status`` 函数：

    此函数解释灰度传感器数据（ ``val_list`` ），以确定小车的导航状态。

    根据哪个传感器检测到线路，小车的状态可以是“forward”（前进）、“left”（左转）、“right”（右转）或“stop”（停止）。

    .. code-block:: python

        def get_status(val_list):
            _state = px.get_line_status(val_list)  # [bool, bool, bool], 0 表示线路，1 表示背景
            if _state == [0, 0, 0]:
                return 'stop'
            elif _state[1] == 1:
                return 'forward'
            elif _state[0] == 1:
                return 'right'
            elif _state[2] == 1:
                return 'left'

* 主循环：

    ``while True`` 循环不断检查灰度数据并相应调整小车的运动。

    根据 ``gm_state``，它设置转向角度和运动方向。

    .. code-block:: python

        if __name__=='__main__':
            try:
                while True:
                    gm_val_list = px.get_grayscale_data()
                    gm_state = get_status(gm_val_list)
                    print("gm_val_list: %s, %s"%(gm_val_list, gm_state))

                    if gm_state != "stop":
                        last_state = gm_state

                    if gm_state == 'forward':
                        px.set_dir_servo_angle(0)
                        px.forward(px_power)
                    elif gm_state == 'left':
                        px.set_dir_servo_angle(offset)
                        px.forward(px_power)
                    elif gm_state == 'right':
                        px.set_dir_servo_angle(-offset)
                        px.forward(px_power)
                    else:
                        outHandle()

* 安全与清理：

    ``try...finally`` 块确保脚本中断或结束时小车能够安全停止。

    .. code-block:: python

        finally:
        px.stop()
        print("stop and exit")
        sleep(0.1)

总结，该脚本利用灰度传感器引导 Picarx 机器人小车沿线路导航。它通过连续读取传感器数据来确定方向，并相应调整小车的运动和转向。 ``outHandle`` 函数为小车在需要大幅调整路径时提供额外逻辑支持。
