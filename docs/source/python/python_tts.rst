
テキストから音声へ
===========================

テキストから音声（TTS）の機能を使用する前に、スピーカーをアクティブにして、音を出せるように設定してください。

**picar-x** フォルダ内の ``i2samp.sh`` を実行し、i2sアンプを使用するために必要なすべてをインストールします。

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x
    sudo bash i2samp.sh 

.. image:: img/tt_bash.png

いくつかのプロンプトが表示され、リクエストの確認を求められます。すべてのプロンプトに **Y** で返答してください。Raspberry Piのシステムに変更が加えられた後、これらの変更を有効にするためにコンピュータを再起動する必要があります。

再起動後、アンプをテストするために ``i2samp.sh`` スクリプトを再度実行してください。スピーカーから音が正常に再生されれば、設定は完了です。

**コードを実行する**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 tts_example.py
    
コードを実行すると、PiCar-Xは「Hello」、「Hi」、「Good bye」、「Nice to meet you」と言います。

.. image:: img/how_are_you.jpg

**コード**

.. note::
    下のコードは **変更/リセット/コピー/実行/停止** ができます。しかし、それをする前に、 ``picar-x/example`` のようなソースコードのパスに移動する必要があります。コードを変更した後、その効果を直接見るために実行することができます。

.. raw:: html

    <run></run>

.. code-block:: python

    from robot_hat import TTS


    if __name__ == "__main__":
        words = ["Hello", "Hi", "Good bye", "Nice to meet you"]
        tts_robot = TTS()
        for i in words:
            print(i)
            tts_robot.say(i)


**どのように動作するのか？** 

`eSpeak <http://espeak.sourceforge.net/>`_ ソフトウェアは、TTSの機能を実装するために使用されます。

robot_hatの中のTTSモジュールをインポートし、テキストを音声に変換する機能をカプセル化します。

.. code-block::

    from robot_hat import TTS

文字列リスト ``words`` を作成し、 ``TTS()`` クラスのインスタンス化されたオブジェクト ``tts_robot`` を作成し、最終的に ``tts_robot.say()`` 関数を使用して、リスト内の単語を音声で話します。

.. code-block::

    words = ["Hello", "Hi", "Good bye", "Nice to meet you"]
    tts_robot = TTS()
    for i in words:
        print(i)
        tts_robot.say(i)
