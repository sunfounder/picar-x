.. _play_python:

玩转 Python
=======================

对于想用 Python 编程的初学者来说，掌握一些基础 Python 技能并熟悉 Raspberry Pi OS 会非常有帮助。  
本章节将一步步带你从设置树莓派开始，逐渐实现 PiCar-X 的运动控制、计算机视觉，再到语音与 AI 交互。

.. _quick_guide_python:

1. Python 快速入门
---------------------------

学习如何搭建 Raspberry Pi 环境：  
安装树莓派操作系统、配置 Wi-Fi，并启用远程访问，让你可以轻松运行 Python 代码。  
如果你已经熟悉树莓派的基本使用和命令行操作，可以直接跳过本部分进入后续章节。

.. toctree:: 
    :maxdepth: 1
    
    ../_shared/pi_start/need_components
    ../_shared/pi_start/install_os_trixie
    ../_shared/pi_start/power_supply_robot_hat
    ../_shared/pi_start/set_up_pi
    install_all_modules
    py_servo_adjust

2. 基础运动控制
-----------------------

在组装完成你的 PiCar-X 之后，从简单的运动程序开始。  
本部分将教你如何控制电机，实现前进、后退、转弯，并使用基础传感器完成避障、循迹等功能。

.. toctree:: 
    :maxdepth: 1
    
    python_calibrate
    python_move
    python_keyboard
    python_avoid
    python_cliff
    python_line_track

3. 计算机视觉
----------------------

让 PiCar-X 通过摄像头“看见”世界。  
本章节涵盖有趣的视觉项目，包括人脸跟踪、录像、与物体互动，以及通过视频或手机 App 控制小车。

.. toctree:: 
    :maxdepth: 1

    python_computer_vision
    python_stare_at_you
    python_record
    python_bull_fight
    python_video_car
    control_by_app
