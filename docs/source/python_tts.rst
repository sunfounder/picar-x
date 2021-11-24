文字转语音
============================

在使用文字转语音 (TTS) 功能之前，请先激活扬声器，使其启用并可以发出声音。

在 **picar-x** 文件夹中运行 ``i2samp.sh``，此脚本将安装使用 i2s 放大器所需的一切。

.. raw:: html

    <run></run>

.. code-block::

    sudo bash i2samp.sh 

.. image:: img/tt_bash.png

会有几个提示要求确认请求。 用 **Y** 响应所有提示。 对树莓派系统进行更改后，需要重新启动计算机才能使这些更改生效。

重新启动后，再次运行 ``i2samp.sh`` 脚本来测试放大器。 如果扬声器成功播放声音，则配置完成。

**运行代码**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/picar-x/example
    sudo python3 tts_example.py
    
运行代码后，帕克会说“你好”、“嗨”、“再见”、“很高兴见到你”。

**代码**

.. note::
    您可以 **修改/重置/复制/运行/停止** 下面的代码。 但在此之前，您需要转到像 ``picar-x/example`` 这样的源代码路径。 修改代码后，可以直接运行看看效果。

.. raw:: html

    <run></run>

.. code-block:: python

    import sys
    sys.path.append(r'/home/pi/picar-x/lib')
    from tts import TTS

    if __name__ == "__main__":
        words = ["Hello", "Hi", "Good bye", "Nice to meet you"]
        tts_robot = TTS()
        tts_robot.lang("en-US")
        for i in words:
            print(i)
            tts_robot.say(i)


**这个怎么运作？**

`eSpeak <http://espeak.sourceforge.net/>`_ 软件用于实现TTS的功能。

使用 ``lang("")`` 设置语言，使用 ``say("")`` 设置文本音频。

.. note:: 

    通过使用以下字符设置 ``lang("")`` 的参数来设置语言。

.. list-table:: Language
    :widths: 15 50

    *   - zh-CN 
        - 中文
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