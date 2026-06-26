.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _py_online_llm:

18. Verbindung zu Online-LLMs herstellen
========================================

In dieser Lektion lernst du, wie du deinen PiCar-X (oder Raspberry Pi) mit verschiedenen **Online-Large-Language-Models (LLMs)** verbindest.
Jeder Anbieter erfordert einen API-Schlüssel und bietet unterschiedliche Modelle zur Auswahl an.

Wir werden lernen, wie man:

* API-Schlüssel sicher erstellt und speichert.
* Ein passendes Modell auswählt.
* Beispielcode ausführt, um mit den Modellen zu chatten.

Lass es uns Schritt für Schritt für jeden Anbieter durchgehen.

----

Bevor du beginnst
-----------------

Stelle sicher, dass du Folgendes abgeschlossen hast:

* :ref:`install_all_modules` — Installiere die Module ``robot-hat``, ``vilib``, ``picar-x`` und führe dann das Skript ``i2samp.sh`` aus.


OpenAI
----------

OpenAI bietet leistungsstarke Modelle wie **GPT-4o** und **GPT-4.1**, die sowohl Text- als auch Vision-Aufgaben unterstützen.

So richtest du es ein:

**API-Schlüssel abrufen und speichern**

#. Gehe zu |link_openai_platform| und melde dich an. Auf der Seite **API keys** klicke auf **Create new secret key**.

   .. image:: img/llm_openai_create.png

#. Gib die Details ein (Owner, Name, Projekt und Berechtigungen falls nötig), dann klicke **Create secret key**.

   .. image:: img/llm_openai_create_confirm.png

#. Kopiere den Schlüssel sofort — du kannst ihn später nicht mehr einsehen. Wenn du ihn verlierst, musst du einen neuen erstellen.

   .. image:: img/llm_openai_copy.png

#. Erstelle in deinem Projektordner (z. B. ``/picar-x/example``) eine Datei namens ``secret.py``:

   .. code-block:: bash

       cd ~/picar-x/example
       sudo nano secret.py

#. Füge den Schlüssel wie folgt ein:

   .. code-block:: python

       # secret.py
       # Store secrets here. Never commit this file to Git.
       OPENAI_API_KEY = "sk-xxx"

**Abrechnung aktivieren und Modelle prüfen**

#. Bevor du den Schlüssel verwendest, gehe in deinem OpenAI-Konto zur **Billing**-Seite, hinterlege Zahlungsinformationen und lade ein kleines Guthaben auf.

   .. image:: img/llm_openai_billing.png

#. Gehe dann zur **Limits**-Seite, um zu sehen, welche Modelle verfügbar sind, und kopiere die genaue Modell-ID für den Code.

   .. image:: img/llm_openai_models.png

**Mit Beispielcode testen**

#. Öffne die Beispieldatei:

   .. code-block:: bash

       cd ~/picar-x/example
       sudo nano 18.online_llm_test.py

#. Ersetze den Inhalt durch folgenden Code und aktualisiere ``model="xxx"`` (z. B. ``gpt-4o``):

   .. code-block:: python

       from picarx.llm import OpenAI
       from secret import OPENAI_API_KEY

       INSTRUCTIONS = "You are a helpful assistant."
       WELCOME = "Hello, I am a helpful assistant. How can I help you?"

       llm = OpenAI(
           api_key=OPENAI_API_KEY,
           model="gpt-4o",
       )

   Speichern und beenden (``Ctrl+X``, dann ``Y``, dann ``Enter``).

#. Test ausführen:

   .. code-block:: bash

       sudo python3 18.online_llm_test.py


----

Gemini
------------------

Gemini ist die Modellfamilie von Google. Schnell und ideal für allgemeine Anwendungsfälle.

**API-Schlüssel abrufen und speichern**

#. Melde dich bei |link_google_ai| an und gehe zur API Keys-Seite.

   .. image:: img/llm_gemini_get.png

#. Klicke oben rechts auf **Create API key**.

   .. image:: img/llm_gemini_create.png

#. Du kannst einen Schlüssel für ein bestehendes oder ein neues Projekt erstellen.

   .. image:: img/llm_gemini_choose.png

#. Kopiere den generierten API-Schlüssel.

   .. image:: img/llm_gemini_copy.png

#. In deinem Projektordner:

   .. code-block:: bash

       cd ~/picar-x/example
       sudo nano secret.py

#. Füge den Schlüssel hinzu:

   .. code-block:: python

        # secret.py
        # Store secrets here. Never commit this file to Git.
        GEMINI_API_KEY = "AIxxx"

