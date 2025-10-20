
16. 使用 Vosk（离线）的语音控制小车
==============================================

Vosk 是一个轻量级的语音转文字（STT）引擎，支持多种语言，并且可以在树莓派上完全 **离线** 运行。  
你只需联网一次下载语言模型，之后就可以在没有网络连接的情况下正常使用。

在本课程中，我们将：

* 检查树莓派上的麦克风。  
* 安装并测试 Vosk 的语言模型。  
* 构建一台 **语音控制的 PiCar-X**，通过唤醒词启动，并识别诸如 **forward**、**backward**、**left** 和 **right** 等语音指令。

----

开始之前
----------------

确保你已经准备好以下内容：

* :ref:`install_all_modules` — 安装 ``robot-hat``、 ``vilib``、 ``picar-x`` 模块，然后运行脚本 ``i2samp.sh``。

----

1. 检查麦克风
--------------------------

在使用语音识别前，先确保你的 USB 麦克风工作正常。

#. 列出可用的录音设备：

   .. code-block:: bash

      arecord -l

   找到类似 ``card 1: ... device 0`` 的行。

#. 录制一个 3 秒的测试音频（将 ``1,0`` 替换为上面找到的数字）：

   .. code-block:: bash

      arecord -D plughw:1,0 -f S16_LE -r 16000 -d 3 test.wav

   * 示例：如果你的设备是 ``card 2, device 0``，使用：

   .. code-block:: bash

      arecord -D plughw:2,0 -f S16_LE -r 16000 -d 3 test.wav

#. 回放录制的音频，确认录音是否成功：

   .. code-block:: bash

      aplay test.wav

#. 如果录音声音太小，可以调整麦克风音量：

   .. code-block:: bash

      alsamixer

   * 按 **F6** 选择你的 USB 麦克风。  
   * 找到 **Mic** 或 **Capture** 通道。  
   * 确保麦克风未静音（**[MM]** 表示静音，按 ``M`` 解除静音 → 应显示 **[OO]**）。  
   * 使用 ↑ / ↓ 方向键调整音量。

.. _test_vosk:

2. 测试 Vosk
--------------------------

**步骤如下**：

#. 创建一个新文件：

   .. code-block:: bash

      cd ~/picar-x/example
      sudo nano test_stt_vosk.py

#. 将以下示例代码复制进去，然后按 ``Ctrl+X``，再按 ``Y`` 和 ``Enter`` 保存退出。

   .. code-block:: python

      from picarx.stt import Vosk

      vosk = Vosk(language="en-us")

      print(vosk.available_languages)

      while True:
          print("Say something")
          result = vosk.listen(stream=False)
          print(result)

#. 运行程序：

   .. code-block:: bash

      sudo python3 test_stt_vosk.py

#. 第一次使用新语言运行时，Vosk 会**自动下载语言模型** （默认下载 **small** 版本）。  
   同时会打印支持的语言列表，然后你会看到：

   .. code-block:: text

        vosk-model-small-en-us-0.15.zip: 100%|███████████████████| 39.3M/39.3M [00:05<00:00, 7.85MB/s]
        ['ar', 'ar-tn', 'ca', 'cn', 'cs', 'de', 'en-gb', 'en-in', 'en-us', 'eo', 'es', 'fa', 'fr', 'gu', 'hi', 'it', 'ja', 'ko', 'kz', 'nl', 'pl', 'pt', 'ru', 'sv', 'te', 'tg', 'tr', 'ua', 'uz', 'vn']
        Say something

   这意味着：

   * 模型文件（``vosk-model-small-en-us-0.15``）已成功下载。  
   * 已打印支持的语言列表。  
   * 系统正在监听麦克风输入 —— 对 PiCar-X 说话，识别出的文本会实时显示在终端中。

   **提示**：

   * 保持麦克风距离 15–30 厘米。  
   * 选择与你的语言和口音匹配的模型。

**流式模式（可选）**

你也可以使用流式识别模式，在说话时实时查看部分识别结果。

