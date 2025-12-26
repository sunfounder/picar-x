.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

.. _py_online_llm:

18. オンラインLLMへの接続
================================

このレッスンでは、PiCar-X（または Raspberry Pi）をさまざまな **オンライン大規模言語モデル（LLM）** に接続する方法を学びます。  
各プロバイダーでは APIキー が必要で、利用可能なモデルも異なります。

以下の内容を解説します：

* APIキーを安全に作成・保存する方法  
* ニーズに合ったモデルの選び方  
* サンプルコードを実行してモデルとチャットする方法

各プロバイダーごとに、ステップごとに見ていきましょう。

----

始める前に
----------------

以下を完了していることを確認してください：

* :ref:`install_all_modules` — ``robot-hat``、 ``vilib``、 ``picar-x`` モジュールをインストールし、その後スクリプト ``i2samp.sh`` を実行します。

----

OpenAI
----------

OpenAI では、**GPT-4o** や **GPT-4.1** といったテキスト・ビジョン両対応の強力なモデルを提供しています。

以下が設定手順です：

**APIキーの取得と保存**

#. |link_openai_platform| にアクセスしてログインします。 **API keys** ページで **Create new secret key** をクリック。

   .. image:: img/llm_openai_create.png

#. 詳細（Owner、Name、Project、必要なら権限）を入力し、**Create secret key** をクリック。

   .. image:: img/llm_openai_create_confirm.png

#. キーが作成されたら、その場ですぐにコピーしてください。一度閉じると再表示できません。失くした場合は新しいキーを発行する必要があります。

   .. image:: img/llm_openai_copy.png

#. プロジェクトフォルダ（例： ``/picar-x/example``）内に ``secret.py`` というファイルを作成：

   .. code-block:: bash
   
       cd ~/picar-x/example
       sudo nano secret.py

#. 以下のようにキーをファイルへ貼り付けます：

   .. code-block:: python
   
       # secret.py
       # Store secrets here. Never commit this file to Git.
       OPENAI_API_KEY = "sk-xxx"

**課金の有効化とモデルの確認**

#. キーを使う前に、OpenAI アカウントの **Billing** ページで支払い情報を登録し、少額のクレジットを追加します。

   .. image:: img/llm_openai_billing.png

#. その後、**Limits** ページで利用可能なモデルを確認し、コードで使用する正確なモデルIDをコピーします。

   .. image:: img/llm_openai_models.png

**サンプルコードでテスト**

#. サンプルコードを開きます：

   .. code-block:: bash
   
       cd ~/picar-x/example
       sudo nano 18.online_llm_test.py

#. 以下のコードを貼り付け、 ``model="xxx"`` を希望するモデル（例： ``gpt-4o``）に変更します：

   .. code-block:: python
   
       from picarx.llm import OpenAI
       from secret import OPENAI_API_KEY
       
       INSTRUCTIONS = "You are a helpful assistant."
       WELCOME = "Hello, I am a helpful assistant. How can I help you?"
       
       llm = OpenAI(
           api_key=OPENAI_API_KEY,
           model="gpt-4o",
       )
  
   保存して終了します（``Ctrl+X`` → ``Y`` → ``Enter``）。

#. 最後にテストを実行：

   .. code-block:: bash
   
       sudo python3 18.online_llm_test.py

   

----

Gemini
------------------

Gemini は Google が提供する AI モデルファミリーです。高速で、汎用的なタスクに優れています。

**APIキーの取得と保存**

#. |link_google_ai| にログインし、API Keys ページへ移動します。

   .. image:: img/llm_gemini_get.png

#. 右上の **Create API key** ボタンをクリック。

   .. image:: img/llm_gemini_create.png

#. 既存のプロジェクトまたは新しいプロジェクトに対してキーを作成できます。

   .. image:: img/llm_gemini_choose.png

#. 生成された APIキー をコピーします。

   .. image:: img/llm_gemini_copy.png

#. プロジェクトフォルダ内で以下を実行：

   .. code-block:: bash

       cd ~/picar-x/example
       sudo nano secret.py

#. キーを貼り付けます：

   .. code-block:: python

        # secret.py
        # Store secrets here. Never commit this file to Git.
       GEMINI_API_KEY = "AIxxx"

