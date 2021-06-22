Text to Speak
===========================

Before using TTS functions, you must activate speaker so that it can make a sound.

Run ``i2samp.sh`` in the **picar-x** folder, and this script will install everything needed to use i2s amplifier.

.. code-block::

    sudo bash i2samp.sh 

.. image:: img/tt_bash.png

You will be prompted several times to confirm the request, all with **Y**. Finally, some changes made to your system require your computer to reboot to take effect.

After rebooting, you can run the ``i2samp.sh`` script again, which will test the amplifier for you. If you hear the sound successfully, the configuration is complete. 

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

We use `eSpeak <http://espeak.sourceforge.net/>`_ to implement the functions of tts.

You can use ``lang("")`` to set the language and ``say("")`` to speak out the text.

You can set the language by setting the parameters of ``lang("")`` with the following characters.

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