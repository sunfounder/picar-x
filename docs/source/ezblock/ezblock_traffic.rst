Traffic Sign Detection
===============================

In addition to color, face detection, PiCar-X can also do traffic sign detection.

Now let's combine this traffic sign detection with the line following function. Let PiCar-X track the line, and when you put the Stop sign in front of it, it will stop. When you place a Forward sign in front of it, it will continue to move forward.


**TIPS**

#. PiCar will recognize 4 different traffic sign models included in the printable PDF below. 

    .. image:: img/taffics_sign.png

    * :download:`[PDF]Traffic Sign Cards <https://github.com/sunfounder/sf-pdf/raw/master/prop_card/object_detection/traffic-sign-cards.pdf>`

#. **Set ref to ()** block is used to set the grayscale threshold, you need to modify it according to the actual situation. You can go ahead and run :ref:`test_grayscale` to see the values of the grayscale module on the white and black surfaces, and fill in their middle values in this block.



**EXAMPLE**

.. note::

    * You can write the program according to the following picture, please refer to the tutorial: :ref:`ezblock:create_project_latest`.
    * Or find the code with the same name on the **Examples** page of the EzBlock Studio and click **Run** or **Edit** directly.


.. image:: img/sp210513_101526.png

.. image:: img/sp210513_110948.png

.. image:: img/sp210512_171425.png

.. image:: img/sp210512_171454.png