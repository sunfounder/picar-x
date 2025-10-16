.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

.. _setup_pi:

4. Raspberry Pi のセットアップ
==================================

PiCar-X をプログラミングして制御するためには、まず Raspberry Pi にアクセスする必要があります。  
ここでは、モニター・キーボード・マウスを使用する方法と、ヘッドレス（画面なし）でリモートログインする方法の 2 つを紹介します。

画面がある場合
-------------------------

.. note:: ロボットに搭載されている Raspberry Pi Zero 2W は画面接続が難しいため、**ヘッドレス接続（画面なし）** を推奨します。

**必要なもの**

* Raspberry Pi
* 電源アダプター
* microSD カード
* HDMI ケーブル
* モニター
* マウス
* キーボード

#. microSD カードを Raspberry Pi に挿入します。  
#. マウス、キーボード、モニターを接続します（Pi 4/5 の場合は電源ポート側の **HDMI0** を使用）。  
#. Raspberry Pi の電源を入れます。  
#. 少し待つと Raspberry Pi OS のデスクトップが表示され、ターミナルを開いてコマンドを入力できます。

    .. image:: img/bookwarm.png
        :align: center


画面がない場合（ヘッドレス設定）
-----------------------------------------

モニターを使わなくても、Raspberry Pi をリモートで設定・ログインできます。  
これは最も便利な方法です。

**必要なもの**

* Raspberry Pi
* 電源アダプター
* microSD カード
* 同じネットワーク上のコンピュータ

**ヒント**

* Wi-Fi を利用するために **無線 LAN の国** を正しく設定してください（ISO/IEC alpha-2 コード、例：``US``、``UK``、``CN``）。  
* Raspberry Pi とコンピュータが同じローカルネットワーク上にあることを確認してください。  
* より安定した接続を得るために、可能であれば有線接続（Ethernet）を使用してください。  


**SSH 接続**

1. PC でターミナル（Windows は **PowerShell**、macOS/Linux は **Terminal**）を開き、次を入力します：

   .. code-block::

      ssh <ユーザー名>@<ホスト名>.local
      # 例:
      ssh daisy@picarx.local

#. あるいは、ルーターの DHCP／クライアントリストから Pi の IP を確認し、以下のように接続します：

   .. code-block::

      ssh <ユーザー名>@<IP>
      
      # 例:

      ssh daisy@192.xxx.xx.xx

#. 初回ログイン時にはセキュリティプロンプトが表示されます。「yes」と入力して進みます。

#. Raspberry Pi Imager で設定したパスワードを入力します（入力中に文字が表示されないのは正常です）。

   .. note::
      パスワード入力時に文字が表示されないのは標準的なセキュリティ仕様です。落ち着いて入力してください。

#. 接続が成功すると、Raspberry Pi のリモート操作が可能になります。

   .. image:: img/ssh_login.png
      :align: center

**トラブルシューティング**

* **ssh: Could not resolve hostname ...**  

  * ホスト名が正しいか確認してください。  
  * 解決しない場合は ``<hostname>.local`` ではなく IP アドレスで接続してください。

* **The term 'ssh' is not recognized...（Windows）**  

  * OpenSSH がインストールされていない可能性があります。手動で OpenSSH をインストールするか（:ref:`openssh_powershell` 参照）、  
    サードパーティの SSH クライアントを使用してください（:ref:`login_windows` 参照）。

* **Permission denied (publickey,password)**  

  * Raspberry Pi Imager で設定したユーザー名とパスワードを使用しているか確認してください。

* **Connection refused**  

  * 電源投入後 1〜2 分待ってから接続してください。  
  * Raspberry Pi Imager で SSH が有効になっているか確認してください。

**グラフィカルアクセスのオプション**

コマンドラインではなく GUI を使いたい場合は、次の 2 つの方法があります：

    .. image:: img/bookwarm.png
        :align: center

* :ref:`remote_desktop`: **VNC（Virtual Network Computing）** を有効にして、Pi 上でフルデスクトップ環境を利用する。  
* |link_rpi_connect|: **Raspberry Pi Connect** を使って、ブラウザ経由で安全なリモートアクセスを行う。

これで、モニターなしでも Raspberry Pi を操作できるようになります。  
コマンドライン操作は SSH で、GUI は VNC または Raspberry Pi Connect で利用できます。