**利用可能なモデルを確認**

公式 |link_gemini_model| ページにアクセスし、モデル一覧とその正確な API ID、各モデルの最適化用途を確認します。

   .. image:: img/llm_gemini_model.png

**サンプルコードでテスト**

#. テストファイルを開きます：

   .. code-block:: bash

       cd ~/picar-x/example
       sudo nano 18.online_llm_test.py

#. 以下のコードを貼り付け、 ``model="xxx"`` を希望のモデル（例： ``gemini-2.5-flash``）に変更します：

   .. code-block:: python

       from picarx.llm import Gemini
       from secret import GEMINI_API_KEY

       INSTRUCTIONS = "You are a helpful assistant."
       WELCOME = "Hello, I am a helpful assistant. How can I help you?"

       llm = Gemini(
           api_key=GEMINI_API_KEY,
           model="gemini-2.5-flash",
       )

#. 保存して実行します：

   .. code-block:: bash

       sudo python3 18.online_llm_test.py


----

Qwen
------------------

Qwen は Alibaba Cloud が提供する大規模言語モデルおよびマルチモーダルモデルのファミリーです。  
これらのモデルはテキスト生成・推論・マルチモーダル理解（画像解析など）をサポートしています。

**APIキーの取得**

Qwen モデルを利用するには **APIキー** が必要です。  
国際ユーザーは **DashScope International（Model Studio）** コンソールを使用します。  
中国本土ユーザーは **Bailian（百炼）** コンソールを使用します。

* **国際ユーザー向け**

  #. Alibaba Cloud の公式 |link_qwen_inter| ページにアクセス。  
  #. **Alibaba Cloud** アカウントでログインまたは新規作成。  
  #. **Model Studio** へ移動（リージョンはシンガポールまたは北京を選択）。  
    
      * ページ上部に「Activate Now（今すぐ有効化）」のプロンプトが表示されたらクリックして Model Studio を有効化し、無料枠を受け取ります（シンガポール限定）。  
      * 有効化は無料で、無料枠を超えるまでは課金されません。  
      * 有効化のプロンプトがない場合は、すでに利用可能な状態です。
  
  #. **Key Management** ページの **API Key** タブで **Create API Key** をクリック。  
  #. 作成後、APIキーをコピーして安全に保管します。
  
    .. image:: img/llm_qwen_api_key.png
        :width: 800
  
  .. note::
     香港・マカオ・台湾のユーザーも **International（Model Studio）** を選択してください。
  
* **中国本土ユーザー向け**

  中国本土の場合は **Alibaba Cloud Bailian（百炼）** コンソールを使用します：
  
  #. |link_aliyun| （百炼コンソール）にログインし、アカウント認証を完了します。  
  #. **Create API Key** を選択。モデルサービスが未有効化の場合は **Activate** をクリックし、利用規約に同意して無料枠を有効化します。その後、**Create API Key** ボタンが有効になります。  
  
     .. image:: img/llm_qwen_aliyun_create.png
  
  #. 再度 **Create API Key** をクリックし、アカウントを確認して **Confirm** をクリック。  
  
     .. image:: img/llm_qwen_aliyun_confirm.png
  
  #. 作成後、APIキーをコピーします。  
  
     .. image:: img/llm_qwen_aliyun_copy.png

**APIキーの保存**

#. プロジェクトフォルダで以下を実行：

   .. code-block:: bash

       cd ~/picar-x/example
       sudo nano secret.py

#. 以下のようにキーを貼り付けます：

   .. code-block:: python

        # secret.py
        # Store secrets here. Never commit this file to Git.
        
        QWEN_API_KEY = "sk-xxx"

**サンプルコードでテスト**

#. テストファイルを開きます：

   .. code-block:: bash

       cd ~/picar-x/example
       sudo nano 18.online_llm_test.py

#. 以下のコードに置き換え、 ``model="xxx"`` を希望するモデル（例： ``qwen-plus``）に変更します：

   .. code-block:: python
   
      from picarx.llm import Qwen
      from secret import QWEN_API_KEY

      INSTRUCTIONS = "You are a helpful assistant."
      WELCOME = "Hello, I am a helpful assistant. How can I help you?"

      llm = Qwen(
          api_key=QWEN_API_KEY,
          model="qwen-plus",
      )

