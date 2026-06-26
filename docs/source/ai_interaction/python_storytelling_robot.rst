.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

15. KI-Geschichten erzählender Roboter mit Piper und OpenAI
====================================================================

In der vorherigen Lektion haben wir zwei integrierte TTS-Engines auf dem Raspberry Pi ausprobiert (**Espeak** und **Pico2Wave**). Jetzt erkunden wir zwei leistungsstärkere Optionen: **Piper** (offline, neuronales Netzwerk) und **OpenAI TTS** (online, cloudbasiert).

* **Piper**: Eine lokale TTS-Engine, die offline auf dem Raspberry Pi läuft.
* **OpenAI TTS**: Ein Online-Dienst, der sehr natürliche, menschenähnliche Stimmen erzeugt.

Am Ende wird dein PiCar-X **herumfahren und Witze erzählen**, wie ein kleiner Geschichtenerzähler.

----

Bevor du beginnst
-----------------

Stelle sicher, dass du Folgendes abgeschlossen hast:

* :ref:`install_all_modules` — Installiere die Module ``robot-hat``, ``vilib``, ``picar-x`` und führe dann das Skript ``i2samp.sh`` aus.

----

.. _test_piper:

1. Piper testen
------------------

**Schritte zum Ausprobieren**:

#. Neue Datei erstellen:

   .. code-block:: bash

      cd ~/picar-x/example
      sudo nano test_tts_piper.py

#. Beispielcode in die Datei einfügen. Mit ``Ctrl+X``, dann ``Y`` und schließlich ``Enter`` speichern und beenden.

   .. code-block:: python

       from picarx.tts import Piper

       tts = Piper()

       # List supported languages
       print(tts.available_countrys())

       # List models for English (en_us)
       print(tts.available_models('en_us'))

       # Set a voice model (auto-download if not already present)
       tts.set_model("en_US-amy-low")

       # Say something
       tts.say("Hello! I'm Piper TTS.")

   * ``available_countrys()``: Zeigt die unterstützten Sprachen an.
   * ``available_models()``: Listet verfügbare Modelle für die angegebene Sprache.
   * ``set_model()``: Legt das Sprachmodell fest (lädt es automatisch herunter, falls nötig).
   * ``say()``: Wandelt Text in Sprache um und spielt ihn ab.

#. Programm ausführen:

   .. code-block:: bash

      sudo python3 test_tts_piper.py

#. Beim ersten Ausführen wird das gewählte Sprachmodell automatisch heruntergeladen.

   * Du solltest dann hören, wie der PiCar-X sagt: ``Hello! I'm Piper TTS.``

   * Du kannst das Sprachmodell ändern, indem du ``set_model()`` mit einem anderen Namen verwendest.


2. OpenAI TTS testen
-------------------------------

**API-Schlüssel abrufen und speichern**

#. Gehe zu |link_openai_platform| und melde dich an. Auf der Seite **API keys** klicke auf **Create new secret key**.

   .. image:: img/llm_openai_create.png

#. Fülle die Details aus (Owner, Name, Projekt und Berechtigungen falls nötig), dann klicke **Create secret key**.

   .. image:: img/llm_openai_create_confirm.png

#. Sobald der Schlüssel erstellt ist, kopiere ihn sofort — du kannst ihn später nicht mehr einsehen. Wenn du ihn verlierst, musst du einen neuen erstellen.

   .. image:: img/llm_openai_copy.png

#. Erstelle in deinem Projektordner (z. B. ``/picar-x/example``) eine Datei namens ``secret.py``:

   .. code-block:: bash

       cd ~/picar-x/example
       sudo nano secret.py

#. Füge deinen Schlüssel wie folgt in die Datei ein:

   .. code-block:: python

       # secret.py
       # Store secrets here. Never commit this file to Git.
       OPENAI_API_KEY = "sk-xxx"

**Testprogramm schreiben und ausführen**

#. Neue Datei erstellen:

   .. code-block:: bash

       cd ~/picar-x/example
       sudo nano test_tts_openai.py

#. Kopiere den folgenden Beispielcode in die Datei. Drücke ``Ctrl+X``, dann ``Y`` und schließlich ``Enter`` zum Speichern und Beenden.

   .. code-block:: python

      from picarx.tts import OpenAI_TTS
      from secret import OPENAI_API_KEY   # or use the try/except version shown above

      # Initialize OpenAI TTS
      tts = OpenAI_TTS(api_key=OPENAI_API_KEY)
      tts.set_model('gpt-4o-mini-tts')  # low-latency TTS model
      tts.set_voice('alloy')            # pick a voice

      # Quick hello (sanity check)
      tts.say("Hello! I'm OpenAI TTS.")

#. Programm ausführen:

   .. code-block:: bash

       sudo python3 test_tts_openai.py

#. Du solltest hören, wie der PiCar-X sagt:

   ``Hello! I'm OpenAI TTS.``

3. Geschichten erzählender Roboter
--------------------------------------------------

Nachdem wir sowohl **Piper** als auch **OpenAI TTS** getestet haben, setzen wir sie nun in einem echten Projekt ein:
ein **Geschichten erzählendes Roboterauto**, das während der Fahrt Witze erzählt.

In diesem Programm wird der PiCar-X:

* dich beim Start mit TTS begrüßen.
* vorwärts fahren und den ersten Witz erzählen.
* erneut vorwärts fahren und einen zweiten Witz erzählen.
* schließlich rückwärts fahren, „nach Hause“ zurückkehren und sich verabschieden.

Es ist, als hättest du einen kleinen Geschichtenerzähler auf Rädern!

**Code ausführen**

.. code-block:: bash

    cd ~/picar-x/example
    sudo python3 15.storytelling_robot.py

