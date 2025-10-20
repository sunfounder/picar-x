.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

15. Piper と OpenAI を使った AI ストーリーテリングロボット
==========================================================

前回のレッスンでは、Raspberry Pi 上の2つの組み込み TTS エンジン（ **Espeak** と **Pico2Wave** ）を試しました。  
今回はさらに強力な2つの選択肢 — **Piper** （オフライン）と **OpenAI TTS** （オンライン）を探ります。

* **Piper**：Raspberry Pi 上で動作するローカル TTS エンジン（オフライン対応）。  
* **OpenAI TTS**：自然で人間らしい声を提供するオンライン音声合成サービス。  

最終的に、PiCar-X が走りながらジョークを話す **小さなストーリーテラー** になります。

----

始める前に
----------------

以下を完了していることを確認してください：

* :ref:`install_all_modules` — ``robot-hat``、 ``vilib``、 ``picar-x`` モジュールをインストールし、その後スクリプト ``i2samp.sh`` を実行します。

----

.. _test_piper:

1. Piper のテスト
------------------

**手順**：

#. 新しいファイルを作成：

   .. code-block:: bash

      cd ~/picar-x/example
      sudo nano test_tts_piper.py

#. 以下のコードをファイルにコピーし、``Ctrl+X`` → ``Y`` → ``Enter`` で保存・終了。

   .. code-block:: python

       from picarx.tts import Piper

       tts = Piper()

       # サポートされている言語の一覧
       print(tts.available_countrys())

       # 英語（en_us）のモデル一覧
       print(tts.available_models('en_us'))

       # 音声モデルを設定（未インストールなら自動ダウンロード）
       tts.set_model("en_US-amy-low")

       # 音声を再生
       tts.say("Hello! I'm Piper TTS.")

   * ``available_countrys()``：サポートされている言語を表示。  
   * ``available_models()``：言語ごとの利用可能な音声モデルを表示。  
   * ``set_model()``：音声モデルを設定（未ダウンロードなら自動取得）。  
   * ``say()``：テキストを音声に変換し再生。

#. プログラムを実行：

   .. code-block:: bash

      sudo python3 test_tts_piper.py

#. 初回実行時、選択した音声モデルが自動でダウンロードされます。

   * PiCar-X が ``Hello! I'm Piper TTS.`` と話すはずです。  
   * 別の言語モデルを使用したい場合は、``set_model()`` に別のモデル名を指定してください。

2. OpenAI TTS のテスト
-------------------------------

**APIキーを取得して保存する**

#. |link_openai_platform| にアクセスしてログインします。 **API keys** ページで **Create new secret key** をクリック。

   .. image:: img/llm_openai_create.png

#. 情報（Owner、Name、Project、必要に応じて権限）を入力し、**Create secret key** をクリック。

   .. image:: img/llm_openai_create_confirm.png

#. キーが生成されたら、すぐにコピーしてください。一度閉じると再表示できません。紛失した場合は新しいキーを作成する必要があります。

   .. image:: img/llm_openai_copy.png

#. プロジェクトフォルダ（例： ``/picar-x/example``）で ``secret.py`` というファイルを作成します：

   .. code-block:: bash

       cd ~/picar-x/example
       sudo nano secret.py

#. 以下のようにキーを貼り付けます：

   .. code-block:: python

       # secret.py
       # Store secrets here. Never commit this file to Git.
       OPENAI_API_KEY = "sk-xxx"

**テストプログラムの作成と実行**

#. 新しいファイルを作成：

   .. code-block:: bash

       cd ~/picar-x/example
       sudo nano test_tts_openai.py

#. 以下のコードをコピーし、``Ctrl+X`` → ``Y`` → ``Enter`` で保存・終了します。

   .. code-block:: python

      from picarx.tts import OpenAI_TTS
      from secret import OPENAI_API_KEY   # または try/except バージョンを使用

      # OpenAI TTS を初期化
      tts = OpenAI_TTS(api_key=OPENAI_API_KEY)
      tts.set_model('gpt-4o-mini-tts')  # 低遅延TTSモデル
      tts.set_voice('alloy')            # 音声を選択

      # 簡単なテスト
      tts.say("Hello! I'm OpenAI TTS.")

#. プログラムを実行：

   .. code-block:: bash

       sudo python3 test_tts_openai.py

#. PiCar-X が次のように話すはずです：

   ``Hello! I'm OpenAI TTS.``

**利用可能なモデルと音声**

