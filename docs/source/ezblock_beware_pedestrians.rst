Beware of Pedestrians
=============================

This project demonstrates PiCar-X performing appropriate measures based on road conditions (pedestrians) while driving.

If you put a photo of a person in front of PiCar-X, you will see the face circled in the Video Monitor.

When PiCar-X detects a human face, we make it stop automatically.

For driving safety, we wrote a judgment procedure: detecting a human face 10 times in a unit time, and if the face appears more than 3 times, it stops driving.

* `How to Use the Video Function? <https://docs.sunfounder.com/projects/ezblock3/en/latest/use_video.html>`_

.. image:: img/block/face_detection.PNG


**EXAMPLE**

.. image:: img/block/sp210512_185509.png