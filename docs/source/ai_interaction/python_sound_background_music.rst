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

13. Play Music and Sound Effects
=====================================

In this project, you will learn how to make the PiCar-X play background music or sound effects. You can also play music files that you have stored.

**Before You Start**

Make sure you‘ve completed:

* :ref:`install_all_modules` — Install ``robot-hat``, ``vilib``, ``picar-x`` modules, then run the script ``i2samp.sh``.


**Run the Code**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 13.sound_background_music.py
    
After the code runs, please operate according to the prompt that printed on the terminal.

Input key to call the function!

    * space: Play sound effect (Car horn)
    * c: Play sound effect with threads
    * q: Play/Stop Music

**Code**

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

**How it works?**

Functions related to background music include these:

* ``music = Music()`` : Declare the object.
* ``music.music_set_volume(20)`` : Set the volume, the range is 0~100.
* ``music.music_play('../musics/slow-trail-Ahjay_Stelino.mp3')`` : Play music files, here is the **slow-trail-Ahjay_Stelino.mp3** file under the ``../musics`` path.
* ``music.music_stop()`` : Stop playing background music.

.. note::

    You can add different sound effects or music to ``musics`` or ``sounds`` folder via :ref:`filezilla`.
