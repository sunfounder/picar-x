Color Detection
===========================

PiCar-X is a self-driving car with a built-in camera, which allows Ezblock programs to utilize object detection and color recognition code. In this section, Ezblock will be used to create a program for color detection. 

.. note:: 

    Before attempting this section, make sure that the Raspberry Pi Camera’s FFC cable is properly and securely connected. For detailed instructions on securely connecting the FCC cable, please reference: :ref:`assembly_instructions`.

In this program, Ezblock will first be told the Hue-Saturation-Value (HSV) space range of the color to be detected, then utilize OpenCV to process the colors in the HSV range to remove the background noise, and finally, box the matching color.

Ezblock includes 6 color models for PiCar-X, “red”, “orange”, “yellow”, “green”, “blue”, and “purple”. Color cards have been prepared in the following PDF, and will need to be printed on a color printer.

* :download:`[PDF]Color Cards <https://github.com/sunfounder/sf-pdf/raw/master/prop_card/object_detection/color-cards.pdf>`

.. image:: img/color_card.png
    :width: 600

.. note::

    The printed colors may have a slightly different hue from the Ezblock color models due to printer toner differences, or the printed medium, such as a tan-colored paper. This can cause a less accurate color recognition.


.. image:: img/ezblock_color_detect.PNG

**TIPS**

.. image:: img/sp210512_121105.png

Drag the Video widget from the remote Control page, and it will generate a video monitor. For more information on how to use the Video widget, please reference the tutorial on Ezblock video here: `How to Use the Video Function? <https://docs.sunfounder.com/projects/ezblock3/en/latest/use_video.html>`_

.. image:: img/sp210512_121125.png

Enable the video monitor by setting the **camera monitor** block to **on**. Note: Setting the **camera monitor** to **off** will close the monitor, but object detection will still be available.

.. image:: img/sp210512_134133.png

Use the **color detection** block to enable the color detection. Note: only one color can be detected at a time.

**EXAMPLE**

.. note::

    * You can write the program according to the following picture, please refer to the tutorial: `How to Create a New Project? <https://docs.sunfounder.com/projects/ezblock3/en/latest/create_new.html>`_
    * Or find the code with the same name on the **Examples** page of the EzBlock Studio and click **Run** or **Edit** directly.

.. image:: img/sp210512_134636.png