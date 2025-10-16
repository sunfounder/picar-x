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

5. すべてのモジュールをインストール（重要）
============================================

インターネットに接続されていることを確認し、システムを更新します：

.. raw:: html

    <run></run>

.. code-block::

    sudo apt update
    sudo apt upgrade

.. note::

    Lite 版 OS を使用している場合は、Python3 関連のパッケージをインストールする必要があります。

    .. raw:: html

        <run></run>

    .. code-block::

        sudo apt install git python3-pip python3-setuptools python3-smbus


``robot-hat`` をインストールします。

.. raw:: html

    <run></run>

.. code-block::

    cd ~/
    git clone -b 2.5.x https://github.com/sunfounder/robot-hat.git --depth 1
    cd robot-hat
    sudo python3 install.py


次に ``vilib`` モジュールをダウンロードしてインストールします。

.. raw:: html

    <run></run>

.. code-block::

    cd ~/
    git clone -b picamera2 https://github.com/sunfounder/vilib.git --depth 1
    cd vilib
    sudo python3 install.py

``picar-x`` モジュールをダウンロードしてインストールします。

.. raw:: html

    <run></run>

.. code-block::

    cd ~/
    git clone -b 2.1.x https://github.com/sunfounder/picar-x.git --depth 1
    cd picar-x
    sudo pip3 install . --break

このステップには少し時間がかかるので、しばらくお待ちください。

最後に、``i2samp.sh`` スクリプトを実行して i2s アンプに必要なコンポーネントをインストールします。  
これを行わないと、Picar-X から音が出ません。

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x
    sudo bash i2samp.sh

.. image:: img/i2s.png

``y`` を入力し、Enter を押してスクリプトを実行します。

.. image:: img/i2s2.png

``y`` を入力し、Enter を押して ``/dev/zero`` をバックグラウンドで実行します。

.. image:: img/i2s3.png

``y`` を入力し、Enter を押して Picar-X を再起動します。

.. note::
    再起動後に音が出ない場合は、i2samp.sh スクリプトを複数回実行する必要があるかもしれません。
