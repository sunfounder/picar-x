
Mac OS X-Nutzer
==========================

Für Mac-Nutzer ist der direkte Zugriff auf den Raspberry Pi-Desktop über VNC bequemer als über die Befehlszeile. Sie können darauf über den Finder zugreifen, indem Sie das festgelegte Kontopasswort eingeben, nachdem Sie VNC auf der Raspberry Pi-Seite aktiviert haben.

Beachten Sie, dass diese Methode die Kommunikation zwischen dem Mac und dem Raspberry Pi nicht verschlüsselt. 
Die Kommunikation findet innerhalb Ihres Heim- oder Geschäftsnetzwerks statt, sodass es auch ungeschützt kein Problem darstellt. 
Wenn Sie jedoch Bedenken haben, können Sie eine VNC-Anwendung wie `VNC® Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ installieren.

Alternativ wäre es praktisch, wenn Sie einen temporären Monitor (TV), eine Maus und eine Tastatur verwenden könnten, um den Raspberry Pi-Desktop direkt zu öffnen und VNC einzurichten. 
Wenn nicht, ist das kein Problem, Sie können auch den SSH-Befehl verwenden, um die Bash-Shell des Raspberry Pi zu öffnen und dann den Befehl verwenden, um VNC einzurichten.


* :ref:`have_temp_monitor`
* :ref:`no_temp_monitor`


.. _have_temp_monitor:

Haben Sie Einen Temporären Monitor (oder TV)?
---------------------------------------------------------------------

#. Schließen Sie einen Monitor (oder TV), eine Maus und eine Tastatur an den Raspberry Pi an und schalten Sie ihn ein. Wählen Sie das Menü entsprechend den Nummern in der Abbildung.


    .. image:: img/mac_vnc1.png
        :align: center

#. Der folgende Bildschirm wird angezeigt. Setzen Sie **VNC** auf **Enabled** im Reiter **Interfaces**, und klicken Sie auf **OK**.

    .. image:: img/mac_vnc2.png
        :align: center


#. Ein VNC-Symbol erscheint oben rechts auf dem Bildschirm und der VNC-Server startet.

    .. image:: img/mac_vnc3.png
        :align: center


#. Öffnen Sie das VNC-Serverfenster, indem Sie auf das **VNC**-Symbol klicken, dann klicken Sie auf die **Menu**-Schaltfläche in der oberen rechten Ecke und wählen **Options**.

    .. image:: img/mac_vnc4.png
        :align: center

#. Sie werden mit dem folgenden Bildschirm präsentiert, auf dem Sie die Optionen ändern können.

    .. image:: img/mac_vnc5.png
        :align: center

    Stellen Sie **Encryption** auf **Prefer off** und **Authentication** auf **VNC password**. 
    
#. Wenn Sie auf die Schaltfläche **OK** klicken, wird der Passworteingabebildschirm angezeigt. Sie können dasselbe Passwort wie das Raspberry Pi-Passwort oder ein anderes Passwort verwenden, also geben Sie es ein und klicken Sie auf **OK**. 

    .. image:: img/mac_vnc16.png
        :align: center

    Sie sind jetzt bereit, von Ihrem Mac aus eine Verbindung herzustellen. Es ist in Ordnung, den Monitor zu trennen.

**Von hier an wird es die Operation auf der Mac-Seite sein.**

#. Wählen Sie jetzt **Connect to Server** aus dem Finder-Menü, das Sie durch Rechtsklick öffnen können.

    .. image:: img/mac_vnc10.png
        :align: center

#. Geben Sie ``vnc://<benutzername>@<hostname>.local`` (oder ``vnc://<benutzername>@<IP-Adresse>``) ein. Nach der Eingabe klicken Sie auf **Connect**.

        .. image:: img/mac_vnc11.png
            :align: center


#. Sie werden nach einem Passwort gefragt, also geben Sie es bitte ein.

        .. image:: img/mac_vnc12.png
            :align: center

#. Der Desktop des Raspberry Pi wird angezeigt, und Sie können ihn direkt vom Mac aus bedienen.

        .. image:: img/mac_vnc13.png
            :align: center

.. _no_temp_monitor:

Keinen Temporären Monitor (oder TV)?
---------------------------------------------------------------------------

* Sie können den SSH-Befehl anwenden, um die Bash-Shell des Raspberry Pi zu öffnen.
* Bash ist die Standard-Standard-Shell für Linux.
* Die Shell selbst ist ein Befehl (Anweisung), wenn der Benutzer Unix/Linux verwendet.
* Das meiste, was Sie tun müssen, kann über die Shell erledigt werden.
* Nachdem Sie den Raspberry Pi eingerichtet haben, können Sie vom Mac aus über den **Finder** auf den Desktop des Raspberry Pi zugreifen.


#. Geben Sie ``ssh <benutzername>@<hostname>.local`` ein, um sich mit dem Raspberry Pi zu verbinden.


    .. code-block::

        ssh pi@raspberrypi.local


    .. image:: img/mac_vnc14.png


#. Die folgende Nachricht wird nur beim ersten Anmelden angezeigt, also geben Sie **yes** ein.

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        This key is not known by any other names
        Are you sure you want to continue connecting (yes/no/[fingerprint])?


#. Geben Sie das Passwort für den Raspberry Pi ein. Das eingegebene Passwort wird nicht angezeigt, seien Sie also vorsichtig, keinen Fehler zu machen.

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


    

#. Richten Sie Ihren Raspberry Pi so ein, dass Sie sich über VNC von Ihrem Mac aus anmelden können, sobald Sie sich erfolgreich eingeloggt haben. Der erste Schritt besteht darin, Ihr Betriebssystem zu aktualisieren, indem Sie die folgenden Befehle ausführen.

    .. code-block::

        sudo apt update
        sudo apt upgrade


    ``Möchten Sie fortfahren? [Y/n]``, geben Sie ``Y`` ein, wenn Sie dazu aufgefordert werden.

    Es kann einige Zeit dauern, bis das Update abgeschlossen ist. (Es hängt von der Menge der Updates zu diesem Zeitpunkt ab.)


#. Geben Sie den folgenden Befehl ein, um den **VNC-Server** zu aktivieren.

    .. code-block::

        sudo raspi-config

#. Der folgende Bildschirm wird angezeigt. Wählen Sie mit den Pfeiltasten auf der Tastatur **Interface Options** aus und drücken Sie die **Enter**-Taste.

    .. image:: img/image282.png
        :align: center

#. Wählen Sie dann **VNC**.

    .. image:: img/image288.png
        :align: center

#. Verwenden Sie die Pfeiltasten auf der Tastatur, um **<Yes>** -> **<OK>** -> **<Finish>** auszuwählen und die Einrichtung abzuschließen.

    .. image:: img/mac_vnc8.png
        :align: center


#. Jetzt, da der VNC-Server gestartet wurde, ändern wir die Einstellungen für die Verbindung von einem Mac aus.

    Um Parameter für alle Programme für alle Benutzerkonten auf dem Computer festzulegen, erstellen Sie ``/etc/vnc/config.d/common.custom``.

    .. code-block::

        sudo nano /etc/vnc/config.d/common.custom

    Nachdem Sie ``Authentication=VncAuthenter`` eingegeben haben, drücken Sie ``Ctrl+X`` -> ``Y`` -> ``Enter``, um zu speichern und zu beenden.

    .. image:: img/mac_vnc15.png
        :align: center

#. Setzen Sie zusätzlich ein Passwort für die Anmeldung über VNC von einem Mac aus. Sie können dasselbe Passwort wie das Raspberry Pi-Passwort oder ein anderes Passwort verwenden. 


    .. code-block::

        sudo vncpasswd -service


#. Nachdem die Einrichtung abgeschlossen ist, starten Sie den Raspberry Pi neu, um die Änderungen anzuwenden.

    .. code-block::

        sudo sudo reboot

#. Wählen Sie jetzt **Connect to Server** aus dem **Finder**-Menü, das Sie durch Rechtsklick öffnen können.

    .. image:: img/mac_vnc10.png
        :align: center

#. Geben Sie ``vnc://<benutzername>@<hostname>.local`` (oder ``vnc://<benutzername>@<IP-Adresse>``) ein. Nach der Eingabe klicken Sie auf **Connect**.

        .. image:: img/mac_vnc11.png
            :align: center


#. Sie werden nach einem Passwort gefragt, also geben Sie es bitte ein.

        .. image:: img/mac_vnc12.png
            :align: center

#. Der Desktop des Raspberry Pi wird angezeigt, und Sie können ihn direkt vom Mac aus bedienen.

        .. image:: img/mac_vnc13.png
            :align: center

