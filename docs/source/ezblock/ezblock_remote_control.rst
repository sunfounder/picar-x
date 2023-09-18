.. _ezb_remote_control:

Fernsteuerung
=======================

Dieses Projekt zeigt, wie Sie die PiCar-X mithilfe des Joystick-Widgets fernsteuern können. 
Hinweis: Nachdem Sie das Joystick-Widget von der Fernsteuerungsseite gezogen und abgelegt haben, verwenden Sie die „Map“-Funktion, um die X- und Y-Achsen-Werte des Joysticks zu kalibrieren. Weitere Informationen zur Fernsteuerungsfunktion finden Sie unter folgendem Link:

* :ref:`ezblock:remote_control_latest`


.. image:: img/remote_control23.png

**TIPPS**

.. image:: img/sp210512_114004.png

Um die Fernsteuerungsfunktion zu nutzen, öffnen Sie die Fernsteuerungsseite über die linke Seite der Hauptseite.

.. image:: img/sp210512_114042.png

Ziehen Sie einen Joystick in den mittleren Bereich der Fernsteuerungsseite. Durch Verschieben des weißen Punktes in der Mitte und sanftes Ziehen in eine beliebige Richtung werden ein (X, Y)-Koordinatenpaar erzeugt. Der Bereich der X- oder Y-Achse ist standardmäßig von „-100“ bis „100“ festgelegt. Verschieben Sie den weißen Punkt und ziehen Sie ihn direkt zum äußersten linken Rand des Joysticks, ergibt dies einen X-Wert von „-100“ und einen Y-Wert von „0“.

.. image:: img/sp210512_114136.png

Nachdem ein Widget auf der Fernsteuerungsseite gezogen und abgelegt wurde, erscheint eine neue Kategorie - Remote - mit dem obigen Block.
Dieser Block liest den Joystick-Wert auf der Fernsteuerungsseite. Im Dropdown-Menü können Sie auf die Y-Achsen-Lesung umschalten.

.. image:: img/sp210512_114235.png

Der „Map Value“-Block kann eine Zahl von einem Bereich in einen anderen umkodieren. Wenn der Bereich von 0 bis 100 festgelegt ist und die „Map Value“-Nummer 50 beträgt, dann entspricht das einer Position von 50 % des Bereichs oder „50“. Wenn der Bereich von 0 bis 255 festgelegt ist und die „Map Value“-Nummer 50 beträgt, dann entspricht dies einer Position von 50 % des Bereichs oder „127,5“.

**BEISPIEL**

.. note::

    * Sie können das Programm gemäß dem folgenden Bild erstellen. Bitte beziehen Sie sich auf das Tutorial: :ref:`ezblock:create_project_latest`.
    * Oder finden Sie den Code mit dem gleichen Namen auf der **Beispiele**-Seite des EzBlock Studios und klicken Sie direkt auf **Ausführen** oder **Bearbeiten**.

.. image:: img/sp210512_114416.png
