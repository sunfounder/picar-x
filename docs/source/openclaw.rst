.. _picarx_skill:

.. start_using_picarx

22. OpenClawを使用してPiCar-Xを制御する
=============================================


**OpenClawとは？**

ChatGPTのアップグレード版と考えてください。従来のチャットボットは会話（テキスト生成）しかできませんが、OpenClawは行動できます。自然言語での指示を理解し、実際にコンピュータ上でコマンドの実行、ファイル管理、さまざまなツールの呼び出しなどの操作を行うことができます。

以下はいくつかの素晴らしい応用シナリオです：

* **個人オールラウンドアシスタント：** スケジュール管理、リマインダー設定、タスク追跡を手伝ってもらいましょう。チャットアプリ（Telegram、WhatsAppなど）で伝えるだけで、記憶して実行します。
* **自動化の「接着剤」：** さまざまなサービスをつなぐバインダーとして機能します。例えば、ウェブサイトの価格変動を監視し、値下げが検出されたら自動的にn8nワークフローを起動してメール通知を送信できます。
* **専任開発アシスタント：** サーバー管理、スクリプト実行、ログ確認を手伝ってもらえます。「システム負荷を確認して」と言うだけで、サーバーにSSH接続し、コマンドを実行して結果を返します。
* **ハードウェアの「遊び相手」：** これは非常に興味深いユースケースです。Raspberry Piに接続されたハードウェアをOpenClawに制御させることができます。例えば、ある開発者はロボットアーム付き掃除ロボットの制御に使用し、また別の例ではレーシングシミュレーターのデータを分析してLEDスクリーンに表示させました。Raspberry Piの公式チームは、結婚式のための自動フォトブースを会話だけで構築し、コードを一行も書かずに作り上げました！


.. important::

   Raspberry Pi Zero 2WのRAMは512MBのみですが、OpenClawは最低1GBが必要です。そのため正常に動作しません。Raspberry Pi 4/5以上を推奨します。

OpenClawクイックスタート
-------------------------------

OpenClawのパワーをできるだけ早く体験したい場合は、この方法を使用してください。インタラクティブなセットアップウィザードが自動的にインストールされ起動します。

1.  Raspberry Piでターミナルを開き、以下のコマンドを直接実行します。このコマンドは公式サイトからインストールスクリプトをダウンロードして実行します：

    .. code-block:: bash

       curl -fsSL https://openclaw.ai/install.sh | bash

    .. note:: 新しいバージョンは急速に更新されるため、インストール手順が若干異なる場合は正常です。

2.  スクリプトが自動的にOpenClawをダウンロードしてインストールします。

    .. image:: /img/openclaw/install_open_claw.png


3.  次に、OpenClawを信頼するかどうかを尋ねるセキュリティプロンプトが表示されます。安全で信頼できると確認したら、矢印キーで「Yes」に移動しEnterを押します。

    .. image:: /img/openclaw/security_open_claw.png


4.  Quick Startを選択し、Enterを押します。

    .. image:: /img/openclaw/quickstart_open_claw.png

5.  モデルを選択し、Enterを押します。ここではOpenAIを例として使用します。

    .. image:: /img/openclaw/model_provider_open_claw.png

6.  OpenAI API Keyを選択します。

    .. image:: /img/openclaw/api_key_open_claw.png

7.  今すぐAPIキーを貼り付けます。

    .. image:: /img/openclaw/paste_api_key_open_claw.png

8.  |link_openai_platform| にアクセスしてログインします。\ **API keys**\ ページで\ **Create new secret key**\ をクリックします。

    .. image:: /img/openclaw/llm_openai_create.png

9.  詳細（Owner、Name、Project、必要に応じて権限）を入力し、\ **Create secret key**\ をクリックします。

    .. image:: /img/openclaw/llm_openai_create_confirm.png

10. キーが作成されたらすぐにコピーしてください — 再度表示することはできません。紛失した場合は新しいキーを生成する必要があります。

    .. image:: /img/openclaw/llm_openai_copy.png

11. OpenClawの設定にキーを貼り付けます。

    .. image:: /img/openclaw/paste_api_key_enter_open_claw.png

12. 使用したいモデルを選択します。この例では\ **Keep current**\ を使用します。

    .. image:: /img/openclaw/model_config_open_claw.png

13. 次はチャンネル選択です。チャンネルとは、OpenClawが対応するTelegram、WhatsApp、Discordなどの通信サービスを指します。下矢印キーで「Skip for now」オプションを選択し、Enterを押します。

    .. image:: /img/openclaw/channel_open_claw.png

