.. _control_by_app:

12. 通过 APP 控制
==================================

SunFounder Controller 可用于控制基于 Raspberry Pi/Pico 的机器人。

该 APP 集成了按钮、开关、摇杆、方向键、滑块和推力滑块等控件；还包含数字显示、超声雷达、灰度检测和速度计等输入控件。

您可以在 17 个区域（A-Q）中放置不同的控件，自定义您的控制器。

此外，该应用程序还支持实时视频流服务。

接下来，让我们使用该 APP 自定义一个 PiCar-X 控制器。

**操作步骤**

#. 安装 ``sunfounder-controller`` 模块。

    首先需要安装 ``robot-hat``、 ``vilib``  和 ``picar-x`` 模块，详细说明见：:ref:`install_all_modules`。

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~
        git clone https://github.com/sunfounder/sunfounder-controller.git
        cd ~/sunfounder-controller
        sudo python3 setup.py install

#. 运行代码。

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/picar-x/example
        sudo python3 12.app_control.py


#. 从 **APP Store(iOS)** 或 **Google Play(Android)** 下载并安装 `SunFounder Controller <https://docs.sunfounder.com/projects/sf-controller/en/latest/>`_。

#. 打开并创建一个新的控制器。

    在 SunFounder Controller APP 中点击 “+” 图标创建一个新的控制器。

    .. image:: img/app1.jpg

    在预设区域中，有一些产品的预设控制器可供选择，您可以根据需要使用。在这里，我们选择 **PiCar-X**。

    .. image:: img/app_control_preset.jpg

#. 连接到 PiCar-X。

    点击 **Connect** 按钮后，APP 会自动搜索附近的机器人。其名称在 ``picarx_control.py`` 文件中定义，并且必须始终处于运行状态。

    .. image:: img/app9.jpg
    
    点击产品名称后，会出现 “连接成功” 的提示信息，产品名称将显示在右上角。

    .. image:: img/app10.jpg

    .. note::

        * 请确保您的移动设备连接到与 PiCar-X 相同的局域网。
        * 如果无法自动搜索，您也可以手动输入 IP 地址进行连接。

        .. image:: img/app11.PNG

#. 启动控制器。

    点击 **Run** 按钮启动控制器，您将看到车辆拍摄的画面，现在您可以使用这些控件来操作您的 PiCar-X。

    .. image:: img/app12.png
    
    以下是控件的功能说明：

    * **A**：显示车辆当前速度。
    * **E**：启动避障功能。
    * **I**：启动循迹功能。
    * **J**：语音识别，按住此控件开始讲话，松开后显示识别的语音。代码中设置了 ``forward``、 ``backward`` 、 ``left`` 和 ``right`` 四个命令来控制车辆。
    * **K**：控制车辆前进、后退、左转和右转。
    * **Q**：控制摄像头（头部）上下左右移动。
    * **N**：启动颜色识别功能。
    * **O**：启动人脸识别功能。
    * **P**：启动物体识别功能，可识别近 90 种物体，具体模型列表请参考：https://github.com/sunfounder/vilib/blob/master/workspace/coco_labels.txt。
