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
