.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_tts:

3. Text to Speech & Sound Effect
=========================================

In this example, we use PiCar-X's (to be precise, Robot HAT’s) sound effects. 
It consists of three parts, namely Muisc, Sound, Text to Speech.

.. image:: img/how_are_you.jpg

**Install i2samp**

Before using the Text-to-Speech (TTS) and Sound Effect functions, 
first activate the speaker so that it will be enabled and can make sounds.

Run ``i2samp.sh`` in the **picar-x** folder, 
and this script will install everything needed to use i2s amplifier.

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x
    sudo bash i2samp.sh 

.. image:: img/tt_bash.png

There will be several prompts asking to confirm the request. Respond to all prompts with a **Y**. After the changes have been made to the Raspberry Pi system, the computer will need to reboot for these changes to take effect.

After rebooting, run the ``i2samp.sh`` script again to test the amplifier. If a sound successfully plays from the speaker, the configuration is complete.

**Run the Code**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 3.tts_example.py
    
After the code runs, please operate according to the prompt that printed on the terminal.

Input key to call the function!

    * space: Play sound effect (Car horn)
    * c: Play sound effect with threads
    * t: Text to speak (Say Hello)
    * q: Play/Stop Music

**Code**

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

**How it works?**

Functions related to background music include these:

* ``music = Music()`` : Declare the object.
* ``music.music_set_volume(20)`` : Set the volume, the range is 0~100.
* ``music.music_play('../musics/slow-trail-Ahjay_Stelino.mp3')`` : Play music files, here is the **slow-trail-Ahjay_Stelino.mp3** file under the ``../musics`` path.
* ``music.music_stop()`` : Stop playing background music.

.. note::

    You can add different sound effects or music to ``musics`` or ``sounds`` folder via :ref:`filezilla`.

Functions related to sound effects include these:

* ``music = Music()``
* ``music.sound_play('../sounds/car-double-horn.wav')`` : Play the sound effect file.
* ``muisc.sound_play_threading('../sounds/car-double-horn.wav')`` : Play the sound effect file in a new thread mode without suspending the main thread.


The `eSpeak <http://espeak.sourceforge.net/>`_ software is used to implement the functions of TTS.

Import the TTS module in robot_hat, which encapsulates functions that convert text to speech.

Functions related to Text to Speech include these:

* ``tts = TTS()``
* ``tts.say(words)`` : Text audio.
* ``tts.lang("en-US")`` :  Set the language.

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