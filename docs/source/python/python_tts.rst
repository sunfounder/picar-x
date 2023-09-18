Text-zu-Sprache
========================

Bevor Sie die Text-zu-Sprache (TTS) Funktionen nutzen können, aktivieren Sie zuerst den Lautsprecher, damit dieser einsatzbereit ist und Töne abgeben kann.

Führen Sie ``i2samp.sh`` im Ordner **picar-x** aus. Dieses Skript installiert alles, was Sie zur Verwendung des i2s-Verstärkers benötigen.

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x
    sudo bash i2samp.sh

.. image:: img/tt_bash.png

Es erscheinen mehrere Aufforderungen zur Bestätigung der Anfrage. Beantworten Sie alle Aufforderungen mit einem **Y**. Nachdem die Änderungen am Raspberry Pi-System vorgenommen wurden, ist ein Neustart erforderlich, damit diese wirksam werden.

Nach dem Neustart führen Sie das Skript ``i2samp.sh`` erneut aus, um den Verstärker zu testen. Wenn ein Ton erfolgreich über den Lautsprecher abgespielt wird, ist die Konfiguration abgeschlossen.

**Code ausführen**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 tts_example.py

Nach dem Ausführen des Codes wird der PiCar-X "Hallo", "Hi", "Auf Wiedersehen", "Schön, Sie kennenzulernen" sagen.

.. image:: img/how_are_you.jpg

**Code**

.. note::
    Sie können den untenstehenden Code **modifizieren/zurücksetzen/kopieren/ausführen/stoppen**. Bevor Sie das tun, navigieren Sie jedoch zum Quellcodepfad, beispielsweise ``picar-x/example``. Nachdem Sie den Code geändert haben, können Sie ihn direkt ausführen, um die Ergebnisse zu sehen.

.. raw:: html

    <run></run>

.. code-block:: python

    from robot_hat import TTS

    if __name__ == "__main__":
        words = ["Hallo", "Hi", "Auf Wiedersehen", "Schön, Sie kennenzulernen"]
        tts_robot = TTS()
        for i in words:
            print(i)
            tts_robot.say(i)

**Wie funktioniert es?**

Die Software `eSpeak <http://espeak.sourceforge.net/>`_ wird verwendet, um die Funktionen von TTS umzusetzen.

Importieren Sie das TTS-Modul aus robot_hat, welches Funktionen kapselt, die Text in Sprache umwandeln.

.. code-block::

    from robot_hat import TTS

Erstellen Sie eine String-Liste ``words``, dann erstellen Sie ein instanziiertes Objekt der TTS()-Klasse ``tts_robot`` und verwenden Sie schließlich die Funktion ``tts_robot.say()``, um die Wörter in der Liste auszusprechen.

.. code-block::

    words = ["Hallo", "Hi", "Auf Wiedersehen", "Schön, Sie kennenzulernen"]
    tts_robot = TTS()
    for i in words:
        print(i)
        tts_robot.say(i)
