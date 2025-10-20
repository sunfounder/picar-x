
15. 使用 Piper 和 OpenAI 的 AI 讲故事机器人
========================================================

在上一节课中，我们尝试了树莓派上两个内置的 TTS 引擎（**Espeak** 和 **Pico2Wave**）。  
现在我们将探索另外两种更强大的选项：**Piper** （离线，基于神经网络）和 **OpenAI TTS** （在线，云端）。

* **Piper**：一种在树莓派上本地运行的离线 TTS 引擎。  
* **OpenAI TTS**：一种提供非常自然、人类般语音的在线服务。

在本节课结束时，你的 PiCar-X 将能够一边行驶，一边像个小讲故事的人一样讲笑话。  

----

开始之前
----------------

确保你已经准备好以下内容：

* :ref:`install_all_modules` — 安装 ``robot-hat``、 ``vilib``、 ``picar-x`` 模块，然后运行脚本 ``i2samp.sh``。

----

.. _test_piper:

1. 测试 Piper
------------------

**操作步骤**：

#. 创建一个新文件：

   .. code-block:: bash

      cd ~/picar-x/example
      sudo nano test_tts_piper.py

#. 将下面的示例代码复制到文件中。按 ``Ctrl+X``，然后 ``Y``，最后 ``Enter`` 保存并退出。

   .. code-block:: python

       from picarx.tts import Piper

       tts = Piper()

       # 列出支持的语言
       print(tts.available_countrys())

       # 列出英语（en_us）的可用模型
       print(tts.available_models('en_us'))

       # 设置语音模型（如果本地没有会自动下载）
       tts.set_model("en_US-amy-low")

       # 播放语音
       tts.say("Hello! I'm Piper TTS.")

   * ``available_countrys()``：打印支持的语言。  
   * ``available_models()``：列出指定语言的可用模型。  
   * ``set_model()``：设置语音模型（若无则自动下载）。  
   * ``say()``：将文本转换为语音并播放。

#. 运行程序：

   .. code-block:: bash

      sudo python3 test_tts_piper.py

#. 第一次运行时，会自动下载所选语音模型。 

   * 你将听到 PiCar-X 说出：``Hello! I'm Piper TTS.``

   * 你可以通过调用 ``set_model()`` 并传入其他模型名称来切换语言模型。


2. 测试 OpenAI TTS
-------------------------------

**获取并保存 API Key**

#. 前往 |link_openai_platform| 并登录。在 **API keys** 页面，点击 **Create new secret key**。

   .. image:: img/llm_openai_create.png

#. 填写详细信息（Owner、Name、Project 以及必要的权限），然后点击 **Create secret key**。

   .. image:: img/llm_openai_create_confirm.png

#. 密钥创建后请立即复制 —— 之后将无法再次查看。如果丢失，你必须重新生成一个新密钥。

   .. image:: img/llm_openai_copy.png

#. 在你的项目文件夹中（例如：``/picar-x/example``），创建一个名为 ``secret.py`` 的文件：

   .. code-block:: bash

       cd ~/picar-x/example
       sudo nano secret.py

#. 将密钥粘贴到文件中，如下所示：

   .. code-block:: python

       # secret.py
       # Store secrets here. Never commit this file to Git.
       OPENAI_API_KEY = "sk-xxx"

**编写并运行测试程序**

#. 创建一个新文件：

   .. code-block:: bash

       cd ~/picar-x/example
       sudo nano test_tts_openai.py

#. 将以下示例代码复制到文件中。按 ``Ctrl+X``，然后 ``Y``，最后 ``Enter`` 保存并退出。

   .. code-block:: python

      from picarx.tts import OpenAI_TTS
      from secret import OPENAI_API_KEY   # or use the try/except version shown above

      # 初始化 OpenAI TTS
      tts = OpenAI_TTS(api_key=OPENAI_API_KEY)
      tts.set_model('gpt-4o-mini-tts')  # 低延迟 TTS 模型
      tts.set_voice('alloy')            # 选择一个声音

      # 快速打招呼（检查是否正常）
      tts.say("Hello! I'm OpenAI TTS.")

#. 运行程序：

   .. code-block:: bash

       sudo python3 test_tts_openai.py

#. 你应该听到 PiCar-X 说出：

   ``Hello! I'm OpenAI TTS.``

**可用的模型与声音**

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - 分类
     - 选项
   * - 模型
     - 
       - ``tts-1``  
       - ``tts-1-hd``  
       - ``gpt-4o-mini-tts``  
       - ``accent``  
       - ``emotional-range``  
       - ``intonation``  
       - ``impressions``  
       - ``speed-of-speech``  
       - ``tone``  
       - ``whispering``
   * - 声音
     - 
       - ``alloy``  
       - ``ash``  
       - ``ballad``  
       - ``coral``  
       - ``echo``  
       - ``fable``  
       - ``nova``  
       - ``onyx``  
       - ``sage``  
       - ``shimmer``


3. 讲故事机器人
------------------------

现在我们已经测试了 **Piper** 和 **OpenAI TTS**，接下来让我们将它们应用到一个真实项目中：  
一个会 **讲故事的小车机器人**，它会一边行驶一边讲笑话。

