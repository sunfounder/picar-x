.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

16. Vosk（オフライン）で音声操作カー
==============================================

Vosk は軽量な音声認識（STT）エンジンで、多くの言語をサポートし、Raspberry Pi 上で完全に **オフライン** で動作します。  
言語モデルを一度ダウンロードすれば、その後はインターネット接続なしで使用できます。

このレッスンでは以下を行います：

* Raspberry Pi でマイクをチェックする  
* Vosk をインストールし、言語モデルでテストする  
* 「forward」「backward」「left」「right」などの音声コマンドに反応する **音声操作 PiCar-X** を作成する

----

始める前に
----------------

以下を完了していることを確認してください：

* :ref:`install_all_modules` — ``robot-hat``、 ``vilib``、 ``picar-x`` モジュールをインストールし、その後スクリプト ``i2samp.sh`` を実行します。

----

1. マイクのチェック
--------------------------

音声認識を使う前に、USB マイクが正しく動作しているか確認しましょう。

#. 使用可能な録音デバイスをリスト表示：

   .. code-block:: bash

      arecord -l

   ``card 1: ... device 0`` のような行を探します。

#. 短いサンプルを録音します（``1,0`` は取得した番号に置き換えてください）：

   .. code-block:: bash

      arecord -D plughw:1,0 -f S16_LE -r 16000 -d 3 test.wav

   * 例：デバイスが ``card 2, device 0`` の場合：

   .. code-block:: bash

      arecord -D plughw:2,0 -f S16_LE -r 16000 -d 3 test.wav

#. 再生して録音を確認します：

   .. code-block:: bash

      aplay test.wav

#. 必要に応じてマイクの音量を調整します：

   .. code-block:: bash

      alsamixer

   * **F6** を押して USB マイクを選択  
   * **Mic** または **Capture** チャンネルを探す  
   * ミュートされていないことを確認（**[MM]** はミュート → ``M`` を押して **[OO]** にする）  
   * ↑ / ↓ キーで録音音量を調整

.. _test_vosk:

2. Vosk のテスト
--------------------------

**手順**：

#. 新しいファイルを作成：

   .. code-block:: bash

      cd ~/picar-x/example
      sudo nano test_stt_vosk.py

#. 次のコードを貼り付け、 ``Ctrl+X`` → ``Y`` → ``Enter`` で保存：

   .. code-block:: python

      from picarx.stt import Vosk

      vosk = Vosk(language="en-us")

      print(vosk.available_languages)

      while True:
          print("Say something")
          result = vosk.listen(stream=False)
          print(result)

#. 実行：

   .. code-block:: bash

      sudo python3 test_stt_vosk.py

#. 初回実行時、Vosk は選択した言語モデルを **自動的にダウンロード** します（デフォルトでは small モデル）。  
   その後、対応言語リストが表示され、以下のようになります：

   .. code-block:: text

        vosk-model-small-en-us-0.15.zip: 100%|███████████████████| 39.3M/39.3M [00:05<00:00, 7.85MB/s]
        ['ar', 'ar-tn', 'ca', 'cn', 'cs', 'de', 'en-gb', 'en-in', 'en-us', 'eo', 'es', 'fa', 'fr', 'gu', 'hi', 'it', 'ja', 'ko', 'kz', 'nl', 'pl', 'pt', 'ru', 'sv', 'te', 'tg', 'tr', 'ua', 'uz', 'vn']
        Say something

   これは次を意味します：

   * モデルファイル（``vosk-model-small-en-us-0.15``）がダウンロード完了  
   * 対応言語リストが出力された  
   * システムがリッスン中 — PiCar-X のマイクに向かって話すと認識テキストがターミナルに表示されます

   **ヒント**：

   * マイクは 15〜30 cm 離すと精度が上がります  
   * 自分の言語・アクセントに合ったモデルを選びましょう

**ストリーミングモード（オプション）**

話している途中の部分的な認識結果もリアルタイムで確認することができます。

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


3. 音声操作カー
-------------------------

いよいよ音声認識を PiCar-X に接続しましょう！

**ウェイクワード** （「ヘイ ロボット」）を使用し、  
車がアクティブ化されたあとだけ音声コマンドを受け付けるようにします。  
これにより CPU の負荷を減らし、不要な誤作動を防げます。

**コードの実行**

.. code-block:: bash

   cd ~/picar-x/example
   sudo python3 16.voice_controlled_car.py

このプログラムでは、車は次のように動作します：

* ウェイクワード **「hey robot」** を待機します。  
* その後、自然な文章で話しても、キーワード（**forward**、**backward**、**left**、**right**）が含まれていれば反応します。  

  例：

  * 「Can you move forward a little?」 → 車が前進します。  
  * 「Please turn left now.」 → 車が左に曲がります。  

* コマンド **「sleep」** で制御ループを停止し、待機モードに戻ります。

**コード**

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

トラブルシューティング
-----------------------

* **「arecord」で No such file or directory と出る場合**

  カード／デバイス番号が間違っている可能性があります。  
  次のコマンドを実行して：

  .. code-block:: bash

     arecord -l

  USB マイクに対応する番号を確認し、 ``1,0`` をその番号に置き換えてください。

* **録音ファイルに音が入っていない場合**

  ミキサーを開いてマイク音量を確認します：

  .. code-block:: bash

     alsamixer

  * **F6** を押して USB マイクを選択  
  * **Mic/Capture** がミュートされていないことを確認（**[OO]** であること。 **[MM]** はミュート）  
  * ↑キーで音量を上げる

* **Vosk が音声を認識しない場合**

  * 使用している **言語コード** がモデルに合っているか確認（例：英語なら ``en-us``、中国語なら ``zh-cn``）。  
  * マイクは 15〜30cm 離し、周囲の雑音を避ける。  
  * はっきり・ゆっくり話す。

* **ウェイクワード（「hey robot」）が反応しない場合**

  * 速すぎない自然なトーンで発話する。  
  * そもそもテキストとして認識されているかを確認。表示がなければマイクが動作していない可能性あり。

* **認識が遅い／反応にラグがある場合**

  * デフォルトでは **small モデル** （軽量モデル）が自動ダウンロードされます（高速だが精度は低め）。  
  * それでも遅い場合は、他のプログラムを終了して CPU を空けてください。
