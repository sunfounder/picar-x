.. _remote_desktop:

Remote Desktop 
=====================

Es gibt zwei Möglichkeiten, den Desktop des Raspberry Pi remote zu steuern: **VNC** und **XRDP**. Sie können eine beliebige Methode verwenden.

VNC 
--------------

Sie können die Funktion des Remote-Desktops über VNC nutzen.

**VNC-Dienst aktivieren**

Der VNC-Dienst ist im System installiert, ist jedoch standardmäßig deaktiviert. Sie müssen ihn in der Konfiguration aktivieren.

**Schritt 1**

Geben Sie den folgenden Befehl ein:

.. raw:: html

    <run></run>

.. code-block:: 

    sudo raspi-config

.. image:: img/image287.png
   :align: center

**Schritt 2**

Wählen Sie **3** **Interfacing Options**, indem Sie die Pfeiltaste nach unten auf Ihrer Tastatur drücken, und drücken Sie dann die **Enter**-Taste.

.. image:: img/image282.png
   :align: center

**Schritt 3**

**P3 VNC**

.. image:: img/image288.png
   :align: center

**Schritt 4**

Wählen Sie  **Yes -> OK -> Finish**, um die Konfiguration zu verlassen.

.. image:: img/image289.png
   :align: center

**Anmeldung bei VNC**

**Schritt 1**

Laden Sie den `VNC Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ auf Ihren Computer herunter und installieren Sie ihn. Öffnen Sie ihn nach Abschluss der Installation.

**Schritt 2**

Wählen Sie dann **Neue Verbindung**.

.. image:: img/image290.png
   :align: center

**Schritt 3**

Geben Sie ``<Hostname>.local`` oder ``<IP address>`` des Raspberry Pi und einen beliebigen **Namen** ein.

.. image:: img/image291.png
   :align: center

**Schritt 4**

Doppelklicken Sie auf die gerade erstellte **Verbindung**:

.. image:: img/image292.png
   :align: center

**Schritt 5**

Geben Sie Benutzername und Passwort ein.

.. image:: img/image293.png
   :align: center

**Schritt 6**

Jetzt sehen Sie den Desktop des Raspberry Pi:

.. image:: img/image294.png
   :align: center

Das ist das Ende des VNC-Teils.

XRDP
-----------------------

Eine weitere Methode für den Remote-Desktop ist XRDP. Es bietet eine grafische Anmeldung bei entfernten Maschinen über das RDP-Protokoll (Microsoft Remote Desktop Protocol).

**XRDP installieren**

**Schritt 1**

Melden Sie sich über SSH am Raspberry Pi an.

**Schritt 2**

Geben Sie die folgenden Anweisungen ein, um XRDP zu installieren.

.. raw:: html

    <run></run>

.. code-block:: 

   sudo apt-get update
   sudo apt-get install xrdp

**Schritt 3**

Die Installation wird gestartet.

Geben Sie ``Y`` ein und drücken Sie die Eingabetaste, um zu bestätigen.

.. image:: img/image295.png
   :align: center

**Schritt 4**

Nach Abschluss der Installation sollten Sie sich über Anwendungen für die Windows-Remotedesktopverbindung bei Ihrem Raspberry Pi anmelden können.

**Anmeldung bei XRDP**

**Schritt 1**

Wenn Sie Windows verwenden, können Sie die Remotedesktop-Funktion von Windows nutzen. Wenn Sie ein Mac-Benutzer sind, können Sie Microsoft Remote Desktop aus dem App Store herunterladen und verwenden. Der Unterschied zwischen den beiden ist nicht groß. Das folgende Beispiel zeigt die Verwendung von Windows Remotedesktop.

**Schritt 2**

Geben Sie in der Ausführen-Box (``WIN+R``) "mstsc" ein, um die Remotedesktopverbindung zu öffnen, und geben Sie die ``<Hostname>.local`` oder ``<IP-Adresse>`` des Raspberry Pi ein. Klicken Sie dann auf **Verbinden**.

.. image:: img/image296.png
   :align: center

**Schritt 3**

Dann wird die Anmeldeseite von XRDP angezeigt. Geben Sie Ihren Benutzernamen und Ihr Passwort ein. Klicken Sie anschließend auf **OK**.

.. image:: img/image297.png
   :align: center

**Schritt 4**

Hier haben Sie sich erfolgreich über den Remote-Desktop bei Ihrem Raspberry Pi angemeldet.

.. image:: img/image20.png
   :align: center