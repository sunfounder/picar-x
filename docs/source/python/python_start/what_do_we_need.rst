1. 你还需要准备什么？
===============================

在开始使用 PiCar-X 之前，我们先来准备必要的硬件。  
这些部件就像是 PiCar-X 的 **大脑、心脏和感官**——缺少它们，小车就无法正常运行。

必需组件
------------------------------

* **Raspberry Pi（树莓派）**

  树莓派是 PiCar-X 的“大脑”，负责所有计算、感知和控制任务。
  
  .. image:: img/need_pi.jpg

  * **兼容型号**：支持 Raspberry Pi 5、4、3 以及 Raspberry Pi Zero 2 W（推荐 Pi 5 或 Pi 4）。  
  * **最低配置**：2GB RAM —— 足够运行 PiCar-X 的基本功能（运动、传感器、摄像头流）以及 **在线 AI 服务** （如 OpenAI Whisper、TTS 或 LLM）。  
  * **推荐配置**：4GB RAM 或以上 —— 能流畅运行 **本地 AI 模型** （如 Vosk 语音识别、Piper TTS、轻量级 LLM）并同时进行摄像头流媒体与控制任务。
  

* **电源适配器**

  PiCar-X 配有 **18650 电池组** 和带有充电电路的 **Robot HAT** 控制板。
  
  .. image:: img/need_power.png
    :width: 400

  * 充电建议使用 **5V 3A 电源适配器**，例如官方的 **Raspberry Pi 15W USB-C 适配器**。  
  * 也可以使用 **USB-C PD 快充** 或 **QC 2.0 快充**。  
  * 从 0% 充到 100% 通常约需 **2 小时**。
  

* **Micro SD 卡**

  树莓派没有内置硬盘，系统启动和所有文件都保存在 **Micro SD 卡** 上。
  
  .. image:: img/need_sd.jpg
    :width: 200

  * 最低容量：16GB  
  * 推荐容量：32GB（更稳定）  
  * 品牌建议：使用 **SanDisk** 或 **Samsung** 等可靠品牌，避免读写错误。
  

可选组件
------------------------

这些不是必须的，但能大大提升你的体验，尤其是调试时非常有用：

* **显示器（HDMI 或电视）**

  对初学者非常友好，可以更直观地设置树莓派系统并运行图形程序。
  
  .. image:: img/need_screen.png
    :width: 400

* **HDMI 连接线（标准 / Mini / Micro）**
 
  不同树莓派型号的 HDMI 接口不同，请准备对应的线缆：
  
  * Raspberry Pi 4 / 5：Micro HDMI  
  * Raspberry Pi 3：标准 HDMI  
  * Raspberry Pi Zero 2W：Mini HDMI

  .. image:: img/need_hdmi.png
    :width: 400

* **键盘与鼠标**

  在树莓派系统初始配置时非常实用。后续可通过 SSH/VNC 远程访问，但我们建议初学者准备一套基础 USB 或无线键鼠。
  
  .. image:: img/need_keyboard_mouse.png
    :width: 500
  

**准备小贴士**

* 如果你购买了 **PiCar-X 套件**，大部分配件已经包含，但仍需自行准备 Raspberry Pi 主板、Micro SD 卡和电源适配器。  
* 不知道该买什么？👉 最稳定、通用的选择是：  
  **Raspberry Pi 4（2GB） + 官方电源 + 32GB Micro SD 卡**。
