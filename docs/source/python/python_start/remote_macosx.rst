
Mac OS X Benutzer
==========================

Für Mac-Nutzer ist der direkte Zugriff auf den Raspberry Pi Desktop über VNC bequemer als über die Befehlszeile. Sie können darauf über den Finder zugreifen, indem Sie das festgelegte Kontopasswort eingeben, nachdem Sie VNC auf der Raspberry Pi-Seite aktiviert haben.

Beachten Sie, dass diese Methode die Kommunikation zwischen dem Mac und dem Raspberry Pi nicht verschlüsselt. Die Kommunikation erfolgt innerhalb Ihres Heim- oder Firmennetzwerks, daher ist eine fehlende Verschlüsselung in der Regel kein Problem. Wenn Sie jedoch Bedenken haben, können Sie eine VNC-Anwendung wie `VNC® Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ installieren.

Alternativ könnten Sie einen temporären Monitor (TV), eine Maus und eine Tastatur verwenden, um den Raspberry Pi Desktop direkt zu öffnen und VNC einzurichten. Wenn nicht, ist das kein Problem. Sie können auch den SSH-Befehl verwenden, um die Bash-Shell des Raspberry Pi zu öffnen und dann den Befehl zur Einrichtung des VNC zu nutzen.

* :ref:`have_temp_monitor`
* :ref:`no_temp_monitor`


.. _have_temp_monitor:

Haben Sie einen temporären Monitor (oder TV)?
---------------------------------------------------------------------

#. Schließen Sie einen Monitor (oder TV), eine Maus und eine Tastatur an den Raspberry Pi an und schalten Sie ihn ein. Wählen Sie das Menü entsprechend den Zahlen in der Abbildung.

    .. image:: img/mac_vnc1.png
        :align: center

#. Der folgende Bildschirm wird angezeigt. Setzen Sie **VNC** auf **Aktiviert** im Tab **Schnittstellen** und klicken Sie auf **OK**.

    .. image:: img/mac_vnc2.png
        :align: center

#. Ein VNC-Symbol erscheint oben rechts auf dem Bildschirm und der VNC-Server startet.

    .. image:: img/mac_vnc3.png
        :align: center

#. Öffnen Sie das VNC-Serverfenster, indem Sie auf das **VNC**-Symbol klicken. Klicken Sie dann auf den **Menü**-Button in der oberen rechten Ecke und wählen Sie **Optionen**.

    .. image:: img/mac_vnc4.png
        :align: center

#. Sie werden mit dem folgenden Bildschirm präsentiert, auf dem Sie die Optionen ändern können.

    .. image:: img/mac_vnc5.png
        :align: center

    Setzen Sie **Verschlüsselung** auf **Bevorzuge aus** und **Authentifizierung** auf **VNC-Passwort**. 

#. Wenn Sie auf die Schaltfläche **OK** klicken, wird der Passworteingabe-Bildschirm angezeigt. Sie können dasselbe Passwort wie das Raspberry Pi-Passwort oder ein anderes Passwort verwenden. Geben Sie es ein und klicken Sie auf **OK**.

    .. image:: img/mac_vnc16.png
        :align: center

    Jetzt können Sie von Ihrem Mac aus verbinden. Es ist in Ordnung, den Monitor zu trennen.

**Von hier an wird auf der Mac-Seite gearbeitet.**

#. Wählen Sie nun **Mit Server verbinden** aus dem Finder-Menü, das Sie durch Rechtsklick öffnen können.

    .. image:: img/mac_vnc10.png
        :align: center

#. Geben Sie ``vnc://<Benutzername>@<Hostname>.local`` (oder ``vnc://<Benutzername>@<IP-Adresse>``) ein. Nach der Eingabe klicken Sie auf **Verbinden**.

        .. image:: img/mac_vnc11.png
            :align: center

#. Sie werden nach einem Passwort gefragt, bitte geben Sie es ein.

        .. image:: img/mac_vnc12.png
            :align: center

#. Der Desktop des Raspberry Pi wird angezeigt, und Sie können ihn direkt vom Mac aus bedienen.

        .. image:: img/mac_vnc13.png
            :align: center



.. _no_temp_monitor:

Keinen temporären Monitor (oder Fernseher) zur Verfügung?
---------------------------------------------------------------------------

* Sie können den SSH-Befehl nutzen, um die Bash-Shell des Raspberry Pi zu öffnen.
* Bash ist die standardmäßige Shell für Linux.
* Die Shell an sich stellt einen Befehl (Anweisung) dar, wenn der Benutzer Unix/Linux verwendet.
* Das Meiste, was Sie tun müssen, kann über die Shell durchgeführt werden.
* Nachdem Sie den Raspberry Pi konfiguriert haben, können Sie mithilfe des **Finders** auf dem Mac auf den Desktop des Raspberry Pi zugreifen.

#. Geben Sie ``ssh <Benutzername>@<Hostname>.local`` ein, um eine Verbindung zum Raspberry Pi herzustellen.

    .. code-block::

        ssh pi@raspberrypi.local

    .. image:: img/mac_vnc14.png

#. Die folgende Meldung erscheint nur beim ersten Einloggen. Bestätigen Sie mit **ja**.

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        This key is not known by any other names
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. Geben Sie das Passwort für den Raspberry Pi ein. Das eingegebene Passwort wird nicht angezeigt, achten Sie daher darauf, keinen Fehler zu machen.

    .. code-block::

        pi@raspberrypi.local's password: 
        Linux raspberrypi 5.15.61-v8+ #1579 SMP PREEMPT Fri Aug 26 11:16:44 BST 2022 aarch64

        The programs included with the Debian GNU/Linux system are free software;
        the exact distribution terms for each program are described in the
        individual files in /usr/share/doc/*/copyright.

        Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
        permitted by applicable law.
        Last login: Thu Sep 22 12:18:22 2022
        pi@raspberrypi:~ $

#. Konfigurieren Sie Ihren Raspberry Pi so, dass Sie sich von Ihrem Mac aus über VNC einloggen können. Aktualisieren Sie zuerst Ihr Betriebssystem mit den folgenden Befehlen:

    .. code-block::

        sudo apt update
        sudo apt upgrade

    Bei der Frage „Möchten Sie fortfahren? [Y/n]“, bestätigen Sie mit ``Y``.

    Die Aktualisierung kann je nach Anzahl der Updates einige Zeit in Anspruch nehmen.

#. Führen Sie den folgenden Befehl aus, um den **VNC Server** zu aktivieren:

    .. code-block::

        sudo raspi-config

#. Das folgende Menü wird angezeigt. Wählen Sie mit den Pfeiltasten die Option **3 Interface Options** und bestätigen Sie mit der **Enter**-Taste.

    .. image:: img/image282.png
        :align: center

#. Wählen Sie anschließend **P3 VNC**.

    .. image:: img/image288.png
        :align: center

#. Nutzen Sie die Pfeiltasten, um **<Ja>** -> **<OK>** -> **<Fertigstellen>** auszuwählen und die Konfiguration abzuschließen.

    .. image:: img/mac_vnc8.png
        :align: center

#. Nachdem der VNC-Server gestartet ist, passen Sie die Einstellungen für die Verbindung von einem Mac an.

    Um Parameter für alle Programme und alle Benutzerkonten auf dem Computer festzulegen, erstellen Sie ``/etc/vnc/config.d/common.custom``.

    .. code-block::

        sudo nano /etc/vnc/config.d/common.custom

    Nach Eingabe von ``Authentication=VncAuthenter``, drücken Sie ``Ctrl+X`` -> ``Y`` -> ``Enter``, um zu speichern und zu beenden.

    .. image:: img/mac_vnc15.png
        :align: center

#. Legen Sie außerdem ein Passwort für die Anmeldung über VNC von einem Mac aus fest. Sie können dasselbe Passwort wie für den Raspberry Pi verwenden oder ein anderes.

    .. code-block::

        sudo vncpasswd -service

#. Nach Abschluss der Einrichtung starten Sie den Raspberry Pi neu, um die Änderungen zu übernehmen.

    .. code-block::

        sudo sudo reboot

#. Wählen Sie anschließend **Mit Server verbinden** im **Finder**-Menü, das Sie mit einem Rechtsklick öffnen können.

    .. image:: img/mac_vnc10.png
        :align: center

#. Geben Sie ``vnc://<Benutzername>@<Hostname>.local`` (oder ``vnc://<Benutzername>@<IP-Adresse>``) ein und klicken Sie nach der Eingabe auf **Verbinden**.

    .. image:: img/mac_vnc11.png
        :align: center

#. Sie werden nach einem Passwort gefragt. Bitte geben Sie dieses ein.

    .. image:: img/mac_vnc12.png
        :align: center

#. Der Desktop des Raspberry Pi wird angezeigt, und Sie können ihn direkt vom Mac aus steuern.

    .. image:: img/mac_vnc13.png
        :align: center
