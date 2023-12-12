.. _py_tts:

3. テキストから音声へ & 効果音
=========================================

この例では、PiCar-X（正確にはRobot HAT）の音声効果を使用します。
これは音楽、サウンド、テキストから音声への3つの部分から構成されています。

.. image:: img/how_are_you.jpg

**i2sampのインストール**

テキストから音声への変換（TTS）と効果音の機能を使用する前に、
まずスピーカーをアクティブにして、音を出せるようにしましょう。

**picar-x** フォルダ内で ``i2samp.sh`` を実行し、
このスクリプトはi2sアンプを使用するために必要なものをすべてインストールします。

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x
    sudo bash i2samp.sh 

.. image:: img/tt_bash.png

いくつかの確認プロンプトが表示されますので、すべてのプロンプトに対して **Y** と回答してください。Raspberry Piシステムに変更が加えられた後、これらの変更が有効になるためにコンピュータを再起動する必要があります。

再起動後、再び ``i2samp.sh`` スクリプトを実行してアンプをテストします。スピーカーから音が正常に鳴る場合は、設定が完了しています。

**コードの実行**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 3.tts_example.py
    
コードを実行した後、ターミナルに表示されたプロンプトに従って操作してください。

機能を呼び出すためにキーを入力してください！

    * space: 効果音を再生（クラクション）
    * c: スレッドで効果音を再生
    * t: テキストを話す（ハローと言う）
    * q: 音楽の再生/停止

**コード**

.. code-block:: python

    from time import sleep
    from robot_hat import Music,TTS
    import readchar

    music = Music()
    tts = TTS()

    manual = '''
    Input key to call the function!
        space: Play sound effect (Car horn)
        c: Play sound effect with threads
        t: Text to speak
        q: Play/Stop Music
    '''

    def main():
        print(manual)

        flag_bgm = False
        music.music_set_volume(20)
        tts.lang("en-US")


        while True:
            key = readchar.readkey()
            key = key.lower()
            if key == "q":
                flag_bgm = not flag_bgm
                if flag_bgm is True:
                    music.music_play('../musics/slow-trail-Ahjay_Stelino.mp3')
                else:
                    music.music_stop()

            elif key == readchar.key.SPACE:
                music.sound_play('../sounds/car-double-horn.wav')
                sleep(0.05)

            elif key == "c":
                music.sound_play_threading('../sounds/car-double-horn.wav')
                sleep(0.05)

            elif key == "t":
                words = "Hello"
                tts.say(words)

    if __name__ == "__main__":
        main()

**どのように動作するのか？**

背景音楽に関連する機能には以下のものがあります：

* ``music = Music()`` : オブジェクトを宣言。
* ``music.music_set_volume(20)`` : 音量を設定します。範囲は0〜100です。
* ``music.music_play('../musics/slow-trail-Ahjay_Stelino.mp3')`` : 音楽ファイルを再生します。ここでは ``../musics`` パス下の **slow-trail-Ahjay_Stelino.mp3** ファイルです。
* ``music.music_stop()`` : 背景音楽の再生を停止します。

.. note::

    ``musics`` や ``sounds`` フォルダに異なる効果音や音楽を :ref:`filezilla` を通じて追加することができます。

効果音に関連する機能には以下のものがあります：

* ``music = Music()``
* ``music.sound_play('../sounds/car-double-horn.wav')`` : 効果音のファイルを再生します。
* ``muisc.sound_play_threading('../sounds/car-double-horn.wav')`` : メインスレッドを中断せずに新しいスレッドモードで効果音のファイルを再生します。


テキストから音声への機能は `eSpeak <http://espeak.sourceforge.net/>`_ ソフトウェアを使用して実装されています。

robot_hatのTTSモジュールをインポートし、テキストを音声に変換する機能をカプセル化します。

テキストから音声への関連機能には以下のものがあります：

* ``tts = TTS()``
* ``tts.say(words)`` : テキストのオーディオ。
* ``tts.lang("en-US")`` : 言語を設定します。

.. note:: 

    ``lang("")`` のパラメータに以下の文字を設定することで言語を設定します。

.. list-table:: Language
    :widths: 15 50

    *   - zh-CN 
        - Mandarin (Chinese)
    *   - en-US 
        - English-United States
    *   - en-GB     
        - English-United Kingdom
    *   - de-DE     
        - Germany-Deutsch
    *   - es-ES     
        - España-Español
    *   - fr-FR  
        - France-Le français
    *   - it-IT  
        - Italia-lingua italiana