Text to Speak
===========================

在使用TTS功能之前，您需要先激活 amplifier ，让它能够发出声音。

在 **picar-x** 目录下，运行 ``i2samp.sh`` script , This script will install everything needed to use i2s amplifier.

.. code-block::

    sudo bash i2samp.sh 

.. image:: img/tt_bash.png

你会被提示多次确认请求，都选 **Y** 。最后，some changes made to your system require your computer to reboot to take effect.

重启之后，你可以再运行一次  ``i2samp.sh`` script ， 它会为你测试  amplifier 。 如果你成功听到了声音，就代表已经配置完成了。 


**Code**

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


**How it works?** 

我们使用了 `eSpeak <http://espeak.sourceforge.net/>`_ 来实现tts的功能。

你可以用 ``tts.lang("")`` 来设置语种，用 ``tts.say("")`` 说出text

你可以将 ``lang`` 的参数以下字符来设置语种。

.. list-table:: Language
    :widths: 15 50

    *   - zh-CN 
        - 普通话(中国)
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