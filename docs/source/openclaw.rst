.. _picarx_skill:

.. start_using_picarx

22. PiCar-X mit OpenClaw steuern
====================================


**Was ist OpenClaw?**

Stellen Sie es sich als eine erweiterte Version von ChatGPT vor. Während herkömmliche Chatbots nur sprechen (Text generieren) können, kann OpenClaw handeln. Es versteht Ihre Anweisungen in natürlicher Sprache und kann tatsächlich Operationen auf Ihrem Computer ausführen, wie z. B. Befehle ausführen, Dateien verwalten und verschiedene Werkzeuge aufrufen.

Hier sind einige fantastische Anwendungsszenarien:

* **Persönlicher Allround-Assistent:** Lassen Sie es Ihnen helfen, Ihren Zeitplan zu verwalten, Erinnerungen zu setzen und Aufgaben zu verfolgen. Sie müssen es nur in einer Chat-App (wie Telegram, WhatsApp) mitteilen, und es wird sich daran erinnern und es ausführen.
* **Automatisierungs-"Kleber":** Es kann als Bindeglied für Ihre verschiedenen Dienste fungieren. Sie können es beispielsweise eine Website auf Preisänderungen überwachen lassen. Sobald ein Preisverfall erkannt wird, kann es automatisch einen n8n-Automatisierungsworkflow auslösen, um Ihnen eine E-Mail-Benachrichtigung zu senden.
* **Dedizierter Entwicklungsassistent:** Lassen Sie es Ihnen bei der Verwaltung von Servern, der Ausführung von Skripten und der Überprüfung von Protokollen helfen. Sie können einfach sagen: "Überprüfe die Systemauslastung für mich", und es kann sich per SSH in Ihren Server einloggen, den Befehl ausführen und die Ergebnisse zurückgeben.
* **Hardware-"Spielkamerad":** Dies ist ein sehr interessanter Anwendungsfall. Sie können OpenClaw Hardware steuern lassen, die an einen Raspberry Pi angeschlossen ist. Zum Beispiel hat ein Entwickler es verwendet, um einen Roboter-Staubsauger mit einem mechanischen Arm zu steuern, oder es sogar Rennsimulator-Daten analysieren und auf einem LED-Bildschirm anzeigen lassen. Das offizielle Raspberry Pi-Team hat es sogar verwendet, um eine automatische Fotokabine für eine Hochzeit zu bauen, nur durch Konversation, ohne eine einzige Zeile Code zu schreiben!


.. important::

   Der Raspberry Pi Zero 2W hat nur 512 MB RAM, während OpenClaw mindestens 1 GB benötigt. Daher kann er nicht ordnungsgemäß ausgeführt werden. Ein Raspberry Pi 4/5 oder höher wird empfohlen.

OpenClaw Schnellstart
------------------------------

Wenn Sie die Leistungsfähigkeit von OpenClaw so schnell wie möglich erleben möchten, verwenden Sie diese Methode. Sie installiert automatisch und startet einen interaktiven Einrichtungsassistenten.

1.  Öffnen Sie das Terminal auf Ihrem Raspberry Pi und führen Sie den folgenden Befehl direkt aus. Dieser Befehl lädt das Installationsskript von der offiziellen Website herunter und führt es aus:

    .. code-block:: bash

       curl -fsSL https://openclaw.ai/install.sh | bash

    .. note:: Da neue Versionen schnell aktualisiert werden, ist es normal, wenn Ihre Installationsschritte leicht abweichen.

2.  Das Skript wird OpenClaw automatisch herunterladen und installieren.

    .. image:: /img/openclaw/install_open_claw.png


3.  Sie sehen dann eine Sicherheitsabfrage, ob Sie OpenClaw vertrauen. Sobald Sie sicher sind, dass es sicher und zuverlässig ist, navigieren Sie mit den Pfeiltasten zu "Yes" und drücken Sie Enter.

    .. image:: /img/openclaw/security_open_claw.png


4.  Wählen Sie Quick Start und drücken Sie dann Enter.

    .. image:: /img/openclaw/quickstart_open_claw.png

5.  Wählen Sie Ihr Modell und drücken Sie dann Enter. Hier verwenden wir OpenAI als Beispiel.

    .. image:: /img/openclaw/model_provider_open_claw.png

6.  Wählen Sie OpenAI API Key.

    .. image:: /img/openclaw/api_key_open_claw.png

7.  Fügen Sie jetzt den API-Schlüssel ein.

    .. image:: /img/openclaw/paste_api_key_open_claw.png

