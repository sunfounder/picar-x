Introduction 
====================

Experiments have been conducted on self-driving cars since at least the 1920s; promising trials took place in the 1950s and work has proceeded since then. 
The first self-sufficient and truly autonomous cars appeared in the 1980s, 
with Carnegie Mellon University's Navlab and ALV projects in 1984 and Mercedes-Benz and Bundeswehr University Munich's Eureka Prometheus Project in 1987. 
Since then, numerous major companies and research organizations have developed working autonomous vehicles including Mercedes-Benz, General Motors, 
Continental Automotive Systems, Autoliv Inc., Bosch, Nissan, Toyota, Audi, Volvo, Vislab from University of Parma, Oxford University and Google. 
In July 2013, Vislab demonstrated BRAiVE, a vehicle that moved autonomously on a mixed traffic route open to public traffic.
As of 2019, twenty-nine U.S. states have passed laws permitting autonomous cars.

Some UNECE members and EU members and the UK have some rules and regulations related to automated and fully automated cars: 
In Europe, cities in Belgium, France, Italy and the UK are planning to operate transport systems for driverless cars, and Germany, 
the Netherlands, and Spain have allowed testing robotic cars in traffic.
In 2020, the UK, the EU and Japan are also on track to regulate automated cars.

* REF: `History of self-driving cars - Wikipedia <https://en.wikipedia.org/wiki/History_of_self-driving_cars>`_


如今，自动驾驶已经是最为近在咫尺的技术革命。有专家预测，大约在2025年，四级汽车有可能进入市场。允许驾驶员将注意力完全转移到其他事物上，并且只要系统正常运行，便不再需要关注交通状况。

* `SAE Levels of Driving Automation™  <https://www.sae.org/blog/sae-j3016-update>`_
* `ABI Research Forecasts 8 Million Vehicles to Ship with SAE Level 3, 4 and 5 Autonomous Technology in 2025 <https://www.abiresearch.com/press/abi-research-forecasts-8-million-vehicles-ship-sae-level-3-4-and-5-autonomous-technology-2025/>`_

近来在软件(人工智能)，硬件(GPUs, FPGAs等等)和云计算的飞速发展正在推动着这一个技术革命。

* 2010年10月，由意大利技术公司Vislab设计的无人驾驶货车历时三个月，`从意大利开始到达中国 <http://edition.cnn.com/2010/TECH/innovation/10/27/driverless.car/>`_ ，里程全长8,077英里。
* 2015年4月，由德尔福汽车公司（Delphi Automotive）设计的汽车从 `旧金山到纽约 <https://money.cnn.com/2015/04/03/autos/delphi-driverless-car-cross-country-trip/>`_ ，穿越了3400英里，在计算机控制下完成了该距离的99％。 
* 2018年12月，Alphabet的Waymo在亚利桑那州推出了 `4级自动驾驶出租车服务 <https://www.reuters.com/article/us-waymo-selfdriving-focus/waymo-unveils-self-driving-taxi-service-in-arizona-for-paying-customers-idUSKBN1O41M2>`_ ，在那里之前他们已经测试无人驾驶汽车-座位上没有安全驾驶员-超过一年，超过1000万英里。
* 2020年10月，百度在北京全面开放 `Apollo Robotaxi自动驾驶出租车服务 <http://autonews.gasgoo.com/icv/70017615.html>`_ 。行车路线将覆盖当地的居民区、商业休闲区及工业园区等多维度实用生活场景。

然而尽管每天都能收集到大量数据（包括真实的驾驶记录和仿真场景的训练数据），却任未能完全满足自动驾驶车辆日益增长的AI模型的复杂度。
根据 `RAND的报道 <https://www.rand.org/pubs/research_reports/RR1478.html>`_ ，达到这个级别的自主学习，需要训练数亿英里甚至数千亿英里的训练数据，以证明可靠性。

因此，尽管自动驾驶汽车的未来充满希望和令人兴奋，但距离技术成熟和全面普及还有几年的路程。

要想让一种技术的能够快速成熟，那最好的方法是让每个人都能够容易的获得去使用它，尽最大可能的降低入门的条件。这正是我们推出PiCar-X的主要动机。
我们目标是帮助自动驾驶初学者以及想要了解自动驾驶的同学了解其发展历程、技术概论以及最新的动态等内容。


About PiCar-X
-------------------

PiCar-X is an AI self-driving robot car for Raspberry Pi, on which RPi works as the control center. 
The mounted camera module, ultrasonic module, line tracking module can separately realize the functions of color detection, 
face detection, automatic obstacle avoidance, automatic line tracking, etc.

其所有的功能（包括GPIO控制、计算机视觉和深度学习），是由Python（实际编程语言），OpenCV（功能强大的计算机视觉软件包）和Tensorflow（Google流行的深度学习框架）等软件实现的。


Think Further
---------------------
这是可选阅读。如果您想更深入地学习深度学习，这里还有一些其他资源可供您参考。

`Machine Learning - Andrew Ng <https://www.coursera.org/learn/machine-learning>`_ : This course provides a broad introduction to machine learning, datamining, and statistical pattern recognition. 

`Neural Networks and Deep Learning <http://neuralnetworksanddeeplearning.com/>`_ : This book will teach you about: Neural networks, a beautiful biologically-inspired programming paradigm which enables a computer to learn from observational data. Deep learning, a powerful set of techniques for learning in neural networks

`Rethinking the Inception Architecture for Computer Vision <https://arxiv.org/abs/1512.00567>`_ : Exploring ways to scale up networks in ways that aim at utilizing the added computation as efficiently as possible by suitably factorized convolutions and aggressive regularization.