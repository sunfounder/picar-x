.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

14. Espeak と Pico2Wave を使った音声案内カー
=================================================

このレッスンでは、Raspberry Pi に標準搭載されている 2 つのテキスト読み上げ（TTS）エンジン  
**Espeak** と **Pico2Wave** を使って、PiCar-X に「話す力」を与えます。

これら 2 つのエンジンはいずれもオフラインで動作し、使い方が簡単ですが、音質はかなり異なります。

* **Espeak**：とても軽量で高速。ただし声はロボット的。スピード・ピッチ・音量などを細かく調整可能。  
* **Pico2Wave**：Espeak よりも滑らかで自然な声を生成。ただし設定項目は少なめ。

このレッスンでは、**音質の違い** と **機能の違い** を体験し、  
動く前に行動を音声で案内する「音声プロンプトカー」を作ります。

----

始める前に
----------------

以下を完了していることを確認してください：

* :ref:`install_all_modules` — ``robot-hat``、 ``vilib``、 ``picar-x`` モジュールをインストールし、その後スクリプト ``i2samp.sh`` を実行します。

----

1. Espeak のテスト
--------------------

Espeak は Raspberry Pi OS に標準で含まれる軽量な TTS エンジンです。  
声は少しロボット的ですが、音量・ピッチ・速度などを細かく調整できます。

**試してみる手順：**

* 新しいファイルを作成：

  .. code-block:: bash
  
      cd ~/picar-x/example
      sudo nano test_tts_espeak.py

* 次のコードを貼り付けて、``Ctrl+X`` → ``Y`` → ``Enter`` で保存します。

  .. code-block:: python
  
      from picarx.tts import Espeak

      tts = Espeak()
  
      # Quick hello (sanity check)
      tts.say("Hello! I'm Espeak TTS.")
  
      # Optional voice tuning
      # tts.set_amp(100)   # 0 to 200
      # tts.set_speed(150) # 80 to 260
      # tts.set_gap(5)     # 0 to 200
      # tts.set_pitch(50)  # 0 to 99

* 次のコマンドでプログラムを実行します：

  .. code-block:: bash

     sudo python3 test_tts_espeak.py

* PiCar-X が「Hello! I'm Espeak TTS.」と話すのが聞こえるはずです。  
* コード内の音声調整用の行をアンコメントして、 ``amp`` （音量）、 ``speed`` （速度）、 ``gap`` （単語間の間隔）、 ``pitch`` （ピッチ）の違いを試してみましょう。

----

2. Pico2Wave のテスト
---------------------

Pico2Wave は Espeak よりも自然で人間らしい音声を生成します。  
使い方はシンプルですが、調整できるのは言語のみで、ピッチや速度は変更できません。

**試してみる手順：**

* 次のコマンドで新しいファイルを作成します：

  .. code-block:: bash

      cd ~/picar-x/example
      sudo nano test_tts_pico2wave.py

* 以下のコードを貼り付け、``Ctrl+X`` → ``Y`` → ``Enter`` で保存します。

  .. code-block:: python
  
      from picarx.tts import Pico2Wave
  
      tts = Pico2Wave()
  
      tts.set_lang('en-US')  # en-US, en-GB, de-DE, es-ES, fr-FR, it-IT
  
      # クイックチェック（動作確認）
      tts.say("Hello! I'm Pico2Wave TTS.")

* 次のコマンドでプログラムを実行します：

  .. code-block:: bash

    sudo python3 test_tts_pico2wave.py

* PiCar-X が「Hello! I'm Pico2Wave TTS.」と話すのが聞こえるはずです。  
* 言語を ``es-ES`` （スペイン語）などに切り替えて、音声の違いを確認してみましょう。

----

3. 音声プロンプトカー
-----------------------

**Pico2Wave** または **Espeak** を PiCar-X の走行コードと組み合わせて、「音声プロンプトカー」を作りましょう。  
各アクションの前に、車がこれから行う動作を音声で案内します。

**コードを実行**

.. code-block:: bash

    cd ~/picar-x/example
    sudo python3 14.voice_promt_car.py
    
このコードを実行すると、PiCar-X が前進・後退・旋回を行い、そのたびにまず動作内容をアナウンスします。  
これにより、車はより安全でフレンドリー、そしてインタラクティブになります。

**コード**


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

トラブルシューティング
----------------------

* **Espeak や Pico2Wave を実行しても音が出ない**

  * スピーカー／ヘッドホンが接続され、ミュートになっていないか確認してください。  
  * ターミナルでクイックテストを実行：

    .. code-block:: bash

       espeak "Hello world"
       pico2wave -w test.wav "Hello world" && aplay test.wav

  これでも音が出ない場合は、問題は Python コードではなくオーディオ出力側にあります。

* **Espeak の声が速すぎる／ロボットっぽい**

  * コード内のパラメータを調整してみてください：

    .. code-block:: python

       tts.set_speed(120)   # 遅くする
       tts.set_pitch(60)    # ピッチを変える

* **コード実行時に Permission denied が出る**

  * ``sudo`` を付けて実行してみてください：

    .. code-block:: bash

       sudo python3 test_tts_espeak.py


比較: Espeak と Pico2Wave
-------------------------------------

.. list-table::
   :widths: 20 40 40
   :header-rows: 1

   * - 機能
     - Espeak
     - Pico2Wave
   * - 音質
     - ロボット的／合成的
     - より自然で人間らしい
   * - 言語
     - 既定は英語
     - 少なめだが主要言語をサポート
   * - 調整可能項目
     - あり（速度・ピッチ など）
     - なし（言語のみ）
   * - パフォーマンス
     - 非常に高速・軽量
     - やや遅く・やや重い