8.  Gehen Sie zu |link_openai_platform| und melden Sie sich an. Klicken Sie auf der Seite **API keys** auf **Create new secret key**.

    .. image:: /img/openclaw/llm_openai_create.png

9.  Geben Sie die Details ein (Owner, Name, Project und Berechtigungen falls nötig) und klicken Sie dann auf **Create secret key**.

    .. image:: /img/openclaw/llm_openai_create_confirm.png

10. Sobald der Schlüssel erstellt ist, kopieren Sie ihn sofort — Sie können ihn später nicht mehr einsehen. Wenn Sie ihn verlieren, müssen Sie einen neuen erstellen.

    .. image:: /img/openclaw/llm_openai_copy.png

11. Fügen Sie den Schlüssel in die OpenClaw-Konfiguration ein.

    .. image:: /img/openclaw/paste_api_key_enter_open_claw.png

12. Wählen Sie das Modell, das Sie verwenden möchten. In diesem Beispiel verwenden wir **Keep current**.

    .. image:: /img/openclaw/model_config_open_claw.png

13. Als nächstes kommt die Kanalauswahl. Kanäle beziehen sich auf die von OpenClaw unterstützten Kommunikationsdienste wie Telegram, WhatsApp, Discord und mehr. Verwenden Sie die Pfeiltaste nach unten, um die Option "Skip for now" auszuwählen, und drücken Sie dann Enter.

    .. image:: /img/openclaw/channel_open_claw.png

14. Als nächstes werden Sie aufgefordert, Skills sofort zu konfigurieren. Wählen Sie "Yes" und drücken Sie Enter.

    .. image:: /img/openclaw/config_skill_open_claw.png

15. Installieren Sie die Skills, die Sie benötigen. Im folgenden Beispiel wählen wir die Option "Skip for now" (drücken Sie die Leertaste zum Auswählen) und drücken dann Enter.

    .. image:: /img/openclaw/install_skill_open_claw.png


16. Als nächstes kommen Hooks; wir werden "command-logger" und "session-memory" auswählen.

    .. image:: /img/openclaw/hooks2_open_claw.png


17. Die Installation ist nun abgeschlossen. Sie können OpenClaw starten, indem Sie "Hatch in TUI" auswählen und Enter drücken.

   .. image:: /img/openclaw/hatch_open_claw.png


.. note::

   Sie können OpenClaw starten, indem Sie den folgenden Befehl eingeben:

    .. code-block:: bash

       openclaw tui

   Und Sie können Strg+C zweimal drücken, um die TUI-Oberfläche zu verlassen.

------------------------------------------------------------------------

OpenClaw den PiCar-X bedienen lassen
----------------------------------------------

**Was ist PiCar-X Skill?**

PiCar-X Skill ist eine Erweiterung für OpenClaw, mit der Sie Ihren SunFounder PiCar-X Roboterwagen über natürliche Sprache steuern können. Anstatt Python-Skripte zu schreiben oder Servowinkel zu merken, können Sie OpenClaw einfach sagen, was Sie mit dem PiCar-X tun möchten — wie "vorwärts fahren", "überprüfe, was voraus ist" oder "links abbiegen" — und OpenClaw führt automatisch den entsprechenden Python-Code aus.

Hier sind einige Dinge, die Sie mit PiCar-X Skill tun können:

* **Fahren:** Vorwärts, rückwärts fahren, links/rechts mit Lenkservosteuerung abbiegen
* **Kamera-Gimbal:** Horizontal schwenken, vertikal neigen über das 2-Achsen-Kamera-Gimbal
* **Sensoren:** Ultraschall-Abstand messen, Graustufensensor-Daten für Linienverfolgung und Klippenerkennung auslesen
* **Sound:** Soundeffekte und Musik über den Lautsprecher des Wagens abspielen
* **Kamera-Vision:** Fotos aufnehmen, Gesichter erkennen, Farben verfolgen, QR-Codes, Gesten und Verkehrszeichen erkennen

----------------------------------------------------------------

Voraussetzungen
------------------------------

Bevor Sie PiCar-X Skill mit OpenClaw verwenden können, stellen Sie Folgendes sicher:

1. **PiCar-X** ist ordnungsgemäß zusammengebaut und mit Ihrem Raspberry Pi verbunden
2. **OpenClaw** ist installiert und läuft
3. Die folgenden Python-Bibliotheken sind installiert:

   - ``picarx``
   - ``robot_hat``
   - ``vilib``

