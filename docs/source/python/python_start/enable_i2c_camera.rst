I2Cインターフェースを有効にする
========================================

Raspberry Pi の I2C インターフェイスを使用していますが、デフォルトでは無効になっているため、最初に有効にする必要があります。

#. 以下のコマンドを入力してください:

    .. raw:: html

        <run></run>

    .. code-block::

        sudo raspi-config

#. キーボードの下矢印キーを押して **3 Interfacing Options** を選択し、 **Enter** キーを押します。

    .. image:: img/image282.png
        :align: center

#. 次に、 **P5 I2C** を選択します。

    .. image:: img/image283.png
        :align: center

#. キーボードの矢印キーを使用して、 **<Yes>** -> **<OK>** を選択し、I2Cのセットアップを完了します。

    .. image:: img/image284.png
        :align: center

#. **<Finish>** を選択すると、設定が有効になるために再起動する必要があることをポップアップでお知らせします。 **<Yes>** を選択してください。

    .. image:: img/camera_enable2.png
        :align: center
