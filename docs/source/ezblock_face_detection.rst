Face Detection
======================

In addition to color detection, PiCar-X also provides face detection. Here we use Joystick to adjust the direction of the camera and let the faces number be displayed in 
the debug monitor.

**TIPS**

.. image:: img/block/sp210512_141947.png

You need to set face detection status to true to enable face detection.

.. image:: img/block/sp210512_142327.png

These two blocks are used to adjust the orientation of the pan-tilt camera. As the value increases, the camera rotates to the right or up.

.. image:: img/block/sp210512_142407.png

You can read the image detection results through this block, modify the drop-down menu options, and choose to read the coordinates, size or number of the image detection results.

.. image:: img/block/sp210512_142616.png

you may want to use text block to print the combination of texts & data at once.

**EXAMPLE**

.. image:: img/block/sp210512_142830.png