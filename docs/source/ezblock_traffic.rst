Traffic Sign Detection
===============================

该示例在自动驾驶（ :ref:`Minecart` ）的基础上增加了交通标志识别。换而言之，PiCar-X依然会沿着道路行驶，但是改变它行驶与停止的条件将不再是前方障碍物，而是路边的交通标志。

在这里，检测到 **STOP** 标志将会让它停止，检测到 **Forward** 标志将会让他向前行驶。

它的工作逻辑也适用于其他的目标检测任务（如颜色识别，用于检测红绿灯）。打开video，你将能看到PiCar-X时是如何完成检测任务的。

**TIPS**

.. image:: img/block/sp210513_101526.png

.. image:: img/block/sp210513_110948.png

.. image:: img/block/sp210512_171425.png

.. image:: img/block/sp210512_171454.png