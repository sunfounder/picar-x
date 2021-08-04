Text to Speech
===========================

Before using the Text-to-Speech (TTS) functions, first activate the speaker so that it will be enabled and can make sounds.

Run ``i2samp.sh`` in the **picar-x** folder, and this script will install everything needed to use i2s amplifier.

.. code-block::

    sudo bash i2samp.sh 

.. image:: img/tt_bash.png

There will be several prompts asking to confirm the request. Respond to all prompts with a **Y**. After the changes have been made to the Raspberry Pi system, the computer will need to reboot for these changes to take effect.

After rebooting, run the ``i2samp.sh`` script again to test the amplifier. If a sound successfully plays from the speaker, the configuration is complete.

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

The `eSpeak <http://espeak.sourceforge.net/>`_ software is used to implement the functions of TTS.

Use ``lang("")`` to set the language, and ``say("")`` for text audio.

.. note:: 

    Set the language by setting the parameters of ``lang("")`` with the following characters.

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