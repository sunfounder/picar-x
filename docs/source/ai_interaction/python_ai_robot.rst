.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _ai_voice_assistant_car:

21. KI-Sprachassistent-Auto
===========================

In dieser Lektion verwandelst du deinen PiCar-X in einen **KI-gestützten Sprachassistenten auf Rädern**.  
Der Roboter kann auf deine Stimme reagieren, erkennen, was du sagst, mit Emotion sprechen  
und seine „Gefühle“ durch Bewegungen, Gesten und Lichter ausdrücken.

Du wirst ein **voll interaktives Sprachassistent-Auto** bauen, das folgende Komponenten nutzt:

* **LLM** – Large Language Model (OpenAI GPT oder Doubao).  
* **STT** – Speech-to-Text (Sprache zu Text).  
* **TTS** – Text-to-Speech (Text zu Sprache).  
* **Sensoren + Aktionen** – Ultraschall, Kamera und eingebaute Ausdrucksaktionen.

----

Bevor du beginnst
-----------------

Stelle sicher, dass du Folgendes abgeschlossen hast:

* :ref:`install_all_modules` — Installiere die Module ``robot-hat``, ``vilib``, ``picar-x`` und führe dann das Skript ``i2samp.sh`` aus.
* :ref:`test_piper` — Überprüfe die unterstützten Sprachen von **Piper TTS**.  
* :ref:`test_vosk` — Überprüfe die unterstützten Sprachen von **Vosk STT**.  
* :ref:`py_online_llm` — Dieser Schritt ist **sehr wichtig**: Besorge dir deinen **OpenAI**- oder **Doubao**-API-Schlüssel, oder den API-Schlüssel eines anderen unterstützten LLM.

Du solltest bereits haben:

* Ein funktionierendes **Mikrofon** und einen **Lautsprecher** auf deinem PiCar-X.  
* Einen **gültigen API-Schlüssel** in ``secret.py`` gespeichert.  
* Eine stabile Netzwerkverbindung (eine **Kabelverbindung** wird für bessere Stabilität empfohlen).

----

Beispiel ausführen
------------------

Beide Sprachversionen befinden sich im selben Verzeichnis:

.. code-block:: bash

   cd ~/picar-x/example

**Englische Version** (OpenAI GPT, Anleitung auf Englisch):

.. code-block:: bash

   sudo python3 21.voice_active_car_gpt.py

* LLM: ``OpenAI GPT-4o-mini``  
* TTS: ``en_US-ryan-low`` (Piper)  
* STT: Vosk (``en-us``)

Aktivierungswort:

.. code-block::

   "Hey buddy"

---

**Chinesische Version** (Doubao, Anleitung auf Chinesisch):

.. code-block:: bash

   sudo python3 21.voice_active_car_doubao_cn.py

* LLM: ``Doubao-seed-1-6-250615``  
* TTS: ``zh_CN-huayan-x_low`` (Piper)  
* STT: Vosk (``cn``)

Aktivierungswort:

.. code-block::

   "你好 滴滴"

.. note::

   Du kannst das **Aktivierungswort** und den **Roboternamen** im Code ändern:  
   ``NAME = "Buddy"`` oder ``NAME = "滴滴"``  
   ``WAKE_WORD = ["hey buddy"]`` oder ``WAKE_WORD = ["你好 滴滴"]``

----

Was passieren wird
------------------

Wenn du dieses Beispiel erfolgreich ausführst:

* Der Roboter **wartet auf das Aktivierungswort** (z. B. „Hey Buddy“ / „你好 滴滴“).  
* Wenn er das Aktivierungswort hört:

  * Die LEDs beginnen zu **blinken** und bleiben eingeschaltet.  
  * Der Roboter **begrüßt dich** mit fröhlicher Stimme.

* Anschließend beginnt er **in Echtzeit auf deine Stimme zu hören**.  
* Nachdem er verstanden hat, was du gesagt hast, führt er Folgendes aus:

  * Sendet deine Sprache an das **LLM** (OpenAI oder Doubao).  
  * **„Denkt“** und blinkt mit den LEDs während der Verarbeitung.  
  * Antwortet mit einer **TTS-Stimme**.  
  * Führt **entsprechende Aktionen** aus (z. B. Nicken, Drehen, Jubeln).

* Wenn du dich ihm zu sehr näherst, erkennt der Ultraschallsensor:

  * Eine automatische **Rückwärtsbewegung** zur Sicherheit.  
  * Unterbricht die aktuelle Runde mit einer Warnung.

**Beispielinteraktion**

.. code-block:: text

   Du: Hey Buddy
   Roboter: Hallo!

   Du: Dreh dich nach links und schau dich um.
   Roboter: Alles klar, ich drehe meinen Kopf nach links wie eine neugierige Katze!
   AKTIONEN: turn_left, look_left

----

Wechseln zu anderen LLMs oder TTS
---------------------------------

Du kannst ganz einfach zu anderen LLMs, TTS- oder STT-Sprachen wechseln — mit nur wenigen Codeänderungen:

* Unterstützte LLMs:

  * OpenAI
  * Doubao
  * Deepseek
  * Gemini
  * Qwen
  * Grok

* :ref:`test_piper` — Überprüfe die unterstützten Sprachen von **Piper TTS**.  
* :ref:`test_vosk` — Überprüfe die unterstützten Sprachen von **Vosk STT**.  

Zum Wechseln musst du einfach den Initialisierungsteil im Code anpassen:

