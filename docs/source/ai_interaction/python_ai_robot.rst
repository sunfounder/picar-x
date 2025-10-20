

.. _ai_voice_assistant_car:

21. AI 语音助手小车
===========================

本课程将把你的 PiCar-X 变成一台 **由AI驱动的轮式语音助手**。  
机器人能够通过你的语音唤醒，识别你说的话，用情绪化的声音回应，  
并通过动作、手势和灯光来“表达”它的情感。

你将构建一个 **完全交互式的语音助手小车**，使用以下组件：

* **LLM** - 大语言模型（OpenAI GPT 或 豆包 Doubao）。  
* **STT** - 语音转文本（语音识别）。  
* **TTS** - 文本转语音（语音合成）。  
* **传感器 + 动作** - 超声波、摄像头以及内置的情绪表达动作。

----

开始之前
----------------

请确保你已经完成以下步骤：

* :ref:`install_all_modules` — 安装 ``robot-hat``、 ``vilib``、 ``picar-x`` 模块，然后运行脚本 ``i2samp.sh``。
* :ref:`test_piper` — 检查 **Piper TTS** 支持的语言。  
* :ref:`test_vosk` — 检查 **Vosk STT** 支持的语言。  
* :ref:`py_online_llm` — 这一步 **非常重要**：获取你的 **OpenAI** 或 **豆包 Doubao** API key，或其他支持的 LLM 的 API key。

你还需要具备：

* PiCar-X 上可用的 **麦克风** 和 **扬声器**。  
* 已在 ``secret.py`` 中存储的 **有效 API key**。  
* 稳定的网络连接（推荐使用 **有线连接** 以获得更高稳定性）。

----

运行示例
---------------

中英文两个版本的示例文件都放在同一个目录下：

.. code-block:: bash

   cd ~/picar-x/example

**英文版本** （使用 OpenAI GPT，英文指令）：

.. code-block:: bash

   sudo python3 21.voice_active_car_gpt.py

* LLM: ``OpenAI GPT-4o-mini``  
* TTS: ``en_US-ryan-low`` （Piper）  
* STT: Vosk（``en-us``）

唤醒词：

.. code-block::

   "Hey buddy"

---

**中文版本** （使用 豆包 Doubao，中文指令）：

.. code-block:: bash

   sudo python3 21.voice_active_car_doubao_cn.py

* LLM: ``Doubao-seed-1-6-250615``  
* TTS: ``zh_CN-huayan-x_low`` （Piper）  
* STT: Vosk（``cn``）

唤醒词：

.. code-block::

   "你好 滴滴"

.. note::

   你可以在代码中修改 **唤醒词** 和 **机器人名称**：  
   ``NAME = "Buddy"`` 或 ``NAME = "滴滴"``  
   ``WAKE_WORD = ["hey buddy"]`` 或 ``WAKE_WORD = ["你好 滴滴"]``

----

运行效果
-----------------

当你成功运行这个示例后：

* 机器人会 **等待唤醒词** （例如 “Hey Buddy” / “你好 滴滴”）。  
* 当它听到唤醒词时：

  * LED 会 **闪烁** 并保持亮起。  
  * 机器人会用愉快的声音 **问候你**。

* 随后它开始 **实时监听你的声音**。  
* 当识别出你说的话后，它会：

  * 将你的语音发送给 **LLM** （OpenAI 或 豆包 Doubao）。  
  * 在处理时 **思考** 并闪烁 LED。  
  * 用 **TTS 语音** 回复你。  
  * 执行 **相应的动作** （例如：点头、转向、庆祝）。

* 如果你靠得太近，超声波传感器会：

  * 自动触发 **后退** 以保证安全。  
  * 打断当前回合并给出警告提示。

**示例交互**

.. code-block:: text

   You: Hey Buddy
   Robot: Hi there!

   You: Turn left and look around.
   Robot: Roger that, turning my head left like a curious cat!
   ACTIONS: turn_left, look_left

----

切换其他 LLM 或 TTS
------------------------------

你可以通过简单修改代码轻松切换到其他 LLM、TTS 或 STT 语言：

* 支持的 LLM：

  * OpenAI
  * 豆包 Doubao
  * Deepseek
  * Gemini
  * Qwen
  * Grok

* :ref:`test_piper` — 检查 **Piper TTS** 支持的语言。  
* :ref:`test_vosk` — 检查 **Vosk STT** 支持的语言。

要切换，只需修改代码的初始化部分：

