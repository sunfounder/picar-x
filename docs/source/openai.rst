AIとのインタラクション：GPT-4Oの活用
=====================================================
以前のプロジェクトでは、PiCar-Xをプログラミングしてあらかじめ決められたタスクを実行していましたが、これは少し退屈に感じることがあるかもしれません。このプロジェクトでは、ダイナミックなエンゲージメントに向けたスリリングな一歩を踏み出します。これまでよりもずっと多くを理解できるようになった車に、挑戦してみましょう！

このプロジェクトでは、システムにGPT-4Oを統合するためのすべての技術的なステップを詳細に説明します。これには、必要な仮想環境の設定、重要なライブラリのインストール、APIキーとアシスタントIDの設定が含まれます。

.. note::

   このプロジェクトでは、|link_openai_platform| の利用が必要で、OpenAIの利用料金がかかります。さらに、OpenAI APIはChatGPTとは別に請求され、その価格はhttps://openai.com/api/pricing/で確認できます。

   したがって、このプロジェクトを進めるか、OpenAI APIが資金供給されているかを確認する必要があります。

マイクを使って直接コミュニケーションを取る場合でも、コマンドウィンドウにテキストを入力するのが好みの場合でも、GPT-4Oを搭載したPiCar-Xの応答はきっと驚くべきものになるでしょう！

このプロジェクトに飛び込んで、PiCar-Xとの新しいレベルのインタラクションを解き放ちましょう！

1. 必要なパッケージと依存関係のインストール
--------------------------------------------------------------
.. note::

   最初にPiCar-Xの必要なモジュールをインストールする必要があります。詳細は :ref:`install_all_modules` を参照してください。
   
このセクションでは、仮想環境を作成してアクティブ化し、その中に必要なパッケージと依存関係をインストールします。これにより、インストールされたパッケージがシステム全体に影響を与えず、プロジェクトの依存関係の分離を維持し、他のプロジェクトやシステムパッケージとの競合を防ぎます。

#. ``python -m venv`` コマンドを使用して ``my_venv`` という名前の仮想環境を作成し、システムレベルのパッケージも含めます。 ``--system-site-packages`` オプションを使用すると、仮想環境がシステム全体にインストールされたパッケージにアクセスできるようになります。これは、システムレベルのライブラリが必要な場合に便利です。

   .. code-block:: shell

      python -m venv --system-site-packages my_venv

#. ``my_venv`` ディレクトリに移動し、``source bin/activate`` コマンドを使って仮想環境をアクティブ化します。コマンドプロンプトが変わり、仮想環境がアクティブであることを示します。

   .. code-block:: shell

      cd my_venv
      source bin/activate

#. 仮想環境がアクティブになった状態で、必要なPythonパッケージをインストールします。これらのパッケージは仮想環境内にのみインストールされ、他のシステムパッケージに影響を与えることはありません。

   .. code-block:: shell

      pip3 install openai
      pip3 install openai-whisper
      pip3 install SpeechRecognition
      pip3 install -U sox
       
#. 最後に、管理者権限が必要なシステムレベルの依存関係を ``apt`` コマンドを使用してインストールします。

   .. code-block:: shell

      sudo apt install python3-pyaudio
      sudo apt install sox


2. APIキーとアシスタントIDの取得
-----------------------------------------

**APIキーの取得**

#. |link_openai_platform| にアクセスし、右上の **Create new secret key** ボタンをクリックします。

   .. image:: img/apt_create_api_key.png
      :width: 700
      :align: center

#. オーナー、名前、プロジェクト、権限を必要に応じて選択し、 **Create secret key** をクリックします。

   .. image:: img/apt_create_api_key2.png
      :width: 700
      :align: center

#. 生成されたら、このシークレットキーを安全でアクセスしやすい場所に保存してください。セキュリティ上の理由から、このシークレットキーはOpenAIアカウントで再表示することはできません。シークレットキーを紛失した場合は、新しいものを生成する必要があります。

   .. image:: img/apt_create_api_key_copy.png
      :width: 700
      :align: center

**アシスタントIDの取得**

#. 次に、**Assistants** をクリックし、**Create** をクリックします。**Dashboard** ページ上にいることを確認してください。

   .. image:: img/apt_create_assistant.png
      :width: 700
      :align: center

#. カーソルをここに移動して、**assistant ID** をコピーし、テキストボックスまたは他の場所に貼り付けます。これは、このアシスタントのユニークな識別子です。

   .. image:: img/apt_create_assistant_id.png
      :width: 700
      :align: center

