介绍
====================


自动驾驶汽车的历史
----------------------------------------

至少从20世纪20年代开始，就已经进行了自动驾驶汽车的实验。
1950年代进行了有希望的试验，此后工作一直在向前推进。
第一辆自给自足和真正的自动驾驶汽车出现在20世纪80年代。
1984年，卡耐基梅隆大学的Navlab和ALV项目。
以及1987年梅赛德斯-奔驰和慕尼黑联邦国防大学的Eureka Prometheus项目。自20世纪80年代末以来。
许多研究机构和主要的汽车制造商已经开发出可以使用的自动驾驶车辆。
包括。梅赛德斯-奔驰、通用汽车、大陆汽车系统、Autoliv公司、博世、日产、丰田。
奥迪、沃尔沃、帕尔马大学的Vislab、牛津大学和谷歌。
2013年7月，Vislab展示了BRAiVE，一辆在向公众开放的混合交通路线上自主行驶的车辆。
截至2019年，美国有29个州已经通过法律，允许自动驾驶汽车在公共道路上行驶。

一些联合国欧洲经济委员会成员和欧盟成员，包括英国。
已经颁布了与自动驾驶和全自动驾驶汽车有关的规则和条例。
在欧洲，比利时、法国、意大利和英国的城市已经制定了运营无人驾驶汽车运输系统的计划。
而德国、荷兰和西班牙已经允许在公共交通中测试机器人汽车。
2020年，英国、欧盟和日本已经走上了规范自动驾驶汽车的轨道。

.. * Reference: `History of self-driving cars - Wikipedia <https://en.wikipedia.org/wiki/History_of_self-driving_cars>`_


今天，自动驾驶汽车是目前最接近的技术革命。一些专家预测，到2025年，4级汽车可能会进入市场。4级汽车将允许司机将注意力完全转移到其他方面，只要系统运行正常，就不需要注意交通状况。

.. 分级参考:

.. * `SAE Levels of Driving Automation™  <https://www.sae.org/blog/sae-j3016-update>`_
.. * `ABI Research Forecasts 8 Million Vehicles to Ship with SAE Level 3, 4 and 5 Autonomous Technology in 2025 <https://www.abiresearch.com/press/abi-research-forecasts-8-million-vehicles-ship-sae-level-3-4-and-5-autonomous-technology-2025/>`_

.. .. image:: img/self_driving_car.jpeg

.. 最近，软件（人工智能、机器学习）、硬件（GPU、FPGA、加速计等）和云计算的快速发展正在推动这场技术革命向前发展。

.. * 2010年10月，意大利技术公司 **Vislab** 设计的一辆无人驾驶卡车花了三个月时间， `从意大利到中国 <http://edition.cnn.com/2010/TECH/innovation/10/27/driverless.car/>`_ ，总距离为8，077英里。
.. * 2015年4月，一辆由 **Delphi Automotive** 设计的汽车从 `旧金山到纽约 <https://money.cnn.com/2015/04/03/autos/delphi-driverless-car-cross-country- trip/>`_ ，穿越了3400英里，在计算机控制下完成了该距离的99%。
.. * 2018年12月， **Alphabet** 的 **Waymo** 在亚利桑那州推出了 `4级自动驾驶出租车服务 <https://www.reuters.com/article/us-waymo-selfdriving-focus/waymo-unveils-self-driving-taxi-service-in-arizona-for-paying-customers-idUSKBN1O41M2>`_ ，他们从2008年开始就在那里测试无人驾驶汽车。在无人驾驶的情况下，这些车辆运行了一年多，行驶了超过1000万英里。
.. * 2020年10月， **百度** 在北京全面开通了 `阿波罗Robotaxi 自动驾驶出租车服务 <http://autonews.gasgoo.com/icv/70017615.html>`_ 。驾驶路线覆盖了当地的住宅、商业、休闲和工业园区等区域，并提供完全自主的驾驶系统。

然而，尽管每天都收集了大量的数据，包括来自真实驾驶记录和模拟场景的训练数据，但自动驾驶汽车的人工智能模型的复杂性还没有完全满足。

根据兰德公司的报告，达到适当的自主学习水平需要来自数亿，甚至数千亿英里的训练数据，以建立一个可靠性的水平。

..`兰德公司的报告 <https://www.rand.org/pubs/research_reports/RR1478.html>`_ 

因此，尽管自动驾驶汽车的未来很有希望，令人振奋，但在技术成熟到可以完全进入自动驾驶汽车市场之前，还有很多年的发展时间要走。

让一项新兴技术迅速成熟的行之有效的方法是，通过最大限度地减少市场准入要求，使每个人都能轻松获得该技术。
这就是Emakefun推出帕克的动机。

Emakefun的目标是帮助初学者、新手和那些只是想了解自动驾驶的人，了解自动驾驶汽车的开发过程、技术和最新创新。


关于帕克
-------------------

.. image:: img/picar-x.jpg

帕克是树莓派平台的人工智能控制的自动驾驶机器人汽车，在此基础上，树莓派充当控制中心。帕克的2轴摄像头模块、超声波模块和线路跟踪模块可以提供颜色/脸部/交通标志检测、自动避障、自动线路跟踪等功能。

通过Emakefun设计的Robot HAT板，帕克集成了左/右驱动电机、用于转向的伺服电机和摄像头的平移/倾斜功能，并预先设置了Robot HAT的ADC、PWM和数字I2C引脚，以实现对Raspberry Pi标准功能的扩展。一个扬声器和一个蓝牙芯片都被设计到Robot HAT中，用于远程控制文字转语音、声音效果，甚至背景音乐功能。

帕克的所有功能，包括GPIO控制、计算机视觉和深度学习，都是通过开源的Python编程语言、OpenCV的计算机视觉库软件和谷歌的TensorFlow深度学习框架实现的。其他软件也被包括在内，以优化帕克的能力，让用户有一个接近无限的学习环境。


深度学习和神经网络
-------------------------------------------------
要了解更多关于深度学习和神经网络的信息，Emakefun推荐以下资源。

`机器学习--Andrew Ng <https://www.coursera.org/learn/machine-learning>`_ ：该课程对机器学习、数据挖掘和统计模式识别进行了广泛介绍。

`神经网络和深度学习 <http://neuralnetworksanddeeplearning.com/>`_ : 这本电子书涵盖了神经网络和深度学习，前者是一种受生物启发的编程范式，使计算机能够从观察数据中学习，后者是神经网络中机器学习的一套强大技术。

`重新思考计算机视觉的初始架构 <https://arxiv.org/abs/1512.00567>`_ ：这篇高水平的白皮书探讨了用户可以通过因子化卷积和积极的正则化，尽可能有效地利用增加的计算来扩展网络的方法。