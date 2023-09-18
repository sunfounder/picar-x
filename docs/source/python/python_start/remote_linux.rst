Linux/Unix-Benutzer
==========================

#. Navigieren Sie zu **Anwendungen** -> **Dienstprogramme**, suchen Sie das **Terminal** und öffnen Sie es.

    .. image:: img/image21.png
        :align: center

#. Überprüfen Sie, ob Ihr Raspberry Pi im selben Netzwerk ist, indem Sie ``ping <hostname>.local`` eingeben.

    .. code-block::

        ping raspberrypi.local

    .. image:: img/mac-ping.png
        :width: 550
        :align: center

    Wie oben gezeigt, können Sie die IP-Adresse des Raspberry Pi sehen, nachdem er mit dem Netzwerk verbunden wurde.

    * Wenn das Terminal den Hinweis ``Ping-Anforderung konnte Host pi.local nicht finden. Bitte überprüfen Sie den Namen und versuchen Sie es erneut.`` gibt, folgen Sie den Anweisungen und stellen Sie sicher, dass der von Ihnen eingegebene Hostname korrekt ist.
    * Sie erhalten die IP nicht? Überprüfen Sie Ihre Netzwerk- oder WLAN-Konfiguration auf dem Raspberry Pi.

#. Geben Sie ``ssh <username>@<hostname>.local`` (oder ``ssh <username>@<IP-Adresse>``) ein.

    .. code-block::

        ssh pi@raspberrypi.local

    .. note::

        Wenn die Meldung ``Der Begriff 'ssh' wird nicht als Name eines Cmdlet erkannt...`` erscheint,
        
        bedeutet das, dass Ihr System veraltet ist und keine vorinstallierten SSH-Tools hat. Sie müssen manuell :ref:`openssh_powershell` installieren.
        
        Oder verwenden Sie ein Drittanbieter-Tool wie :ref:`login_windows`.

#. Die folgende Nachricht wird nur angezeigt, wenn Sie sich zum ersten Mal anmelden. Geben Sie also ``ja`` ein.

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        This key is not known by any other names
        Are you sure you want to continue connecting (yes/no/[fingerprint])?

#. Geben Sie das Passwort ein, das Sie zuvor festgelegt haben. (Meins ist ``raspberry``.)

    .. note::
        Beim Eingeben des Passworts werden die Zeichen im Fenster nicht angezeigt, 
        was normal ist. Es ist wichtig, dass Sie das korrekte Passwort eingeben.

#. Nun haben wir den Raspberry Pi verbunden und sind bereit, zum nächsten Schritt überzugehen.

    .. image:: img/mac-ssh-terminal.png
        :width: 550
        :align: center