Sie können die Installation mit folgendem Befehl überprüfen:

.. code-block:: bash

   python3 -c "import picarx"

Wenn dieser Befehl ohne Fehler ausgeführt wird, können Sie fortfahren.

----------------------------------------------------------------

PiCar-X Skill installieren
------------------------------

Befolgen Sie diese Schritte, um den PiCar-X Skill für OpenClaw zu installieren:

1. **Kopieren Sie die PiCar-X Skill-Dateien** in das OpenClaw Skills-Verzeichnis:

   .. code-block:: bash

      cp -r ~/picar-x/picarx-control ~/.openclaw/workspace/skills/

2. **Überprüfen Sie die Installation**, indem Sie die Skill-Dateien auflisten:

   .. code-block:: bash

      ls ~/.openclaw/workspace/skills/picarx-control/

   Sie sollten ``SKILL.md``, ``install.sh``, ``scripts/`` und ``references/`` in der Ausgabe sehen.

Die ``SKILL.md``-Datei des Skills enthält alle Anweisungen, die OpenClaw benötigt — Sicherheitsregeln, Codevorlagen für jede Fähigkeit und eine Zuordnung von natürlicher Sprache zu Python-Code. OpenClaw liest diese Datei und verwendet sie, um zu entscheiden, welcher Code auf Ihrem PiCar-X ausgeführt werden soll.

----------------------------------------------------------------

PiCar-X Skill über die CLI testen
----------------------------------------------

Bevor Sie den Skill mit OpenClaw verwenden, möchten Sie möglicherweise die grundlegende Funktionalität direkt vom Terminal aus mit dem enthaltenen CLI-Tool testen.

**Ultraschall-Abstand prüfen:**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/picarx-control/scripts/pc.py sensor distance

**Vorwärts fahren:**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/picarx-control/scripts/pc.py move forward --speed 60

**Rückwärts fahren:**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/picarx-control/scripts/pc.py move backward --speed 60

**Links abbiegen:**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/picarx-control/scripts/pc.py turn left --angle 30

**Rechts abbiegen:**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/picarx-control/scripts/pc.py turn right --angle 30

**Kamera horizontal schwenken:**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/picarx-control/scripts/pc.py cam pan --angle 30

**Kamera vertikal neigen:**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/picarx-control/scripts/pc.py cam tilt --angle 20

**Soundeffekt abspielen:**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/picarx-control/scripts/pc.py sound play /path/to/sound.wav --volume 80

**Graustufensensor-Daten auslesen (Linienverfolgung):**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/picarx-control/scripts/pc.py sensor grayscale

**Servo-Kalibrierung ausführen:**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/picarx-control/scripts/pc.py calibrate

----------------------------------------------------------------

PiCar-X Skill in OpenClaw verwenden
----------------------------------------------------

Sobald Sie überprüft haben, dass PiCar-X Skill über die Kommandozeile funktioniert, können Sie ihn innerhalb von OpenClaw verwenden.

1. **OpenClaw TUI starten**:

   .. code-block:: bash

      openclaw tui

2. **Senden Sie Befehle in natürlicher Sprache**, um den PiCar-X zu steuern. Hier sind einige Beispiele:

   * "Fahre vorwärts"
   * "Fahre rückwärts"
   * "Biege links ab"
   * "Biege rechts ab"
   * "Prüfe, ob etwas voraus ist"
   * "Schaue nach links"
   * "Schaue nach oben"
   * "Schaue nach unten"
   * "Mache ein Foto"
   * "Erkenne Gesichter"
   * "Finde die Farbe Rot"
   * "Folge der Linie"
   * "Prüfe, ob eine Klippe voraus ist"

3. **OpenClaw übersetzt automatisch** Ihre Anfrage in den entsprechenden Python-Code und führt ihn auf dem PiCar-X aus.

----------------------------------------------------------------

Verfügbare Aktionen und Befehle
-------------------------------------------

Hier ist die vollständige Liste der von PiCar-X Skill unterstützten Funktionen:

