.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _openssh_powershell:

Installieren Sie OpenSSH über Powershell
============================================

Wenn Sie ``ssh <Benutzername>@<Hostname>.local`` (oder ``ssh <Benutzername>@<IP-Adresse>``) verwenden, um sich mit Ihrem Raspberry Pi zu verbinden, aber die folgende Fehlermeldung angezeigt wird:

    .. code-block::

        ssh: Der Begriff "ssh" wird nicht als Name eines Cmdlets, einer Funktion, einer Skriptdatei oder eines ausführbaren Programms erkannt. Überprüfen Sie die Rechtschreibung des Namens oder, falls ein Pfad angegeben wurde, stellen Sie sicher, dass der Pfad korrekt ist, und versuchen Sie es erneut.


Dann bedeutet dies, dass Ihr Computersystem zu alt ist und nicht über `OpenSSH <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui>`_ vorinstalliert ist. Sie müssen der folgenden Anleitung folgen, um es manuell zu installieren.

#. Geben Sie ``powershell`` in die Suchleiste Ihres Windows-Desktops ein, klicken Sie mit der rechten Maustaste auf ``Windows PowerShell`` und wählen Sie im angezeigten Menü ``Als Administrator ausführen``.

    .. image:: img/powershell_ssh.png
        :align: center

#. Verwenden Sie den folgenden Befehl, um ``OpenSSH.Client`` zu installieren.

    .. code-block::

        Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

#. Nach der Installation wird die folgende Ausgabe zurückgegeben.

    .. code-block::

        Pfad          :
        Online        : True
        Neustart erforderlich : False

#. Überprüfen Sie die Installation mit dem folgenden Befehl.

    .. code-block::

        Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

#. Es wird Ihnen jetzt mitgeteilt, dass ``OpenSSH.Client`` erfolgreich installiert wurde.

    .. code-block::

        Name  : OpenSSH.Client~~~~0.0.1.0
        Zustand : Installiert

        Name  : OpenSSH.Server~~~~0.0.1.0
        Zustand : Nicht vorhanden

    .. warning:: 
        Wenn die obige Aufforderung nicht angezeigt wird, bedeutet dies, dass Ihr Windows-System immer noch zu alt ist, und Sie sollten ein SSH-Tool von Drittanbietern installieren, wie :ref:`login_windows`.

#. Starten Sie jetzt PowerShell neu und führen Sie es weiterhin als Administrator aus. An diesem Punkt können Sie sich mit dem Befehl ``ssh`` auf Ihrem Raspberry Pi anmelden, wo Sie aufgefordert werden, das zuvor eingerichtete Passwort einzugeben.

    .. image:: img/powershell_login.png