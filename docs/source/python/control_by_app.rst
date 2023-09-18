.. _control_by_app:

Steuerung durch die App
=======================

Der SunFounder-Controller dient zur Steuerung von Robotern, die auf Raspberry Pi/Pico basieren.

Die App bietet verschiedene Widgets wie Tasten, Schalter, Joystick, Steuerkreuz, Schieberegler und Gashebel; Digitale Anzeigen, Ultraschallradar, Graustufen-Erkennung und Tachometer sind als Eingabewidgets verfügbar.

Es gibt 17 Bereiche von A-Q, in denen unterschiedliche Widgets für die individuelle Gestaltung des Controllers platziert werden können.

Zusätzlich bietet diese Anwendung einen Live-Videostreaming-Service.

Lassen Sie uns einen PiCar-X-Controller mit dieser App anpassen.

**Wie macht man das?**

#. Installieren Sie das ``sunfounder-controller`` Modul.

    Zuerst müssen die Module ``robot-hat``, ``vilib`` und ``picar-x`` installiert werden. Einzelheiten finden Sie unter: :ref:`install_all_modules`.


    .. raw:: html

        <run></run>

    .. code-block::

        cd ~
        git clone https://github.com/sunfounder/sunfounder-controller.git
        cd ~/sunfounder-controller
        sudo python3 setup.py install

#. Starten Sie den Code.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/picar-x/example
        sudo python3 app_control.py

#. Installieren Sie den `SunFounder Controller <https://docs.sunfounder.com/projects/sf-controller/en/latest/>`_ aus dem **APP Store(iOS)** oder **Google Play(Android)**.


#. Erstellen Sie einen neuen Controller.

    Erstellen Sie einen neuen Controller, indem Sie im SunFounder Controller APP auf das Pluszeichen klicken.

    .. image:: img/app1.PNG

    Benennen Sie ihn und wählen Sie den Controllertyp aus. Im Bereich "Voreinstellungen" finden Sie vorkonfigurierte Controller für einige Produkte, die Sie bei Bedarf nutzen können. Sie können Ihren Controller auch individuell anpassen, indem Sie die folgenden Schritte befolgen.

    .. image:: img/app2.PNG

#. Fügen Sie diesem Controller verschiedene Widgets hinzu.

    Sie können verschiedene Arten und Formen von Widgets in den **A-Q** 17 kleinen Bereichen innerhalb dieses Controllers hinzufügen.

    .. image:: img/app3.PNG

    In the **A** area, add an **Speedometer** widget to display the car's speed.

    .. image:: img/app4.PNG
    
    .. note::
    
        Ein ausgewähltes Widget kann gelöscht werden, indem man es anklickt, nach links wischt, um die Schaltfläche **Delete** zu finden, und darauf klickt.

        .. image:: img/app5.PNG

    Legen Sie den Namen, die Maximal- und Minimalwerte sowie die Einheiten fest, indem Sie auf das **Settings** -Symbol in der oberen rechten Ecke klicken.

    .. image:: img/app6.PNG

    Legen Sie für das **Grayscale Detection**-Widget im Bereich **D** die ``Line_Ref`` und ``Cliff_Ref`` Ihrer aktuellen Umgebung fest.

    .. image:: img/app7.PNG

    Fügen Sie schließlich die verbleibenden Widgets hinzu und klicken Sie auf die Schaltfläche oben rechts, um zu speichern.

    .. image:: img/app8.PNG

#. Verbinden Sie sich mit PiCar-X.

    Wenn Sie auf die Schaltfläche **Connect** klicken, wird automatisch nach in der Nähe befindlichen Robotern gesucht. Der Name ist in ``picarx_control.py`` definiert und muss ständig laufen.

    .. image:: img/app9.PNG
    
    Sobald Sie auf den Produktnamen klicken, erscheint die Meldung "Erfolgreich verbunden", und der Produktname wird in der oberen rechten Ecke angezeigt.

    .. image:: img/app10.PNG

    .. note::

        * Stellen Sie sicher, dass Ihr mobiles Gerät mit demselben LAN wie PiCar-X verbunden ist.
        * Falls die automatische Suche nicht funktioniert, können Sie auch manuell die IP eingeben, um die Verbindung herzustellen.

        .. image:: img/app11.PNG

#. Starten Sie diesen Controller.

    Klicken Sie auf die Schaltfläche **Run**, um den Controller zu starten. Sie sehen das aufgenommene Videomaterial des Autos, und nun können Sie Ihr PiCar-X mit diesen Widgets steuern.

    .. image:: img/app12.PNG
    
    Hier sind die Funktionen der Widgets.

    * **A**: Zeigt die aktuelle Geschwindigkeit des Autos an.
    * **D**: Zeigt die Daten der drei Sensoren im Graustufenmodul an, die drei Zustände haben: **schwarzer Block**: schwarze Linie erkannt; **weiß**: weiß erkannt; **Ausrufezeichen**: Abgrund erkannt.
    * **E**: Aktiviert die Hindernisvermeidungsfunktion.
    * **I**: Aktiviert die Linienverfolgungsfunktion.
    * **J**: Spracherkennung; halten Sie dieses Widget gedrückt, um zu sprechen, und es zeigt die erkannte Stimme an, wenn Sie es loslassen. Im Code haben wir die vier Befehle ``vorwärts``, ``rückwärts``, ``links`` und ``rechts`` zur Steuerung des Autos festgelegt.
    * **K**: Steuert die Vorwärts-, Rückwärts-, Links- und Rechtsbewegungen des Autos.
    * **Q**: Bewegt den Kopf (Kamera) nach oben, unten, links und rechts.
    * **N**: Aktiviert die Farberkennungsfunktion.
    * **O**: Aktiviert die Gesichtserkennungsfunktion.
    * **P**: Aktiviert die Objekterkennungsfunktion, die fast 90 verschiedene Objekte erkennen kann. Für eine Liste der Modelle verweisen wir auf: https://github.com/sunfounder/vilib/blob/master/workspace/coco_labels.txt.

