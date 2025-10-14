.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!


.. _remote_desktop:

Remote-Desktop-Zugriff für Raspberry Pi
==================================================

Für alle, die eine grafische Benutzeroberfläche (GUI) dem Arbeiten über die Kommandozeile vorziehen, bietet der Raspberry Pi eine einfache Möglichkeit, per Remote Desktop zuzugreifen.  
In dieser Anleitung lernst du, wie du **VNC (Virtual Network Computing)** einrichtest und verwendest.

Wir empfehlen die Verwendung von `VNC® Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_.

**VNC-Dienst auf dem Raspberry Pi aktivieren**

Der VNC-Dienst ist in Raspberry Pi OS standardmäßig vorinstalliert, aber deaktiviert.  
So aktivierst du ihn:

#. Gib folgenden Befehl im Terminal deines Raspberry Pi ein:

    .. raw:: html

        <run></run>

    .. code-block::

        sudo raspi-config

#. Navigiere mit der Pfeiltaste nach unten zu **Interfacing Options** und drücke **Enter**.

    .. image:: img/config_interface.png
        :align: center

#. Wähle **VNC** aus den Optionen.

    .. image:: img/vnc.png
        :align: center

#. Wähle **<Yes>** → **<OK>** → **<Finish>**, um den VNC-Dienst zu aktivieren.

    .. image:: img/vnc_yes.png
        :align: center

**Anmeldung über VNC Viewer**

#. Lade `VNC Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ auf deinem Computer herunter und installiere es.

#. Starte den VNC Viewer. Gib den Hostnamen oder die IP-Adresse deines Raspberry Pi ein und drücke Enter.

    .. image:: img/vnc_viewer1.png
        :align: center

#. Gib deinen Raspberry-Pi-Benutzernamen und dein Passwort ein und klicke auf **OK**.

    .. image:: img/vnc_viewer2.png
        :align: center

#. Nach einigen Sekunden erscheint der Desktop des Raspberry Pi OS.  
   Jetzt kannst du z. B. das Terminal öffnen und Befehle eingeben.

    .. image:: img/bookwarm.png
        :align: center
