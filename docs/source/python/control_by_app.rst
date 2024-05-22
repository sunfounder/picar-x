.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

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
        
        cd ~/picar-x/example
        sudo python3 13.app_control.py

#. Installieren Sie `SunFounder Controller <https://docs.sunfounder.com/projects/sf-controller/en/latest/>`_ aus dem **App Store(iOS)** oder **Google Play(Android)**.

#. Öffnen und erstellen Sie einen neuen Controller.

    Erstellen Sie einen neuen Controller, indem Sie im SunFounder Controller-App auf das + Zeichen klicken.

    .. image:: img/app1.PNG

    Im Abschnitt 'Voreinstellungen' gibt es voreingestellte Controller für einige Produkte, die Sie bei Bedarf verwenden können. Hier wählen wir PiCar-X aus.
    
    .. image:: img/app_control_preset.jpg

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
    * **E**: Schaltet die Hindernisvermeidungsfunktion ein.
    * **I**: Schaltet die Linienverfolgungsfunktion ein.
    * **J**: Spracherkennung, halten Sie dieses Widget gedrückt, um zu sprechen, und es zeigt die erkannte Stimme an, wenn Sie es loslassen. Wir haben die 4 Befehle ``forward``, ``backard``, ``left`` und ``right`` im Code festgelegt, um das Auto zu steuern.
    * **K**: Steuert Vorwärts-, Rückwärts-, Links- und Rechtsbewegungen des Autos.
    * **Q**: Dreht den Kopf (Kamera) nach oben, unten, links und rechts.
    * **N**: Schaltet die Farberkennungsfunktion ein.
    * **O**: Schaltet die Gesichtserkennungsfunktion ein.
    * **P**: Schaltet die Objekterkennungsfunktion ein, sie kann fast 90 Arten von Objekten erkennen, für die Liste der Modelle, siehe: https://github.com/sunfounder/vilib/blob/master/workspace/coco_labels.txt.



