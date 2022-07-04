Beware of Pedestrians
=============================

This project will make the PiCar-X perform appropriate measures based on road conditions. While driving, the PiCar-X will come to a complete stop if a pedestrian is detected in its path.

Once the program is running, hold a photo of a person in front of the PiCar-X. The Video Monitor will detect the person's face, and the PiCar-X will automatically come to a stop.

To simulate driving safety protocols, a judgment procedure is created that will send a **[count]** value to a **if do else** block. The judgement procedure will look for a human face 10 times, and if a face does appear it will increment **[count]** by +1. When **[count]** is larger than 3, the PiCar-X will stop moving.

* :ref:`ezblock:remote_control_latest`

.. image:: img/face_detection.PNG


**EXAMPLE**

.. note::

    * You can write the program according to the following picture, please refer to the tutorial: :ref:`ezblock:create_project_latest`.
    * Or find the code with the same name on the **Examples** page of the EzBlock Studio and click **Run** or **Edit** directly.

.. image:: img/sp210512_185509.png