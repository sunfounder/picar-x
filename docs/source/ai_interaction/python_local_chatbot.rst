
19. 本地语音聊天机器人
===========================

在本课中，你将把之前学到的一切结合起来——**语音识别（STT）**、  
**文本转语音（TTS）**，以及 **本地 LLM（Ollama）**——在你的 PiCar-X 系统上构建一个完全离线运行的 **语音聊天机器人**。

工作流程很简单：

#. **监听** — 麦克风捕获你的语音，并使用 **Vosk** 转写。  
#. **思考** — 将文本发送到运行在 Ollama 上的本地 **LLM** （例如 ``llama3.2:3b``）。  
#. **说话** — 聊天机器人使用 **Piper TTS** 朗读回答。  

这将创建一个 **免手动的对话式机器人**，能够实时理解并回应。

----

开始之前
----------------

确保你已经准备好以下内容：

* 已测试 **Piper TTS** （:ref:`test_piper`）并选择一个可用的语音模型。  
* 已测试 **Vosk STT** （:ref:`test_vosk`）并选择合适的语言包（例如 ``en-us``）。  
* 在你的树莓派或另一台计算机上安装了 **Ollama** （:ref:`download_ollama`），并下载了一个模型，如 ``llama3.2:3b`` （如果内存有限，可选择更小的 ``moondream:1.8b``）。

----

运行代码
--------------

#. 打开示例脚本：

   .. code-block:: bash

      cd ~/picar-x/example
      sudo nano 19.local_voice_chatbot.py

#. 按需更新参数：

   * ``stt = Vosk(language="en-us")``：将其改为与你的口音 / 语言包匹配（例如 ``en-us``、``zh-cn``、``es``）。  
   * ``tts.set_model("en_US-amy-low")``：替换为你在 :ref:`test_piper` 中验证过的 Piper 语音模型。  
   * ``llm = Ollama(ip="localhost", model="llama3.2:3b")``：根据你的环境更新 ``ip`` 与 ``model``。  

     * ``ip``：如果 Ollama 在 **同一台树莓派** 上运行，使用 ``localhost``。如果在局域网的另一台电脑上运行，请在 Ollama 中启用 **Expose to network**，并将 ``ip`` 设置为那台电脑的局域网 IP。  
     * ``model``：必须与您在 Ollama 中下载 / 启用的模型名称 **完全一致**。  

#. 运行脚本：

   .. code-block:: bash

      cd ~/picar-x/example
      sudo python3 19.local_voice_chatbot.py

#. 运行后，你应当看到：

   * 机器人用语音播放欢迎语。  
   * 它等待语音输入。  
   * Vosk 将你的语音转写为文本。  
   * 文本被发送到 Ollama，后者以流式方式返回回复。  
   * 对回复进行清理（移除隐藏推理）后，由 Piper 朗读播放。  
   * 随时可通过 ``Ctrl+C`` 停止程序。

----

代码
----

