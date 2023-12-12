.. _install_all_modules:

すべてのモジュールをインストールする（重要）
============================================

インターネットに接続していることを確認し、システムをアップデートしてください：

.. raw:: html

    <run></run>

.. code-block::

    sudo apt update
    sudo apt upgrade

.. note::

    LiteバージョンのOSをインストールする場合は、Python3関連のパッケージをインストールする必要があります。

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


次に、 ``vilib`` モジュールをダウンロードしてインストールします。

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

このステップには少し時間がかかりますので、ご patienceください。

最後に、i2sアンプに必要なコンポーネントをインストールするためのスクリプト ``i2samp.sh`` を実行する必要があります。そうしないと、picar-xに音が出ません。

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x
    sudo bash i2samp.sh
	
.. image:: img/i2s.png

スクリプトを続けて実行するために ``y`` と入力し、Enterキーを押します。

.. image:: img/i2s2.png

バックグラウンドで ``/dev/zero`` を実行するために ``y`` と入力し、Enterキーを押します。

.. image:: img/i2s3.png

Picar-Xを再起動するために ``y`` と入力し、Enterキーを押します。

.. note::
    再起動後に音が出ない場合は、i2samp.shスクリプトを何度か実行する必要があるかもしれません。
