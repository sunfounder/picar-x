颜色检测
============================

帕克是一款内置摄像头的自动驾驶汽车，它允许 Ezblock 程序利用物体检测和颜色识别代码。 在本节中，Ezblock 将用于创建颜色检测程序。

.. note:: 

    在尝试本部分之前，请确保树莓派相机的 FFC 电缆已正确且牢固地连接。 有关牢固连接 FCC 电缆的详细说明，请参考：:ref:`部件清单和装配说明`。

在这个程序中，Ezblock首先会被告知待检测颜色的HSV（Hue-Saturation-Value）空间范围，然后利用OpenCV对HSV范围内的颜色进行处理去除背景噪声，最后对匹配颜色进行框选。

Ezblock 包括帕克的 6 种颜色模型，“红色”、“橙色”、“黄色”、“绿色”、“蓝色”和“紫色”。 色卡已在以下 PDF 中准备好，需可以下载下来打印。

* :download:`[PDF]颜色卡 <https://gitee.com/sunfounder/sf-pdf/raw/master/prop_card/object_detection/color-cards.pdf>`

.. image:: img/block/color_card.png
    :width: 600

.. note::

    由于打印机碳粉或打印介质（如棕褐色纸）的不同，打印颜色可能与颜色模型的色调略有不同。这可能会导致不太准确的颜色识别。


.. image:: img/block/ezblock_color_detect.PNG

**提示**

.. image:: img/block/sp210512_121105.png

从远程控制页面拖动视频小部件，它将生成一个视频监视器。 

.. 有关如何使用视频小部件的更多信息，请参阅此处的 Ezblock 视频教程： `如何使用视频功能？ <https://docs.sunfounder.com/projects/ezblock3/en/latest/use_video.html>`_

.. image:: img/block/sp210512_121125.png

通过将 **视频监视器** 块设置为 **开** 来启用视频监视器。 注意：将 **视频监视器** 设置为 **关** 将关闭监视器，但对象检测仍然可用。

.. image:: img/block/sp210512_134133.png

使用 **颜色检测** 块来启用颜色检测。 注意：一次只能检测一种颜色。

**示例**

.. image:: img/block/sp210512_134636.png