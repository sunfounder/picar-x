.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

Betriebssystem Installieren
==================================

**Benötigte Komponenten**

* Raspberry Pi 4B/Zero 2 W/3B 3B+/2B/Zero W
* 1 x Personal Computer
* 1 x Micro SD-Karte

**Schritte**


#. Besuchen Sie die Download-Seite der Raspberry Pi-Software: `Raspberry Pi Imager <https://www.raspberrypi.org/software/>`_. Wählen Sie die Imager-Version für Ihr Betriebssystem aus. Nach dem Herunterladen öffnen Sie die Datei, um die Installation zu starten.

    .. image:: img/os_install_imager.png


#. Nach dem Start des Installationsprogramms zeigt Ihr Betriebssystem möglicherweise eine Sicherheitswarnung an. Beispielsweise könnte Windows eine Warnmeldung anzeigen. Wenn dies der Fall ist, wählen Sie **More info** und dann **Run anyway**. Folgen Sie den Anweisungen auf dem Bildschirm, um den Raspberry Pi Imager zu installieren.

    .. image:: img/os_info.png


#. Legen Sie Ihre SD-Karte in den SD-Kartenslot Ihres Computers oder Laptops ein.

#. Öffnen Sie die Raspberry Pi Imager-Anwendung entweder durch Klicken auf das Symbol oder durch Ausführen von ``rpi-imager`` in Ihrem Terminal.

    .. image:: img/os_open_imager.png

#. Klicken Sie auf **CHOOSE DEVICE** und wählen Sie Ihr spezifisches Raspberry Pi-Modell aus der Liste aus (Hinweis: Raspberry Pi 5 ist nicht anwendbar).

    .. image:: img/os_choose_device.png

#. Wählen Sie **CHOOSE OS** und dann **Raspberry Pi OS (Legacy)**.

    .. warning::
        * Bitte installieren Sie nicht die **Bookworm**-Version, da die Lautsprecher nicht funktionieren werden.
        * Sie müssen die Version **Raspberry Pi OS (Legacy)** - **Debian Bullseye** installieren.

    .. image:: img/os_choose_os.png


#. Klicken Sie auf **Choose Storage** und wählen Sie das richtige Speichergerät für die Installation aus.

    .. note::

        Stellen Sie sicher, dass Sie das richtige Gerät auswählen, insbesondere wenn mehrere Speichergeräte angeschlossen sind. Trennen Sie andere Geräte, wenn Sie sich nicht sicher sind.

    .. image:: img/os_choose_sd.png

#. Drücken Sie **NEXT** und wählen Sie **EDIT SETTINGS**, um Ihre Betriebssystemeinstellungen anzupassen.

    .. image:: img/os_enter_setting.png

#. Legen Sie den **hostname** Ihres Raspberry Pi fest.

    .. note::

        Der Hostname ist der Name, mit dem sich Ihr Raspberry Pi im Netzwerk identifiziert. Sie können sich mit `<hostname>.local` oder `<hostname>.lan` mit Ihrem Pi verbinden.

    .. image:: img/os_set_hostname.png

#. Erstellen Sie einen **Username** und ein **Password** für das Administratorkonto des Raspberry Pi.

    .. note::

        Das Festlegen eines einzigartigen Benutzernamens und Passworts ist aus Sicherheitsgründen wichtig, da der Raspberry Pi kein Standardpasswort hat.

    .. image:: img/os_set_username.png

#. Richten Sie das drahtlose LAN ein, indem Sie den **SSID** und das **Password** Ihres Netzwerks eingeben.

    .. note::

        ``Wireless LAN-Land`` sollte auf den zweistelligen `ISO/IEC Alpha2-Code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ für das Land eingestellt werden, in dem Sie Ihren Raspberry Pi verwenden.

    .. image:: img/os_set_wifi.png


#. Klicken Sie auf **SERVICES** und aktivieren Sie **SSH** für den passwortbasierten Fernzugriff. Denken Sie daran, auf **Save** zu klicken.

    .. image:: img/os_enable_ssh.png

#. Bestätigen Sie Ihre Auswahl, indem Sie auf **Yes** klicken.

    .. image:: img/os_click_yes.png

#. Sichern Sie vorhandene Dateien auf Ihrer SD-Karte, um Datenverlust zu vermeiden. Klicken Sie auf **Yes**, um fortzufahren, wenn keine Sicherung erforderlich ist.

    .. image:: img/os_continue.png

#. Warten Sie, während das Betriebssystem auf die SD-Karte geschrieben wird. Nach Abschluss erscheint ein Bestätigungsfenster.

    .. image:: img/os_finish.png
        :align: center
