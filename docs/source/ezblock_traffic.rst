交通标志检测
================================

该项目使用图像检测功能来寻找交通标志，
并使帕克按照标志上的说明进行操作。
**交通标志检测** 块启动后，将识别以下 PDF 中包含的 4 种不同交通标志模型。
当帕克检测到 **停止（STOP）** 标志时，它会停下来，
**向前（FORWARD）** 标志将使其向前行驶，而 **向左（LEFT）** 或 **向右（RIGHT）** 箭头将使其转向该方向。

* :download:`[PDF]交通标志卡 <https://github.com/sunfounder/sf-pdf/raw/master/prop_card/object_detection/traffic-sign-cards.pdf>`

.. image:: img/block/taffics_sign.png

.. note::

    由于打印机碳粉或打印介质（如棕褐色纸）的不同，打印的交通标志颜色可能与 Ezblock 颜色模型的色调略有不同。 这会导致不太准确的颜色识别。

该项目基于 :ref:`矿车` ，但帕克使用一种算法进行交通标志检测，而不是使用灰度传感器。 检测结果可以通过 Ezblock Studio 中的视频监视器查看。

.. image:: img/block/traffic_detect.PNG


**示例**

.. image:: img/block/sp210513_101526.png

.. image:: img/block/sp210513_110948.png

.. image:: img/block/sp210512_171425.png

.. image:: img/block/sp210512_171454.png