Download and run the code
============================

Download the code and install the 3 modules
----------------------------------------------
We can use the command ``git clone`` in the terminal to download the file.

First install ``robot-hat`` .

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/
    git clone https://github.com/sunfounder/robot-hat.git
    cd robot-hat
    sudo python3 setup.py install

.. note::
    Running ``setup.py`` will download some necessary components. Your download may have failed due to network issues. You may need to download again at this point.
    See the following interface, type ``Y`` and press Enter.
	
	.. image:: img/dowload_code.png

Then download and install the ``vilib`` module.

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/
    git clone https://github.com/sunfounder/vilib.git
    cd vilib
    sudo python3 install.py

Then download and install the ``picar-x`` module.

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/
    git clone -b v2.0 https://github.com/sunfounder/picar-x.git
    cd picar-x
    sudo python3 setup.py install

This step will take a little while, so please be patient.

Finally, you need to run the script ``i2samp.sh`` to install the components required by the i2s amplifier, otherwise the picar-x will have no sound.

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/picar-x
    sudo bash i2samp.sh
	
.. image:: img/i2s.png

Type ``y`` and press enter to continue running the script.

.. image:: img/i2s2.png

Type ``y`` and press enter to run ``/dev/zero`` in the background.

.. image:: img/i2s3.png

Type ``y`` and press enter to restart the machine.

.. note::
    If there is no sound after restarting, you may need to run the i2samp.sh script several times.