#. 実行します：

   .. code-block:: bash
   
       sudo python3 18.online_llm_test.py

Grok (xAI)
------------------
Grok は Elon Musk 氏のチームが開発した xAI の対話型 AI です。xAI API を通じて接続できます。

**APIキーの取得と保存**

#. |link_grok_ai| でアカウントを作成します。まず少額のクレジットをチャージしてください — チャージしないと API は利用できません。

#. API Keys ページで **Create API key** をクリック。  

   .. image:: img/llm_grok_create.png

#. キー名を入力し、**Create API key** をクリック。 

   .. image:: img/llm_grok_name.png

#. 生成されたキーをコピーして安全に保管します。 

   .. image:: img/llm_grok_copy.png

#. プロジェクトフォルダで以下を実行：

   .. code-block:: bash

       cd ~/picar-x/example
       sudo nano secret.py

#. 以下のように貼り付けます：

   .. code-block:: python

        # secret.py
        # Store secrets here. Never commit this file to Git.
        
        GROK_API_KEY = "xai-xxx"

**利用可能なモデルの確認**

xAI コンソールの Models ページにアクセスし、利用可能なモデルと API ID を確認します。コードにはこの ID を使用します。

   .. image:: img/llm_grok_model.png

**サンプルコードでテスト**

#. テストファイルを開きます：

   .. code-block:: bash

       cd ~/picar-x/example
       sudo nano 18.online_llm_test.py

#. 以下のコードに置き換え、 ``model="xxx"`` を希望のモデル（例： ``grok-4-latest``）に変更します：

   .. code-block:: python
   
       from picarx.llm import Grok
       from secret import GROK_API_KEY
   
       INSTRUCTIONS = "You are a helpful assistant."
       WELCOME = "Hello, I am a helpful assistant. How can I help you?"
   
       llm = Grok(
           api_key=GROK_API_KEY,
           model="grok-4-latest",
       )

#. 実行：

   .. code-block:: bash
   
       sudo python3 18.online_llm_test.py
   

----

DeepSeek
------------------

DeepSeek は中国の LLM プロバイダーで、低価格で高性能なモデルを提供しています。

**APIキーの取得と保存**

#. |link_deepseek| にログインします。 

#. 右上メニューから **API Keys → Create API Key** を選択。 

   .. image:: img/llm_deepseek_create.png

#. 名前を入力し、**Create** をクリックしてキーをコピーします。

   .. image:: img/llm_deepseek_copy.png

#. プロジェクトフォルダで以下を実行：

   .. code-block:: bash

       cd ~/picar-x/example
       sudo nano secret.py

#. キーを追加します：

   .. code-block:: python

       # secret.py
       DEEPSEEK_API_KEY = "sk-xxx"

**課金の有効化**

まずアカウントに少額（例：¥10 RMB）をチャージする必要があります。

   .. image:: img/llm_deepseek_chognzhi.png

**利用可能なモデル**

2025-09-12 時点で DeepSeek が提供しているモデル：

* ``deepseek-chat``  
* ``deepseek-reasoner``  

**サンプルコードでテスト**

#. テストファイルを開きます：

   .. code-block:: bash

       cd ~/picar-x/example
       sudo nano 18.online_llm_test.py

#. 以下のコードに置き換え、 ``model="xxx"`` を希望のモデル（例： ``deepseek-chat``）に変更します：

   .. code-block:: python
   
       from picarx.llm import Deepseek
       from secret import DEEPSEEK_API_KEY
   
       INSTRUCTIONS = "You are a helpful assistant."
       WELCOME = "Hello, I am a helpful assistant. How can I help you?"
   
       llm = Deepseek(
           api_key=DEEPSEEK_API_KEY,
           model="deepseek-chat",
           max_messages=20,
       )

#. 実行：

   .. code-block:: bash
   
       sudo python3 18.online_llm_test.py


----

Doubao
------------------
Doubao は ByteDance（バイトダンス）が提供する AI モデルプラットフォーム（Volcengine Ark）です。

**APIキーの取得と保存**

