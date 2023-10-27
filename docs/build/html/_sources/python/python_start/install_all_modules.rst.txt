.. _install_all_modules:


全てのモジュールをインストールする（重要）
============================================

インターネットに接続されていることを確認しシステムの更新を行います。

.. raw:: html

    <run></run>

.. code-block::

    sudo apt update
    sudo apt upgrade

.. note::

    Raspberry pi OSのLite版OSをインストールしていた場合は別途Python3関連のパッケージをインストールする必要があります。

    .. raw:: html

        <run></run>

    .. code-block::
    
        sudo apt install git python3-pip python3-setuptools python3-smbus


``robot-hat`` をインストールします。

.. raw:: html

    <run></run>

.. code-block::

    cd ~/
    git clone -b v2.0 https://github.com/sunfounder/robot-hat.git
    cd robot-hat
    sudo python3 setup.py install

次に ``vilib`` モジュールをダウンロードしてインストールします。

.. raw:: html

    <run></run>

.. code-block::

    cd ~/
    git clone -b picamera2 https://github.com/sunfounder/vilib.git
    cd vilib
    sudo python3 install.py

``picar-x`` モジュールをダウンロードしてインストールします。

.. raw:: html

    <run></run>

.. code-block::

    cd ~/
    git clone -b v2.0 https://github.com/sunfounder/picar-x.git
    cd picar-x
    sudo python3 setup.py install

この手順には少し時間がかかりますのでしばらくお待ちください。

最後にスクリプト ``i2samp.sh`` を実行してi2sアンプに必要なコンポーネントをインストールする必要があります。これによりpicar-xから音を出せる様になります。

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x
    sudo bash i2samp.sh
	
.. image:: img/i2s.png

``y`` と入力してリターンキーを押すと必要なスクリプトが走ります。

.. image:: img/i2s2.png

``y`` と入力してリターンキーを押して ``/dev/zero`` をバックグラウンドで走らせます。

.. image:: img/i2s3.png

``y`` と入力してリターンキーを押してPicar-Xを再起動します。

.. note::
    再起動後に音が出ない場合にはi2samp.shを何回か実行してみてください。１回でうまく設定できない事があります。