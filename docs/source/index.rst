.. note::

    你好，欢迎来到 SunFounder 树莓派、Arduino 和 ESP32 爱好者社区的 Facebook 页面！与其他爱好者一起深入探讨树莓派、Arduino 和 ESP32。

    **为什么加入？**

    - **专家支持**: 通过我们的社区和团队的帮助解决售后问题和技术挑战。
    - **学习与分享**: 交流技巧和教程，提升你的技能。
    - **独家预览**: 提前了解新产品发布和预告。
    - **特别折扣**: 尊享我们最新产品的专属折扣。
    - **节日促销和赠品**: 参与赠品活动和节日促销。

    👉 准备好与我们一起探索和创造了吗？点击 [|link_sf_facebook|] 加入我们吧！

欢迎来到帕克的文档!
===================================

感谢你选择我们的帕克智能小车。

.. note::
   
    本文档支持以下语言版本。

        * |link_zh_tutorials|
        * |link_jp_tutorials|
        * |link_en_tutorials|
    
    请点击相应的链接以选择您偏好的语言版本查阅。

.. warning::

    我们提供两个版本的PiCar-X。需要特别注意的是，每个版本在线教程中的脚本不能互换使用。
    
    为确保正确设置，您需要根据说明书中提供的短链接确定您的版本：

    * 若链接为 "picar-x.rtfd.io"，请继续阅读此教程。
    * 若链接显示为 "picar-x-v20.rtfd.io"，请前往 |link_picarx_v2| 查看教程。

    .. image:: img/short_link.jpg
        :width: 500
        :align: center


.. image:: img/picar-x.jpg
   :width: 400
   :align: center

帕克是树莓派平台的人工智能驱动的自动驾驶机器人小车。
它拥有两轴相机模块、超声波模块和线路跟踪模块可以提供颜色/脸部/交通标志的检测功能以及自动避开障碍物、自动跟踪线路等功能。


本教程包括组件清单、装配图、Robot HAT介绍，以及基于图形化编程和Python语言的帕克编程教程。

编程部分分为两章： :ref:`play_ezblock` 和 :ref:`play_python`。每个编程章节都允许用户从让帕克执行基本动作开始，一直到设计多人游戏，甚至更多的游戏!

EzBlock Studio是SunFounder创建的一个软件开发平台，用于帮助初学者和新手开始在树莓派平台上进行编程。Ezbock Studio有两种编程语言环境：一种是图形用户界面环境，一种是命令行Python环境。

EzBlock几乎可用于所有类型的设备，包括Mac、PC和Android。EzBlock最近已经升级到3.0版本，它使用WebSocket提供蓝牙和Wi-Fi支持。

对于只想学习Python 3.0编程的用户，还包括树莓派操作系统的基础知识介绍，以及提供基本Python编程技能的教程。

**目录**

.. toctree::
   :maxdepth: 2

   关于帕克 <self>
   introduction
   list_and_assembly
   about_robot_hat 
   ezblock/play_with_ezblock
   python/play_with_python
   appendix/appendix
   faq

版权声明
--------------------------

本手册中包括但不限于文字、图片、代码等所有内容均归SunFounder公司所有。 根据相关规定和版权法，您只能将其用于个人学习、调查、欣赏或其他非商业或非营利目的，不得侵犯作者和相关权利人的合法权利。 对于任何个人或组织未经许可将其用于商业利益，本公司保留采取法律行动的权利。