在这个程序中，PiCar-X 将会：

* 启动时用 TTS 问候你。  
* 向前移动并讲第一个笑话。  
* 再次向前移动并讲第二个笑话。  
* 最后倒车返回“家”，并说再见。

就像一个会讲故事的小车机器人！

**运行代码**

.. code-block:: bash

    cd ~/picar-x/example
    sudo python3 15.storytelling_robot.py

**代码**



.. code-block:: python

   from picarx import Picarx
   import time

   # === TTS Configuration ===
   # Default: Piper
   from picarx.tts import Piper
   tts = Piper()
   tts.set_model("en_US-amy-low")  # use the voice model you installed

   # Optional: switch to OpenAI TTS
   # from picarx.tts import OpenAI_TTS
   # from secret import OPENAI_API_KEY
   # tts = OpenAI_TTS(api_key=OPENAI_API_KEY)
   # tts.set_model("gpt-4o-mini-tts")  # low-latency TTS model
   # tts.set_voice("alloy")            # choose a voice

   # === PiCar-X Setup ===
   px = Picarx()

   # Quick hello (sanity check)
   tts.say("Hello! I'm PiCar-X speaking with Piper.")

   def main():
       try:
           # Leg 1
           px.forward(30)
           time.sleep(3)
           px.stop()
           tts.say("Why can't your nose be twelve inches long? Because then it would be a foot!")

           # Leg 2
           px.forward(30)
           time.sleep(3)
           px.stop()
           tts.say("Why did the cow go to outer space? To see the moooon!")

           # Wrap-up
           tts.say("That's all for today. Goodbye, let's go home and sleep.")
           px.backward(30)
           time.sleep(6)
           px.stop()

       except KeyboardInterrupt:
           px.stop()
       finally:
           px.stop()
           px.set_dir_servo_angle(0)

   if __name__ == "__main__":
       main()

----

故障排查
-------------------

* **未找到模块 'secret'（No module named 'secret'）**

  这表示 ``secret.py`` 不在与你的 Python 文件相同的文件夹中。  
  将 ``secret.py`` 移动到你运行脚本的同一目录，例如：

  .. code-block:: bash

     ls ~/picar-x/example
     # 确认同时能看到：secret.py 和你的 .py 文件

* **OpenAI：无效的 API key / 401（Invalid API key / 401）**

  * 检查是否粘贴了完整密钥（以 ``sk-`` 开头），并确保没有多余的空格/换行。  
  * 确保在代码中正确导入：

    .. code-block:: python

       from secret import OPENAI_API_KEY

  * 确认树莓派可联网（尝试 ``ping api.openai.com``）。

* **OpenAI：额度用尽 / 计费错误（Quota exceeded / billing error）**

  * 你可能需要在 OpenAI 控制台中添加计费或提高额度。  
  * 解决账户/计费问题后再重试。

* **Piper：调用 tts.say() 但没有声音**

  * 确认语音模型确实已存在：

    .. code-block:: bash

       ls ~/.local/share/piper/voices

  * 确认代码里的模型名完全一致：

    .. code-block:: python

       tts.set_model("en_US-amy-low")

  * 检查树莓派的音频输出设备/音量（``alsamixer``），并确认扬声器已连接且供电正常。

* **ALSA / 声卡错误（如 “Audio device busy” 或 “No such file or directory”）**

  * 关闭占用音频的其他程序。  
  * 若设备一直“忙”，重启树莓派。  
  * 使用 HDMI 还是耳机口，请在 Raspberry Pi OS 的音频设置中选对输出设备。

* **运行 Python 时 Permission denied**

  * 若环境需要，尝试使用 ``sudo``：

    .. code-block:: bash

       sudo python3 test_tts_piper.py



TTS 引擎对比
-------------------------

.. list-table:: 特性对比：Espeak vs Pico2Wave vs Piper vs OpenAI TTS
   :header-rows: 1
   :widths: 18 18 20 22 22

   * - 项目
     - Espeak
     - Pico2Wave
     - Piper
     - OpenAI TTS
   * - 运行环境
     - 树莓派内置（离线）
     - 树莓派内置（离线）
     - 树莓派 / 电脑（离线，需要模型）
     - 云端（在线，需要 API key）
   * - 音色质量
     - 机械感强
     - 比 Espeak 更自然
     - 自然（神经网络 TTS）
     - 非常自然/接近人声
   * - 可控项
     - 语速、音调、音量
     - 控制项较少
     - 可选不同音色/模型
     - 可选模型与音色
   * - 语言
     - 多（质量不一）
     - 语言较少
     - 多语音/多语言可选
     - 英语最佳（其他视可用性）
   * - 时延/速度
     - 很快
     - 快
     - 在 Pi 4/5 上配“low”模型可实时
     - 取决于网络（通常较低时延）
   * - 部署难度
     - 极低
     - 极低
     - 需下载 ``.onnx`` + ``.onnx.json`` 模型
     - 需创建 API key、安装客户端
   * - 最佳适用
     - 快速测试、基础播报
     - 稍好一些的离线音色
     - 需要更好音质的本地项目
     - 最高音质、丰富音色选项
