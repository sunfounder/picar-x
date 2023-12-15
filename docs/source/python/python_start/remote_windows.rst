Windows-Nutzer
=======================

Anmeldung am Raspberry Pi Aus der Ferne
---------------------------------------------

Wenn Sie win10 verwenden, können Sie folgenden Weg nutzen, um sich aus der Ferne am Raspberry Pi anzumelden.

#. Geben Sie in das Suchfeld Ihres Windows-Desktops ``powershell`` ein, klicken Sie mit der rechten Maustaste auf die ``Windows PowerShell`` und wählen Sie ``Run as administrator`` aus dem erscheinenden Menü.

    .. image:: img/powershell_ssh.png
        :align: center

#. Überprüfen Sie dann die IP-Adresse Ihres Raspberry Pi, indem Sie ``ping -4 <hostname>.local`` eingeben. 

    .. code-block::

        ping -4 raspberrypi.local

    .. image:: img/sp221221_145225.png
        :width: 550
        :align: center

    Wie oben gezeigt, können Sie die IP-Adresse des Raspberry Pi sehen, nachdem er mit dem Netzwerk verbunden wurde.

    * Wenn das Terminal ``Ping-Anforderung konnte Host pi.local nicht finden. Bitte überprüfen Sie den Namen und versuchen Sie es erneut.`` anzeigt, folgen Sie den Anweisungen, um sicherzustellen, dass der Hostname, den Sie ausfüllen, korrekt ist.
    * Bekommen Sie immer noch keine IP? Überprüfen Sie Ihre Netzwerk- oder WLAN-Konfiguration auf dem Raspberry Pi.


#. Jetzt können Sie sich mit ``ssh <username>@<hostname>.local`` (oder ``ssh <username>@<IP address>``) an Ihrem Raspberry Pi anmelden.

    .. code-block::

        ssh pi@raspberrypi.local

    .. warning::

        Wenn eine Aufforderung erscheint ``The term 'ssh' is not recognized as the name of a cmdlet...``
        
        Das bedeutet, dass Ihr System zu alt ist und keine vorinstallierten SSH-Tools hat, Sie müssen manuell :ref:`openssh_powershell` installieren.
        
        Oder verwenden Sie ein Drittanbieter-Tool wie :ref:`login_windows`.


#. Die folgende Nachricht wird nur beim ersten Anmelden angezeigt, also geben Sie ``yes`` ein.

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        This key is not known by any other names
        Are you sure you want to continue connecting (yes/no/[fingerprint])?


#. Geben Sie das zuvor festgelegte Passwort ein. (Meines ist ``raspberry``.)

    .. note::
        Wenn Sie das Passwort eingeben, werden die Zeichen nicht im
        Fenster angezeigt, was normal ist. Wichtig ist, dass Sie das
        korrekte Passwort eingeben.

#. Wir haben jetzt den Raspberry Pi verbunden und sind bereit für den nächsten Schritt.

    .. image:: img/sp221221_140628.png
        :width: 550
        :align: center

.. _remote_desktop:

Remote-Desktop
------------------

Wenn Sie mit der Nutzung des Befehlsfensters für den Zugriff auf Ihren Raspberry Pi nicht zufrieden sind, können Sie auch die Remote-Desktop-Funktion verwenden, um Dateien auf Ihrem Raspberry Pi einfach über eine grafische Benutzeroberfläche (GUI) zu verwalten.

Hier verwenden wir `VNC® Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_.

**VNC-Dienst Aktivieren**

Der VNC-Dienst ist im System installiert. Standardmäßig ist VNC
deaktiviert. Sie müssen es in der Konfiguration aktivieren.

#. Geben Sie den folgenden Befehl ein:

    .. raw:: html

        <run></run>

    .. code-block:: 

        sudo raspi-config

    .. image:: img/image287.png
        :align: center

#. Wählen Sie **3** **Interfacing Options** durch Drücken der Abwärtspfeiltaste auf Ihrer Tastatur, dann drücken Sie die **Enter**-Taste.

    .. image:: img/image282.png
        :align: center

#. Dann **VNC**. 

    .. image:: img/image288.png
        :align: center

#. Verwenden Sie die Pfeiltasten auf der Tastatur, um **<Yes>** -> **<OK>** -> **<Finish>** auszuwählen und die Einrichtung abzuschließen.

    .. image:: img/mac_vnc8.png
        :align: center

**Anmeldung beim VNC**

#. Sie müssen den `VNC Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ auf Ihrem persönlichen Computer herunterladen und installieren.

#. Öffnen Sie ihn, sobald die Installation abgeschlossen ist. Geben Sie dann den Hostnamen oder die IP-Adresse ein und drücken Sie Enter.

    .. image:: img/vnc_viewer1.png
        :align: center

#. Nachdem Sie Ihren Raspberry Pi-Namen und Ihr Passwort eingegeben haben, klicken Sie auf **OK**.

    .. image:: img/vnc_viewer2.png
        :align: center

#. Jetzt können Sie den Desktop des Raspberry Pi sehen.

    .. image:: img/image294.png
        :align: center