#. |link_doubao| にログインします。

#. 左メニューをスクロールし、**API Key Management → Create API Key** をクリック。 

   .. image:: img/llm_doubao_create.png

#. 名前を入力し、**Create** をクリック。  

   .. image:: img/llm_doubao_name.png

#. **Show API Key** アイコンをクリックしてキーをコピーします。 

   .. image:: img/llm_doubao_copy.png

#. プロジェクトフォルダで以下を実行：

   .. code-block:: bash

       cd ~/picar-x/example
       sudo nano secret.py

#. キーを追加します：

   .. code-block:: python

       # secret.py
       DOUBAO_API_KEY = "xxx"

**モデルの選択**

#. モデルマーケットプレイスに移動してモデルを選択します。  

   .. image:: img/llm_doubao_model_select.png

#. 例として **Doubao-seed-1.6** を選択し、**API 接入** をクリック。 

   .. image:: img/llm_doubao_model.png

#. 使用する API Key を選択し、**Use API** をクリック。 

   .. image:: img/llm_doubao_use_api.png

#. **Enable Model** をクリック。 

   .. image:: img/llm_doubao_kaitong.png

#. モデル ID にカーソルを合わせてコピーします。 

   .. image:: img/llm_doubao_copy_id.png

**サンプルコードでテスト**

#. テストファイルを開きます：

   .. code-block:: bash

       cd ~/picar-x/example
       sudo nano 18.online_llm_test.py

#. 以下のコードに置き換え、 ``model="xxx"`` を希望のモデル（例： ``doubao-seed-1-6-250615``）に変更します：

   .. code-block:: python
   
       from picarx.llm import Doubao
       from secret import DOUBAO_API_KEY
   
       INSTRUCTIONS = "You are a helpful assistant."
       WELCOME = "Hello, I am a helpful assistant. How can I help you?"
   
       llm = Doubao(
           api_key=DOUBAO_API_KEY,
           model="doubao-seed-1-6-250615",
       )

#. 実行：

   .. code-block:: bash
   
       sudo python3 18.online_llm_test.py


General
--------------

このプロジェクトでは、複数の LLM プラットフォームに **統一インターフェース** で接続することができます。  
対応済みのプロバイダーは以下の通りです：

* **OpenAI** （ChatGPT / GPT-4o, GPT-4, GPT-3.5）  
* **Gemini** （Google AI Studio / Vertex AI）  
* **Grok** （xAI）  
* **DeepSeek**  
* **Qwen（通义千问）**  
* **Doubao（豆包）**

さらに、**OpenAI API 形式に互換性のある任意の LLM サービス** にも接続可能です。  
その場合は、自分で **API Key** と正しい **base_url** を取得する必要があります。

**APIキーの取得と保存**

#. 利用するプラットフォームのコンソールで **APIキー** を取得します。  

#. プロジェクトフォルダでファイルを作成：

   .. code-block:: bash

      cd ~/picar-x/example
      nano secret.py

#. 取得したキーを ``secret.py`` に追加：

   .. code-block:: python

      # secret.py
      API_KEY = "your_api_key_here"

.. warning::

   APIキーは絶対に公開しないでください。 ``secret.py`` を公開リポジトリにアップロードしないこと。

**サンプルコードでテスト**

#. テストファイルを開きます：

   .. code-block:: bash

      cd ~/picar-x/example
      sudo nano 18.online_llm_test.py

#. Python ファイルの内容を以下のコードに置き換え、 ``base_url`` および ``model`` を適切に設定します：

   .. note::

      ``base_url`` について：  
      OpenAI API 形式とその互換 API に対応しています。  
      各プロバイダーのドキュメントで ``base_url`` を確認してください。  

   .. code-block:: python

      from picarx.llm import LLM
      from secret import API_KEY

      INSTRUCTIONS = "You are a helpful assistant."
      WELCOME = "Hello, I am a helpful assistant. How can I help you?"

      llm = LLM(
          base_url="https://api.example.com/v1",  # プロバイダーの base_url を入力
          api_key=API_KEY,
          model="your-model-name-here",           # 使用するモデル名
      )

#. 実行：

   .. code-block:: bash

      python3 18.online_llm_test.py




