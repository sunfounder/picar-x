Background Music
======================

In addition to programming the PiCar-X to play sound effects or text-to-speech (TTS), the PiCar-X will also play background music. This project will also use a **Slider** widget for adjusting the music volume. 

* :ref:`ezblock:remote_control_latest`

For a detailed tutorial on Ezblocks remote control functions, please reference the :ref:`ezb_remote_control` tutorial.

**TIPS**

.. image:: img/sp210512_152803.png

The **play background music** block will need to be added to the **Start** function. Use the drop-down menu to choose different background music for the PiCar-X to play.

.. image:: img/sp210512_153123.png

The block **set background music volume to** will adjust the volume between the range of 0 to 100.

.. image:: img/sp210512_154708.png

Drag a **Slider** bar from the **Remote Control** page to adjust music volume.

.. image:: img/sp210512_154259.png

The **slider [A] get value** block will read the slider value. The example above has slider ‘A’ selected. If there are multiple sliders, use the drop-down menu to select the appropriate one.

**EXAMPLE**

.. note::

    * You can write the program according to the following picture, please refer to the tutorial: :ref:`ezblock:create_project_latest`.
    * Or find the code with the same name on the **Examples** page of the EzBlock Studio and click **Run** or **Edit** directly.

.. image:: img/sp210512_155406.png