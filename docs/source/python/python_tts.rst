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

3. Text-zu-Sprache & Soundeffekte
=========================================

In diesem Beispiel verwenden wir die Soundeffekte von PiCar-X (genauer gesagt, von Robot HAT). 
Es besteht aus drei Teilen, nämlich Musik, Sound und Text-zu-Sprache.

.. image:: img/how_are_you.jpg

**i2samp installieren**

Bevor Sie die Funktionen Text-zu-Sprache (TTS) und Soundeffekte verwenden, 
aktivieren Sie zuerst den Lautsprecher, damit er eingeschaltet wird und Töne erzeugen kann.

Führen Sie ``i2samp.sh`` im **picar-x** Ordner aus, 
und dieses Skript installiert alles, was benötigt wird, um den i2s-Verstärker zu nutzen.

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x
    sudo bash i2samp.sh 

.. image:: img/tt_bash.png

Es wird mehrere Aufforderungen geben, um die Anfrage zu bestätigen. Antworten Sie auf alle Aufforderungen mit einem **Y**. Nachdem die Änderungen am Raspberry Pi-System vorgenommen wurden, muss der Computer neu gestartet werden, damit diese Änderungen wirksam werden.

Nach dem Neustart führen Sie das Skript ``i2samp.sh`` erneut aus, um den Verstärker zu testen. Wenn ein Ton erfolgreich vom Lautsprecher abgespielt wird, ist die Konfiguration abgeschlossen.

**Code ausführen**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 3.tts_example.py
    
Nachdem der Code ausgeführt wurde, bedienen Sie sich bitte gemäß der Aufforderung, die im Terminal angezeigt wird.

Taste drücken, um die Funktion aufzurufen!

    * Leertaste: Soundeffekt abspielen (Autohupe)
    * c: Soundeffekt mit Threads abspielen
    * t: Text in Sprache umwandeln (Sagen Sie Hallo)
    * q: Musik abspielen/stoppen

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

**Wie funktioniert des?**

Funktionen, die mit Hintergrundmusik zusammenhängen, umfassen Folgendes:

* ``music = Music()`` : Deklariert das Objekt.
* ``music.music_set_volume(20)`` : Stellt die Lautstärke ein, der Bereich liegt zwischen 0 und 100.
* ``music.music_play('../musics/slow-trail-Ahjay_Stelino.mp3')`` : Spielt Musikdateien ab, hier ist die Datei **slow-trail-Ahjay_Stelino.mp3** unter dem Pfad ``../musics``.
* ``music.music_stop()`` : Stoppt das Abspielen von Hintergrundmusik.

.. note::

    Sie können verschiedene Soundeffekte oder Musik zur ``musics`` oder ``sounds``-Ordner hinzufügen über :ref:`filezilla`.

Funktionen, die mit Soundeffekten zusammenhängen, umfassen Folgendes:

* ``music = Music()``
* ``music.sound_play('../sounds/car-double-horn.wav')`` : Spielt die Soundeffekt-Datei ab.
* ``muisc.sound_play_threading('../sounds/car-double-horn.wav')`` : Spielt die Soundeffekt-Datei im neuen Thread-Modus ab, ohne den Haupt-Thread zu unterbrechen.


Die Software `eSpeak <http://espeak.sourceforge.net/>`_ wird verwendet, um die Funktionen von TTS zu implementieren.

Importieren Sie das TTS-Modul in robot_hat, das Funktionen zur Umwandlung von Text in Sprache kapselt.

Funktionen, die mit Text-zu-Sprache zusammenhängen, umfassen Folgendes:

* ``tts = TTS()``
* ``tts.say(words)`` : Textaudio.
* ``tts.lang("en-US")`` :  Setzt die Sprache.

.. note:: 

    Stellen Sie die Sprache ein, indem Sie die Parameter von ``lang("")`` mit den folgenden Zeichen setzen.

.. list-table:: Language
    :widths: 15 50

    *   - zh-CN 
        - Mandarin (Chinesisch)
    *   - en-US 
        - Englisch-Vereinigte Staaten
    *   - en-GB     
        - Englisch-Vereinigtes Königreich
    *   - de-DE     
        - Deutschland-Deutsch
    *   - es-ES     
        - Spanien-Spanisch
    *   - fr-FR  
        - Frankreich-Französisch
    *   - it-IT  
        - Italien-Italienisch