**Verfügbare Modelle prüfen**

Gehe zur offiziellen |link_gemini_model|-Seite. Dort findest du eine Liste der Modelle, ihre genauen API-IDs und ihre Anwendungsbereiche.

   .. image:: img/llm_gemini_model.png

**Mit Beispielcode testen**

#. Öffne die Testdatei:

   .. code-block:: bash

       cd ~/picar-x/example
       sudo nano 18.online_llm_test.py

#. Ersetze den Inhalt und passe ``model="xxx"`` an (z. B. ``gemini-2.5-flash``):

   .. code-block:: python

       from picarx.llm import Gemini
       from secret import GEMINI_API_KEY

       INSTRUCTIONS = "You are a helpful assistant."
       WELCOME = "Hello, I am a helpful assistant. How can I help you?"

       llm = Gemini(
           api_key=GEMINI_API_KEY,
           model="gemini-2.5-flash",
       )

#. Speichern und ausführen:

   .. code-block:: bash

       sudo python3 18.online_llm_test.py

----

Qwen
------------------

Qwen ist eine Familie von großen Sprach- und Multimodalmodellen, die von Alibaba Cloud bereitgestellt werden.
Diese Modelle unterstützen Textgenerierung, logisches Schlussfolgern und multimodales Verständnis (z. B. Bildanalyse).

**API-Schlüssel abrufen**

Um Qwen-Modelle aufzurufen, benötigst du einen **API-Schlüssel**.
Internationale Nutzer verwenden in der Regel die **DashScope International (Model Studio)** Konsole.
Nutzer in Festlandchina können die **Bailian (百炼)** Konsole verwenden.

* **Für internationale Nutzer**

  #. Gehe zur offiziellen |link_qwen_inter|-Seite von **Alibaba Cloud**.
  #. Melde dich an oder erstelle ein **Alibaba Cloud** Konto.
  #. Navigiere zu **Model Studio** (Region Singapur oder Peking wählen).

      * Wenn ein "Activate Now"-Hinweis oben erscheint, aktiviere Model Studio, um ein kostenloses Kontingent zu erhalten (nur Singapur).
      * Die Aktivierung ist kostenlos — Gebühren fallen erst nach Verbrauch des Freikontingents an.
      * Wenn keine Aktivierungsaufforderung erscheint, ist der Dienst bereits aktiv.

  #. Gehe zur Seite **Key Management**. Auf dem Reiter **API Key** klicke auf **Create API Key**.
  #. Nach der Erstellung kopiere deinen API-Schlüssel und bewahre ihn sicher auf.

    .. image:: img/llm_qwen_api_key.png
        :width: 800

  .. note::
     Nutzer aus Hongkong, Macau und Taiwan sollten ebenfalls die **International (Model Studio)** Option wählen.

* **Für Nutzer in Festlandchina**

  #. Melde dich bei |link_aliyun| (Bailian-Konsole) an und verifiziere dein Konto.
  #. Wähle **Create API Key**. Wenn eine Aktivierungsaufforderung erscheint, aktiviere den Dienst, stimme den Bedingungen zu und beanspruche dein kostenloses Kontingent.

     .. image:: img/llm_qwen_aliyun_create.png

  #. Klicke erneut auf **Create API Key**, überprüfe dein Konto und bestätige.

     .. image:: img/llm_qwen_aliyun_confirm.png

  #. Nach der Erstellung kopiere den API-Schlüssel.

     .. image:: img/llm_qwen_aliyun_copy.png

**API-Schlüssel speichern**

#. In deinem Projektordner:

   .. code-block:: bash

       cd ~/picar-x/example
       sudo nano secret.py

#. Füge den Schlüssel wie folgt ein:

   .. code-block:: python

        # secret.py
        # Store secrets here. Never commit this file to Git.

        QWEN_API_KEY = "sk-xxx"

**Mit Beispielcode testen**

#. Öffne die Testdatei:

   .. code-block:: bash

       cd ~/picar-x/example
       sudo nano 18.online_llm_test.py

#. Ersetze den Inhalt durch folgenden Code und aktualisiere ``model="xxx"`` (z. B. ``qwen-plus``):

   .. code-block:: python

      from picarx.llm import Qwen
      from secret import QWEN_API_KEY

      INSTRUCTIONS = "You are a helpful assistant."
      WELCOME = "Hello, I am a helpful assistant. How can I help you?"

      llm = Qwen(
          api_key=QWEN_API_KEY,
          model="qwen-plus",
      )