.. code-block:: python

   from picarx.stt import Vosk

   vosk = Vosk(language="en-us")

   while True:
       print("Say something")
       for result in vosk.listen(stream=True):
           if result["done"]:
               print(f"final:   {result['final']}")
           else:
               print(f"partial: {result['partial']}", end="\r", flush=True)


3. 语音控制小车
-------------------------

现在，让我们把语音识别和 PiCar-X 连接起来！

我们将使用一个 **唤醒词** （"hey robot"），只有当小车被激活后才会监听指令。  
这不仅节省 CPU，还可以避免误触发。

**运行代码**

.. code-block:: bash

   cd ~/picar-x/example
   sudo python3 16.voice_controlled_car.py

在这个程序中，小车将会：

* 等待唤醒词 **"hey robot"**。  
* 之后你就可以自然地说话了 —— 只要你的句子中包含以下任一关键词（**forward**、**backward**、**left**、**right**），小车就会做出对应动作。  

  例如：

  * “Can you move forward a little?” → 小车前进。  
  * “Please turn left now.” → 小车左转。

* 当你说 **"sleep"** 时，小车会停止控制循环，重新进入等待模式。

**代码**


.. code-block:: python

   from picarx import Picarx
   from picarx.stt import Vosk
   import time

   px = Picarx()
   stt = Vosk(language="en-us")

   WAKE_WORDS = ["hey robot"]

   print('Say "hey robot" to wake me up! Then say: forward / backward / left / right. Say "sleep" to stop listening.')

   try:
       while True:
           # --- wait for wake word once ---
           stt.wait_until_heard(WAKE_WORDS)
           print("Wake word detected. Listening for commands... (say 'sleep' to pause)")

           # --- command loop: multiple commands after one wake ---
           while True:
               res = stt.listen(stream=False)
               text = res.get("text", "") if isinstance(res, dict) else str(res)
               text = text.lower().strip()
               if not text:
                   continue

               print("Heard:", text)

               if "sleep" in text:
                   # pause command mode; go back to wait for wake word
                   px.stop(); px.set_dir_servo_angle(0)
                   print("Sleeping. Say 'hey robot' to wake me again.")
                   break

               elif "forward" in text:
                   px.set_dir_servo_angle(0)
                   px.forward(30); time.sleep(1); px.stop()

               elif "backward" in text:
                   px.set_dir_servo_angle(0)
                   px.backward(30); time.sleep(1); px.stop()

               elif "left" in text:
                   px.set_dir_servo_angle(-25)
                   px.forward(30); time.sleep(1)
                   px.stop(); px.set_dir_servo_angle(0)

               elif "right" in text:
                   px.set_dir_servo_angle(25)
                   px.forward(30); time.sleep(1)
                   px.stop(); px.set_dir_servo_angle(0)
               # (ignore other words)

   except KeyboardInterrupt:
       pass
   finally:
       px.stop(); px.set_dir_servo_angle(0)
       print("Stopped and centered. Bye.")

故障排查
-----------------

* **No such file or directory（运行 `arecord` 时出现）**

  你可能使用了错误的声卡 / 设备编号。  
  运行：

  .. code-block:: bash

     arecord -l

  然后用 USB 麦克风对应的编号替换 ``1,0``。

* **录音文件没有声音**

  打开混音器检查麦克风音量：

  .. code-block:: bash

     alsamixer

  * 按 **F6** 选择你的 USB 麦克风。  
  * 确保 **Mic/Capture** 没有被静音（应显示 **[OO]** 而不是 **[MM]**）。  
  * 使用 ↑ 键提高音量。

* **Vosk 无法识别语音**

  * 确保 **语言代码** 与模型匹配（例如英语为 ``en-us``，中文为 ``zh-cn``）。  
  * 保持麦克风距离 15–30 厘米，并避免背景噪音。  
  * 清晰、适中速度地说话。

* **唤醒词（“hey robot”）无法触发**

  * 语气自然，不要太快。  
  * 检查程序是否有识别输出，如果没有，说明麦克风可能未正常工作。

* **识别延迟高 / 速度慢**

  * 默认下载的是 **small 模型** （速度较快但准确率较低）。  
  * 如果仍然较慢，可关闭其他程序释放 CPU。
