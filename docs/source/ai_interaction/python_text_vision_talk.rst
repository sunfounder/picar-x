.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

17. Ollama を使った Text Vision Talk
==============================================

このレッスンでは、大規模言語モデル（LLM）とビジョンモデルをローカルで動かすツール **Ollama** の使い方を学びます。  
Ollama のインストール、モデルのダウンロード、PiCar-X との接続方法を紹介します。

このセットアップにより、PiCar-X がカメラでスナップショットを撮り、  
モデルがそれを「見て、説明」することができるようになります。  
つまり、画像について自由に質問すると、モデルが自然な言葉で答えてくれるようになります。

.. _download_ollama:

1. Ollama（LLM）のインストールとモデルのダウンロード
------------------------------------------------------

**Ollama** は以下のどちらにでもインストールできます：

* Raspberry Pi（ローカル実行）  
* 同じローカルネットワーク内の別のコンピュータ（Mac / Windows / Linux）

**ハードウェア別の推奨モデル**

|link_ollama_hub| にある任意のモデルを選べます。  
モデルには 3B、7B、13B、70B… などさまざまなサイズがあります。  
小さいモデルは軽くて速い一方、大きなモデルは高品質ですが高性能なハードウェアが必要です。

以下の表を参考に、デバイスに合ったモデルサイズを選びましょう。

.. list-table::
   :header-rows: 1
   :widths: 20 20 40

   * - モデルサイズ
     - 最小RAM要件
     - 推奨ハードウェア
   * - 約3Bパラメータ
     - 8GB（16GB推奨）
     - Raspberry Pi 5（16GB）または中性能PC/Mac
   * - 約7Bパラメータ
     - 16GB以上
     - Pi 5（16GB、ぎりぎり動作）または中性能PC/Mac
   * - 約13Bパラメータ
     - 32GB以上
     - RAMを多く積んだデスクトップPC/Mac
   * - 30B以上
     - 64GB以上
     - ワークステーション／サーバー／GPU推奨
   * - 70B以上
     - 128GB以上
     - 複数GPU搭載の高性能サーバー

**Raspberry Pi にインストールする場合**

Raspberry Pi に Ollama を直接インストールして実行する場合：

* **64bit版 Raspberry Pi OS** を使用  
* 強く推奨： **Raspberry Pi 5（16GB RAM）**

以下のコマンドを実行します：

.. code-block:: bash

   # Ollama をインストール
   curl -fsSL https://ollama.com/install.sh | sh

   # 軽量モデルを取得（テストに最適）
   ollama pull llama3.2:3b

   # 簡単な実行テスト（'hi' と入力して Enter）
   ollama run llama3.2:3b

   # API を起動（デフォルトポート11434）
   # LANアクセスを許可する場合は以下のように設定
   OLLAMA_HOST=0.0.0.0 ollama serve

**Mac / Windows / Linux（デスクトップ）にインストール**

1. |link_ollama| から Ollama をダウンロードしてインストール。

   .. image:: img/llm_ollama_download.png

2. Ollama アプリを開き、**Model Selector** でモデルを検索。  
   例えば、軽量な ``llama3.2:3b`` を入力して選択。

   .. image:: img/llm_ollama_choose.png

3. ダウンロード完了後、チャットウィンドウで「Hi」と入力すると、自動的にモデルが起動します。

   .. image:: img/llm_olama_llama_download.png

4. **Settings** → **Expose Ollama to the network** を有効化します。  
   これで Raspberry Pi から LAN 経由で接続可能になります。

   .. image:: img/llm_olama_windows_enable.png

.. warning::

   以下のようなエラーが出た場合：

   ``Error: model requires more system memory ...``

   → モデルが大きすぎてマシンのメモリが不足しています。  
   **小さいモデルを使用** するか、メモリの多いコンピュータに切り替えてください。

2. Ollama のテスト
------------------

Ollama のインストールとモデルの準備が完了したら、最小限のチャットループで簡単にテストできます。

**手順**

#. 新しいファイルを作成：

   .. code-block:: bash

      cd ~/picar-x/example
      nano test_llm_ollama.py

#. 以下のコードを貼り付けて保存（``Ctrl+X`` → ``Y`` → ``Enter``）：

   .. code-block:: python
 
      from picarx.llm import Ollama
 
      INSTRUCTIONS = "You are a helpful assistant."
      WELCOME = "Hello, I am a helpful assistant. How can I help you?"
 
      # If Ollama runs on the same Raspberry Pi, use "localhost".
      # If it runs on another computer in your LAN, replace with that computer's IP address.
      llm = Ollama(
          ip="localhost",
          model="llama3.2:3b"   # you can replace with any model
      )
 
      # Basic configuration
      llm.set_max_messages(20)
      llm.set_instructions(INSTRUCTIONS)
      llm.set_welcome(WELCOME)
 
      print(WELCOME)
 
      while True:
          text = input(">>> ")
          if text.strip().lower() in {"exit", "quit"}:
              break
 
          # Response with streaming output
          response = llm.prompt(text, stream=True)
          for token in response:
              if token:
                  print(token, end="", flush=True)
          print("")

#. プログラムを実行：

   .. code-block:: bash

      python3 test_llm_ollama.py

