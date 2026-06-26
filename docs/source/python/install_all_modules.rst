.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

.. _install_all_modules:


すべてのモジュールをインストールする（重要）
================================================

#. **システムの準備**

   Raspberry Pi がインターネットに接続されていることを確認し、システムを更新します。

   ::

      sudo apt update
      sudo apt upgrade

   .. note::
      Raspberry Pi OS Lite を使用している場合は、まず必要な Python 3 パッケージをインストールしてください。

      ::

         sudo apt install git python3-pip python3-setuptools python3-smbus

#. **robot-hat のインストール**

   ``robot-hat`` モジュールをダウンロードしてインストールします。

   ::

      cd ~/
      git clone -b 2.5.x https://github.com/sunfounder/robot-hat.git --depth 1
      cd robot-hat
      sudo python3 install.py

#. **vilib のインストール**

   ``vilib`` モジュールをダウンロードしてインストールします。

   ::

      cd ~/
      git clone https://github.com/sunfounder/vilib.git --depth 1
      cd vilib
      sudo python3 install.py

#. **picar-x のインストール**

   ``picar-x`` モジュールをダウンロードしてインストールします。

   ::

      cd ~/
      git clone -b 2.1.x https://github.com/sunfounder/picar-x.git --depth 1
      cd picar-x
      sudo pip3 install . --break

   この手順には少し時間がかかる場合があります。しばらくお待ちください。

#. **サウンドを有効にする（I2S アンプ）**

   音声出力を有効にするため、 ``i2samp.sh`` スクリプトを実行して、必要な I2S アンプ関連コンポーネントをインストールします。

   ::

      cd ~/robot-hat
      sudo bash i2samp.sh

   画面の指示に従い、 ``y`` を入力して Enter キーを押し、 ``/dev/zero`` をバックグラウンドで実行し、Picar-X を再起動してください。

   .. note::
      再起動後に音が出ない場合は、 ``i2samp.sh`` スクリプトを数回実行してみてください。
