Welcome to PiCar-X's documentation!
===================================

Thanks for choosing our PiCar-X.

PiCar-X is an AI self-driving robot car for Raspberry Pi, on which RPi works as the 
control center. The mounted camera module, ultrasonic module, line tracking module 
can separately realize the functions of color detection, face detection, automatic 
obstacle avoidance, automatic line tracking, etc.

对于本文，您被建议的阅读顺序是:

1. :ref:`Introduction` ，了解PiCar-X与自动驾驶的背景。
#. 核对你的零件没有缺失。
#. Building the PiCar-x 。

   .. note:: 在进行小车构建（到安装舵机步骤）的时候，你会被要求完成 :ref:`Quick Guide on Ezblock` 或者 :ref:`Quick Guide on Python` 。当然你也可以完成其中一个Quick Guide后再进行组装。

#. Check :ref:`Ezblock Project` 或者 :ref:`Python Project`。

如遇到了问题，请查看 :ref:`FAQ` 或者 send an email to service@sunfounder.com .


**Two Ways to Play**


如果你想避免艰难晦涩的 coding ，想要快速玩耍PiCar-X，可以直接进行基于 Ezblock 的使用。它将会需要你按照 :ref:`Quick Guide on Ezblock` 的指示完成配置 —— 
Ezblock Studio is a development platform developed by SunFounder designed for beginners to lower the barriers to getting started with Raspberry Pi. 
It has two programming languages: Graphical and Python, and available on almost all different types of devices. 
With Bluetooth and Wi-Fi support, you can download code, remote control a Raspberry Pi, on Ezblock Studio.

如果你更适应于传统编程的用户，我们建议你使用基于 Python 的玩法，这将要求你掌握基本的 Python 编程技能和基本的 Linux 操作系统知识。
请遵照 :ref:`Quick Guide on Python` 的指示，从源生的 Raspberry Pi OS 中配置出适应PiCar-X运作的环境。


**Content**

.. toctree::
   :maxdepth: 2

   introduction
   quick_guide_on_ezblock  
   example_ezblock
   quick_guide_on_python    
   example_python
   faq

Copyright Notice
--------------------------

All contents including but not limited to texts, images, and code in this manual are owned by the SunFounder Company. You should only use it for personal study,investigation, enjoyment, or other non-commercial or nonprofit purposes, under therelated regulations and copyrights laws, without infringing the legal rights of the author and relevant right holders. For any individual or organization that uses these for commercial profit without permission, the Company reserves the right to take legal action.


   