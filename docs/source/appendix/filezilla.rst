.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _filezilla:

Filezilla Software
==========================

.. image:: img/filezilla_icon.png

Das File Transfer Protocol (FTP) ist ein standardisiertes Kommunikationsprotokoll, das für die Übertragung von Computerdateien von einem Server auf einen Client in einem Computernetzwerk verwendet wird.

Filezilla ist eine Open-Source-Software, die nicht nur FTP unterstützt, sondern auch FTP über TLS (FTPS) und SFTP. Mit Filezilla können wir lokale Dateien (wie Bilder und Audio usw.) auf den Raspberry Pi hochladen oder Dateien vom Raspberry Pi auf das lokale Gerät herunterladen.

**Schritt 1**: Laden Sie Filezilla herunter.

Laden Sie den Client von der offiziellen Website von Filezilla `Filezilla’s offizielle Website <https://filezilla-project.org/>`_ herunter. Filezilla bietet ein sehr gutes Tutorial, siehe: `Dokumentation - Filezilla <https://wiki.filezilla-project.org/Documentation>`_.

**Schritt 2**: Verbindung zum Raspberry Pi herstellen

Nach einer schnellen Installation öffnen Sie das Programm und verbinden es nun `mit einem FTP-Server <https://wiki.filezilla-project.org/Using#Connecting_to_an_FTP_server>`_. Es gibt 3 Möglichkeiten zur Verbindung, hier verwenden wir die **Quick Connect**. Geben Sie den **hostname/IP**, **username**, **password** und **port (22)** ein, klicken Sie dann auf **Quick Connect** oder drücken Sie **Enter**, um die Verbindung zum Server herzustellen.

.. image:: img/filezilla_connect.png

.. note::

    Schnellverbinden ist eine gute Möglichkeit, Ihre Anmeldeinformationen zu testen. Wenn Sie einen dauerhaften Eintrag erstellen möchten, können Sie nach einer erfolgreichen Schnellverbindung **File** -> **Copy Current Connection to Site Manager** wählen, den Namen eingeben und auf **OK** klicken. Beim nächsten Mal können Sie die Verbindung herstellen, indem Sie die zuvor gespeicherte Seite unter **File** -> **Site Manager** auswählen.
    
    .. image:: img/ftp_site.png

**Schritt 3**: Dateien hoch-/herunterladen.

Sie können lokale Dateien auf den Raspberry Pi übertragen, indem Sie diese per Drag-and-Drop hochladen, oder die auf dem Raspberry Pi befindlichen Dateien lokal herunterladen.

.. image:: img/upload_ftp.png

