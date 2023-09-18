Verkehrsschilderkennung
===============================

Neben der Farberkennung und der Gesichtserkennung kann der PiCar-X auch Verkehrsschilder erkennen.

Lassen Sie uns nun diese Verkehrsschilderkennung mit der Linienverfolgungsfunktion kombinieren. Der PiCar-X wird der Linie folgen, und wenn Sie das Stoppschild davor platzieren, wird er anhalten. Wenn Sie ein Vorwärtsschild davor platzieren, wird er weiterhin vorwärts fahren.


**TIPPS**

#. Der PiCar erkennt 4 verschiedene Verkehrsschildmodelle, die im druckbaren PDF unten enthalten sind. 

    .. image:: img/taffics_sign.png

    * :download:`[PDF]Verkehrsschildkarten <https://github.com/sunfounder/sf-pdf/raw/master/prop_card/object_detection/traffic-sign-cards.pdf>`

#. Der Block **Set ref to ()** wird verwendet, um den Grauwert-Schwellenwert festzulegen. Sie müssen ihn entsprechend der tatsächlichen Situation anpassen. Sie können den Befehl :ref:`test_grayscale` ausführen, um die Werte des Grauwertmoduls auf weißen und schwarzen Oberflächen zu sehen, und deren mittlere Werte in diesem Block eintragen.



**BEISPIEL**

.. note::

    * Sie können das Programm gemäß der folgenden Abbildung schreiben. Bitte beachten Sie das Tutorial: :ref:`ezblock:create_project_latest`.
    * Oder finden Sie den Code mit demselben Namen auf der **Examples** -Seite des EzBlock Studios und klicken Sie direkt auf **Run** oder **Edit**.

.. image:: img/sp210513_101526.png

.. image:: img/sp210513_110948.png

.. image:: img/sp210512_171425.png

.. image:: img/sp210512_171454.png