.. code-block:: python

   import re
   import time
   from picarx.llm import Ollama
   from picarx.stt import Vosk
   from picarx.tts import Piper

   # Initialize speech recognition
   stt = Vosk(language="en-us")

   # Initialize TTS
   tts = Piper()
   tts.set_model("en_US-amy-low")

   # Instructions for the LLM
   INSTRUCTIONS = (
       "You are a helpful assistant. Answer directly in plain English. "
       "Do NOT include any hidden thinking, analysis, or tags like <think>."
   )
   WELCOME = "Hello! I'm your voice chatbot. Speak when you're ready."

   # Initialize Ollama connection
   llm = Ollama(ip="localhost", model="llama3.2:3b")
   llm.set_max_messages(20)
   llm.set_instructions(INSTRUCTIONS)

   # Utility: clean hidden reasoning
   def strip_thinking(text: str) -> str:
       if not text:
           return ""
       text = re.sub(r"<\s*think[^>]*>.*?<\s*/\s*think\s*>", "", text, flags=re.DOTALL|re.IGNORECASE)
       text = re.sub(r"<\s*thinking[^>]*>.*?<\s*/\s*thinking\s*>", "", text, flags=re.DOTALL|re.IGNORECASE)
       text = re.sub(r"```(?:\s*thinking)?\s*.*?```", "", text, flags=re.DOTALL|re.IGNORECASE)
       text = re.sub(r"\[/?thinking\]", "", text, flags=re.IGNORECASE)
       return re.sub(r"\s+\n", "\n", text).strip()

   def main():
       print(WELCOME)
       tts.say(WELCOME)

       try:
           while True:
               print("\n🎤 Listening... (Press Ctrl+C to stop)")

               # Collect final transcript from Vosk
               text = ""
               for result in stt.listen(stream=True):
                   if result["done"]:
                       text = result["final"].strip()
                       print(f"[YOU] {text}")
                   else:
                       print(f"[YOU] {result['partial']}", end="\r", flush=True)

               if not text:
                   print("[INFO] Nothing recognized. Try again.")
                   time.sleep(0.1)
                   continue

               # Query Ollama with streaming
               reply_accum = ""
               response = llm.prompt(text, stream=True)
               for next_word in response:
                   if next_word:
                       print(next_word, end="", flush=True)
                       reply_accum += next_word
               print("")

               # Clean and speak
               clean = strip_thinking(reply_accum)
               if clean:
                   tts.say(clean)
               else:
                   tts.say("Sorry, I didn't catch that.")

               time.sleep(0.05)

       except KeyboardInterrupt:
           print("\n[INFO] Stopping...")
       finally:
           tts.say("Goodbye!")
           print("Bye.")

   if __name__ == "__main__":
       main()

----

代码解析
-------------

**导入与全局设置**

.. code-block:: python

   import re
   import time
   from picarx.llm import Ollama
   from picarx.stt import Vosk
   from picarx.tts import Piper

引入你之前构建的三个子系统：  
用于语音转文本（STT）的 **Vosk**，用于 LLM 的 **Ollama**，以及用于文本转语音（TTS）的 **Piper**。



**初始化 STT（Vosk）**

.. code-block:: python

   stt = Vosk(language="en-us")

加载美式英语的 Vosk 模型。  
将语言代码（例如 ``zh-cn``、``es``）改为与你的语音包匹配的语言，以获得更高准确率。



**初始化 TTS（Piper）**

.. code-block:: python

   tts = Piper()
   tts.set_model("en_US-amy-low")

创建一个 Piper 引擎并选择特定音色。  
选择你在 :ref:`test_piper` 中已经测试通过的模型。较低质量的音色更快且占用更少 CPU。



**LLM 指令与欢迎语**

.. code-block:: python

   INSTRUCTIONS = (
       "You are a helpful assistant. Answer directly in plain English. "
       "Do NOT include any hidden thinking, analysis, or tags like <think>."
   )
   WELCOME = "Hello! I'm your voice chatbot. Speak when you're ready."

两个关键的用户体验设计：

* 保持 **回答简短直接** （有助于提升 TTS 清晰度）。  
* 明确禁止隐藏的“思维链”标签，以 **减少噪声输出**。



**连接 Ollama 并设置会话范围**

.. code-block:: python

   llm = Ollama(ip="localhost", model="llama3.2:3b")
   llm.set_max_messages(20)
   llm.set_instructions(INSTRUCTIONS)

* ``ip="localhost"`` 假设 Ollama 运行在同一台树莓派上。若运行在局域网的另一台机器上，请在 Ollama 中启用 *Expose to network*，并填写该机器的 **局域网 IP**。  
* ``set_max_messages(20)`` 保持较短的对话历史。如果内存 / 时延紧张，可再调小。



**在说话前移除隐藏推理 / 标签**