#. これで、PiCar-X とターミナルから直接チャットできます。

   * |link_ollama_hub| にある **任意のモデル** を選択可能ですが、RAM が 8〜16GB しかない場合は ``moondream:1.8b`` や ``phi3:mini`` などの小型モデルを推奨。  
   * コードに指定したモデル名と、Ollama で ``pull`` したモデル名が一致していることを確認。  
   * ``exit`` または ``quit`` と入力するとプログラムを終了します。  
   * 接続できない場合は、Ollama が起動しているか、リモート利用時は両方のデバイスが同一 LAN 上にあるかを確認してください。



3. Ollamaとのビジョン対話
--------------------------

このデモでは、 **質問を入力するたびに Pi カメラでスナップショットを撮影** します。  
プログラムはあなたの入力テキストと撮影した写真を、Ollama のローカルビジョンモデルに送信し、  
モデルが英語でストリーミング返信を返します。  
これは「見て、話す」シンプルなベースラインで、今後カラー／顔／QR認識などにも拡張可能です。

**事前準備**

#. **Ollama** アプリ（またはサービス）を起動し、 **ビジョン対応モデル** を pull しておく。

   * メモリが 16GB 以上ある場合 → ``llava:7b`` がおすすめ。
   * メモリが 8GB の場合 → ``moondream:1.8b`` や ``granite3.2-vision:2b`` のような軽量モデルを推奨。

   .. image:: img/llm_ollama_image_model.png

**デモの実行**

#. サンプルフォルダへ移動してスクリプトを実行：

   .. code-block:: bash

      cd ~/picar-x/example
      python3 17.text_vision_talk.py

#. 実行時の流れ：

   * プログラムがウェルカムメッセージを表示し、``>>>`` で入力待ち。
   * **何か入力するたびに** （例：「hello」「黄色はある？」「顔はある？」「机の上に何がある？」など）：

     * Pi カメラで写真を撮影（ ``/tmp/llm-img.jpg`` に保存）  
     * テキストと画像を Ollama 経由でビジョンモデルに送信  
     * モデルからの応答をストリーミングでターミナルに表示

   * ``exit`` または ``quit`` と入力すると終了します。

.. code-block:: python

   from picarx.llm import Ollama
   from picamera2 import Picamera2
   import time

   """
   You need to set up Ollama first.

   Note: At least 8GB RAM is recommended for small vision models (e.g., moondream:1.8b).
         For llava:7b, more memory is preferred (≥16GB).
   """

   INSTRUCTIONS = "You are a helpful assistant."
   WELCOME = "Hello, I am a helpful assistant. How can I help you?"

   # If Ollama runs on the same Pi, use "localhost".
   # If it runs on another computer in your LAN, replace with that computer's IP.
   llm = Ollama(
       ip="localhost",          # e.g., "192.168.100.145" if remote
       model="llava:7b"         # change to "moondream:1.8b" or "granite3.2-vision:2b" for 8GB RAM
   )

   # Basic configuration
   llm.set_max_messages(20)
   llm.set_instructions(INSTRUCTIONS)
   llm.set_welcome(WELCOME)

   # Init camera
   camera = Picamera2()
   config = camera.create_still_configuration(
       main={"size": (1280, 720)},
   )
   camera.configure(config)
   camera.start()
   time.sleep(2)

   print(WELCOME)

   while True:
       input_text = input(">>> ")
       if input_text.strip().lower() in {"exit", "quit"}:
           break

       # Capture image
       img_path = "/tmp/llm-img.jpg"
       camera.capture_file(img_path)

       # Response with stream (text + image)
       response = llm.prompt(input_text, stream=True, image_path=img_path)
       for next_word in response:
           if next_word:
               print(next_word, end="", flush=True)
       print("")

トラブルシューティング
-----------------------

* **「model requires more system memory ...」のようなエラーが出る**

  * モデルが大きすぎて、デバイスのメモリが不足しています。  
  * ``moondream:1.8b`` や ``granite3.2-vision:2b`` のような小型モデルを使用してください。  
  * または、RAM の多いマシンに切り替えて、Ollama をネットワーク越しに利用してください。

* **Ollama に接続できない（connection refused）**

  以下を確認してください：

  * Ollama が実行中であること（``ollama serve`` またはデスクトップアプリが開いている）。  
  * リモート利用の場合、Ollama の設定で **Expose to network** が有効になっている。  
  * コード内の ``ip="..."`` が正しい LAN IP アドレスになっている。  
  * 両方のデバイスが同じローカルネットワーク上にあることを確認する。

* **Pi カメラで何も撮影できない**

  * ``Picamera2`` がインストールされ、テストスクリプトで正常に動作するか確認する。  
  * カメラケーブルが正しく接続され、``raspi-config`` で有効化されていることを確認する。  
  * スクリプトが ``/tmp/llm-img.jpg`` への書き込み権限を持っているか確認する。

* **出力が遅い**

  * 小さいモデルを使うと応答速度は速くなるが、返答内容はシンプルになる傾向があります。  
  * カメラの解像度を下げる（例：1280×720 → 640×480）と画像処理が速くなります。  
  * Pi 上で他のプログラムを閉じて、CPU と RAM を解放してください。
