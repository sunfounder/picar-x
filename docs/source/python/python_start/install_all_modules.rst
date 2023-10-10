.. _install_all_modules:


すべてのモジュールをインストールする（重要）
============================================

インターネットに接続されていることを確認し、システムを更新してください:

.. raw:: html

    <run></run>

.. code-block::

    sudo apt update
    sudo apt upgrade

.. note::

    LiteバージョンのOSをインストールしている場合、Python3関連のパッケージをインストールする必要があります。

    .. raw:: html

        <run></run>

    .. code-block::

        sudo apt install git python3-pip python3-setuptools python3-smbus

``robot-hat`` をインストールしてください。

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

このステップは少し時間がかかるので、お待ちください。

最後に、i2sアンプに必要なコンポーネントをインストールするために、スクリプト ``i2samp.sh`` を実行する必要があります。そうしないと、picar-xに音が出ません。

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x
    sudo bash i2samp.sh
	
.. image:: img/i2s.png

``y`` を入力して、Enterキーを押し、スクリプトの実行を続行します。

.. image:: img/i2s2.png

``y`` を入力して、Enterキーを押し、 ``/dev/zero`` をバックグラウンドで実行します。

.. image:: img/i2s3.png

``y`` を入力して、Enterキーを押し、Picar-Xを再起動します。

.. note::
    再起動後に音が出ない場合、i2samp.shスクリプトを数回実行する必要があるかもしれません。