#. Ausführen:

   .. code-block:: bash

       sudo python3 18.online_llm_test.py

Grok (xAI)
------------------

Grok ist eine von xAI entwickelte konversationelle KI, gegründet vom Team um Elon Musk. Du kannst dich über die xAI API verbinden.

**API-Schlüssel abrufen und speichern**

#. Registriere dich unter |link_grok_ai| und lade Guthaben auf — ohne Guthaben funktioniert die API nicht.

#. Gehe zur Seite **API Keys** und klicke auf **Create API key**.

   .. image:: img/llm_grok_create.png

#. Vergib einen Namen für den Schlüssel und klicke **Create API key**.

   .. image:: img/llm_grok_name.png

#. Kopiere den generierten Schlüssel und bewahre ihn sicher auf.

   .. image:: img/llm_grok_copy.png

#. In deinem Projektordner:

   .. code-block:: bash

       cd ~/picar-x/example
       sudo nano secret.py

#. Füge den Schlüssel wie folgt ein:

   .. code-block:: python

        # secret.py
        # Store secrets here. Never commit this file to Git.

        GROK_API_KEY = "xai-xxx"

**Verfügbare Modelle prüfen**

Gehe zur Models-Seite in der xAI-Konsole. Hier siehst du alle verfügbaren Modelle und deren API-IDs — diese IDs werden im Code verwendet.

   .. image:: img/llm_grok_model.png

**Mit Beispielcode testen**

#. Öffne die Testdatei:

   .. code-block:: bash

       cd ~/picar-x/example
       sudo nano 18.online_llm_test.py

#. Ersetze den Inhalt durch folgenden Code und passe ``model="xxx"`` an (z. B. ``grok-4-latest``):

   .. code-block:: python

       from picarx.llm import Grok
       from secret import GROK_API_KEY

       INSTRUCTIONS = "You are a helpful assistant."
       WELCOME = "Hello, I am a helpful assistant. How can I help you?"

       llm = Grok(
           api_key=GROK_API_KEY,
           model="grok-4-latest",
       )

#. Ausführen:

   .. code-block:: bash

       sudo python3 18.online_llm_test.py

----

DeepSeek
------------------

DeepSeek ist ein chinesischer LLM-Anbieter, der günstige und leistungsfähige Modelle anbietet.

**API-Schlüssel abrufen und speichern**

#. Melde dich bei |link_deepseek| an.

#. Wähle im Menü oben rechts **API Keys → Create API Key**.

   .. image:: img/llm_deepseek_create.png

#. Vergib einen Namen, klicke **Create**, dann kopiere den Schlüssel.

   .. image:: img/llm_deepseek_copy.png

#. In deinem Projektordner:

   .. code-block:: bash

       cd ~/picar-x/example
       sudo nano secret.py

#. Füge den Schlüssel hinzu:

   .. code-block:: python

       # secret.py
       DEEPSEEK_API_KEY = "sk-xxx"

**Abrechnung aktivieren**

Lade ein kleines Guthaben auf (z. B. ¥10 RMB), bevor du die API nutzt.

   .. image:: img/llm_deepseek_chognzhi.png

**Verfügbare Modelle**

Stand: 2025-09-12 bietet DeepSeek folgende Modelle an:

* ``deepseek-chat``
* ``deepseek-reasoner``

**Mit Beispielcode testen**

#. Öffne die Testdatei:

   .. code-block:: bash

       cd ~/picar-x/example
       sudo nano 18.online_llm_test.py

#. Ersetze den Inhalt durch folgenden Code und aktualisiere ``model="xxx"`` (z. B. ``deepseek-chat``):

   .. code-block:: python

       from picarx.llm import Deepseek
       from secret import DEEPSEEK_API_KEY

       INSTRUCTIONS = "You are a helpful assistant."
       WELCOME = "Hello, I am a helpful assistant. How can I help you?"

       llm = Deepseek(
           api_key=DEEPSEEK_API_KEY,
           model="deepseek-chat",
           max_messages=20,
       )

#. Ausführen:

   .. code-block:: bash

       sudo python3 18.online_llm_test.py

----

Doubao
------------------

Doubao ist die KI-Modellplattform von ByteDance (Volcengine Ark).

**API-Schlüssel abrufen und speichern**

#. Melde dich bei |link_doubao| an.

#. Scrolle im linken Menü nach unten zu **API Key Management → Create API Key**.

   .. image:: img/llm_doubao_create.png

