.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

.. _what_do_we_need:

1. ほかに必要なものは？
===============================

PiCar-X を動かす前に、まず基本となるハードウェアを準備しましょう。  
これらのコンポーネントは PiCar-X の **脳・心臓・感覚器官** のようなものです。  
これらがなければ、車は正常に動作しません。

必要なコンポーネント
------------------------------

* **Raspberry Pi**

  Raspberry Pi は PiCar-X の **脳** として、計算・センシング・制御のすべてを担います。
  
  .. image:: img/need_pi.jpg

  * **対応モデル**：Raspberry Pi 5、4、3、Raspberry Pi Zero 2 W（推奨：Pi 5 または Pi 4）  
  * **最低スペック**：2GB RAM — 標準的な PiCar-X 機能（走行、センサー、カメラストリーミング）や  
    **OpenAI Whisper、TTS、LLM などのオンライン AI サービス** の利用が可能。  
  * **推奨スペック**：4GB 以上 — **Vosk 音声認識**、**Piper TTS**、軽量 LLM などを  
    カメラストリーミングや制御タスクと並行して動かしてもスムーズに動作します。  


* **電源アダプター**

  PiCar-X には **18650 バッテリーパック** と、充電回路を備えた **Robot HAT** ボードが付属しています。
  
  .. image:: img/need_power.png
    :width: 400

  * 充電には **5V 3A 電源** （公式の Raspberry Pi 15W USB-C アダプターなど）を推奨。  
  * **USB-C Power Delivery（PD）充電器** や **QC 2.0 急速充電器** も利用可能。  
  * フル充電（0% → 100%）にはおよそ **2 時間** かかります。  


* **Micro SD カード**

  Raspberry Pi にはハードディスクがなく、起動やファイル保存は **Micro SD カード** で行います。
  
  .. image:: img/need_sd.jpg
    :width: 200

  * 最低容量：16GB  
  * 推奨容量：32GB（より安定）  
  * ブランド：SanDisk や Samsung など信頼できるものを推奨（読み書きエラー防止のため）  


オプションコンポーネント
------------------------

以下は必須ではありませんが、学習やデバッグをより快適にするためにあると便利です：

* **モニター（HDMI またはテレビ）**

  初心者の方には HDMI 入力付きのディスプレイを強くおすすめします。  
  Raspberry Pi OS の初期設定や GUI プログラムの実行が簡単になります。

  .. image:: img/need_screen.png
    :width: 400

* **HDMI ケーブル（Standard / Mini / Micro）**

  Raspberry Pi のモデルによって HDMI 端子が異なります。事前にモデルを確認して適切なケーブルを準備してください。

  * **Raspberry Pi 4 / 5**：Micro HDMI  
  * **Raspberry Pi 3**：Standard HDMI  
  * **Raspberry Pi Zero 2W**：Mini HDMI

  .. image:: img/need_hdmi.png
    :width: 400

* **キーボード＆マウス**

  Raspberry Pi OS の初期設定にとても便利です。  
  設定後は SSH や VNC でリモートアクセスも可能ですが、初心者にはシンプルな USB またはワイヤレスのセットを推奨します。

  .. image:: img/need_keyboard_mouse.png
    :width: 500
 

**準備のヒント**

* **PiCar-X キット** を購入した場合、多くのアクセサリーは同梱されていますが、  
  Raspberry Pi 本体、Micro SD カード、電源アダプターは別途用意する必要があります。  
* 何を買えばいいかわからない場合は、もっとも安定して汎用的な構成として  
  👉 **Raspberry Pi 4（2GB）+ 公式電源 + 32GB Micro SD カード** をおすすめします。
