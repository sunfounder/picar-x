Einrichten Ihres Raspberry Pi
=======================================

Stromversorgung für Raspberry Pi (Wichtig)
----------------------------------------------

#. Stecken Sie die mit Raspberry Pi OS eingerichtete SD-Karte in den microSD-Kartensteckplatz auf der Unterseite des Raspberry Pi.

    .. image:: img/insert_sd_card.png
        :width: 500
        :align: center

#. Befolgen Sie die Montageanweisungen, stecken Sie das Batteriekabel ein und schalten Sie den Netzschalter ein. Stecken Sie dann das USB-C-Kabel ein, um die Batterie mit Strom zu versorgen. Warten Sie 1-2 Minuten, und Sie werden einen Ton hören, der anzeigt, dass der Raspberry Pi erfolgreich gestartet ist.

    .. image:: img/Z_BTR.JPG
        :width: 800
        :align: center

.. note::

    Es wird empfohlen, das USB-C-Kabel eingesteckt zu lassen, da der anschließende Software-Setup-Prozess einige Zeit in Anspruch nehmen kann."



Wenn Sie einen Bildschirm haben
-------------------------------------------

.. note:: Das auf dem Roboter installierte Raspberry Pi ZERO lässt sich nicht einfach mit einem Bildschirm verbinden. Bitte nutzen Sie die Methode ohne Bildschirm zur Einrichtung.

Falls Sie einen Bildschirm haben, wird es für Sie einfacher sein, auf dem Raspberry Pi zu arbeiten.

**Benötigte Komponenten**

* Ein beliebiges Raspberry Pi   
* 1 * Netzteil
* 1 * Micro SD-Karte
* 1 * Bildschirm-Netzteil
* 1 * HDMI-Kabel
* 1 * Bildschirm
* 1 * Maus
* 1 * Tastatur


#. Schließen Sie Maus und Tastatur an.

#. Verbinden Sie den Bildschirm über den HDMI-Anschluss des Raspberry Pi und stellen Sie sicher, dass Ihr Bildschirm an eine Steckdose angeschlossen und eingeschaltet ist.

    .. note::

        Wenn Sie ein Raspberry Pi 4 verwenden, müssen Sie den Bildschirm mit dem HDMI0-Port verbinden (am nächsten zum Stromanschluss).

#. Verwenden Sie das Netzteil, um den Raspberry Pi mit Strom zu versorgen. Nach einigen Sekunden wird der Raspberry Pi OS Desktop angezeigt.

    .. image:: img/image20.png
        :align: center

Wenn Sie keinen Bildschirm haben
-------------------------------------------

Falls Sie keinen Monitor besitzen, können Sie sich aus der Ferne in Ihren Raspberry Pi einloggen.

Sie können den SSH-Befehl nutzen, um die Bash-Shell des Raspberry Pi zu öffnen. Bash ist die standardmäßige Shell für Linux. Die Shell selbst ist ein Befehl (Anweisung), wenn der Benutzer Unix/Linux verwendet. Das Meiste von dem, was Sie tun müssen, kann über die Shell erfolgen.

Wenn Sie nicht zufrieden damit sind, Ihr Raspberry Pi nur über das Befehlsfenster zu bedienen, können Sie auch die Remote-Desktop-Funktion nutzen, um Dateien auf Ihrem Raspberry Pi mithilfe einer grafischen Benutzeroberfläche zu verwalten.

Siehe unten detaillierte Anleitungen für jedes System.



.. toctree::

    remote_macosx
    remote_windows
    remote_linux

