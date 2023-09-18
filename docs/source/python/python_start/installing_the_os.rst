OS Installation
=======================

**Benötigte Komponenten**

================== ======================
Raspberry Pi        Personal Computer
Micro SD-Karte 
================== ======================

**Schritt 1**

Raspberry Pi hat ein grafisches SD-Kartenschreibtool entwickelt, das
auf Mac OS, Ubuntu 18.04 und Windows funktioniert. Es ist die einfachste Option für die meisten
Benutzer, da es das Image herunterlädt und automatisch auf die
SD-Karte installiert.

Besuchen Sie die Download-Seite: https://www.raspberrypi.org/software/. Klicken Sie auf
den Link für den Raspberry Pi Imager, der zu Ihrem Betriebssystem passt. Nachdem der Download abgeschlossen ist, klicken Sie darauf, um den Installer zu starten.

.. image:: img/image11.png
    :align: center

**Schritt 2**

Wenn Sie den Installer starten, versucht Ihr Betriebssystem möglicherweise, 
die Ausführung zu blockieren. Zum Beispiel erhalte ich unter Windows folgende
Meldung:

Wenn dies erscheint, klicken Sie auf **Mehr Infos** und dann auf **Trotzdem ausführen** und
folgen Sie den Anweisungen, um den Raspberry Pi Imager zu installieren.

.. image:: img/image12.png
    :align: center

**Schritt 3**

Stecken Sie Ihre SD-Karte in den SD-Karten-Slot Ihres Computers oder Laptops.

**Schritt 4**

Wählen Sie im Raspberry Pi Imager das Betriebssystem aus, das Sie installieren möchten, und
die SD-Karte, auf die es installiert werden soll.

.. image:: img/sp230607_161330.png
    :align: center

.. note::

    1) Sie müssen beim ersten Mal mit dem Internet verbunden sein.

    2) Das Betriebssystem wird dann für die spätere Offline-Nutzung gespeichert (lastdownload.cache, C:/Users/IhrName/AppData/Local/Raspberry Pi/Imager/cache). Das nächste Mal, wenn Sie die Software öffnen, wird angezeigt "Veröffentlicht: Datum, im Cache auf Ihrem Computer".

**Schritt 5**

Wählen Sie die von Ihnen verwendete SD-Karte aus.

.. image:: img/image14.png
    :align: center

**Schritt 6**

Um zur Seite für erweiterte Optionen zu gelangen, klicken Sie auf die Einstellungsschaltfläche (erscheint nach Auswahl des Betriebssystems) oder drücken Sie Strg+Shift+X. 
Aktivieren Sie SSH und legen Sie den Benutzernamen und Namen fest. Sie können wählen, diese Bildanpassungsoptionen immer zu verwenden.

.. note::

    Wenn das Kontrollkästchen "Hostname festlegen" nicht aktiviert ist, wird der Standard-Hostname weiterhin ``raspberrypi`` sein. Wir werden diesen Hostnamen verwenden, um auf den Raspberry Pi aus der Ferne zuzugreifen.

.. image:: img/image15.png
    :align: center

Scrollen Sie anschließend nach unten, um die WLAN-Konfiguration abzuschließen, und klicken Sie auf **SPEICHERN**.

.. note::

    **WLAN-Land** sollte den zweibuchstabigen `ISO/IEC alpha2 code <https://de.wikipedia.org/wiki/ISO_3166-1_alpha-2>`_ für das Land, in dem Sie Ihren Raspberry Pi verwenden, festlegen. Bitte verweisen Sie auf den folgenden Link: https://de.wikipedia.org/wiki/ISO_3166-1_alpha-2

.. image:: img/image16.png
    :align: center

**Schritt 7**

Klicken Sie auf die Schaltfläche **SCHREIBEN**.

.. image:: img/image17.png
    :align: center

**Schritt 8**

Wenn sich derzeit Dateien auf Ihrer SD-Karte befinden, möchten Sie diese Dateien möglicherweise zuerst sichern, um einen dauerhaften Verlust zu verhindern. Wenn keine Datei gesichert werden muss, klicken Sie auf **Ja**.

.. image:: img/image18.png
    :align: center

**Schritt 9**

Nach einer gewissen Wartezeit erscheint das folgende Fenster, das das erfolgreiche Schreiben anzeigt.

.. image:: img/image19.png
    :align: center