#. Gib einen Namen ein und klicke auf **Create**.

   .. image:: img/llm_doubao_name.png

#. Klicke auf das **Schlüssel-Symbol**, um den API-Schlüssel anzuzeigen, und kopiere ihn.

   .. image:: img/llm_doubao_copy.png

#. In deinem Projektordner:

   .. code-block:: bash

       cd ~/picar-x/example
       sudo nano secret.py

#. Füge den Schlüssel hinzu:

   .. code-block:: python

       # secret.py
       DOUBAO_API_KEY = "xxx"

**Ein Modell auswählen**

#. Gehe zum Modell-Marktplatz und wähle ein Modell aus.

   .. image:: img/llm_doubao_model_select.png

#. Wähle z. B. **Doubao-seed-1.6** und klicke auf **API 接入**.

   .. image:: img/llm_doubao_model.png

#. Wähle deinen API-Schlüssel und klicke auf **Use API**.

   .. image:: img/llm_doubao_use_api.png

#. Klicke auf **Enable Model**.

   .. image:: img/llm_doubao_kaitong.png

#. Fahre mit der Maus über die Modell-ID, um sie zu kopieren.

   .. image:: img/llm_doubao_copy_id.png

**Mit Beispielcode testen**

#. Öffne die Testdatei:

   .. code-block:: bash

       cd ~/picar-x/example
       sudo nano 18.online_llm_test.py

#. Ersetze den Inhalt durch folgenden Code und passe ``model="xxx"`` an (z. B. ``doubao-seed-1-6-250615``):

   .. code-block:: python

       from picarx.llm import Doubao
       from secret import DOUBAO_API_KEY

       INSTRUCTIONS = "You are a helpful assistant."
       WELCOME = "Hello, I am a helpful assistant. How can I help you?"

       llm = Doubao(
           api_key=DOUBAO_API_KEY,
           model="doubao-seed-1-6-250615",
       )

#. Ausführen:

   .. code-block:: bash

       sudo python3 18.online_llm_test.py


Allgemein
--------------

Dieses Projekt unterstützt die Verbindung zu mehreren LLM-Plattformen über eine einheitliche Schnittstelle.
Integrierte Unterstützung besteht für:

* **OpenAI** (ChatGPT / GPT-4o, GPT-4, GPT-3.5)
* **Gemini** (Google AI Studio / Vertex AI)
* **Grok** (xAI)
* **DeepSeek**
* **Qwen (通义千问)**
* **Doubao (豆包)**

Zusätzlich kannst du dich mit **jedem anderen LLM-Dienst verbinden, der das OpenAI-API-Format unterstützt**.
Dazu benötigst du lediglich einen **API-Schlüssel** und die passende **base_url**.

**API-Schlüssel abrufen und speichern**

#. Hole dir einen **API-Schlüssel** von der gewünschten Plattform (siehe jeweilige offizielle Dokumentation).

#. In deinem Projektordner, erstelle eine neue Datei:

   .. code-block:: bash

      cd ~/picar-x/example
      nano secret.py

#. Füge deinen Schlüssel in ``secret.py`` ein:

   .. code-block:: python

      # secret.py
      API_KEY = "your_api_key_here"

.. warning::

   Bewahre deinen API-Schlüssel sicher auf. Lade ``secret.py`` nicht in öffentliche Repositories hoch.

**Mit Beispielcode testen**

#. Öffne die Testdatei:

   .. code-block:: bash

      cd ~/picar-x/example
      sudo nano 18.online_llm_test.py

#. Ersetze den Inhalt durch folgenden Code und trage die korrekte ``base_url`` und ``model`` deines Anbieters ein:

   .. note::

      Zu ``base_url``:
      Unterstützt wird das **OpenAI API Format**, sowie alle APIs, die **kompatibel** damit sind.
      Jeder Anbieter hat seine eigene ``base_url`` — siehe Dokumentation.

   .. code-block:: python

      from picarx.llm import LLM
      from secret import API_KEY

      INSTRUCTIONS = "You are a helpful assistant."
      WELCOME = "Hello, I am a helpful assistant. How can I help you?"

      llm = LLM(
          base_url="https://api.example.com/v1",  # trage die base_url deines Anbieters ein
          api_key=API_KEY,
          model="your-model-name-here",           # wähle ein Modell von deinem Anbieter
      )

#. Programm ausführen:

   .. code-block:: bash

      python3 18.online_llm_test.py
