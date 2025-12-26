.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

19. ローカル音声チャットボット
==============================

このレッスンでは、これまでに学んだ **音声認識（STT）**、  
**テキスト読み上げ（TTS）**、そして **ローカルLLM（Ollama）** を組み合わせ、  
PiCar-X 上で完全オフラインで動作する **音声チャットボット** を作成します。

ワークフローはシンプルです：

#. **Listen（聞く）**  — マイクがあなたの音声を取り込み、**Vosk** で書き起こします。  
#. **Think（考える）**  — テキストを Ollama 上で動作するローカル **LLM** （例： ``llama3.2:3b`` ）に送ります。  
#. **Speak（話す）**  — **Piper TTS** を使ってチャットボットが音声で返答します。  

これにより、リアルタイムで理解して応答できる **ハンズフリー会話ロボット** が完成します。

----

始める前に
----------------

以下を準備しておいてください：

* :ref:`install_all_modules` — ``robot-hat``、 ``vilib``、 ``picar-x`` モジュールをインストールし、その後スクリプト ``i2samp.sh`` を実行します。
* **Piper TTS** （:ref:`test_piper`）をテストし、動作する音声モデルを選定。  
* **Vosk STT** （:ref:`test_vosk`）をテストし、適切な言語パック（例： ``en-us``）を選定。  
* **Ollama** （:ref:`download_ollama`）を Pi または別のコンピュータにインストールし、 ``llama3.2:3b``  のようなモデルをダウンロード（メモリに制約がある場合は ``moondream:1.8b`` などの小型モデル）。

----

コードの実行
--------------

#. 例のスクリプトを開きます：

   .. code-block:: bash

      cd ~/picar-x/example
      sudo nano 19.local_voice_chatbot.py

#. 必要に応じてパラメータを更新します：

   * ``stt = Vosk(language="en-us")`` ：アクセント／言語パックに合わせて変更（例： ``en-us`` 、 ``zh-cn`` 、 ``es``）。  
   * ``tts.set_model("en_US-amy-low")`` ：:ref:`test_piper` で確認した Piper の音声モデルに置き換え。  
   * ``llm = Ollama(ip="localhost", model="llama3.2:3b")`` ：自身の環境に合わせて ``ip`` と ``model`` を更新。  

     * ``ip`` ：Ollama が **同じ Pi** で動作している場合は ``localhost`` を使用。LAN 内の別マシンで動作させる場合は、Ollama で **Expose to network** を有効にし、そのマシンの LAN IP を ``ip`` に設定。  
     * ``model`` ：Ollama でダウンロード／有効化したモデル名と **完全一致** させること。  

#. スクリプトを実行します：

   .. code-block:: bash

      cd ~/picar-x/example
      sudo python3 19.local_voice_chatbot.py

#. 実行後は、次のような挙動になります：

   * ボットが音声でウェルカムメッセージを話します。  
   * 音声入力を待機します。  
   * Vosk があなたの音声をテキストに書き起こします。  
   * そのテキストが Ollama に送られ、ストリーミングで返信が返ってきます。  
   * 返信は（非表示の推論などを除去して）整形され、Piper により音声で再生されます。  
   * ``Ctrl+C`` でいつでもプログラムを停止できます。

----

コード
---------


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

コード分析
-------------

**インポートとグローバル設定**

.. code-block:: python

   import re
   import time
   from picarx.llm import Ollama
   from picarx.stt import Vosk
   from picarx.tts import Piper

先に作成した3つのサブシステムを取り込みます：   
**Vosk** （音声→テキストの STT）、 **Ollama** （LLM）、 **Piper** （テキスト→音声の TTS）。



**STT（Vosk）の初期化**

.. code-block:: python

   stt = Vosk(language="en-us")

米国英語の Vosk モデルを読み込みます。  
精度を上げるには、言語コード（例： ``zh-cn`` 、 ``es`` ）を使用中の言語パックに合わせて変更してください。



**TTS（Piper）の初期化**

.. code-block:: python

   tts = Piper()
   tts.set_model("en_US-amy-low")

Piper エンジンを作成し、特定の音声モデルを選択します。  
:ref:`test_piper` で確認済みのモデルを選びましょう。低品質の音声ほど高速・低CPUです。



**LLM向けプロンプトとウェルカム文**

.. code-block:: python

   INSTRUCTIONS = (
       "You are a helpful assistant. Answer directly in plain English. "
       "Do NOT include any hidden thinking, analysis, or tags like <think>."
   )
   WELCOME = "Hello! I'm your voice chatbot. Speak when you're ready."

UX上の重要ポイント：

* **簡潔で直接的な回答** を促し、TTSの聞き取りやすさを向上。  
* 隠れた「思考の連鎖」タグを明示的に禁止し、ノイズの少ない出力に。



**Ollama への接続と会話スコープの設定**

.. code-block:: python

   llm = Ollama(ip="localhost", model="llama3.2:3b")
   llm.set_max_messages(20)
   llm.set_instructions(INSTRUCTIONS)

