.. _install_all_modules:


Alle Module installieren  (Wichtig)
==============================================

Stellen Sie sicher, dass Sie mit dem Internet verbunden sind und aktualisieren Sie Ihr System:

.. raw:: html

    <run></run>

.. code-block::

    sudo apt update
    sudo apt upgrade

.. note::

    Python3-bezogene Pakete müssen installiert sein, wenn Sie die Lite-Version des Betriebssystems installieren.

    .. raw:: html

        <run></run>

    .. code-block::
    
        sudo apt install git python3-pip python3-setuptools python3-smbus


Installieren Sie das Modul ``robot-hat``.

.. raw:: html

    <run></run>

.. code-block::

    cd ~/
    git clone -b v2.0 https://github.com/sunfounder/robot-hat.git
    cd robot-hat
    sudo python3 setup.py install

Laden Sie dann das Modul ``vilib`` herunter und installieren Sie es.

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

Schließlich müssen Sie das Skript ``i2samp.sh`` ausführen, um die für den i2s-Verstärker erforderlichen Komponenten zu installieren. Andernfalls hat der Picar-X keinen Ton.

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x
    sudo bash i2samp.sh
	
.. image:: img/i2s.png

Geben Sie "y" ein und drücken Sie die Eingabetaste, um das Skript fortzusetzen.

.. image:: img/i2s2.png

Geben Sie "y" ein und drücken Sie die Eingabetaste, um ``/dev/zero`` im Hintergrund auszuführen.

.. image:: img/i2s3.png

Geben Sie "y" ein und drücken Sie die Eingabetaste, um den Picar-X neu zu starten.

.. note::
    Wenn nach dem Neustart kein Ton vorhanden ist, müssen Sie das i2samp.sh-Skript möglicherweise mehrmals ausführen.