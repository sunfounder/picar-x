Minecart Plus
=======================

In this project, derailment recovery has been added to the :ref:`ezb_minecart` project to let the PiCar-X adapt and recover from a more severe curve.

.. image:: img/minec.png


**TIPS**

#. Use another **to do something** block to allow the PiCar-X to back up and recover from a sharp curve. Note that the new **to do something** function does not return any values, but is used just for reorienting the PiCar-X.

    .. image:: img/sp210512_171727.png

#. **Set ref to ()** block is used to set the grayscale threshold, you need to modify it according to the actual situation. You can go ahead and run :ref:`test_grayscale` to see the values of the grayscale module on the white and black surfaces, and fill in their middle values in this block.


**EXAMPLE**

.. note::

    * You can write the program according to the following picture, please refer to the tutorial: :ref:`ezblock:create_project_latest`.
    * Or find the code with the same name on the **Examples** page of the EzBlock Studio and click **Run** or **Edit** directly.

.. image:: img/sp210512_171914.png

.. image:: img/sp210512_171932.png

.. image:: img/sp210512_171425.png

.. image:: img/sp210512_171454.png