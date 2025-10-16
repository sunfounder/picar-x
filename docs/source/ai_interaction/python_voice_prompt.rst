
14. 使用 Espeak 和 Pico2Wave 的语音提示小车
=================================================

在本课程中，我们将使用树莓派上内置的两种文本转语音（TTS）引擎 —— **Espeak** 和 **Pico2Wave** —— 让 PiCar-X “说话”。

这两个引擎都很轻量，并且支持 **离线运行**，但它们的声音风格和功能有很大区别：

* **Espeak**：非常轻量、速度快，但声音偏“机器人”；可调节语速、音高、音量等。  
* **Pico2Wave**：语音更加自然流畅，但可配置选项较少。

你将听到它们在 **语音质量** 和 **功能性** 上的区别，并最终构建一个“语音提示小车”，在小车移动之前先播报动作。

----

1. 测试 Espeak
--------------------

Espeak 是树莓派系统中内置的一个轻量 TTS 引擎。  
它的声音听起来较为机械，但可高度自定义：你可以调整音量、音高、语速等参数。

**步骤如下**：

* 创建一个新文件：

  .. code-block:: bash
  
      cd ~/picar-x/example
      sudo nano test_tts_espeak.py

* 将以下代码复制进去。按 ``Ctrl+X`` → ``Y`` → ``Enter`` 保存并退出。

  .. code-block:: python
  
      from picarx import Picarx
      from picarx.tts import Espeak
      import time
  
      px = Picarx()
      tts = Espeak()
  
      # Quick hello (sanity check)
      tts.say("Hello! I'm Espeak TTS.")
  
      # Optional voice tuning
      # tts.set_amp(100)   # 0 to 200
      # tts.set_speed(150) # 80 to 260
      # tts.set_gap(5)     # 0 to 200
      # tts.set_pitch(50)  # 0 to 99

* 运行程序：

  .. code-block:: bash

     sudo python3 test_tts_espeak.py

* 你会听到 PiCar-X 说出 “Hello! I'm Espeak TTS.”  
* 取消注释上面的可选设置行，尝试不同的 ``amp``、``speed``、``gap``、``pitch`` 值，体验声音的变化。

----

2. 测试 Pico2Wave
---------------------

Pico2Wave 生成的声音更加自然，接近人声。  
它的使用更简单，但灵活性较低 —— 只能设置语言，不能调节语速或音高。

**步骤如下**：

* 创建一个新文件：

  .. code-block:: bash

      cd ~/picar-x/example
      sudo nano test_tts_pico2wave.py

* 将以下代码复制进去。按 ``Ctrl+X`` → ``Y`` → ``Enter`` 保存并退出。

  .. code-block:: python
  
      from picarx import Picarx
      from picarx.tts import Pico2Wave
      import time
  
      px = Picarx()
      tts = Pico2Wave()
  
      tts.set_lang('en-US')  # en-US, en-GB, de-DE, es-ES, fr-FR, it-IT
  
      # Quick hello (sanity check)
      tts.say("Hello! I'm Pico2Wave TTS.")

* 运行程序：

  .. code-block:: bash

    sudo python3 test_tts_pico2wave.py

* 你会听到 PiCar-X 说出 “Hello! I'm Pico2Wave TTS.”  
* 尝试更改语言（例如 ``es-ES`` 表示西班牙语），感受不同语言的语音效果。

----

3. 语音提示小车
--------------------

现在将 **Pico2Wave** 或 **Espeak** 与 PiCar-X 的驾驶代码结合，做一个“语音提示小车”：  
在每个动作之前，小车都会先播报即将执行的操作。

**运行代码**

.. code-block:: bash

    cd ~/picar-x/example
    sudo python3 14.voice_promt_car.py
    
运行后，你会看到 PiCar-X 依次前进、后退和转向，并在每次动作前先进行语音播报。  
这会让你的小车更安全、更友好、更具交互性。

**代码**


.. code-block:: python

  from picarx import Picarx
  from picarx.tts import Espeak
  import time

  # If you want to try Pico2Wave instead of Espeak, uncomment below:
  # from picarx.tts import Pico2Wave
  # tts = Pico2Wave()
  # tts.set_lang('en-US')  # Options: en-US, en-GB, de-DE, es-ES, fr-FR, it-IT

  px = Picarx()
  tts = Espeak()

  # Quick hello (test)
  tts.say("Hello! I'm PiCar-X.")

  def main():
      try:
          # Forward
          tts.say("Moving forward")
          px.forward(30)
          time.sleep(2)
          px.stop()

          # Backward
          tts.say("Moving backward")
          px.backward(30)
          time.sleep(2)
          px.stop()

          # Turn left
          tts.say("Turning left")
          px.set_dir_servo_angle(-20)
          px.forward(30)
          time.sleep(2)
          px.stop()
          px.set_dir_servo_angle(0)

          # Turn right
          tts.say("Turning right")
          px.set_dir_servo_angle(20)
          px.forward(30)
          time.sleep(2)
          px.stop()
          px.set_dir_servo_angle(0)

      except KeyboardInterrupt:
          # Stop if interrupted
          px.stop()
      finally:
          # Reset to safe state
          px.stop()
          px.set_dir_servo_angle(0)

  if __name__ == "__main__":
      main()

----

故障排查
-------------------

* **运行 Espeak 或 Pico2Wave 时没有声音**

  * 检查扬声器或耳机是否连接、音量是否被静音。  
  * 在终端中运行以下命令进行快速测试：

    .. code-block:: bash

       espeak "Hello world"
       pico2wave -w test.wav "Hello world" && aplay test.wav

  如果仍然听不到声音，说明是音频输出的问题，而不是 Python 代码的问题。

* **Espeak 声音太快或太机械**

  * 尝试在代码中调整参数：

    .. code-block:: python

       tts.set_speed(120)   # 减慢语速
       tts.set_pitch(60)    # 改变音高

* **运行代码时出现 Permission denied**

  * 尝试使用 ``sudo`` 运行：

    .. code-block:: bash

       sudo python3 test_tts_espeak.py


Espeak 与 Pico2Wave 对比
-------------------------------------

.. list-table::
   :widths: 20 40 40
   :header-rows: 1

   * - 功能
     - Espeak
     - Pico2Wave
   * - 语音质量
     - 机械感强、电子音
     - 更加自然，接近人声
   * - 语言
     - 默认英语（也支持多语言）
     - 语言较少，但常见语言齐全
   * - 可调节项
     - 是（语速、音高等）
     - 否（仅语言）
   * - 性能
     - 非常快，资源占用小
     - 稍慢，资源占用略高