* ``ip="localhost"`` は Ollama サーバーが同一の Pi 上で動作している前提です。LAN 上の別マシンで動かす場合は、その **LAN IP** を設定し、Ollama 側で *Expose to network* を有効化してください。  
* ``set_max_messages(20)`` は短めの会話履歴を保持します。メモリやレイテンシが厳しければさらに下げます。



**発話前に隠れた推論／タグを除去**

.. code-block:: python

   def strip_thinking(text: str) -> str:
       if not text:
           return ""
       text = re.sub(r"<\s*think[^>]*>.*?<\s*/\s*think\s*>", "", text, flags=re.DOTALL|re.IGNORECASE)
       text = re.sub(r"<\s*thinking[^>]*>.*?<\s*/\s*thinking\s*>", "", text, flags=re.DOTALL|re.IGNORECASE)
       text = re.sub(r"```(?:\s*thinking)?\s*.*?```", "", text, flags=re.DOTALL|re.IGNORECASE)
       text = re.sub(r"\[/?thinking\]", "", text, flags=re.IGNORECASE)
       return re.sub(r"\s+\n", "\n", text).strip()

一部のモデルは内部用のタグ（例： ``<think>…`` ）を出力することがあります。  
この関数でそれらを除去し、TTS が **最終回答のみ** を読み上げるようにします。

**ヒント： ** 生トークンをストリーミング表示していて画面にアーティファクトが出ても、  
この関数により **読み上げ** はクリーンに保たれます。



**メインループ：一度挨拶 → 聞く → 考える → 話す**

.. code-block:: python

   print(WELCOME)
   tts.say(WELCOME)

起動時にターミナルとスピーカーで一度だけ挨拶します。

**Listen（ストリーミングSTT：逐次部分結果）**

.. code-block:: python

   print("\n🎤 Listening... (Press Ctrl+C to stop)")

   text = ""
   for result in stt.listen(stream=True):
       if result["done"]:
           text = result["final"].strip()
           print(f"[YOU] {text}")
       else:
           print(f"[YOU] {result['partial']}", end="\r", flush=True)

* ``stream=True`` により、発話中は **部分（partial）** の字幕を即時表示し、発話終了時に **最終（final）** の文字起こしを受け取れます。  
* 最終認識テキストは ``text`` に格納され、1回だけ出力されます。

**ガード：** 何も認識されなかった場合、LLM 呼び出しをスキップします：

.. code-block:: python

   if not text:
       print("[INFO] Nothing recognized. Try again.")
       time.sleep(0.1)
       continue

空のプロンプトをモデルに送らないことで（時間・トークンの節約）無駄を防ぎます。

**Think（LLM）：ストリーム表示で低遅延**

.. code-block:: python

   reply_accum = ""
   response = llm.prompt(text, stream=True)
   for next_word in response:
       if next_word:
           print(next_word, end="", flush=True)
           reply_accum += next_word
   print("")

* 最終文字起こしをローカル LLM に送信し、**到着したトークンを逐次表示** して低遅延化します。  
* 同時に、全文を ``reply_accum`` に蓄積して後処理に使います。

**注意：** 生トークンを表示したくない場合は ``stream=False`` に設定し、最終文字列だけを出力します。

**Speak（整形してから一度だけTTS）**

.. code-block:: python

   clean = strip_thinking(reply_accum)
   if clean:
       tts.say(clean)
   else:
       tts.say("Sorry, I didn't catch that.")

* 隠れたタグを除去してから **一度だけ** 読み上げます。  
* TTS を1回に統一すると、「[LLM] / [SAY]」のような繰り返しプロンプトを避けられます。

**終了と後処理**

.. code-block:: python

   except KeyboardInterrupt:
       print("\n[INFO] Stopping...")
   finally:
       tts.say("Goodbye!")
       print("Bye.")

**Ctrl+C** で停止します。短い別れの挨拶を発話して、クリーン終了を示します。


----

トラブルシューティング & FAQ
---------------------------------

* **モデルが大きすぎる（メモリエラー）**

  ``moondream:1.8b`` のようなより小さいモデルを使うか、より高性能なコンピュータ上で Ollama を実行してください。  

* **Ollama から応答がない**

  Ollama が起動しているか確認（ ``ollama serve`` またはデスクトップアプリを開く）。リモート運用の場合は **Expose to network** を有効化し、IP アドレスを確認してください。  

* **Vosk が音声を認識しない**

  マイクが正常に動作しているか確認。必要に応じて別の言語パック（ ``zh-cn`` 、 ``es`` など）を試してください。  

* **Piper が無音／エラーになる**

  選択した音声モデルがダウンロード済みで、:ref:`test_piper` でテスト済みであることを確認してください。  

* **回答が長すぎる／話が逸れる**

  ``INSTRUCTIONS`` を編集して、 **"Keep answers short and to the point."** を追加してください。  



