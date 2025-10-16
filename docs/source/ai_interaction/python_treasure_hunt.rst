
.. _py_treasure:

20. 寻宝游戏
============================

在本课中，你将把 PiCar-X 打造成一台**寻宝机器人**。  
在房间里搭一个迷宫，并把六种不同颜色的卡片放在不同角落。  
当找到目标颜色时，你的 PiCar-X会**搜索、识别并庆祝**。

这个项目结合了你目前学到的三项技能：

* **计算机视觉** —— 使用 Pi 摄像头检测彩色卡片。  
* **键盘控制** —— 手动驾驶机器人穿越迷宫。  
* **语音反馈** —— 由 Pico2Wave 播报目标颜色与成功提示。  

这是一个有趣的游戏，展示了机器人如何像寻宝者一样**看、想、做**！

.. note::  
   你可以下载并打印用于稳定颜色识别的:download:`PDF 彩色卡片 <https://github.com/sunfounder/sf-pdf/raw/master/prop_card/object_detection/color-cards.pdf>`。

运行代码
------------

.. raw:: html

    <run></run>

.. code-block:: bash

    cd ~/picar-x/example
    sudo python3 20.treasure_hunt.py

运行后，你会看到类似如下的信息：

.. code-block:: text

    * Running on http://0.0.0.0:9000/ (Press CTRL+C to quit)

然后在浏览器中打开``http://<your IP>:9000/mjpg``以查看实时视频流。  
示例：``http://192.168.18.113:9000/mjpg``

.. image:: img/display.png

游戏规则
----------

1. 机器人随机选择一个**目标颜色**并播报：**“Look for red!”**  
2. 你用键盘驾驶 PiCar-X：

   * ``w`` = 前进  
   * ``a`` = 左转  
   * ``s`` = 后退  
   * ``d`` = 右转  
   * ``space`` = 重复目标  
   * ``Ctrl+C`` = 退出  

3. 当摄像头看到目标彩色卡片时，PiCar-X会说**“Well done!”**  
4. 会选择一个新的目标颜色，继续寻宝！

代码
----


.. code-block:: python

    #!/usr/bin/env python3

    from picarx import Picarx
    from vilib import Vilib
    from picarx.tts import Pico2Wave

    from time import sleep
    import threading
    import readchar
    import random

    # -----------------------
    # Settings
    # -----------------------
    COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
    DETECTION_WIDTH_THRESHOLD = 100  # how wide the color blob must be
    DRIVE_SPEED = 80
    TURN_ANGLE = 30

    MANUAL = """
    Press keys to control PiCar-X:
      w: forward    a: turn left    s: backward    d: turn right
      space: repeat target          Ctrl+C: quit
    """

    # -----------------------
    # Init
    # -----------------------
    px = Picarx()

    tts = Pico2Wave()
    tts.set_lang("en-US")

    current_color = "red"
    key = None
    lock = threading.Lock()

    def say(line: str):
        print(f"[SAY] {line}")
        tts.say(line)

    def renew_color_detect():
        """Choose a new target color and start detection."""
        global current_color
        current_color = random.choice(COLORS)
        Vilib.color_detect(current_color)
        say(f"Look for {current_color}!")

    def key_scan_thread():
        """Background thread reading keys."""
        global key
        while True:
            k = readchar.readkey()
            # Map special keys before lowercasing
            if k == readchar.key.SPACE:
                mapped = "space"
            elif k == readchar.key.CTRL_C:
                mapped = "quit"
            else:
                mapped = k.lower()

            with lock:
                key = mapped

            if mapped == "quit":
                return
            sleep(0.01)

    def car_move(k: str):
        if k == "w":
            px.set_dir_servo_angle(0)
            px.forward(DRIVE_SPEED)
        elif k == "s":
            px.set_dir_servo_angle(0)
            px.backward(DRIVE_SPEED)
        elif k == "a":
            px.set_dir_servo_angle(-TURN_ANGLE)
            px.forward(DRIVE_SPEED)
        elif k == "d":
            px.set_dir_servo_angle(TURN_ANGLE)
            px.forward(DRIVE_SPEED)

    def main():
        global key

        # Start camera and web preview
        Vilib.camera_start(vflip=False, hflip=False)
        Vilib.display(local=False, web=True)
        sleep(0.8)

        print(MANUAL.strip())
        say("Game start!")
        sleep(0.1)
        renew_color_detect()

        # Start keyboard thread (modern style)
        key_thread = threading.Thread(target=key_scan_thread, daemon=True)
        key_thread.start()

        try:
            while True:
                # Check detection: if target color present and wide enough
                if (Vilib.detect_obj_parameter.get("color_n", 0) != 0 and
                    Vilib.detect_obj_parameter.get("color_w", 0) > DETECTION_WIDTH_THRESHOLD):
                    say("Well done!")
                    sleep(0.1)
                    renew_color_detect()

                # Take a snapshot of the last key (and clear it)
                with lock:
                    k = key
                    key = None

                # Handle movement / actions
                if k in ("w", "a", "s", "d"):
                    car_move(k)
                    sleep(0.5)
                    px.stop()
                elif k == "space":
                    say(f"Look for {current_color}!")
                elif k == "quit":
                    print("\n[INFO] Quit requested.")
                    break

                sleep(0.05)

        except KeyboardInterrupt:
            print("\n[INFO] Stopped by user.")
        finally:
            try:
                Vilib.camera_close()
            except Exception:
                pass
            px.stop()
            say("Goodbye!")
            sleep(0.2)

    if __name__ == "__main__":
        main()


工作原理
------------

1. **初始化** 

   * 导入模块并配置 PiCar-X、摄像头和 TTS。  
   * 设置颜色列表、速度和转向角度。  

2. **目标选择**

   * ``renew_color_detect()`` 会随机选择一个目标颜色。  
   * 机器人会通过 Pico2Wave 播报目标颜色。  

3. **键盘控制** 

   * ``key_scan_thread()`` 在后台运行以捕获按键输入。  
   * ``w, a, s, d`` 控制移动；``space`` 重复目标播报。  

4. **颜色检测**  

   * 摄像头会持续检测目标颜色是否出现。  
   * 当检测到的色块足够大时，PiCar-X 会庆祝成功。  

5. **主循环**

   * 持续处理移动、检测与语音反馈。  
   * 退出时会优雅地停止机器人与摄像头。

故障排查
---------------

* **摄像头画面不工作？**  

  运行 ``libcamera-hello`` 检查树莓派摄像头是否正确连接。  

* **机器人无法识别颜色？** 

  确保卡片打印清晰并放置在良好光照下。  
  试着调整 ``DETECTION_WIDTH_THRESHOLD`` 的阈值。  

* **没有语音反馈？**  

  检查是否安装了 ``pico2wave`` 并确认音频输出设备设置正确。  

* **小车无法移动？**  

  确认 PiCar-X 电源已打开，且电机校准无误。  

----

通过完成本课程，你构建了一个 **迷你寻宝游戏**，  
将 **视觉、控制与交互** 集成在同一个项目中！
