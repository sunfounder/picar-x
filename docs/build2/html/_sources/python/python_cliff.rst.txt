.. _py_cliff:

6. 崖検出
===========================

PiCar-Xに少し自己保護意識を与えて、自身のグレースケールモジュールを使用して崖からの突進を避けるようにしましょう。

この例では、車は休止状態になります。
崖に押し出された場合、緊急に目覚め、後退し、「danger」と言います。

**コードの実行**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 6.cliff_detection.py
    

**コード**

.. note::
    以下のコードを **変更/リセット/コピー/実行/停止** することができます。しかし、それをする前に、 ``picar-x/example`` のようなソースコードのパスに移動する必要があります。コードを変更した後、直接実行して効果を確認できます。

.. raw:: html

    <run></run>

.. code-block:: python

    from picarx import Picarx
    from time import sleep
    from robot_hat import TTS

    tts = TTS()
    tts.lang("en-US")

    px = Picarx()
    # px = Picarx(grayscale_pins=['A0', 'A1', 'A2'])
    # manual modify reference value
    px.set_cliff_reference([200, 200, 200])

    current_state = None
    px_power = 10
    offset = 20
    last_state = "safe"

    if __name__=='__main__':
        try:
            while True:
                gm_val_list = px.get_grayscale_data()
                gm_state = px.get_cliff_status(gm_val_list)
                # print("cliff status is:  %s"%gm_state)

                if gm_state is False:
                    state = "safe"
                    px.stop()
                else:
                    state = "danger"   
                    px.backward(80)
                    if last_state == "safe":
                        tts.say("danger")
                        sleep(0.1)
                last_state = state

        finally:
            px.stop()
            print("stop and exit")
            sleep(0.1)

**どのように動作するのか？**

崖を検出する機能は次のようになります：

* ``get_grayscale_data()``：このメソッドは直接3つのセンサーの読み取り値を出力します。右から左に向かっています。エリアが明るいほど、得られる値が大きくなります。

* ``get_cliff_status(gm_val_list)``：このメソッドは3つのプローブの読み取り値を比較し、結果を出力します。結果が真であれば、車の前方に崖があることが検出されます。
