.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _py_tts:

13. Musik und Soundeffekte abspielen
=====================================

In diesem Projekt lernst du, wie du mit dem PiCar-X Hintergrundmusik oder Soundeffekte abspielst. Du kannst auch eigene Musikdateien verwenden, die auf dem Gerät gespeichert sind.

**Bevor du beginnst**

Stelle sicher, dass du Folgendes abgeschlossen hast:

* :ref:`install_all_modules` — Installiere die Module ``robot-hat``, ``vilib``, ``picar-x`` und führe dann das Skript ``i2samp.sh`` aus.


**Code ausführen**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 13.sound_background_music.py

Nachdem der Code ausgeführt wurde, folge den Anweisungen, die im Terminal angezeigt werden.

Drücke die entsprechende Taste, um die gewünschte Funktion auszuführen:

    * **Leertaste**: Soundeffekt (Autohupe) abspielen
    * **c**: Soundeffekt in einem Thread abspielen (gleichzeitig mit anderen Aktionen)
    * **q**: Musik starten oder stoppen

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

**Wie funktioniert das?**

Die Funktionen, die mit Hintergrundmusik zusammenhängen, sind:

* ``music = Music()`` : Erstellt ein Musikobjekt.
* ``music.music_set_volume(20)`` : Legt die Lautstärke fest (Bereich 0–100).
* ``music.music_play('../musics/slow-trail-Ahjay_Stelino.mp3')`` : Spielt eine Musikdatei ab — hier die Datei **slow-trail-Ahjay_Stelino.mp3** im Ordner ``../musics``.
* ``music.music_stop()`` : Stoppt die Wiedergabe der Hintergrundmusik.

.. note::

    Du kannst eigene Soundeffekte oder Musikdateien über :ref:`filezilla` in die Ordner ``musics`` oder ``sounds`` hochladen.
