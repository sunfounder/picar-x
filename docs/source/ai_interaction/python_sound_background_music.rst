.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

.. _py_tts:

13. 音楽と効果音を再生する
=====================================

このプロジェクトでは、PiCar-X でBGM（バックグラウンドミュージック）や効果音を再生する方法を学びます。保存してある音楽ファイルも再生できます。

**始める前に**

以下を完了していることを確認してください：

* :ref:`install_all_modules` — ``robot-hat``、 ``vilib``、 ``picar-x`` モジュールをインストールし、その後スクリプト ``i2samp.sh`` を実行します。


**コードを実行する**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 13.sound_background_music.py
    
コードが動作したら、ターミナルに表示される指示に従って操作してください。

関数を呼び出すためにキー入力！

    * space: 効果音を再生（クラクション）
    * c: スレッドで効果音を再生
    * q: 音楽の再生/停止

**コード**


.. code-block:: python

    from time import sleep
    from picarx.music import Music
    import readchar

    music = Music()

    manual = '''
    Input key to call the function!
        space: Play sound effect (Car horn)
        c: Play sound effect with threads
        q: Play/Stop Music
    '''

    def main():
        print(manual)

        flag_bgm = False
        music.music_set_volume(20)


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


    if __name__ == "__main__":
        main()

**どのように動作するのか？**

BGM（バックグラウンドミュージック）に関連する主な関数は以下のとおりです：

* ``music = Music()`` ： オブジェクトを宣言します。  
* ``music.music_set_volume(20)`` ： 音量を設定します（範囲：0～100）。  
* ``music.music_play('../musics/slow-trail-Ahjay_Stelino.mp3')`` ： 音楽ファイルを再生します。ここでは ``../musics`` パスにある **slow-trail-Ahjay_Stelino.mp3** を再生します。  
* ``music.music_stop()`` ： BGM の再生を停止します。

.. note::

    :ref:`filezilla` を使って ``musics`` または ``sounds`` フォルダに任意の音楽や効果音を追加できます。
