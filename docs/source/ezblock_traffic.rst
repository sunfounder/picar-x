Traffic Sign Detection
===============================

In this project, you will use a new detection function, **traffic sign detection**. The traffic sign detection process is as follows: 

First, the video frames are pre-processed by OpenCV and regions are selected on the image, then the regions are passed into the model that has been trained using TensorFlow. Finally, according to the type and accuracy returned by the model, the corresponding region on the image is framed and labeled with the type and accuracy.

We have trained 4 traffic sign models for PiCar-X, which you can print yourself, but you need to be careful to make sure they are printed in color.


* `Traffic Sign Cards File <https://github.com/sunfounder/picar-x/blob/v2.0/printfile/Traffic%20Sign%20Cards.pdf>`_

.. image:: img/block/taffics_sign.png

.. note::

    Please understand that the printed traffic sign cardboard may be a little different from the one we trained because of the color difference or material, which will lead to a less accurate recognition.

This project is based on :ref:`Minecart` with traffic sign detection, detecting a **STOP** sign will make it stop, and a **FORWARD** sign will make it drive forward. You can view the detection results via Video Monitor on Ezblock Studio.

.. image:: img/block/traffic_detect.PNG


**TIPS**

.. image:: img/block/sp210513_101526.png

.. image:: img/block/sp210513_110948.png

.. image:: img/block/sp210512_171425.png

.. image:: img/block/sp210512_171454.png