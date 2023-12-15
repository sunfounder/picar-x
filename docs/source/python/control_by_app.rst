.. _control_by_app:

13. Durch die App gesteuert
==================================

Der SunFounder-Controller wird verwendet, um auf Raspberry Pi/Pico basierende Roboter zu steuern.

Die App integriert Schaltflächen, Schalter, Joysticks, D-Pads, Schieberegler und Gashebel-Widgets; digitale Anzeigen, Ultraschallradar, Graustufenerkennung und Geschwindigkeitsmesser-Eingabewidgets.

Es gibt 17 Bereiche A-Q, in denen Sie verschiedene Widgets platzieren können, um Ihren eigenen Controller anzupassen.

Zusätzlich bietet diese Anwendung einen Live-Videostreaming-Dienst.

Lassen Sie uns einen PiCar-X-Controller mit dieser App anpassen.

**Wie geht das?**

#. Installieren Sie das Modul ``sunfounder-controller``.

    Die Module ``robot-hat``, ``vilib`` und ``picar-x`` müssen zuerst installiert werden, Details siehe: :ref:`install_all_modules`.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~
        git clone https://github.com/sunfounder/sunfounder-controller.git
        cd ~/sunfounder-controller
        sudo python3 setup.py install

#. Führen Sie den Code aus.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/picar-x/beispiel
        sudo python3 app_steuerung.py

#. Installieren Sie `SunFounder Controller <https://docs.sunfounder.com/projects/sf-controller/en/latest/>`_ aus dem **App Store(iOS)** oder **Google Play(Android)**.

#. Öffnen und erstellen Sie einen neuen Controller.

    Erstellen Sie einen neuen Controller, indem Sie im SunFounder Controller-App auf das + Zeichen klicken.

    .. image:: img/app1.PNG

    Geben Sie ihm einen Namen und wählen Sie den Controllertyp. Im Bereich Voreinstellungen gibt es voreingestellte Controller für einige Produkte, die Sie bei Bedarf verwenden können. Sie können auch Ihren eigenen Controller anpassen, indem Sie die folgenden Schritte befolgen.

    .. image:: img/app2.PNG

#. Fügen Sie verschiedene Widgets zu diesem Controller hinzu.

    Sie können unterschiedliche Typen und Formen von Widgets zu den 17 kleinen Bereichen **A-Q** in diesem Controller hinzufügen.

    .. image:: img/app3.PNG

    Im Bereich **A** fügen Sie ein **Speedometer**-Widget hinzu, um die Geschwindigkeit des Autos anzuzeigen.

    .. image:: img/app4.PNG
    
    .. note::
    
        Sie können das ausgewählte Widget löschen, indem Sie darauf klicken, nach links wischen, um den **Delete**-Button zu finden, und darauf klicken.

        .. image:: img/app5.PNG

    Legen Sie den Namen, die maximalen und minimalen Werte sowie die Einheiten fest, indem Sie auf das **Settings**-Symbol in der oberen rechten Ecke klicken.

    .. image:: img/app6.PNG

    Stellen Sie die Werte ``Linien_Ref`` und ``Klippen_Ref`` für das **Grayscale Detection**-Widget im Bereich **D** entsprechend Ihrer aktuellen Umgebung ein.

    .. image:: img/app7.PNG

    Fügen Sie zuletzt die verbleibenden Widgets hinzu und klicken Sie auf den Button oben rechts, um zu speichern.

    .. image:: img/app8.PNG

#. Verbinden Sie sich mit PiCar-x.

    Wenn Sie auf den **Connect**-Button klicken, wird automatisch nach Robotern in der Nähe gesucht. Der Name ist in ``picarx_control.py`` definiert und muss ständig laufen.

    .. image:: img/app9.PNG
    
    Sobald Sie auf den Produktnamen klicken, erscheint die Meldung „Connected Successfully“ und der Produktname wird in der oberen rechten Ecke angezeigt.

    .. image:: img/app10.PNG

    .. note::

        * Sie müssen sicherstellen, dass Ihr mobiles Gerät mit demselben LAN wie PiCar-X verbunden ist.
        * Wenn es nicht automatisch sucht, können Sie auch manuell die IP eingeben, um sich zu verbinden.

        .. image:: img/app11.PNG

#. Verwenden Sie diesen Controller.

    Klicken Sie auf den **Run**-Button, um den Controller zu starten, Sie sehen das Filmmaterial des Autos und können jetzt Ihr PiCar-X mit diesen Widgets steuern.

    .. image:: img/app12.PNG
    
    Hier sind die Funktionen der Widgets.

    * **A**: Zeigt die aktuelle Geschwindigkeit des Autos an.
    * **D**: Zeigt die Daten der drei Sensoren auf dem Graustufenmodul an, die drei Zustände haben: **black block**: schwarze Linie erkannt; **white**: Weiß erkannt; **exclamation point**: Klippe erkannt.
    * **E**: Schaltet die Hindernisvermeidungsfunktion ein.
    * **I**: Schaltet die Linienverfolgungsfunktion ein.
    * **J**: Spracherkennung, halten Sie dieses Widget gedrückt, um zu sprechen, und es zeigt die erkannte Stimme an, wenn Sie es loslassen. Wir haben die 4 Befehle ``forward``, ``backard``, ``left`` und ``right`` im Code festgelegt, um das Auto zu steuern.
    * **K**: Steuert Vorwärts-, Rückwärts-, Links- und Rechtsbewegungen des Autos.
    * **Q**: Dreht den Kopf (Kamera) nach oben, unten, links und rechts.
    * **N**: Schaltet die Farberkennungsfunktion ein.
    * **O**: Schaltet die Gesichtserkennungsfunktion ein.
    * **P**: Schaltet die Objekterkennungsfunktion ein, sie kann fast 90 Arten von Objekten erkennen, für die Liste der Modelle, siehe: https://github.com/sunfounder/vilib/blob/master/workspace/coco_labels.txt.



