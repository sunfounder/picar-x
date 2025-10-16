
.. _py_tts:

13. 播放音乐与音效
=====================================

在本项目中，你将学习如何让 PiCar-X 播放背景音乐或音效。你也可以播放自己存储的音乐文件。


**运行代码**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 13.sound_background_music.py
    
代码运行后，请按照终端中打印的提示进行操作。

按键以调用功能！

    * space: 播放音效（汽车喇叭）
    * c: 使用线程播放音效
    * q: 播放/停止音乐

**代码**

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

**它是如何工作的？**

与背景音乐相关的函数包括以下几个：

* ``music = Music()`` ：声明对象。  
* ``music.music_set_volume(20)`` ：设置音量，范围是 0~100。  
* ``music.music_play('../musics/slow-trail-Ahjay_Stelino.mp3')`` ：播放音乐文件，这里播放的是 ``../musics`` 路径下的 **slow-trail-Ahjay_Stelino.mp3** 文件。  
* ``music.music_stop()`` ：停止播放背景音乐。

.. note::

    你可以通过 :ref:`filezilla` 将不同的音效或音乐添加到 ``musics`` 或 ``sounds`` 文件夹中。