.. list-table::
   :header-rows: 1
   :widths: 20 80

   * - カテゴリ
     - オプション
   * - モデル
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
   * - 音声
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


3. ストーリーテリングロボット
--------------------------------

Piper と OpenAI TTS の両方をテストしたので、次はこれらを実際のプロジェクトで使ってみましょう。  
車を動かしながらジョークを話す **ストーリーテリングロボットカー** を作ります。

このプログラムでは PiCar-X が次の動作を行います：

* 起動時に TTS であいさつする。  
* 前進しながら最初のジョークを話す。  
* もう一度前進して2つ目のジョークを話す。  
* 最後に後退して“ホーム”に戻り、「さようなら」と話す。

まるで車輪のついた小さなロボットストーリーテラーです！

**コードを実行**

.. code-block:: bash

    cd ~/picar-x/example
    sudo python3 15.storytelling_robot.py

**コード**

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

トラブルシューティング
----------------------

* **No module named 'secret'**

  これは ``secret.py`` があなたの Python ファイルと同じフォルダにないことを意味します。  
  ``secret.py`` を、スクリプトを実行しているのと同じディレクトリへ移動してください。例：

  .. code-block:: bash

     ls ~/picar-x/example
     # secret.py と実行する .py ファイルの両方が見えることを確認

* **OpenAI: Invalid API key / 401**

  * キーを完全に貼り付けたか確認（ ``sk-`` で始まり、余分な空白や改行がないこと）。  
  * コードで正しくインポートしているか確認：

    .. code-block:: python

       from secret import OPENAI_API_KEY

  * Pi のネットワーク接続を確認（ ``ping api.openai.com`` を試す）。

* **OpenAI: Quota exceeded / billing error**

  * OpenAI ダッシュボードで課金設定の追加やクォータ増加が必要な場合があります。  
  * アカウント／課金の問題を解決してから再試行してください。

* **Piper: tts.say() は動くが音が出ない**

  * 音声モデルが実際に存在するか確認：

    .. code-block:: bash

       ls ~/.local/share/piper/voices

  * コード内のモデル名が完全一致しているか確認：

    .. code-block:: python

       tts.set_model("en_US-amy-low")

  * Pi のオーディオ出力デバイス／音量（ ``alsamixer`` ）や、スピーカーの接続・給電を確認。

* **ALSA / サウンドデバイスのエラー（例：「Audio device busy」や「No such file or directory」）**

  * 音声を使用中の他プログラムを終了。  
  * デバイスがビジーのままなら Pi を再起動。  
  * HDMI とヘッドフォン端子の切り替えなど、Raspberry Pi OS のオーディオ設定で正しい出力デバイスを選択。

* **Python 実行時に Permission denied**

  * 環境によっては ``sudo`` が必要な場合があります。次を試してください：

    .. code-block:: bash

       sudo python3 test_tts_piper.py


TTS エンジンの比較
-------------------------

.. list-table:: 機能比較: Espeak vs Pico2Wave vs Piper vs OpenAI TTS
   :header-rows: 1
   :widths: 18 18 20 22 22

   * - 項目
     - Espeak
     - Pico2Wave
     - Piper
     - OpenAI TTS
   * - 実行環境
     - Raspberry Pi（内蔵／オフライン）
     - Raspberry Pi（内蔵／オフライン）
     - Raspberry Pi / PC（オフライン、モデルが必要）
     - クラウド（オンライン、APIキーが必要）
   * - 音声品質
     - ロボット的
     - Espeak より自然
     - 自然（ニューラルTTS）
     - 非常に自然／人間に近い
   * - コントロール
     - 速度・ピッチ・音量
     - 制限あり
     - 複数の音声モデルを選択可能
     - モデルと音声の選択可能
   * - 言語
     - 多言語（品質はまちまち）
     - 限定的
     - 多数の音声／言語をサポート
     - 英語が最も高品質（他言語は提供状況による）
   * - レイテンシ／速度
     - 非常に高速
     - 高速
     - Pi 4/5 で「low」モデル使用時にリアルタイム
     - ネットワーク依存（通常は低遅延）
   * - セットアップ
     - 最小限
     - 最小限
     - ``.onnx`` + ``.onnx.json`` モデルのダウンロード
     - APIキー作成とクライアント導入
   * - 最適な用途
     - 簡単なテスト・基本プロンプト
     - 少し自然なオフライン音声
     - 高品質なローカルプロジェクト
     - 最高品質の音声・豊富な音声オプション
