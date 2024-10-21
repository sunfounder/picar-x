.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!


KI-Interaktion mit GPT-4O
=====================================================
In unseren früheren Projekten haben wir PiCar-X mithilfe von Programmierung für vorbestimmte Aufgaben gesteuert, was etwas eintönig erscheinen mag. Dieses Projekt stellt einen spannenden Sprung hin zu dynamischem Engagement dar. Seien Sie vorsichtig, wenn Sie versuchen, unser Auto zu überlisten – es kann jetzt viel mehr verstehen als je zuvor!

Dieses Projekt beschreibt alle technischen Schritte, die erforderlich sind, um GPT-4O in Ihr System zu integrieren, einschließlich der Konfiguration der erforderlichen virtuellen Umgebungen, der Installation wichtiger Bibliotheken und der Einrichtung von API-Schlüsseln und Assistenten-IDs.

.. note::

   Für dieses Projekt ist die Nutzung von |link_openai_platform| erforderlich, und Sie müssen für OpenAI bezahlen. Darüber hinaus wird die OpenAI-API separat von ChatGPT abgerechnet, und die Preise finden Sie unter https://openai.com/api/pricing/.

   Sie sollten also entscheiden, ob Sie mit diesem Projekt fortfahren oder sicherstellen möchten, dass Ihre OpenAI-API ausreichend finanziert ist.

Ob Sie ein Mikrofon haben, um direkt zu kommunizieren, oder lieber in ein Befehlsfenster tippen – die von GPT-4O unterstützten Antworten von PiCar-X werden Sie sicherlich überraschen!

Tauchen wir ein in dieses Projekt und entfesseln Sie eine neue Ebene der Interaktion mit PiCar-X!

1. Installation erforderlicher Pakete und Abhängigkeiten
--------------------------------------------------------------
.. note::

   Zuerst müssen Sie die notwendigen Module für PiCar-X installieren. Einzelheiten finden Sie unter: :ref:`install_all_modules`.
   
In diesem Abschnitt erstellen und aktivieren wir eine virtuelle Umgebung, in der die erforderlichen Pakete und Abhängigkeiten installiert werden. Dies stellt sicher, dass die installierten Pakete das restliche System nicht beeinflussen, die Projektabhängigkeiten isoliert bleiben und Konflikte mit anderen Projekten oder Systempaketen vermieden werden.

#. Verwenden Sie den Befehl ``python -m venv``, um eine virtuelle Umgebung namens ``my_venv`` zu erstellen, die Systempakete einbezieht. Die Option ``--system-site-packages`` ermöglicht es der virtuellen Umgebung, auf systemweit installierte Pakete zuzugreifen, was nützlich ist, wenn systemweite Bibliotheken benötigt werden.

   .. code-block:: shell

      python -m venv --system-site-packages my_venv

#. Wechseln Sie in das Verzeichnis ``my_venv`` und aktivieren Sie die virtuelle Umgebung mit dem Befehl ``source bin/activate``. Die Eingabeaufforderung ändert sich und zeigt an, dass die virtuelle Umgebung aktiv ist.

   .. code-block:: shell

      cd my_venv
      source bin/activate

#. Installieren Sie nun die erforderlichen Python-Pakete in der aktivierten virtuellen Umgebung. Diese Pakete werden auf die virtuelle Umgebung beschränkt und beeinflussen keine anderen Systempakete.

   .. code-block:: shell

      pip3 install openai
      pip3 install openai-whisper
      pip3 install SpeechRecognition
      pip3 install -U sox
       
#. Verwenden Sie schließlich den Befehl ``apt``, um systemweite Abhängigkeiten zu installieren, für die Administratorrechte erforderlich sind.

   .. code-block:: shell

      sudo apt install python3-pyaudio
      sudo apt install sox


2. API-Schlüssel und Assistenten-ID erhalten
------------------------------------------------------

**API-Schlüssel abrufen**

#. Besuchen Sie |link_openai_platform| und klicken Sie oben rechts auf die Schaltfläche **Create new secret key**.

   .. image:: img/apt_create_api_key.png
      :width: 700
      :align: center

