.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

Aktivierung des I2C-Interface(Wichtig)
========================================

Hier verwenden wir die I2C-Schnittstellen des Raspberry Pi, standardmäßig sind diese jedoch deaktiviert, daher müssen wir sie zunächst aktivieren.

#. Geben Sie den folgenden Befehl ein:

    .. raw:: html

        <run></run>

    .. code-block:: 

        sudo raspi-config

#. Wählen Sie **Interfacing Options** durch Drücken der Abwärtspfeiltaste auf Ihrer Tastatur, dann drücken Sie die **Enter**-Taste.

    .. image:: img/image282.png
        :align: center

#. Dann **I2C**.

    .. image:: img/image283.png
        :align: center

#. Verwenden Sie die Pfeiltasten auf der Tastatur, um **<yes>** -> **<OK>** auszuwählen und die Einrichtung des I2C abzuschließen.

    .. image:: img/image284.png
        :align: center

#. Nachdem Sie **<Finish>** ausgewählt haben, erscheint ein Pop-up, das Sie daran erinnert, dass Sie neu starten müssen, damit die Einstellungen wirksam werden. Wählen Sie **<yes>**.

    .. image:: img/camera_enable2.png
        :align: center