.. code-block:: python

   def strip_thinking(text: str) -> str:
       if not text:
           return ""
       text = re.sub(r"<\s*think[^>]*>.*?<\s*/\s*think\s*>", "", text, flags=re.DOTALL|re.IGNORECASE)
       text = re.sub(r"<\s*thinking[^>]*>.*?<\s*/\s*thinking\s*>", "", text, flags=re.DOTALL|re.IGNORECASE)
       text = re.sub(r"```(?:\s*thinking)?\s*.*?```", "", text, flags=re.DOTALL|re.IGNORECASE)
       text = re.sub(r"\[/?thinking\]", "", text, flags=re.IGNORECASE)
       return re.sub(r"\s+\n", "\n", text).strip()

有些模型可能会输出内部样式的标签（如 ``<think>…``）。  
此函数会移除这些内容，确保你的 TTS **只** 朗读最终答案。

**提示：** 如果你在屏幕上看到其它“流式”杂质（因为你直接打印了原始 token），这个函数已经确保 **语音** 输出保持干净。



**主循环：先问候一次，然后 监听 → 思考 → 说话**

.. code-block:: python

   print(WELCOME)
   tts.say(WELCOME)

通过终端与扬声器向用户问好。程序启动时执行一次。



**监听（带实时部分转写的流式 STT）**

.. code-block:: python

   print("\n🎤 Listening... (Press Ctrl+C to stop)")

   text = ""
   for result in stt.listen(stream=True):
       if result["done"]:
           text = result["final"].strip()
           print(f"[YOU] {text}")
       else:
           print(f"[YOU] {result['partial']}", end="\r", flush=True)

* ``stream=True`` 会生成 **部分** 转写，便于即时反馈，并在话语结束时给出 **最终** 转写。  
* 最终识别文本存入 ``text``，并打印一次。



**保护：若未识别到任何内容，则跳过 LLM 调用**

.. code-block:: python

   if not text:
       print("[INFO] Nothing recognized. Try again.")
       time.sleep(0.1)
       continue

避免向模型发送空提示（节省时间与算力 / 令牌）。



**思考（LLM）并流式打印**

.. code-block:: python

   reply_accum = ""
   response = llm.prompt(text, stream=True)
   for next_word in response:
       if next_word:
           print(next_word, end="", flush=True)
           reply_accum += next_word
   print("")

* 将最终转写发送给本地 LLM，并 **随到随打** token，从而降低延迟。  
* 同时将完整回复累积到 ``reply_accum``，用于后续处理。

**注意：** 如果你 **不想** 展示原始 token，可将 ``stream=False``，只打印最终字符串。



**说话（先清理，再一次性 TTS）**

.. code-block:: python

   clean = strip_thinking(reply_accum)
   if clean:
       tts.say(clean)
   else:
       tts.say("Sorry, I didn't catch that.")

* 清理最终文本，移除隐藏标签，然后 **只朗读一次**。  
* 让 TTS 保持一次性播报，避免出现诸如 “[LLM] / [SAY]” 之类的重复提示。



**退出与清理**

.. code-block:: python

   except KeyboardInterrupt:
       print("\n[INFO] Stopping...")
   finally:
       tts.say("Goodbye!")
       print("Bye.")

使用 ``Ctrl+C`` 结束程序。机器人会简短道别，以提示正常退出。

----

故障排查与常见问题
---------------------

* **模型过大（内存错误）**

  使用较小的模型，如 ``moondream:1.8b``，或在性能更强的计算机上运行 Ollama。

* **Ollama 没有响应**

  确保 Ollama 已在运行（``ollama serve`` 或桌面应用已打开）。  
  如果是远程设备，启用 **Expose to network** 并检查 IP 地址是否正确。

* **Vosk 无法识别语音**

  确认麦克风工作正常。  
  如有需要，可尝试更换语言包（``zh-cn``、``es`` 等）。

* **Piper 没有声音或报错**

  确认所选语音模型已下载，并已在 :ref:`test_piper` 中测试通过。

* **回答太长或偏题**

  编辑 ``INSTRUCTIONS``，添加：**“Keep answers short and to the point.”**。