14. 次に、すぐにスキルを設定するよう促されます。「Yes」を選択してEnterを押します。

    .. image:: /img/openclaw/config_skill_open_claw.png

15. 必要なスキルをインストールします。以下の例では「Skip for now」オプションを選択し（スペースキーで選択）、Enterを押します。

    .. image:: /img/openclaw/install_skill_open_claw.png

16. 次はHooksです。「command-logger」と「session-memory」をチェックします。

    .. image:: /img/openclaw/hooks2_open_claw.png


17. インストールが完了しました。「Hatch in TUI」を選択してEnterを押すとOpenClawを起動できます。

   .. image:: /img/openclaw/hatch_open_claw.png


.. note::

   以下のコマンドを入力してOpenClawを起動できます：

    .. code-block:: bash

       openclaw tui

   ctrl+cを2回押すとTUIインターフェースを終了できます。

------------------------------------------------------------------------

OpenClawでPiCar-Xを操作する
----------------------------------------------

**PiCar-Xスキルとは？**

PiCar-XスキルはOpenClawの拡張機能で、SunFounder PiCar-Xロボットカーを自然言語で制御できます。Pythonスクリプトを書いたりサーボ角度を覚えたりする代わりに、「前進して」「前方を確認して」「左に曲がって」のようにPiCar-Xに何をさせたいかをOpenClawに伝えるだけで、適切なPythonコードが自動的に実行されます。

PiCar-Xスキルでできること：

* **走行：** ステアリングサーボ制御による前進、後退、左折、右折
* **カメラジンバル：** 2軸カメラジンバルによる左右パン、上下チルト
* **センサー：** 超音波距離、ライントラッキングと崖検出のためのグレースケールセンサーデータの読み取り
* **サウンド：** 車載スピーカーによる効果音と音楽の再生
* **カメラビジョン：** 写真撮影、顔検出、色追跡、QRコード認識、ジェスチャー認識、交通標識検出

----------------------------------------------------------------

前提条件
------------------------------

PiCar-XスキルをOpenClawで使用する前に、以下を確認してください：

1. **PiCar-X** が正しく組み立てられ、Raspberry Piに接続されていること
2. **OpenClaw** がインストールされ実行中であること
3. 以下のPythonライブラリがインストールされていること：

   - ``picarx``
   - ``robot_hat``
   - ``vilib``

以下のコマンドでインストールを確認できます：

.. code-block:: bash

   python3 -c "import picarx"

このコマンドがエラーなしで実行されれば、準備完了です。

----------------------------------------------------------------

PiCar-Xスキルのインストール
------------------------------

以下の手順でPiCar-XスキルをOpenClawにインストールします：

1. **PiCar-Xスキルファイルを** OpenClawのスキルディレクトリにコピーします：

   .. code-block:: bash

      cp -r ~/picar-x/picarx-control ~/.openclaw/workspace/skills/

2. **スキルファイルを確認して** インストールを検証します：

   .. code-block:: bash

      ls ~/.openclaw/workspace/skills/picarx-control/

   出力に ``SKILL.md``、``install.sh``、``scripts/``、``references/`` が表示されるはずです。

スキルの ``SKILL.md`` ファイルには、OpenClawが必要とするすべての指示（安全ルール、各機能のコードテンプレート、自然言語リクエストからPythonコードへのマッピング）が含まれています。OpenClawはこのファイルを読み取り、PiCar-Xで実行するコードを決定します。

----------------------------------------------------------------

CLIからPiCar-Xスキルをテストする
----------------------------------------------

OpenClawでスキルを使用する前に、付属のCLIツールを使ってターミナルから直接基本機能をテストできます。

**超音波距離を確認：**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/picarx-control/scripts/pc.py sensor distance

**前進：**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/picarx-control/scripts/pc.py move forward --speed 60

**後退：**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/picarx-control/scripts/pc.py move backward --speed 60

**左折：**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/picarx-control/scripts/pc.py turn left --angle 30

**右折：**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/picarx-control/scripts/pc.py turn right --angle 30

**カメラのパン角度を設定：**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/picarx-control/scripts/pc.py cam pan --angle 30

**カメラのチルト角度を設定：**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/picarx-control/scripts/pc.py cam tilt --angle 20

**効果音を再生：**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/picarx-control/scripts/pc.py sound play /path/to/sound.wav --volume 80

**グレースケールセンサーデータを読み取り（ライントラッキング）：**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/picarx-control/scripts/pc.py sensor grayscale

