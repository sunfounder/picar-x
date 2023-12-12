I2Cインターフェースを有効にする（重要）
========================================

ここではRaspberry PiのI2Cインターフェースを使用しますが、デフォルトでは無効になっているため、まず有効にする必要があります。

#. 次のコマンドを入力します：

    .. raw:: html

        <run></run>

    .. code-block:: 

        sudo raspi-config

#. キーボードの下矢印キーを押して **Interfacing Options** を選択し、 **Enter** キーを押します。

    .. image:: img/image282.png
        :align: center

#. 次に **I2C** を選択します。

    .. image:: img/image283.png
        :align: center

#. キーボードの矢印キーで **<Yes>** -> **<OK>** を選択して、I2Cの設定を完了します。

    .. image:: img/image284.png
        :align: center

#. **<Finish>** を選択した後、設定が有効になるために再起動が必要であることを示すポップアップが表示されます。 **<Yes>** を選択します。

    .. image:: img/camera_enable2.png
        :align: center
