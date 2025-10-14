.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

2. Installation des Betriebssystems
============================================================


**Erforderliche Komponenten**

* Ein Personal Computer
* Eine Micro-SD-Karte und ein Kartenleser

1. Raspberry Pi Imager installieren
-----------------------------------------------

#. Besuchen Sie die Raspberry Pi Software-Downloadseite unter `Raspberry Pi Imager <https://www.raspberrypi.org/software/>`_. Wählen Sie die Imager-Version, die mit Ihrem Betriebssystem kompatibel ist. Laden Sie die Datei herunter und öffnen Sie sie, um die Installation zu starten.

    .. image:: img/os_install_imager.png
        :align: center

#. Während der Installation kann je nach Betriebssystem eine Sicherheitsmeldung erscheinen. Beispielsweise könnte Windows eine Warnmeldung anzeigen. In solchen Fällen wählen Sie **Weitere Informationen** und dann **Trotzdem ausführen**. Folgen Sie den Anweisungen auf dem Bildschirm, um die Installation des Raspberry Pi Imagers abzuschließen.

    .. image:: img/os_info.png
        :align: center

#. Starten Sie die Raspberry Pi Imager-Anwendung, indem Sie auf das Symbol klicken oder ``rpi-imager`` in Ihrem Terminal eingeben.

    .. image:: img/os_open_imager.png
        :align: center

2. OS auf Micro-SD-Karte installieren
------------------------------------------------

#. Setzen Sie Ihre SD-Karte mit einem Kartenleser in Ihren Computer oder Laptop ein.

#. Klicken Sie im Imager auf **Raspberry Pi Device** und wählen Sie das Raspberry Pi-Modell aus der Dropdown-Liste aus.

    .. image:: img/os_choose_device.png
        :align: center

#. Wählen Sie **Betriebssystem** und entscheiden Sie sich für die empfohlene Betriebssystemversion.

    .. image:: img/os_choose_os.png
        :align: center

#. Klicken Sie auf **Speicher wählen** und wählen Sie das entsprechende Speichergerät für die Installation aus.

    .. note::

        Stellen Sie sicher, dass Sie das richtige Speichergerät auswählen. Um Verwechslungen zu vermeiden, trennen Sie alle zusätzlichen Speichergeräte, falls mehrere angeschlossen sind.

    .. image:: img/os_choose_sd.png
        :align: center

#. Klicken Sie auf **NEXT** und dann auf **EINSTELLUNGEN BEARBEITEN**, um Ihre OS-Einstellungen anzupassen.

    .. note::

        Wenn Sie einen Monitor für Ihren Raspberry Pi haben, können Sie die nächsten Schritte überspringen und auf 'Ja' klicken, um die Installation zu starten. Passen Sie andere Einstellungen später am Monitor an.

    .. image:: img/os_enter_setting.png
        :align: center

#. Definieren Sie einen **Hostnamen** für Ihren Raspberry Pi.

    .. note::

        Der Hostname ist die Netzwerkkennung Ihres Raspberry Pi. Sie können auf Ihren Pi mit ``<hostname>.local`` oder ``<hostname>.lan`` zugreifen.

    .. image:: img/os_set_hostname.png
        :align: center

#. Erstellen Sie einen **Benutzernamen** und ein **Passwort** für das Administratorkonto des Raspberry Pi.

    .. note::

        Das Erstellen eines eindeutigen Benutzernamens und Passworts ist wichtig, um Ihren Raspberry Pi zu sichern, da kein Standardpasswort vorhanden ist.

    .. image:: img/os_set_username.png
        :align: center

#. Konfigurieren Sie das drahtlose LAN, indem Sie die **SSID** und das **Passwort** Ihres Netzwerks angeben.

    .. note::

        Stellen Sie das ``Land des drahtlosen LAN`` auf den zweistelligen `ISO/IEC alpha2 Code <https://de.wikipedia.org/wiki/ISO_3166-1_alpha-2#Offiziell_vergebene_code-Elemente>`_ ein, der Ihrem Standort entspricht.

    .. image:: img/os_set_wifi.png
        :align: center


#. Um sich remote mit Ihrem Raspberry Pi zu verbinden, aktivieren Sie SSH im Tab Dienste.

    * Für **Passwort-Authentifizierung** verwenden Sie den Benutzernamen und das Passwort aus dem Allgemeinen Tab.
    * Für Public-Key-Authentifizierung wählen Sie „Nur Public-Key-Authentifizierung zulassen“. Wenn Sie einen RSA-Schlüssel haben, wird dieser verwendet. Wenn nicht, klicken Sie auf „SSH-keygen ausführen“, um ein neues Schlüsselpaar zu generieren.

    .. image:: img/os_enable_ssh.png
        :align: center

#. Das **Optionen** Menü ermöglicht es Ihnen, das Verhalten des Imagers während des Schreibvorgangs zu konfigurieren, einschließlich des Abspielens eines Tons bei Fertigstellung, des Auswerfens des Mediums bei Fertigstellung und der Aktivierung von Telemetrie.

    .. image:: img/os_options.png
        :align: center

    
#. Wenn Sie die Eingabe der Betriebssystemanpassungseinstellungen abgeschlossen haben, klicken Sie auf **Speichern**, um Ihre Anpassung zu speichern. Klicken Sie dann auf **Ja**, um sie beim Schreiben des Images anzuwenden.

    .. image:: img/os_click_yes.png
        :align: center

#. Wenn sich auf der SD-Karte vorhandene Daten befinden, stellen Sie sicher, dass Sie diese sichern, um Datenverlust zu vermeiden. Fahren Sie fort, indem Sie auf **Ja** klicken, wenn keine Sicherung erforderlich ist.

    .. image:: img/os_continue.png
        :align: center

#. Wenn das Popup „Schreiben erfolgreich“ angezeigt wird, wurde Ihr Image vollständig geschrieben und verifiziert. Sie sind jetzt bereit, einen Raspberry Pi von der Micro-SD-Karte zu booten!

    .. image:: img/os_finish.png
        :align: center

#. Nun können Sie die mit Raspberry Pi OS eingerichtete SD-Karte in den microSD-Kartensteckplatz auf der Unterseite des Raspberry Pi einlegen.

    .. image:: img/os_sd_to_pi.jpg
        :width: 500
        :align: center