**サーボキャリブレーションを実行：**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/picarx-control/scripts/pc.py calibrate

----------------------------------------------------------------

OpenClawでPiCar-Xスキルを使用する
----------------------------------------------------

PiCar-Xスキルがコマンドラインから動作することを確認したら、OpenClaw内で使用を開始できます。

1. **OpenClaw TUIを起動**：

   .. code-block:: bash

      openclaw tui

2. **自然言語コマンドを送信** してPiCar-Xを制御します。以下は例です：

   * 「前進して」
   * 「後退して」
   * 「左に曲がって」
   * 「右に曲がって」
   * 「前方に何かあるか確認して」
   * 「左を見て」
   * 「上を見て」
   * 「下を見て」
   * 「写真を撮って」
   * 「顔を検出して」
   * 「赤い色を探して」
   * 「ラインを追跡して」
   * 「前方に崖があるか確認して」

3. **OpenClawが自動的に** リクエストを適切なPythonコードに変換し、PiCar-Xで実行します。

----------------------------------------------------------------

利用可能なアクションとコマンド
-------------------------------------------

以下はPiCar-Xスキルがサポートする全機能のリストです：

走行（ ``pc.py move`` ）
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - アクション
     - 説明
   * - ``forward``
     - 前進
   * - ``backward``
     - 後退

ステアリング（ ``pc.py turn`` ）
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - アクション
     - 説明
   * - ``left``
     - ステアリング角度を調整して左折
   * - ``right``
     - ステアリング角度を調整して右折

カメラジンバル（ ``pc.py cam`` ）
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - 機能
     - 説明
   * - パン
     - カメラを水平に回転（-90° ～ 90°）
   * - チルト
     - カメラを垂直に傾ける（-35° ～ 65°）

センサー
^^^^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - コマンド
     - 説明
   * - ``sensor distance``
     - 超音波距離センサーを読み取り（cmを返す）
   * - ``sensor grayscale``
     - 3チャンネルグレースケールモジュール値を読み取り（ライントラッキングと崖検出用）

サウンド（ ``pc.py sound`` ）
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - コマンド
     - 説明
   * - ``sound play <ファイル>``
     - 効果音ファイルを再生
   * - ``sound music <ファイル>``
     - BGMを再生
   * - ``sound volume <0-100>``
     - スピーカー音量を設定
   * - ``sound stop``
     - 再生を停止

.. note::

   サウンドファイルはRaspberry Pi上でアクセス可能な ``.wav`` 形式のオーディオファイルであれば何でも使用できます。``sound music`` でBGMファイルを再生することもできます。

カメラとビジョン（自然言語 / exec経由）
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - 機能
     - 説明
   * - 写真撮影
     - 写真を撮影して ``~/Pictures/`` に保存
   * - 顔検出
     - 人の顔を検出して位置を報告
   * - 色検出
     - 色（赤、青、緑など）でオブジェクトを特定
   * - ジェスチャー認識
     - グー/チョキ/パーのジェスチャーを認識
   * - 交通標識検出
     - 停止/左折/右折/直進の標識を認識
   * - QRコードスキャン
     - QRコードのデータと位置を読み取り

ライントラッキングと崖検出
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - 機能
     - 説明
   * - ライントラッキング
     - 3チャンネルグレースケールを使用して明るい表面の黒い線を追跡
   * - 崖検出
     - グレースケール閾値を使用してエッジ/落差を検出

----------------------------------------------------------------

トラブルシューティング
------------------------------

OpenClawの問題
^^^^^^^^^^^^^^^^^^^^^^^^

Q. インストール中に ``Error: systemctl is-enabled unavailable: Command failed: systemctl --user is-enabled openclaw-gateway.service`` エラーが発生します。どうすればよいですか？

   今のところ無視して構いませんが、次のステップで問題が発生する可能性があります。その時点で一つずつ参照してください。


Q. ``openclaw tui`` を実行すると ``-bash: openclaw: command not found`` エラーが発生します。どうすればよいですか？

   以下のコマンドを実行してください：

   .. code-block:: bash

      echo 'export PATH="$HOME/.npm-global/bin:$PATH"' >> ~/.bashrc
      source ~/.bashrc

   これで ``openclaw tui`` でTUIインターフェースを起動できるはずです。



Q. ``openclaw tui`` で ``not connected to gateway — message not sent`` または ``gateway disconnected: closed`` が表示されます。

   これはOpenClaw Gatewayサービスが起動していないためです。別のターミナルを開いて以下のコマンドを実行し、OpenClaw Gatewayを起動します：

   .. code-block:: bash

      openclaw gateway

   その後 ``openclaw tui`` を再起動すれば、直接使用できます。


