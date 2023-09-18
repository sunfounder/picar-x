.. _login_windows:

PuTTY
=========================

Wenn Sie ein Windows-Benutzer sind, können Sie einige SSH-Anwendungen verwenden. Hier empfehlen wir `PuTTY <https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html>`_.

**Schritt 1**

Laden Sie PuTTY herunter.

**Schritt 2**

Öffnen Sie PuTTY und klicken Sie auf **Sitzung** in der linken baumartigen Struktur. Geben Sie die IP-Adresse des RPi in das Textfeld unter **Host Name (oder IP-Adresse)** ein und **22** unter **Port** (standardmäßig ist es 22).

.. image:: img/image25.png
    :align: center

**Schritt 3**

Klicken Sie auf **Öffnen**. Beachten Sie, dass beim ersten Anmelden am Raspberry Pi mit der IP-Adresse eine Sicherheitserinnerung angezeigt wird. Klicken Sie einfach auf **Ja**.

**Schritt 4**

Wenn das PuTTY-Fenster "**login as:**" anzeigt, geben Sie "**pi**" (den Benutzernamen des RPi) und das Passwort "**raspberry**" ein (das Standardpasswort, wenn Sie es nicht geändert haben).

.. note::

    Bei der Eingabe des Passworts werden die Zeichen nicht entsprechend im Fenster angezeigt, was normal ist. Sie müssen das korrekte Passwort eingeben.
    
    Wenn neben PuTTY "inactive" angezeigt wird, bedeutet dies, dass die Verbindung unterbrochen wurde und erneut hergestellt werden muss.
    
.. image:: img/image26.png
    :align: center

**Schritt 5**

Jetzt haben wir eine Verbindung zum Raspberry Pi hergestellt und es ist Zeit, mit den nächsten Schritten fortzufahren.