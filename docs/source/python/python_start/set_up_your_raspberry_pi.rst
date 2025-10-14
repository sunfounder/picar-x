.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

4. Richte deinen Raspberry Pi ein
========================================

Um mit der Programmierung und Steuerung deines PiCar-X zu beginnen, musst du zuerst auf deinen Raspberry Pi zugreifen.  
In diesem Abschnitt lernst du zwei gängige Methoden kennen:  
die Verwendung eines Monitors mit Tastatur und Maus oder die Einrichtung einer **Headless-Verbindung** (ohne Bildschirm), um dich **remote von einem anderen Computer** einzuloggen.

Wenn du einen Bildschirm hast
------------------------------

.. note:: Der auf dem Roboter installierte Raspberry Pi Zero 2W ist schwer an einen Bildschirm anzuschließen.  
Wir empfehlen die **Headless-Methode (ohne Bildschirm)**.

**Benötigte Komponenten**

* Raspberry Pi  
* Netzteil  
* Micro-SD-Karte  
* HDMI-Kabel  
* Bildschirm  
* Maus  
* Tastatur

#. Setze die Micro-SD-Karte in deinen Raspberry Pi ein.  
#. Schließe Maus, Tastatur und Bildschirm an (bei Pi 4/5 **HDMI0** verwenden – den Anschluss neben dem Stromanschluss).  
#. Schalte den Raspberry Pi ein.  
#. Nach kurzer Zeit erscheint der Raspberry Pi OS Desktop und du kannst ein Terminal öffnen, um Befehle einzugeben.

    .. image:: img/bookwarm.png
        :align: center


Wenn du keinen Bildschirm hast (Headless Setup)
-----------------------------------------------

Ohne Monitor kannst du deinen Raspberry Pi **fern konfigurieren und einloggen**.  
Dies ist die bequemste Methode für den Einstieg.

**Benötigte Komponenten**

* Raspberry Pi  
* Netzteil  
* Micro-SD-Karte  
* Ein Computer im selben Netzwerk

**Tipps**

* Stelle das **WLAN-Land** korrekt ein (ISO/IEC Alpha-2-Code, z. B. ``US``, ``UK``, ``CN``); sonst funktioniert WLAN nicht.  
* Achte darauf, dass dein Raspberry Pi und dein Computer im **gleichen lokalen Netzwerk** sind.  
* Für eine stabilere Verbindung verwende, wenn möglich, **ein Netzwerkkabel (Ethernet)**.

**Verbindung über SSH herstellen**

1. Öffne auf deinem Computer ein Terminal (Windows: **PowerShell**, macOS/Linux: **Terminal**) und gib ein:

   .. code-block::

      ssh <Benutzername>@<Hostname>.local
      # Beispiel:
      ssh daisy@picarx.local

2. Alternativ kannst du im DHCP-/Client-Register deines Routers die IP-Adresse des Pi finden und dich so verbinden:

   .. code-block::

      ssh <Benutzername>@<IP>
      
      # Beispiel:
      ssh daisy@192.xxx.xx.xx

3. Beim ersten Login erscheint eine Sicherheitsabfrage. Gib ``yes`` ein, um fortzufahren.

4. Gib das Passwort ein, das du im Raspberry Pi Imager festgelegt hast. (Die Zeichen werden beim Tippen **nicht angezeigt** – das ist normal.)

   .. note::
      Dass beim Passwort keine Zeichen angezeigt werden, ist ein Sicherheitsstandard. Tippe einfach sorgfältig.

5. Sobald du verbunden bist, ist dein Raspberry Pi bereit für Remote-Zugriff.

   .. image:: img/ssh_login.png
      :align: center

**Fehlerbehebung**

* **ssh: Could not resolve hostname ...**  
  * Überprüfe, ob der Hostname korrekt ist.  
  * Falls es nicht funktioniert, verwende die IP-Adresse anstelle von ``<hostname>.local``.

* **The term 'ssh' is not recognized... (Windows)**  
  * OpenSSH ist nicht installiert. Installiere es manuell (siehe :ref:`openssh_powershell`) oder verwende einen SSH-Client (siehe :ref:`login_windows`).

* **Permission denied (publickey,password)**  
  * Achte darauf, dass du den richtigen Benutzernamen und das Passwort aus dem Raspberry Pi Imager verwendest.

* **Connection refused**  
  * Warte 1–2 Minuten nach dem Einschalten.  
  * Stelle sicher, dass SSH im Raspberry Pi Imager aktiviert wurde.

**Optionen für grafischen Zugriff**

Wenn du lieber eine grafische Oberfläche als die Kommandozeile verwendest, hast du zwei Möglichkeiten:

    .. image:: img/bookwarm.png
        :align: center

* :ref:`remote_desktop`: Aktiviere **VNC (Virtual Network Computing)**, um den vollständigen Desktop des Pi anzuzeigen.  
* |link_rpi_connect|: Verwende **Raspberry Pi Connect**, um sicher und überall direkt im Browser auf deinen Pi zuzugreifen.

Jetzt kannst du deinen Raspberry Pi **ohne Monitor** steuern –  
entweder über **SSH** für Kommandozeilenoperationen oder über **VNC / Raspberry Pi Connect** für eine grafische Desktop-Erfahrung.