#. 任意の名前を設定し、以下の内容を **Instructions** ボックスにコピーして、アシスタントを説明します。

   .. image:: img/apt_create_assistant_instructions.png
      :width: 700
      :align: center

   .. code-block::

         You are a small car with AI capabilities named PaiCar-X. You can engage in conversations with people and react accordingly to different situations with actions or sounds. You are driven by two rear wheels, with two front wheels that can turn left and right, and equipped with a camera mounted on a 2-axis gimbal.

         ## Response with Json Format, eg:
         {"actions": ["start engine", "honking", "wave hands"], "answer": "Hello, I am PaiCar-X, your good friend."}

         ## Response Style
         Tone: Cheerful, optimistic, humorous, childlike
         Preferred Style: Enjoys incorporating jokes, metaphors, and playful banter; prefers responding from a robotic perspective
         Answer Elaboration: Moderately detailed

         ## Actions you can do:
         ["shake head", "nod", "wave hands", "resist", "act cute", "rub hands", "think", "twist body", "celebrate, "depressed"]
         ## Sound effects:
         ["honking", "start engine"]


#. PiCar-Xはカメラモジュールを搭載しており、これを有効にして、見たものの画像を撮影し、例コードを使用してGPTにアップロードすることができます。そのため、画像解析機能を備えたGPT-4Oを選択することをお勧めします。もちろん、gpt-3.5-turboや他のモデルを選ぶこともできます。

   .. image:: img/apt_create_assistant_model.png
      :width: 700
      :align: center

#. 次に、**Playground** をクリックして、アカウントが正常に機能しているか確認します。

   .. image:: img/apt_playground.png

#. メッセージやアップロードした画像が正常に送信され、返信が届く場合は、アカウントが使用制限に達していないことを意味します。

   .. image:: img/apt_playground_40.png
      :width: 700
      :align: center

#. 情報を入力した後にエラーメッセージが表示される場合、使用制限に達している可能性があります。使用ダッシュボードまたは請求設定を確認してください。

   .. image:: img/apt_playground_40mini_3.5.png
      :width: 700
      :align: center

3. APIキーとアシスタントIDの入力
--------------------------------------------------

#. ``keys.py`` ファイルを開くために、次のコマンドを使用します。

   .. code-block:: shell

      nano ~/picar-x/gpt_examples/keys.py

#. コピーしたAPIキーとアシスタントIDを入力します。

   .. code-block:: shell

      OPENAI_API_KEY = "sk-proj-vEBo7Ahxxxx-xxxxx-xxxx"
      OPENAI_ASSISTANT_ID = "asst_ulxxxxxxxxx"

#. ``Ctrl + X``, ``Y``, ``Enter`` を押して、ファイルを保存して終了します。

4. 実行例
----------------------------------
テキストコミュニケーション
^^^^^^^^^^^^^^^^^^^^^^^^^^

PiCar-Xにマイクがない場合は、キーボード入力を使用してPiCar-Xと対話することができます。以下のコマンドを実行します。

#. sudoを使って以下のコマンドを実行します。PiCar-Xのスピーカーはsudoなしでは機能しません。このプロセスは完了までに時間がかかります。

   .. code-block:: shell

      cd ~/picar-x/gpt_examples/
      sudo ~/my_venv/bin/python3 gpt_car.py --keyboard

#. コマンドが正常に実行されると、PiCar-Xのすべてのコンポーネントが準備完了であることを示す以下の出力が表示されます。

   .. code-block:: shell

      vilib 0.3.8 launching ...
      picamera2 0.3.19

      Web display on:
         http://rpi_ip:9000/mjpg

      Starting web streaming ...
      * Serving Flask app 'vilib.vilib'
      * Debug mode: off

      input:

#. PiCar-Xのカメラフィードをウェブブラウザで見るためのリンクも表示されます： ``http://rpi_ip:9000/mjpg``。

   .. image:: img/apt_ip_camera.png
      :width: 700
      :align: center

#. ターミナルウィンドウにコマンドを入力し、Enterキーを押して送信できます。PiCar-Xの応答があなたを驚かせるかもしれません。

   .. note::
      
      PiCar-Xは、入力を受け取り、それをGPTに送信し、応答を受け取り、それを音声合成で再生する必要があります。このプロセス全体に少し時間がかかるので、しばらくお待ちください。

   .. image:: img/apt_keyboard_input.png
      :width: 700
      :align: center

#. GPT-4Oモデルを使用している場合、PiCar-Xが見ているものに基づいて質問することもできます。

音声コミュニケーション
^^^^^^^^^^^^^^^^^^^^^^^^

PiCar-Xにマイクが搭載されている場合、または|link_microphone|をクリックして購入する場合、音声コマンドを使用してPiCar-Xと対話することができます。

#. まず、Raspberry Piがマイクを検出していることを確認します。

   .. code-block:: shell

      arecord -l

   成功すると、以下のような情報が表示され、マイクが検出されていることがわかります。

   .. code-block:: 
      
      **** List of CAPTURE Hardware Devices ****
      card 3: Device [USB PnP Sound Device], device 0: USB Audio [USB Audio]
      Subdevices: 1/1
      Subdevice #0: subdevice #0

#. 以下のコマンドを実行し、PiCar-Xに向かって話しかけるか、音を出してみてください。マイクがその音を ``op.wav`` ファイルに録音します。録音を停止するには、 ``Ctrl + C`` を押します。

   .. code-block:: shell

      rec op.wav

#. 最後に、録音された音声を再生して、マイクが正常に動作していることを確認するために、以下のコマンドを使用します。

   .. code-block:: shell

      sudo play op.wav

#. sudoを使って以下のコマンドを実行します。PiCar-Xのスピーカーはsudoなしでは機能しません。このプロセスは完了までに時間がかかります。

   .. code-block:: shell

      cd ~/picar-x/gpt_examples/
      sudo ~/my_venv/bin/python3 gpt_car.py

#. コマンドが正常に実行されると、PiCar-Xのすべてのコンポーネントが準備完了であることを示す以下の出力が表示されます。

   .. code-block:: shell
      
      vilib 0.3.8 launching ...
      picamera2 0.3.19

      Web display on:
         http://rpi_ip:9000/mjpg

      Starting web streaming ...
      * Serving Flask app 'vilib.vilib'
      * Debug mode: off

      listening ...

#. PiCar-Xのカメラフィードをウェブブラウザで見るためのリンクも表示されます： ``http://rpi_ip:9000/mjpg``。

   .. image:: img/apt_ip_camera.png
      :width: 700
      :align: center

#. PiCar-Xに向かって話しかけると、その応答があなたを驚かせるかもしれません。

   .. note::
      
      PiCar-Xは、音声をテキストに変換し、それをGPTに送信し、応答を受け取り、それを音声合成で再生する必要があります。このプロセス全体に少し時間がかかるので、しばらくお待ちください。

   .. image:: img/apt_speech_input.png
      :width: 700
      :align: center

#. GPT-4Oモデルを使用している場合、PiCar-Xが見ているものに基づいて質問することもできます。


5. パラメータの変更 [オプション]
-------------------------------------------

``gpt_car.py`` ファイルの以下の行を探します。これらのパラメータを変更して、STTの言語、TTSの音量ゲイン、および音声役割を設定できます。

* **STT (Speech to Text)** は、PiCar-Xのマイクが音声をキャプチャし、それをテキストに変換してGPTに送信するプロセスです。この変換の精度と遅延を向上させるために、特定の言語を指定することができます。

* **TTS (Text to Speech)** は、GPTのテキスト応答を音声に変換し、PiCar-Xのスピーカーを通じて再生するプロセスです。音量ゲインを調整し、TTS出力の音声役割を選択することができます。

.. code-block:: python

   # openai assistant init
   # =================================================================
   openai_helper = OpenAiHelper(OPENAI_API_KEY, OPENAI_ASSISTANT_ID, 'picrawler')

   # LANGUAGE = ['zh', 'en'] # config stt language code, https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes
   LANGUAGE = []

   VOLUME_DB = 3 # tts voloume gain, preferably less than 5db

   # select tts voice role, counld be "alloy, echo, fable, onyx, nova, and shimmer"
   # https://platform.openai.com/docs/guides/text-to-speech/supported-languages
   TTS_VOICE = 'nova'


* ``LANGUAGE`` 変数: 

  * Speech-to-Text (STT) の精度と応答時間を改善します。
  * ``LANGUAGE = []`` はすべての言語をサポートしますが、これによりSTTの精度が低下し、遅延が増加する可能性があります。
  * パフォーマンスを向上させるために、|link_iso_language_code| 言語コードを使用して、特定の言語を設定することをお勧めします。

* ``VOLUME_DB`` 変数:

  * Text-to-Speech (TTS) 出力のゲインを制御します。
  * 値を上げると音量が大きくなりますが、音の歪みを防ぐために5dB未満に設定するのがベストです。

* ``TTS_VOICE`` 変数:

  * Text-to-Speech (TTS) 出力の音声役割を選択します。
  * 使用可能なオプション: ``alloy, echo, fable, onyx, nova, shimmer``。
  * |link_voice_options| から異なる音声を試して、好みのトーンや対象者に適したものを見つけてください。利用可能な音声は、現在英語に最適化されています。