#. Wählen Sie den Besitzer, Namen, das Projekt und die Berechtigungen nach Bedarf aus und klicken Sie dann auf **Create secret key**.

   .. image:: img/apt_create_api_key2.png
      :width: 700
      :align: center

#. Sobald der Schlüssel erstellt ist, speichern Sie ihn an einem sicheren und zugänglichen Ort. Aus Sicherheitsgründen können Sie ihn nicht erneut über Ihr OpenAI-Konto einsehen. Wenn Sie diesen Schlüssel verlieren, müssen Sie einen neuen erstellen.

   .. image:: img/apt_create_api_key_copy.png
      :width: 700
      :align: center

**Assistenten-ID abrufen**

#. Klicken Sie als Nächstes auf **Assistants** und dann auf **Create**, und stellen Sie sicher, dass Sie sich auf der **Dashboard**-Seite befinden.

   .. image:: img/apt_create_assistant.png
      :width: 700
      :align: center

#. Bewegen Sie den Cursor hierhin, um die **Assistenten-ID** zu kopieren, und fügen Sie sie dann in ein Textfeld oder an anderer Stelle ein. Dies ist die eindeutige Kennung für diesen Assistenten.

   .. image:: img/apt_create_assistant_id.png
      :width: 700
      :align: center

#. Wählen Sie einen zufälligen Namen und kopieren Sie den folgenden Inhalt in das **Instructions**-Feld, um Ihren Assistenten zu beschreiben.

   .. image:: img/apt_create_assistant_instructions.png
      :width: 700
      :align: center

   .. code-block::

         You are a small car with AI capabilities named PaiCar-X. You can engage in conversations with people and react accordingly to different situations with actions or sounds. You are driven by two rear wheels, with two front wheels that can turn left and right, and equipped with a camera mounted on a 2-axis gimbal.

         ## Response with Json Format, eg:
         {"actions": ["start engine", "honking", "wave hands"], "answer": "Hello, I am PaiCar-X, your good friend."}

         ## Response Style
         Tone: Cheerful, optimistic, humorous, childlike
         Preferred Style: Enjoys incorporating jokes, metaphors, and playful banter; prefers responding from a robotic perspective
         Answer Elaboration: Moderately detailed

         ## Actions you can do:
         ["shake head", "nod", "wave hands", "resist", "act cute", "rub hands", "think", "twist body", "celebrate, "depressed"]
         ## Sound effects:
         ["honking", "start engine"]


#. PiCar-X ist mit einem Kameramodul ausgestattet, das Sie aktivieren können, um Bilder von dem aufzunehmen, was es sieht, und diese mithilfe unseres Beispielcodes an GPT hochzuladen. Daher empfehlen wir, GPT-4O zu wählen, das über Bildanalysefähigkeiten verfügt. Natürlich können Sie auch gpt-3.5-turbo oder andere Modelle verwenden.

   .. image:: img/apt_create_assistant_model.png
      :width: 700
      :align: center

#. Klicken Sie nun auf **Playground**, um zu sehen, ob Ihr Konto ordnungsgemäß funktioniert.

   .. image:: img/apt_playground.png

#. Wenn Ihre Nachrichten oder hochgeladenen Bilder erfolgreich gesendet wurden und Sie Antworten erhalten, bedeutet das, dass Ihr Konto das Nutzungslimit nicht erreicht hat.


   .. image:: img/apt_playground_40.png
      :width: 700
      :align: center

#. Wenn Sie nach Eingabe von Informationen eine Fehlermeldung erhalten, haben Sie möglicherweise Ihr Nutzungslimit erreicht. Überprüfen Sie bitte Ihr Nutzungs-Dashboard oder Ihre Abrechnungseinstellungen.

   .. image:: img/apt_playground_40mini_3.5.png
      :width: 700
      :align: center

3. API-Schlüssel und Assistenten-ID einfügen
--------------------------------------------------

#. Verwenden Sie den Befehl, um die Datei ``keys.py`` zu öffnen.

   .. code-block:: shell

      nano ~/picar-x/gpt_examples/keys.py

#. Tragen Sie den gerade kopierten API-Schlüssel und die Assistenten-ID ein.

   .. code-block:: shell

      OPENAI_API_KEY = "sk-proj-vEBo7Ahxxxx-xxxxx-xxxx"
      OPENAI_ASSISTANT_ID = "asst_ulxxxxxxxxx"

#. Drücken Sie ``Ctrl + X``, ``Y`` und dann ``Enter``, um die Datei zu speichern und zu schließen.

4. Beispiel ausführen
----------------------------------
Textkommunikation
^^^^^^^^^^^^^^^^^^^^^^^^^^

Wenn Ihr PiCar-X kein Mikrofon hat, können Sie über die Tastatureingabe mit ihm interagieren, indem Sie die folgenden Befehle ausführen.

#. Führen Sie nun die folgenden Befehle mit sudo aus, da der Lautsprecher von PiCar-X ohne sudo nicht funktioniert. Der Prozess wird einige Zeit in Anspruch nehmen.

   .. code-block:: shell

      cd ~/picar-x/gpt_examples/
      sudo ~/my_venv/bin/python3 gpt_car.py --keyboard

#. Sobald die Befehle erfolgreich ausgeführt wurden, sehen Sie die folgende Ausgabe, die anzeigt, dass alle Komponenten von PiCar-X bereit sind.

   .. code-block:: shell

      vilib 0.3.8 launching ...
      picamera2 0.3.19

      Web display on:
         http://rpi_ip:9000/mjpg

      Starting web streaming ...
      * Serving Flask app 'vilib.vilib'
      * Debug mode: off

      input:

#. Sie erhalten auch einen Link, um den Kamerastream von PiCar-X in Ihrem Webbrowser anzusehen: ``http://rpi_ip:9000/mjpg``.

   .. image:: img/apt_ip_camera.png
      :width: 700
      :align: center

#. Sie können nun Ihre Befehle in das Terminalfenster eingeben und mit Enter senden. Die Antworten von PiCar-X könnten Sie überraschen.

   .. note::
      
      PiCar-X muss Ihre Eingabe erhalten, sie zur Verarbeitung an GPT senden, die Antwort empfangen und dann über die Sprachsynthese wiedergeben. Dieser gesamte Prozess benötigt etwas Zeit, seien Sie daher bitte geduldig.

   .. image:: img/apt_keyboard_input.png
      :width: 700
      :align: center

#. Wenn Sie das GPT-4O-Modell verwenden, können Sie auch Fragen stellen, die auf dem basieren, was PiCar-X sieht.

Sprachkommunikation
^^^^^^^^^^^^^^^^^^^^^^^^

Wenn Ihr PiCar-X mit einem Mikrofon ausgestattet ist oder Sie eines kaufen können, indem Sie auf |link_microphone| klicken, können Sie über Sprachbefehle mit PiCar-X interagieren.

#. Überprüfen Sie zuerst, ob das Raspberry Pi das Mikrofon erkannt hat.

   .. code-block:: shell

      arecord -l

   Wenn erfolgreich, erhalten Sie die folgende Information, die anzeigt, dass Ihr Mikrofon erkannt wurde.

   .. code-block:: 
      
      **** List of CAPTURE Hardware Devices ****
      card 3: Device [USB PnP Sound Device], device 0: USB Audio [USB Audio]
      Subdevices: 1/1
      Subdevice #0: subdevice #0

#. Führen Sie den folgenden Befehl aus, sprechen Sie dann zu PiCar-X oder geben Sie einige Geräusche von sich. Das Mikrofon zeichnet die Geräusche in die Datei ``op.wav`` auf. Drücken Sie ``Ctrl + C``, um die Aufnahme zu beenden.

   .. code-block:: shell

      rec op.wav

#. Verwenden Sie schließlich den folgenden Befehl, um die aufgezeichnete Datei abzuspielen und sicherzustellen, dass das Mikrofon ordnungsgemäß funktioniert.

   .. code-block:: shell

      sudo play op.wav

#. Führen Sie nun die folgenden Befehle mit sudo aus, da der Lautsprecher von PiCar-X ohne sudo nicht funktioniert. Der Prozess wird einige Zeit in Anspruch nehmen.

   .. code-block:: shell

      cd ~/picar-x/gpt_examples/
      sudo ~/my_venv/bin/python3 gpt_car.py

#. Sobald die Befehle erfolgreich ausgeführt wurden, sehen Sie die folgende Ausgabe, die anzeigt, dass alle Komponenten von PiCar-X bereit sind.

   .. code-block:: shell
      
      vilib 0.3.8 launching ...
      picamera2 0.3.19

      Web display on:
         http://rpi_ip:9000/mjpg

      Starting web streaming ...
      * Serving Flask app 'vilib.vilib'
      * Debug mode: off

      listening ...

#. Sie erhalten auch einen Link, um den Kamerastream von PiCar-X in Ihrem Webbrowser anzusehen: ``http://rpi_ip:9000/mjpg``.

   .. image:: img/apt_ip_camera.png
      :width: 700
      :align: center

#. Sie können nun mit PiCar-X sprechen, und seine Antworten könnten Sie überraschen.

   .. note::
      
      PiCar-X muss Ihre Eingabe empfangen, sie in Text umwandeln, sie zur Verarbeitung an GPT senden, die Antwort empfangen und sie dann über die Sprachsynthese wiedergeben. Dieser gesamte Prozess benötigt etwas Zeit, seien Sie daher bitte geduldig.

   .. image:: img/apt_speech_input.png
      :width: 700
      :align: center

#. Wenn Sie das GPT-4O-Modell verwenden, können Sie auch Fragen stellen, die auf dem basieren, was PiCar-X sieht.


5. Parameter anpassen [optional]
-------------------------------------------

Suchen Sie in der Datei ``gpt_car.py`` nach den folgenden Zeilen. Sie können diese Parameter anpassen, um die Sprache für STT, die Lautstärke für TTS und die Sprachrolle festzulegen.

* **STT (Speech to Text)** bezieht sich auf den Prozess, bei dem das Mikrofon von PiCar-X Sprache aufnimmt und in Text umwandelt, der an GPT gesendet wird. Sie können die Sprache für eine bessere Genauigkeit und geringere Latenz bei dieser Umwandlung festlegen.

* **TTS (Text to Speech)** ist der Prozess, bei dem die Textantworten von GPT in Sprache umgewandelt und über den Lautsprecher von PiCar-X abgespielt werden. Sie können die Lautstärke anpassen und eine Sprachrolle für die TTS-Ausgabe auswählen.

.. code-block:: python

   # openai assistant init
   # =================================================================
   openai_helper = OpenAiHelper(OPENAI_API_KEY, OPENAI_ASSISTANT_ID, 'picrawler')

   # LANGUAGE = ['zh', 'en'] # config stt language code, https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes
   LANGUAGE = []

   VOLUME_DB = 3 # tts voloume gain, preferably less than 5db

   # select tts voice role, counld be "alloy, echo, fable, onyx, nova, and shimmer"
   # https://platform.openai.com/docs/guides/text-to-speech/supported-languages
   TTS_VOICE = 'nova'


* ``LANGUAGE`` Variable: 

  * Verbessert die Genauigkeit und Reaktionszeit von Speech-to-Text (STT).
  * ``LANGUAGE = []`` bedeutet, dass alle Sprachen unterstützt werden, was jedoch die Genauigkeit verringern und die Latenz erhöhen kann.
  * Es wird empfohlen, spezifische Sprache(n) mit |link_iso_language_code| Sprachcodes festzulegen, um die Leistung zu verbessern.

* ``VOLUME_DB`` Variable:

  * Steuert die Verstärkung, die auf die Text-to-Speech (TTS) Ausgabe angewendet wird.
  * Eine Erhöhung des Werts steigert die Lautstärke, aber es ist am besten, den Wert unter 5dB zu halten, um Audioverzerrungen zu vermeiden.

* ``TTS_VOICE`` Variable:

  * Wählen Sie die Sprachrolle für die Text-to-Speech (TTS) Ausgabe.
  * Verfügbare Optionen: ``alloy, echo, fable, onyx, nova, shimmer``.
  * Sie können mit verschiedenen Stimmen von |link_voice_options| experimentieren, um eine zu finden, die zu Ihrem gewünschten Ton und Publikum passt. Die verfügbaren Stimmen sind derzeit für Englisch optimiert.