Fahren (``pc.py move``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Aktion
     - Beschreibung
   * - ``forward``
     - Vorwärts fahren
   * - ``backward``
     - Rückwärts fahren

Lenkung (``pc.py turn``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Aktion
     - Beschreibung
   * - ``left``
     - Links abbiegen durch Anpassung des Lenkwinkels
   * - ``right``
     - Rechts abbiegen durch Anpassung des Lenkwinkels

Kamera-Gimbal (``pc.py cam``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Funktion
     - Beschreibung
   * - Kamera schwenken
     - Kamera horizontal drehen (-90° bis 90°)
   * - Kamera neigen
     - Kamera vertikal neigen (-35° bis 65°)

Sensoren
^^^^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Befehl
     - Beschreibung
   * - ``sensor distance``
     - Ultraschall-Abstandssensor auslesen (gibt cm zurück)
   * - ``sensor grayscale``
     - 3-Kanal-Graustufenmodul-Werte auslesen (für Linienverfolgung & Klippenerkennung)

Sound (``pc.py sound``)
^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Befehl
     - Beschreibung
   * - ``sound play <datei>``
     - Eine Soundeffekt-Datei abspielen
   * - ``sound music <datei>``
     - Hintergrundmusik abspielen
   * - ``sound volume <0-100>``
     - Lautsprecherlautstärke einstellen
   * - ``sound stop``
     - Wiedergabe stoppen

.. note::

   Die Sounddateien können beliebige ``.wav``-Audiodateien sein, die auf Ihrem Raspberry Pi zugänglich sind. Sie können ``sound music`` auch verwenden, um Hintergrundmusik-Dateien abzuspielen.

Kamera & Vision (über natürliche Sprache / exec)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Funktion
     - Beschreibung
   * - Foto aufnehmen
     - Ein Foto aufnehmen und unter ``~/Pictures/`` speichern
   * - Gesichtserkennung
     - Menschliche Gesichter erkennen und Position melden
   * - Farberkennung
     - Objekte nach Farbe lokalisieren (Rot, Blau, Grün usw.)
   * - Gestenerkennung
     - Schere/Stein/Papier-Gesten erkennen
   * - Verkehrszeichenerkennung
     - Stopp/Links/Rechts/Vorwärts-Schilder erkennen
   * - QR-Code-Scanning
     - QR-Code-Daten und -Position auslesen

Linienverfolgung & Klippenerkennung
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Funktion
     - Beschreibung
   * - Linienverfolgung
     - Einer schwarzen Linie auf hellem Untergrund mit 3-Kanal-Graustufen folgen
   * - Klippenerkennung
     - Kanten/Abgründe mittels Graustufen-Schwellenwerten erkennen

----------------------------------------------------------------

Fehlerbehebung
------------------------------

OpenClaw Probleme
^^^^^^^^^^^^^^^^^^^^^^^^

F. Während der Installation erhalte ich den Fehler ``Error: systemctl is-enabled unavailable: Command failed: systemctl --user is-enabled openclaw-gateway.service``. Was soll ich tun?

   Sie können dies vorerst ignorieren, aber in den nächsten Schritten könnten Probleme auftreten. Bitte beziehen Sie sich dann einzeln darauf.


F. Wenn ich ``openclaw tui`` ausführe, erhalte ich den Fehler ``-bash: openclaw: command not found``. Was soll ich tun?

   Führen Sie den folgenden Befehl aus:

   .. code-block:: bash

      echo 'export PATH="$HOME/.npm-global/bin:$PATH"' >> ~/.bashrc
      source ~/.bashrc

   Sie sollten nun die TUI-Oberfläche mit ``openclaw tui`` starten können.



F. In ``openclaw tui`` sehe ich ``not connected to gateway — message not sent`` oder die Meldung ``gateway disconnected: closed``.

   Dies liegt daran, dass Ihr OpenClaw Gateway-Dienst nicht gestartet ist. Öffnen Sie ein weiteres Terminal und führen Sie den folgenden Befehl aus, um das OpenClaw Gateway zu starten:

   .. code-block:: bash

      openclaw gateway

   Starten Sie dann ``openclaw tui`` neu, und Sie können es direkt verwenden.


F. Ich möchte den OpenClaw Gateway-Dienst so einrichten, dass er im Hintergrund läuft / automatisch beim Booten startet. Wie mache ich das?

   Normalerweise sollte Ihr OpenClaw Gateway-Dienst beim Booten automatisch starten. Wenn nicht, können Sie ihn mit dem folgenden Befehl manuell starten.

   1. Erstellen Sie das Verzeichnis ``~/.config/systemd/user``:

   .. code-block:: bash

      mkdir -p ~/.config/systemd/user


   2. Erstellen Sie die Datei ``openclaw-gateway.service``:

   .. code-block:: bash

      cat > ~/.config/systemd/user/openclaw-gateway.service << EOF
      [Unit]
      Description=OpenClaw Gateway
      After=network.target

      [Service]
      Type=simple
      ExecStart=$HOME/.npm-global/bin/openclaw gateway run
      Restart=on-failure
      RestartSec=10
      Environment="PATH=$HOME/.npm-global/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin"
      Environment="NODE_ENV=production"

      [Install]
      WantedBy=default.target
      EOF


   3. Laden Sie dann die systemd-Konfiguration neu:

   .. code-block:: bash

      systemctl --user daemon-reload

   4. Starten Sie den Dienst:

   .. code-block:: bash

      systemctl --user start openclaw-gateway

   Starten Sie an dieser Stelle ``openclaw tui`` neu, und Sie können es direkt verwenden.

   5. Aktivieren Sie es für den automatischen Start beim Booten:

   .. code-block:: bash

      systemctl --user enable openclaw-gateway


F. Mein OpenClaw kann das System nicht bedienen, was soll ich tun?

   Ein neu installiertes OpenClaw hat möglicherweise standardmäßig keine Berechtigung, Ihr Raspberry Pi-System zu bedienen; es kann nur chatten. Wir müssen die Berechtigungen manuell konfigurieren.

   1.  Öffnen Sie die OpenClaw-Konfigurationsdatei:

      .. code-block:: bash

         nano ~/.openclaw/openclaw.json

   2.  Suchen Sie die ``tools``-Option und ändern Sie ``profile`` und ``exec`` wie gezeigt.

      .. code-block:: json

        "tools": {
            "profile": "coding",
            "exec": {
                "secrity": "full"
            }
        },

   3.  Speichern und beenden.

   4.  Geben Sie den folgenden Befehl im Terminal ein, um das OpenClaw Gateway neu zu starten:

      .. code-block:: bash

         openclaw gateway restart

   Jetzt sollte OpenClaw Lese- und Schreibberechtigungen haben und in der Lage sein, Ihr Raspberry Pi-System zu bedienen.

PiCar-X Probleme
^^^^^^^^^^^^^^^^^^^^^^^^


F. PiCar-X reagiert nicht auf Befehle. Was soll ich tun?

   Überprüfen Sie zunächst, ob der PiCar-X ordnungsgemäß angeschlossen und eingeschaltet ist. Testen Sie dann die grundlegende Funktionalität:

   .. code-block:: bash

      python3 ~/.openclaw/workspace/skills/picarx-control/scripts/pc.py sensor distance

   Wenn dies fehlschlägt, stellen Sie sicher, dass die erforderlichen Python-Bibliotheken installiert sind:

   .. code-block:: bash

      python3 -c "import picarx; import robot_hat; import vilib"

F. Der ``import picarx``-Test schlägt fehl.

   Dies bedeutet, dass die PiCar-X Python-Bibliothek nicht ordnungsgemäß installiert ist. Bitte beziehen Sie sich auf die offizielle PiCar-X-Installationsanleitung, um die erforderlichen Bibliotheken zu installieren. Sie können auch das enthaltene Installationsskript ausführen:

   .. code-block:: bash

      bash ~/.openclaw/workspace/skills/picarx-control/install.sh

F. OpenClaw erkennt den PiCar-X Skill nicht.

   Erinnern Sie OpenClaw daran, die Skills zu synchronisieren, indem Sie in der TUI sagen: *"Please rsync my skills"* oder starten Sie das OpenClaw Gateway neu:

   .. code-block:: bash

      openclaw gateway restart

F. PiCar-X-Bewegungen scheinen ruckartig zu sein oder die Lenkung ist außermittig.

   Dies wird normalerweise durch falsche Servo-Kalibrierungswerte verursacht. Führen Sie das Kalibrierungsskript aus, um den Lenkservo und das Kamera-Gimbal anzupassen:

   .. code-block:: bash

      python3 ~/.openclaw/workspace/skills/picarx-control/scripts/pc.py calibrate

   Sie können auch den Geschwindigkeitsparameter anpassen (z. B. ``--speed 40`` für sanftere Bewegungen verwenden) oder kurze Pausen zwischen aufeinanderfolgenden Befehlen einfügen.

F. Die Graustufenerkennung oder Linienverfolgung funktioniert nicht richtig.

   Stellen Sie sicher, dass das Graustufenmodul ordnungsgemäß für Ihre Oberfläche kalibriert ist. Sie können die Linienreferenzwerte über die Konfiguration einstellen. Beziehen Sie sich auf die Hauptdokumentation des PiCar-X für die Graustufen-Kalibrierungsverfahren.

----------------------------------------------------------------

.. end_using_picarx