.. code-block:: python

   from picarx.llm import Gemini as LLM
   llm = LLM(api_key="YOUR_KEY", model="gemini-pro")

   # 设置模型和语言
   TTS_MODEL = "en_US-ryan-low"
   STT_LANGUAGE = "en-us"


----

动作与声音参考
------------------------

以下是 LLM 可以返回的 **动作关键词** （位于 ``ACTIONS:`` 行之后）及其在机器人上的对应效果。

.. list-table::
   :header-rows: 1
   :widths: 20 55 25

   * - **动作**
     - **功能说明（per preset_actions.py）**
     - **效果 / 备注**
   * - ``shake head``
     - 快速左右摆动摄像头水平角度，幅度逐渐减小，然后回到中间。
     - “否”的手势；车轮保持停止。
   * - ``nod``
     - 上下点头两次，然后回到中间。
     - “是”的手势；车轮保持停止。
   * - ``wave hands``
     - 倾斜摄像头，然后方向舵左右摆动两次（±25°），再回中。
     - 调皮挥手（使用转向舵机模拟“手臂”）。
   * - ``resist``
     - 小幅倾斜；交替（转向 ±15°，水平 ±15°）3 次；停止并回中。
     - “拒绝”/防御动作。
   * - ``act cute``
     - 低头；向前/后快速小幅度移动（短暂电机脉冲），然后复位。
     - 俏皮可爱的小动作；移动时间很短。
   * - ``rub hands``
     - 小幅左右摆动方向舵（±6°）5 次，然后复位。
     - 模仿“搓手”动作。
   * - ``think``
     - 平滑向右转头 + 低头 + 向右打方向；短暂停顿；摆出“思考”姿势；复位。
     - 用于单次“思考”动画。
   * - ``twist body``
     - 三个循环：短暂前进/停止/左转头/左打方向，然后短暂后退/停止/右转头/右打方向。
     - 模仿“扭动身体”动作。
   * - ``celebrate``
     - 抬头；向右两次转头+打方向，再向左两次；最后回中。
     - 欢快庆祝动作。
   * - ``depressed``
     - 多次下压头部，角度和间隔变化；最后长暂停并复位。
     - “伤心”姿态序列。

移动与实用功能
~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 22 58 20

   * - **动作**
     - **功能说明**
     - **备注**
   * - ``forward``
     - 以低速前进约 1 秒，然后停止。
     - 由 ``forward(car)`` 实现（5% 速度 + 1s）。
   * - ``backward``
     - 以低速后退约 1 秒，然后停止。
     - 由 ``backward(car)`` 实现（5% 速度 + 1s）。

音效
~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 24 56 20

   * - **声音**
     - **功能说明**
     - **备注**
   * - ``honking``
     - 异步播放 ``car-double-horn.wav`` （音量约 100）。
     - 通过 ``Music.sound_play_threading`` 触发。
   * - ``start engine``
     - 异步播放 ``car-start-engine.wav`` （音量约 50）。
     - 启动 / 就绪提示音。

传感器触发（自动）
~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **超声波接近** 

  * 触发条件：距离 < 10 cm  
  * 副作用：自动 ``backward`` + 本轮禁用图像  
  * 注入消息：``<<<Ultrasonic sense too close: {distance}cm>>>``

生命周期钩子（LED 指示）
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ``before_listen`` → 闪烁两次（准备聆听）  
* ``before_think`` → 闪烁（思考中）  
* ``before_say`` → LED 常亮（说话中）  
* ``after_say`` → 等待动作完成 → LED 熄灭  
* ``on_stop`` → 停止动作，关闭设备


----

故障排查
---------------

* **机器人对唤醒词没有反应**  

  * 检查麦克风是否正常工作。  
  * 确保 ``WAKE_ENABLE = True``。  
  * 调整唤醒词以匹配你的发音。

* **扬声器没有声音**
 
  * 验证 TTS 模型设置。  
  * 手动测试 Piper 或 Espeak。  
  * 检查扬声器连接与音量。

* **API Key 错误或超时** 
 
  * 在 ``secret.py`` 中检查你的密钥。  
  * 确保网络连接正常。  
  * 确认所用 LLM 受支持。

* **Picar-X 不移动或不执行动作**
 
  * 检查动作名称是否与 ``actions_dict`` 匹配。  
  * 验证电机与舵机连接。

* **超声波传感器频繁误触发。**  

  * 检查传感器的安装高度与角度。  
  * 在代码中调整 ``TOO_CLOSE`` 距离阈值。
