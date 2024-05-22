.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

Richten Sie Ihren Raspberry Pi Ein
======================================
Stromversorgung für den Raspberry Pi (Wichtig)
--------------------------------------------------

#. Setzen Sie die mit dem Raspberry Pi OS eingerichtete SD-Karte in den Micro-SD-Kartensteckplatz auf der Unterseite des Raspberry Pi ein.

    .. image:: img/insert_sd_card.png
        :width: 500
        :align: center

#. Befolgen Sie die Montageanleitung, stecken Sie das Batteriekabel ein und schalten Sie den Stromschalter ein. Anschließend stecken Sie das USB-C-Kabel ein, um die Batterie aufzuladen. Warten Sie 1-2 Minuten, und Sie werden ein Geräusch hören, das anzeigt, dass der Raspberry Pi erfolgreich gestartet ist.

    .. image:: img/Z_BTR.JPG
        :width: 800
        :align: center

    .. note::

        Es wird empfohlen, das USB-C-Kabel eingesteckt zu lassen, da der nachfolgende Software-Einrichtungsprozess eine erhebliche Zeit in Anspruch nehmen kann.


Wenn Sie Einen Bildschirm Haben
------------------------------------

.. note:: Der auf dem Roboter installierte Raspberry Pi ZERO lässt sich nicht leicht mit dem Bildschirm verbinden, bitte verwenden Sie die Methode ohne Bildschirm, um ihn einzurichten.


Wenn Sie einen Bildschirm haben, wird es für Sie einfacher sein, am
Raspberry Pi zu arbeiten.

**Benötigte Komponenten**

* Raspberry Pi 4B/3B 3B+/2B
* 1 * Netzteil
* 1 * Micro-SD-Karte
* 1 * Bildschirm-Netzteil
* 1 * HDMI-Kabel
* 1 * Bildschirm
* 1 * Maus
* 1 * Tastatur

#. Schließen Sie die Maus und die Tastatur an.

#. Verbinden Sie den Bildschirm mit dem HDMI-Port des Raspberry Pi und stellen Sie sicher, dass Ihr Bildschirm an eine Steckdose angeschlossen und eingeschaltet ist.

    .. note::

        Wenn Sie einen Raspberry Pi 4 verwenden, müssen Sie den Bildschirm mit dem HDMI0-Anschluss (am nächsten zum Stromanschluss) verbinden.

#. Verwenden Sie das Netzteil, um den Raspberry Pi mit Strom zu versorgen. Nach einigen Sekunden wird der Raspberry Pi OS-Desktop angezeigt.

    .. image:: img/image20.png
        :align: center

Wenn Sie Keinen Bildschirm Haben
------------------------------------

Wenn Sie keinen Monitor haben, können Sie sich remote in Ihren Raspberry Pi einloggen.

**Benötigte Komponenten**

* * Raspberry Pi 4B/Zero 2 W/3B 3B+/2B/Zero W  
* 1 * Netzteil
* 1 * Micro-SD-Karte

Sie können den SSH-Befehl anwenden, um die Bash-Shell des Raspberry Pi zu öffnen. Bash ist die Standard-Standard-Shell für Linux. Die Shell selbst ist ein Befehl (Anweisung), wenn der Benutzer Unix/Linux verwendet. Das meiste, was Sie tun müssen, kann über die Shell erledigt werden.

Wenn Sie mit der Verwendung des Befehlsfensters für den Zugriff auf Ihren Raspberry Pi nicht zufrieden sind, können Sie auch die Funktion "Remote-Desktop" verwenden, um Dateien auf Ihrem Raspberry Pi einfach über eine grafische Benutzeroberfläche (GUI) zu verwalten.

Siehe unten für detaillierte Tutorials für jedes System.

.. toctree::

    remote_macosx
    remote_windows
    remote_linux

