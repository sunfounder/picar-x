Minecart
=====================

Let's make a minecart project! Stick a dark-colored tape on the white ground as the 
track (as straight as possible, not too curved), and use the Grayscale module to 
make the PiCar-X move along the track.

This means: when moving along the track, the probes on the left and right sides of 
the sensor detect light-colored ground, and the middle probe detects dark tracks.
If the track has an arc (the probe on the left or right side of the sensor detects a dark 
track), you need to adjust the direction of the minecart.
If the minecart reaches the end of the track or derails, the Grayscale module can't detect the 
dark track so stops it.

**EXAMPLE**

.. image:: img/block/sp210512_170342.png

.. image:: img/block/sp210512_171425.png

.. image:: img/block/sp210512_171454.png