**Code**

.. code-block:: python

   from picarx import Picarx
   import time

   # === TTS Configuration ===
   # Default: Piper
   from picarx.tts import Piper
   tts = Piper()
   tts.set_model("en_US-amy-low")  # use the voice model you installed

   # Optional: switch to OpenAI TTS
   # from picarx.tts import OpenAI_TTS
   # from secret import OPENAI_API_KEY
   # tts = OpenAI_TTS(api_key=OPENAI_API_KEY)
   # tts.set_model("gpt-4o-mini-tts")  # low-latency TTS model
   # tts.set_voice("alloy")            # choose a voice

   # === PiCar-X Setup ===
   px = Picarx()

   # Quick hello (sanity check)
   tts.say("Hello! I'm PiCar-X speaking with Piper.")

   def main():
       try:
           # Leg 1
           px.forward(30)
           time.sleep(3)
           px.stop()
           tts.say("Why can't your nose be twelve inches long? Because then it would be a foot!")

           # Leg 2
           px.forward(30)
           time.sleep(3)
           px.stop()
           tts.say("Why did the cow go to outer space? To see the moooon!")

           # Wrap-up
           tts.say("That's all for today. Goodbye, let's go home and sleep.")
           px.backward(30)
           time.sleep(6)
           px.stop()

       except KeyboardInterrupt:
           px.stop()
       finally:
           px.stop()
           px.set_dir_servo_angle(0)

   if __name__ == "__main__":
       main()

----

Fehlerbehebung
-------------------

* **No module named 'secret'**

  Das bedeutet, dass sich ``secret.py`` nicht im gleichen Ordner wie deine Python-Datei befindet.
  Verschiebe ``secret.py`` in das Verzeichnis, aus dem du das Skript startest, z. B.:

  .. code-block:: bash

     ls ~/picar-x/example
     # Stelle sicher, dass du sowohl secret.py als auch deine .py-Datei siehst

* **OpenAI: Invalid API key / 401**

  * Prüfe, ob du den vollständigen Schlüssel eingefügt hast (beginnt mit ``sk-``) und keine zusätzlichen Leerzeichen/Zeilenumbrüche vorhanden sind.
  * Stelle sicher, dass du ihn korrekt importierst:

    .. code-block:: python

       from secret import OPENAI_API_KEY

  * Bestätige die Netzwerkverbindung auf deinem Pi (versuche ``ping api.openai.com``).

* **OpenAI: Quota exceeded / billing error**

  * Eventuell musst du die Abrechnung aktivieren oder das Kontingent im OpenAI-Dashboard erhöhen.
  * Versuche es nach Behebung des Konto-/Abrechnungsproblems erneut.

* **Piper: tts.say() läuft, aber kein Ton**

  * Stelle sicher, dass ein Sprachmodell tatsächlich vorhanden ist:

    .. code-block:: bash

       ls ~/.local/share/piper/voices

  * Bestätige, dass der Modellname im Code exakt übereinstimmt:

    .. code-block:: python

       tts.set_model("en_US-amy-low")

  * Überprüfe das Audioausgabegerät/die Lautstärke auf deinem Pi (``alsamixer``) und dass die Lautsprecher angeschlossen und eingeschaltet sind.

* **ALSA-/Audiogerätefehler (z. B. "Audio device busy" oder "No such file or directory")**

  * Schließe andere Programme, die Audio verwenden.
  * Starte den Pi neu, falls das Gerät belegt bleibt.
  * Wähle für HDMI- vs. Kopfhörerausgang das richtige Gerät in den Audioeinstellungen von Raspberry Pi OS.

* **Permission denied beim Ausführen von Python**

  * Versuche es mit ``sudo``, falls deine Umgebung dies erfordert:

    .. code-block:: bash

       sudo python3 test_tts_piper.py



Vergleich der TTS-Engines
-------------------------

.. list-table:: Funktionsvergleich: Espeak vs Pico2Wave vs Piper vs OpenAI TTS
   :header-rows: 1
   :widths: 18 18 20 22 22

   * - Punkt
     - Espeak
     - Pico2Wave
     - Piper
     - OpenAI TTS
   * - Läuft auf
     - Integriert auf Raspberry Pi (offline)
     - Integriert auf Raspberry Pi (offline)
     - Raspberry Pi / PC (offline, benötigt Modell)
     - Cloud (online, benötigt API-Schlüssel)
   * - Stimmqualität
     - Roboterhaft
     - Natürlicher als Espeak
     - Natürlich (neuronales TTS)
     - Sehr natürlich / menschenähnlich
   * - Steuerung
     - Geschwindigkeit, Tonhöhe, Lautstärke
     - Begrenzte Steuerung
     - Verschiedene Stimmen/Modelle wählbar
     - Modell und Stimmen wählbar
   * - Sprachen
     - Viele (Qualität variiert)
     - Begrenzte Auswahl
     - Viele Stimmen/Sprachen verfügbar
     - Am besten Englisch (andere je nach Verfügbarkeit)
   * - Latenz / Geschwindigkeit
     - Sehr schnell
     - Schnell
     - Echtzeit auf Pi 4/5 mit „low“-Modellen
     - Netzabhängig (meist geringe Latenz)
   * - Einrichtung
     - Minimal
     - Minimal
     - ``.onnx`` + ``.onnx.json``-Modelle herunterladen
     - API-Schlüssel erstellen, Client installieren
   * - Am besten geeignet für
     - Schnelle Tests, einfache Prompts
     - Etwas bessere Offline-Stimme
     - Lokale Projekte mit besserer Qualität
     - Höchste Qualität, viele Stimmoptionen
