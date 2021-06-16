Beware of Pedestrians
=============================

This example demonstrates the process of executing countermeasures based on road conditions (pedestrians) when an intelligent vehicle is driving. 

Ezblock has been provided with a well-trained and usable human face detection model, which PiCar-X calls directly, allowing it to directly recognize the presence of a human face in front of the camera. 

If you put a photo of a person in front of PiCar-X, you will see that part of the human face in the screen of Camera Monitor will be circled and selected.

We instruct PiCar-X to stop automatically when it identifies a human face. With a view to guarantee driving safety more stably, we have programmed a section of frequency judgment of human face appearance for PiCar-X: human face detection is performed 10 times per unit time, and if human face information appears more than 3 times, the driving will stop.


**EXAMPLE**

.. image:: img/block/sp210512_185509.png