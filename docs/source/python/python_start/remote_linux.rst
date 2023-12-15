Linux/Unix-Nutzer
==========================


#. Gehen Sie zu **Applications** ->\ **Utilities**, finden Sie das **Terminal** und öffnen Sie es.

    .. image:: img/image21.png
        :align: center

#. Überprüfen Sie, ob Ihr Raspberry Pi im selben Netzwerk ist, indem Sie ``ping <hostname>.local`` eingeben.

    .. code-block::

        ping raspberrypi.local

    .. image:: img/mac-ping.png
        :width: 550
        :align: center

    Wie oben gezeigt, können Sie die IP-Adresse des Raspberry Pi sehen, nachdem er mit dem Netzwerk verbunden wurde.

    * Wenn das Terminal ``Ping request could not find host pi.local. Please check the name and try again.`` meldet, folgen Sie den Anweisungen, um sicherzustellen, dass der Hostname, den Sie eingeben, korrekt ist.
    * Bekommen Sie immer noch keine IP? Überprüfen Sie Ihre Netzwerk- oder WLAN-Konfiguration auf dem Raspberry Pi.


#. Geben Sie ``ssh <username>@<hostname>.local`` (oder ``ssh <username>@<IP address>``) ein.

    .. code-block::

        ssh pi@raspberrypi.local

    .. note::

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

    .. image:: img/mac-ssh-terminal.png
        :width: 550
        :align: center
