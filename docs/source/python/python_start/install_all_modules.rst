.. _install_all_modules:


Installiere Alle Module(Wichtig)
========================================

Stellen Sie sicher, dass Sie mit dem Internet verbunden sind und aktualisieren Sie Ihr System:

.. raw:: html

    <run></run>

.. code-block::

    sudo apt update
    sudo apt upgrade

.. note::

    Python3-bezogene Pakete müssen installiert werden, wenn Sie die Lite-Version des Betriebssystems installieren.

    .. raw:: html

        <run></run>

    .. code-block::
    
        sudo apt install git python3-pip python3-setuptools python3-smbus


Installieren Sie ``robot-hat``.

.. raw:: html

    <run></run>

.. code-block::

    cd ~/
    git clone -b v2.0 https://github.com/sunfounder/robot-hat.git
    cd robot-hat
    sudo python3 setup.py install


Dann laden Sie das Modul ``vilib`` herunter und installieren Sie es.

.. raw:: html

    <run></run>

.. code-block::

    cd ~/
    git clone -b picamera2 https://github.com/sunfounder/vilib.git
    cd vilib
    sudo python3 install.py

Laden Sie das Modul ``picar-x`` herunter und installieren Sie es.

.. raw:: html

    <run></run>

.. code-block::

    cd ~/
    git clone -b v2.0 https://github.com/sunfounder/picar-x.git
    cd picar-x
    sudo python3 setup.py install

Dieser Schritt dauert eine Weile, bitte haben Sie Geduld.

Schließlich müssen Sie das Skript ``i2samp.sh`` ausführen, um die Komponenten zu installieren, die der i2s-Verstärker benötigt, sonst hat der Picar-X keinen Ton.

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x
    sudo bash i2samp.sh
	
.. image:: img/i2s.png

Geben Sie ``y`` ein und drücken Sie Enter, um das Skript weiter auszuführen.

.. image:: img/i2s2.png

Geben Sie ``y`` ein und drücken Sie Enter, um ``/dev/zero`` im Hintergrund laufen zu lassen.

.. image:: img/i2s3.png

Geben Sie ``y`` ein und drücken Sie Enter, um den Picar-X neu zu starten.

.. note::
    Wenn nach dem Neustart kein Ton vorhanden ist, müssen Sie möglicherweise das i2samp.sh-Skript mehrmals ausführen.
