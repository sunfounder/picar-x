Betriebssysteminstallation
==========================

**Benötigte Komponenten**

* Beliebiges Raspberry Pi 
* 1 x Persönlicher Computer
* 1 x Micro-SD-Karte

**Schritt 1**

Die Entwickler des Raspberry Pi haben ein grafisches SD-Karten-Schreibprogramm entwickelt,
das unter Mac OS, Ubuntu 18.04 und Windows läuft. Es ist die einfachste Option für die meisten
Nutzer, da es das Image herunterlädt und automatisch auf die SD-Karte installiert.

Besuche die Download-Seite: https://www.raspberrypi.org/software/. Klicke auf
den Link für den Raspberry Pi Imager, der zu deinem Betriebssystem passt.
Wenn der Download abgeschlossen ist, klicke darauf, um das Installationsprogramm zu starten.

.. image:: img/image11.png
    :align: center

**Schritt 2**

Wenn du das Installationsprogramm startest, versucht dein Betriebssystem möglicherweise,
die Ausführung zu blockieren. Zum Beispiel erhalte ich unter Windows die folgende
Meldung:

Wenn dies erscheint, klicke auf **Weitere Informationen** und dann auf **Trotzdem ausführen**,
und folge den Anweisungen, um den Raspberry Pi Imager zu installieren.

.. image:: img/image12.png
    :align: center

**Schritt 3**

Lege deine SD-Karte in den SD-Kartenslot deines Computers oder Laptops ein.

**Schritt 4**

Klicke im Raspberry Pi Imager auf **CHOOSE OS** -> **Raspberry Pi OS (Legacy)**.

.. warning::
    * Bitte installiere nicht die **Bookworm**-Version, da der Lautsprecher nicht funktionieren wird.
    * Du musst die Version **Raspberry Pi OS (Legacy)** - **Debian Bullseye** installieren.

.. image:: img/3d33.png
    :align: center

**Schritt 5**

Wähle die SD-Karte aus, die du benutzt.

.. image:: img/image14.png
    :align: center

**Schritt 6**

Um die Seite mit den erweiterten Optionen zu öffnen, klicke auf das **Einstellungen** -Symbol
(erscheint nach der Auswahl des Betriebssystems) oder drücke **Ctrl+Shift+X**.

Stelle jetzt den Hostnamen ein, aktiviere SSH und setze Benutzername sowie Passwort.

.. warning::

    Notiere unbedingt den ``hostname``, ``username`` und das ``password``; sie sind entscheidend für den späteren Fernzugriff auf den Raspberry Pi.

.. image:: img/image15.png
    :align: center

Dann scrolle nach unten, um die WLAN-Konfiguration abzuschließen, und klicke auf **SPEICHERN**.

.. note::

    Das **WLAN-Land** sollte den zweibuchstabigen `ISO/IEC Alpha2-Code <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ für das Land, in dem du deinen Raspberry Pi benutzt, entsprechen. Bitte beachte folgenden Link: https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements.

.. image:: img/image16.png
    :align: center

**Schritt 7**

Klicke auf die Schaltfläche **SCHREIBEN**.

.. image:: img/image17.png
    :align: center

**Schritt 8**

Wenn sich aktuell Dateien auf deiner SD-Karte befinden, möchtest du vielleicht
zuerst diese Dateien sichern, um zu verhindern, dass sie dauerhaft verloren gehen.
Wenn keine Datei gesichert werden muss, klicke auf **Ja**.

.. image:: img/image18.png
    :align: center

**Schritt 9**

Nach einer gewissen Wartezeit erscheint das folgende Fenster, um die Fertigstellung
des Schreibvorgangs anzuzeigen.

.. image:: img/image19.png
    :align: center
