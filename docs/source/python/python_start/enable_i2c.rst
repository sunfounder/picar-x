I2C-Schnittstelle aktivieren (Wichtig)
========================================

Hier verwenden wir die I2C-Schnittstellen des Raspberry Pi, aber standardmäßig sind sie deaktiviert, daher müssen wir sie zuerst aktivieren.

#. Geben Sie den folgenden Befehl ein:

    .. raw:: html

        <run></run>

    .. code-block::

        sudo raspi-config

#. Wählen Sie **Interfacing Options** mit der Abwärtspfeiltaste Ihrer Tastatur und drücken Sie dann die **Enter**-Taste.

    .. image:: img/image282.png
        :align: center

#. Anschließend **I2C**.

    .. image:: img/image283.png
        :align: center

#. Verwenden Sie die Pfeiltasten auf der Tastatur, um **<Yes>** -> **<OK>** auszuwählen und die Einrichtung des I2C abzuschließen.

    .. image:: img/image284.png
        :align: center

