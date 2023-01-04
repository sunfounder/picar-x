文書読み上げ
===========================

読み上げ機能（Text-to-Speech ：TTS） 機能を使用する前に、まずスピーカーを有効にして音を出せるようにします。
なお読み上げは中国語か英語となりますが、上手くローマ字表記をすることで日本語に聞こえる声を出せます。

 **picar-x** フォルダーで ``i2samp.sh`` を実行すると、このスクリプトはI2S（アイ・スクエア・シーと発音：センサーなどとの通信規格の一つです。）アンプを使用するために必要なすべてのモジュールをインストールします。

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/picar-x
    sudo bash i2samp.sh 

.. image:: img/tt_bash.png

実行すると確認を求めるプロンプトがいくつか表示されます。すべて **Y** と入力します。 Raspberry Piシステムに変更を加えた後に有効化にするため再起動する必要があります。

再起動するには **$** プロンプトで **sudo reboot** と入力してください。

再起動後にi2samp.shスクリプトを再度実行してアンプをテストします。 スピーカーからサウンドが再生されれば設定は完了です。

**コードの実行**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/picar-x/example
    sudo python3 tts_example.py
    
コードを実行すれば PiCar-X は \"Hello\"、 \"Hi\"、 \"Good bye\"、 \"Nice to meet you\" と言います。

.. image:: img/how_are_you.jpg

**コード**

.. note::
    以下のコードを **変更/リセット/コピー/実行/停止** することができます。 しかし、その前に ``picar-x/example`` のようなソース コード パスに移動する必要があります。 コードを変更した後、直接実行して効果を確認できます。

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


**どんな動きをするの？** 

 `eSpeak <http://espeak.sourceforge.net/>`_ ソフトウェアは、TTS の機能を実装するために使用されます。

テキストを音声に変換する関数をカプセル化するTTSモジュールをrobot_hatにインポートします。

.. code-block::

    from robot_hat import TTS

文字列リスト ``words`` を作成し、次に TTS() クラス ``tts_robot`` のインスタンス化されたオブジェクトを作成し、最後に ``tts_robot.say()`` 関数を使用してリスト内の単語を音声で話します。

.. code-block::

    words = ["Hello", "Hi", "Good bye", "Nice to meet you"]
    tts_robot = TTS()
    for i in words:
        print(i)
        tts_robot.say(i)