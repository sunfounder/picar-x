Minecart
=====================

Let’s make a minecart project! This project will use the Grayscale module to make the PiCar-X move forward along a track. 
Use dark-colored tape to make a track on the ground as straight as possible, and not too curved. Some experimenting might be needed if the PiCar-X becomes derailed. 

When moving along the track, the probes on the left and right sides of the Grayscale module will detect light-colored ground, and the middle probe will detect the track. If the track has an arc, the probe on the left or right side of the sensor will detect the dark-colored tape, and turn the wheels in that direction. If the minecart reaches the end of the track or derails, the Grayscale module will no longer detect the dark-colored tape track, and the PiCar-X will come to a stop.

**EXAMPLE**

.. image:: img/block/sp210512_170342.png

.. image:: img/block/sp210512_171425.png

.. image:: img/block/sp210512_171454.png