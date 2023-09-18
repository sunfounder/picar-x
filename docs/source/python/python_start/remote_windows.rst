

Windows-Nutzer
=======================

Remote-Anmeldung am Raspberry Pi
---------------------------------------------

Wenn Sie Windows 10 verwenden, können Sie die folgende Methode nutzen, um sich remote am Raspberry Pi anzumelden.

#. Geben Sie ``powershell`` in das Suchfeld Ihres Windows-Desktops ein, klicken Sie mit der rechten Maustaste auf ``Windows PowerShell`` und wählen Sie ``Als Administrator ausführen`` aus dem erscheinenden Menü.

    .. image:: img/powershell_ssh.png
        :align: center

#. Überprüfen Sie dann die IP-Adresse Ihres Raspberry Pi, indem Sie ``ping -4 <hostname>.local`` eingeben.

    .. code-block::

        ping -4 raspberrypi.local

    .. image:: img/sp221221_145225.png
        :width: 550
        :align: center

    Wie oben gezeigt, können Sie die IP-Adresse des Raspberry Pi sehen, nachdem er mit dem Netzwerk verbunden wurde.

    * Wenn das Terminal die Meldung ``Ping request could not find host pi.local. Please check the name and try again.`` anzeigt, befolgen Sie die Anweisungen und stellen Sie sicher, dass der von Ihnen eingegebene Hostname korrekt ist.
    * Sie können die IP immer noch nicht erhalten? Überprüfen Sie Ihre Netzwerk- oder WLAN-Konfiguration auf dem Raspberry Pi.

#. Nun können Sie sich mit dem Befehl ``ssh <username>@<hostname>.local`` (oder ``ssh <username>@<IP address>``) an Ihrem Raspberry Pi anmelden.

    .. code-block::

        ssh pi@raspberrypi.local

    .. warning::

        Wenn die Meldung ``The term 'ssh' is not recognized as the name of a cmdlet...`` erscheint,
        
        bedeutet dies, dass Ihr System veraltet ist und keine vorinstallierten SSH-Tools hat. Sie müssen manuell :ref:`openssh_powershell` installieren.
        
        Oder verwenden Sie ein Drittanbieter-Tool wie :ref:`login_windows`.

#. Die folgende Meldung wird nur bei Ihrer ersten Anmeldung angezeigt. Geben Sie ``yes`` ein.

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        This key is not known by any other names
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. Geben Sie das zuvor festgelegte Passwort ein. (Meins ist ``raspberry``.)

    .. note::
        Wenn Sie das Passwort eingeben, werden die Zeichen nicht entsprechend im
        Fenster angezeigt, was normal ist. Wichtig ist, dass Sie das
        korrekte Passwort eingeben.

#. Nun haben wir den Raspberry Pi verbunden und sind bereit, zum nächsten Schritt zu gehen.

    .. image:: img/sp221221_140628.png
        :width: 550
        :align: center

Remote-Desktop
------------------

Wenn Sie mit dem Befehlsfenster zur Steuerung Ihres Raspberry Pi nicht zufrieden sind, können Sie auch die Remote-Desktop-Funktion nutzen, um Dateien auf Ihrem Raspberry Pi über eine GUI einfach zu verwalten.

Hierfür verwenden wir den `VNC® Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_.

**VNC-Service aktivieren**

Der VNC-Service ist im System installiert. Standardmäßig ist VNC
deaktiviert. Sie müssen ihn in der Konfiguration aktivieren.

#. Geben Sie den folgenden Befehl ein:

    .. code-block:: 

        sudo raspi-config

    .. image:: img/image287.png
        :align: center

#. Wählen Sie **3** **Interfacing Options** mithilfe der Abwärtspfeiltaste Ihrer Tastatur und drücken Sie dann die **Enter**-Taste.

    .. image:: img/image282.png
        :align: center

#. Danach **P3 VNC**. 

    .. image:: img/image288.png
        :align: center

#. Verwenden Sie die Pfeiltasten auf der Tastatur, um **<Ja>** -> **<OK>** -> **<Beenden>** auszuwählen und die Einrichtung abzuschließen.

    .. image:: img/mac_vnc8.png
        :align: center

**Anmeldung bei VNC**

#. Sie müssen den `VNC Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ auf Ihrem Computer herunterladen und installieren.

#. Öffnen Sie ihn nach Abschluss der Installation. Geben Sie dann den Hostnamen oder die IP-Adresse ein und drücken Sie Enter.

    .. image:: img/vnc_viewer1.png
        :align: center

#. Nach Eingabe Ihres Raspberry Pi-Namens und Passworts klicken Sie auf **OK**.

    .. image:: img/vnc_viewer2.png
        :align: center

#. Nun können Sie den Desktop des Raspberry Pi sehen.

    .. image:: img/image294.png
        :align: center
