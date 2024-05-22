.. note::

    你好，欢迎来到 SunFounder 树莓派、Arduino 和 ESP32 爱好者社区的 Facebook 页面！与其他爱好者一起深入探讨树莓派、Arduino 和 ESP32。

    **为什么加入？**

    - **专家支持**: 通过我们的社区和团队的帮助解决售后问题和技术挑战。
    - **学习与分享**: 交流技巧和教程，提升你的技能。
    - **独家预览**: 提前了解新产品发布和预告。
    - **特别折扣**: 尊享我们最新产品的专属折扣。
    - **节日促销和赠品**: 参与赠品活动和节日促销。

    👉 准备好与我们一起探索和创造了吗？点击 [|link_sf_facebook|] 加入我们吧！

文字转语音
============================

在使用文字转语音 (TTS) 功能之前，请先激活扬声器，使其启用并可以发出声音。

在 **picar-x** 文件夹中运行 ``i2samp.sh``，此脚本将安装使用 i2s 放大器所需的一切。

**运行代码**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/picar-x
    sudo bash i2samp.sh 

.. image:: img/tt_bash.png

会有几个提示要求确认请求。 用 **Y** 响应所有提示。 对树莓派系统进行更改后，需要重新启动计算机才能使这些更改生效。

重新启动后，再次运行 ``i2samp.sh`` 脚本来测试放大器。 如果扬声器成功播放声音，则配置完成。

**运行代码**

.. raw:: html

    <run></run>

.. code-block::

    cd /home/pi/picar-x/example
    sudo python3 tts_example.py
    
运行代码后，帕克会说“你好”、“嗨”、“再见”、“很高兴见到你”。

**代码**

.. .. note::
..     您可以 **修改/重置/复制/运行/停止** 下面的代码。 但在此之前，您需要转到像 ``picar-x/example`` 这样的源代码路径。 修改代码后，可以直接运行看看效果。

.. raw:: html

    <run></run>

.. code-block:: python

    from robot_hat import TTS


    if __name__ == "__main__":
        words = ["Hello", "Hi", "Good bye", "Nice to meet you"]
        tts_robot = TTS()
        for i in words:
            print(i)
            tts_robot.say(i)


**这个怎么运作？**

`eSpeak <http://espeak.sourceforge.net/>`_ 软件用于实现TTS的功能。

导入 robot_hat 中的 TTS 模块，其中封装了可以将文字转换成语音的函数。

.. code-block::

    from robot_hat import TTS

创建一个字符串列表 ``words`` ，然后创建TTS()类的实例化对象 ``tts_robot`` ，最后用 ``tts_robot.say()`` 函数将列表中的文字用语音说出来。

.. code-block::

    words = ["Hello", "Hi", "Good bye", "Nice to meet you"]
    tts_robot = TTS()
    for i in words:
        print(i)
        tts_robot.say(i)