Q. OpenClaw Gatewayサービスをバックグラウンドで実行/起動時に自動起動するように設定したいのですが、どうすればよいですか？

   通常、OpenClaw Gatewayサービスは起動時に自動的に開始されるはずです。そうでない場合は、以下のコマンドで手動起動できます。

   1. ``~/.config/systemd/user`` ディレクトリを作成：

   .. code-block:: bash

      mkdir -p ~/.config/systemd/user


   2. ``openclaw-gateway.service`` ファイルを作成：

   .. code-block:: bash

      cat > ~/.config/systemd/user/openclaw-gateway.service << EOF
      [Unit]
      Description=OpenClaw Gateway
      After=network.target

      [Service]
      Type=simple
      ExecStart=$HOME/.npm-global/bin/openclaw gateway run
      Restart=on-failure
      RestartSec=10
      Environment="PATH=$HOME/.npm-global/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin"
      Environment="NODE_ENV=production"

      [Install]
      WantedBy=default.target
      EOF


   3. systemd設定を再読み込み：

   .. code-block:: bash

      systemctl --user daemon-reload

   4. サービスを起動：

   .. code-block:: bash

      systemctl --user start openclaw-gateway

   この時点で ``openclaw tui`` を再起動すれば、直接使用できます。

   5. 起動時に自動起動するように有効化：

   .. code-block:: bash

      systemctl --user enable openclaw-gateway


Q. OpenClawがシステムを操作できません。どうすればよいですか？

   新しくインストールしたOpenClawは、デフォルトではRaspberry Piシステムを操作する権限がない場合があります。チャットのみ可能です。手動で権限を設定する必要があります。

   1.  OpenClaw設定ファイルを開きます：

      .. code-block:: bash

         nano ~/.openclaw/openclaw.json

   2.  ``tools`` オプションを見つけ、``profile`` と ``exec`` を以下のように変更します。

      .. code-block:: json

        "tools": {
            "profile": "coding",
            "exec": {
                "secrity": "full"
            }
        },

   3.  保存して終了します。

   4.  以下のコマンドをターミナルに入力してOpenClaw Gatewayを再起動します：

      .. code-block:: bash

         openclaw gateway restart

   これでOpenClawに読み取り/書き込み権限が付与され、Raspberry Piシステムを操作できるようになります。

PiCar-Xの問題
^^^^^^^^^^^^^^^^^^^^^^^^


Q. PiCar-Xがコマンドに応答しません。どうすればよいですか？

   まず、PiCar-Xが正しく接続され電源が入っていることを確認します。次に基本機能をテストします：

   .. code-block:: bash

      python3 ~/.openclaw/workspace/skills/picarx-control/scripts/pc.py sensor distance

   これが失敗する場合は、必要なPythonライブラリがインストールされていることを確認します：

   .. code-block:: bash

      python3 -c "import picarx; import robot_hat; import vilib"

Q. ``import picarx`` テストが失敗します。

   これはPiCar-X Pythonライブラリが正しくインストールされていないことを意味します。PiCar-X公式インストールガイドを参照して必要なライブラリをインストールしてください。付属のインストールスクリプトを実行することもできます：

   .. code-block:: bash

      bash ~/.openclaw/workspace/skills/picarx-control/install.sh

Q. OpenClawがPiCar-Xスキルを認識しません。

   TUIで *「Please rsync my skills」* と言ってスキルの同期をOpenClawに促すか、OpenClaw Gatewayを再起動します：

   .. code-block:: bash

      openclaw gateway restart

Q. PiCar-Xの動きがぎこちない、またはステアリングがセンターからずれています。

   これは通常、サーボのキャリブレーション値が正しくないことが原因です。キャリブレーションスクリプトを実行してステアリングサーボとカメラジンバルを調整します：

   .. code-block:: bash

      python3 ~/.openclaw/workspace/skills/picarx-control/scripts/pc.py calibrate

   速度パラメータを調整したり（例： ``--speed 40`` でよりスムーズな動きに）、連続コマンド間に短い遅延を追加することもできます。

Q. グレースケールやライントラッキングが正常に動作しません。

   グレースケールモジュールがサーフェスに合わせて適切にキャリブレーションされていることを確認してください。設定を使用してライン基準値を設定できます。グレースケールキャリブレーション手順についてはPiCar-Xのメインドキュメントを参照してください。

----------------------------------------------------------------

.. end_using_picarx
