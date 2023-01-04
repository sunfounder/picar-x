.. _i2c_config:

I2C設定
-----------------------

Raspberry Pi の I2C ポートを有効にします (有効にしている場合はスキップしてください。有効にしたかどうかわからない場合は続行してください)。

.. raw:: html

    <run></run>

.. code-block:: 

    $ sudo raspi-config

**3 インタフェースの設定**

.. image:: img/image282.png
    :align: center

キーボードのに矢印キーを使用して項目を選択し、リターンキーを押して決定します。

**P5 I2C**

.. image:: img/image283.png
    :align: center

**<Yes>を、そして <Ok> -> <Finish>** を選択します。

.. image:: img/image284.png
    :align: center