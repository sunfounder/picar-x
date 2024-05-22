.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _login_windows:

PuTTY
=========================

Wenn Sie ein Windows-Benutzer sind, können Sie einige SSH-Anwendungen verwenden. Hier empfehlen wir `PuTTY <https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html>`_.

**Schritt 1**

PuTTY herunterladen.

**Schritt 2**

Öffnen Sie PuTTY und klicken Sie im baumähnlichen Menü links auf **Session**. Geben Sie die IP-Adresse des RPi in das Feld unter **Host Name (oder IP-Adresse)** und **22** unter **Port** ein (standardmäßig ist es 22).

.. image:: img/image25.png
    :align: center

**Schritt 3**

Klicken Sie auf **Open**. Beachten Sie, dass bei der ersten Anmeldung am Raspberry Pi mit der IP-Adresse eine Sicherheitserinnerung erscheint. Klicken Sie einfach auf **Ja**.

**Schritt 4**

Wenn im PuTTY-Fenster "**login as:**" angezeigt wird, geben Sie
"**pi**" ein (der Benutzername des RPi) und als **Passwort**: "raspberry"
(das Standardpasswort, sofern Sie es nicht geändert haben).

.. note::

    Wenn Sie das Passwort eingeben, werden die Zeichen nicht im Fenster angezeigt, was normal ist. Wichtig ist nur, dass Sie das richtige Passwort eingeben.
    
    Wenn neben PuTTY "inaktiv" angezeigt wird, bedeutet dies, dass die Verbindung unterbrochen wurde und erneut hergestellt werden muss.
    
.. image:: img/image26.png
    :align: center

**Schritt 5**

Jetzt haben wir eine Verbindung zum Raspberry Pi hergestellt und es ist Zeit für die nächsten Schritte.