.. code-block:: python

   from picarx.llm import Gemini as LLM
   llm = LLM(api_key="YOUR_KEY", model="gemini-pro")

   # Modelle und Sprachen festlegen
   TTS_MODEL = "en_US-ryan-low"
   STT_LANGUAGE = "en-us"

----

Aktions- & Sound-Referenz
-------------------------

Unten findest du die **Aktionsschlüsselwörter**, die das LLM nach der Zeile ``ACTIONS:`` zurückgeben kann, und was sie auf dem Roboter auslösen.

.. list-table::
   :header-rows: 1
   :widths: 20 55 25

   * - **Aktion**
     - **Was es macht (siehe preset_actions.py)**
     - **Effekt / Hinweise**
   * - ``shake head``
     - Schwenkt die Kamera schnell nach rechts↔links in abnehmenden Schritten und zentriert dann.
     - „Nein“-Geste; Räder bleiben stehen.
   * - ``nod``
     - Bewegt die Kamera zweimal auf und ab, dann zentriert.
     - „Ja“-Geste; Räder bleiben stehen.
   * - ``wave hands``
     - Neigt die Kamera, dann Lenken links/rechts zweimal (±25°), anschließend Zentrierung.
     - Verspielte Winke-Bewegung (Verwendung des Lenkservos als „Arme“).
   * - ``resist``
     - Kleine Neigung; abwechselnd Lenken/Pan ±15° dreimal; Stoppen und Zentrieren.
     - „Abwehrende“ Bewegung.
   * - ``act cute``
     - Kopf nach unten neigen; kurze Vorwärts-/Rückwärtsbewegungen; Reset.
     - Verspielte „niedliche“ Bewegung; sehr kurze Fahrbewegungen.
   * - ``rub hands``
     - Wiederholte kleine Lenkoszillation (±6°) fünfmal; Reset.
     - Imitiert „Hände reiben“.
   * - ``think``
     - Sanftes Schwenken nach rechts + Neigung nach unten + Lenken nach rechts; kurze Pause; Pose; Reset.
     - Wird als „nachdenkliche“ Animation verwendet.
   * - ``twist body``
     - Drei Zyklen aus Vorwärts/Stop/Pan-links/Lenk-links und Rückwärts/Stop/Pan-rechts/Lenk-rechts.
     - „Körperverdrehungs“-Bewegung.
   * - ``celebrate``
     - Kopf nach oben; zwei Pan-/Lenkbewegungen nach rechts, dann zwei nach links; Zentrierung.
     - Festliche, symmetrische Geste.
   * - ``depressed``
     - Reihe von Neigungen nach unten mit variierenden Winkeln und Pausen; endet mit langem Halten; Reset.
     - „Traurige“ Körperhaltung.

Bewegung & Utility
~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 22 58 20

   * - **Aktion**
     - **Was es macht**
     - **Hinweise**
   * - ``forward``
     - Fährt ~1 Sekunde mit niedriger Geschwindigkeit vorwärts, dann Stopp.
     - Implementiert mit ``forward(car)`` (5 % Geschwindigkeit + 1 s).
   * - ``backward``
     - Fährt ~1 Sekunde mit niedriger Geschwindigkeit rückwärts, dann Stopp.
     - Implementiert mit ``backward(car)`` (5 % Geschwindigkeit + 1 s).

Soundeffekte
~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 24 56 20

   * - **Sound**
     - **Was es macht**
     - **Hinweise**
   * - ``honking``
     - Spielt ``car-double-horn.wav`` asynchron (Lautstärke ~100).
     - Getriggert über ``Music.sound_play_threading``.
   * - ``start engine``
     - Spielt ``car-start-engine.wav`` asynchron (Lautstärke ~50).
     - Start-/Bereitschaftssignal.

Sensor-Trigger (automatisch)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Ultraschall-Näherung**

  * Auslöser: Abstand < 10 cm  
  * Nebeneffekt: automatisches ``backward`` + Deaktivieren des Bildes für diese Runde  
  * Eingefügte Meldung: ``<<<Ultrasonic sense too close: {distance}cm>>>``

Lebenszyklus-Hooks (LED-Indikatoren)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ``before_listen`` → zweimal blinken (bereit zum Zuhören)  
* ``before_think`` → Blinken (Denken)  
* ``before_say`` → LED an (Sprechen)  
* ``after_say`` → auf Aktionen warten → LED aus  
* ``on_stop`` → Aktionen stoppen, Geräte schließen

----

Fehlerbehebung
--------------

* **Der Roboter reagiert nicht auf das Aktivierungswort**  

  * Überprüfe, ob das Mikrofon funktioniert.  
  * Stelle sicher, dass ``WAKE_ENABLE = True`` ist.  
  * Passe das Aktivierungswort an deine Aussprache an.

* **Kein Ton aus dem Lautsprecher**
 
  * Überprüfe die TTS-Modellkonfiguration.  
  * Teste Piper oder Espeak manuell.  
  * Überprüfe Lautsprecheranschluss und Lautstärke.

* **API-Key-Fehler oder Zeitüberschreitung** 
 
  * Überprüfe deinen Schlüssel in ``secret.py``.  
  * Stelle eine stabile Netzwerkverbindung sicher.  
  * Vergewissere dich, dass das LLM unterstützt wird.

* **Picar-X bewegt sich nicht oder reagiert nicht**
 
  * Überprüfe, ob der Aktionsname mit ``actions_dict`` übereinstimmt.  
  * Verifiziere Motor- und Servoverbindungen.

* **Ultraschallsensor löst unerwartet aus**  

  * Überprüfe die Installationshöhe und den Winkel des Sensors.  
  * Passe den ``TOO_CLOSE``-Schwellwert im Code an.
