.. _picarx_skill:

.. start_using_picarx

22. 使用 OpenClaw 控制 PiCar-X
========================================


**什么是 OpenClaw？**

可以将其视为 ChatGPT 的升级版。传统聊天机器人只能对话（生成文本），而 OpenClaw 可以采取行动。它能理解您的自然语言指令，并实际在您的计算机上执行操作，例如运行命令、管理文件以及调用各种工具。

以下是一些精彩的应用场景：

* **个人全能助手：** 让它帮您管理日程、设置提醒、追踪任务。您只需在聊天应用（如 Telegram、WhatsApp）中告诉它，它就会记住并执行。
* **自动化"胶水"：** 它可以充当您各种服务之间的粘合剂。例如，您可以让它监控某个网站的价格变化。一旦检测到降价，它可以自动触发 n8n 自动化工作流向您发送邮件通知。
* **专属开发助手：** 让它帮您管理服务器、运行脚本、查看日志。您只需说"帮我检查一下系统负载"，它就能通过 SSH 登录您的服务器，执行命令并返回结果。
* **硬件"玩伴"：** 这是一个非常有趣的应用场景。您可以让 OpenClaw 控制连接到 Raspberry Pi 的硬件。例如，有开发者用它来控制带机械臂的扫地机器人，甚至让它帮忙分析赛车模拟器数据并显示在 LED 屏幕上。官方 Raspberry Pi 团队甚至用它为一个婚礼搭建了自动拍照亭，全程通过对话完成，一行代码都没写！


.. important::

   Raspberry Pi Zero 2W 只有 512MB 内存，而 OpenClaw 最低要求 1GB，因此无法正常运行。建议使用 Raspberry Pi 4/5 或更高版本。

快速启动 OpenClaw
------------------------------

如果您想尽快体验 OpenClaw 的强大功能，请使用此方法。它将自动安装并启动一个交互式设置向导。

1.  在 Raspberry Pi 上打开终端，直接运行以下命令。此命令将从官网下载安装脚本并执行：

    .. code-block:: bash

       curl -fsSL https://openclaw.ai/install.sh | bash

    .. note:: 由于新版本更新速度很快，如果您的安装步骤略有不同，这是正常现象。

2.  脚本将自动下载并安装 OpenClaw。

    .. image:: /img/openclaw/install_open_claw.png


3.  接下来您会看到一个安全提示，询问您是否信任 OpenClaw。确认它安全可靠后，使用方向键选择"Yes"并按 Enter。

    .. image:: /img/openclaw/security_open_claw.png


4.  选择 Quick Start，然后按 Enter。

    .. image:: /img/openclaw/quickstart_open_claw.png

5.  选择您的模型，然后按 Enter。这里以 OpenAI 为例。

    .. image:: /img/openclaw/model_provider_open_claw.png

6.  选择 OpenAI API Key。

    .. image:: /img/openclaw/api_key_open_claw.png

7.  立即粘贴 API key。

    .. image:: /img/openclaw/paste_api_key_open_claw.png

8.  前往 |link_openai_platform| 并登录。在 **API keys** 页面，点击 **Create new secret key**。

    .. image:: /img/openclaw/llm_openai_create.png

9.  填写详细信息（Owner、Name、Project 以及权限（如有需要）），然后点击 **Create secret key**。

    .. image:: /img/openclaw/llm_openai_create_confirm.png

10. 密钥创建后，请立即复制——您将无法再次查看。如果丢失，需要重新生成。

    .. image:: /img/openclaw/llm_openai_copy.png

11. 将密钥粘贴到 OpenClaw 配置中。

    .. image:: /img/openclaw/paste_api_key_enter_open_claw.png

12. 选择您要使用的模型。在本示例中，我们将使用 **Keep current**。

    .. image:: /img/openclaw/model_config_open_claw.png

13. 接下来是通道（Channel）选择。通道是指 OpenClaw 支持的通信服务，如 Telegram、WhatsApp、Discord 等。使用下方向键选择"Skip for now"选项，然后按 Enter。

    .. image:: /img/openclaw/channel_open_claw.png

14. 接下来会提示您立即配置技能（Skills）。选择"Yes"并按 Enter。

    .. image:: /img/openclaw/config_skill_open_claw.png

15. 安装您需要的技能。在以下示例中，我们选择"Skip for now"选项（按空格键选择），然后按 Enter。

    .. image:: /img/openclaw/install_skill_open_claw.png


16. 接下来是 Hooks；我们将勾选"command-logger"和"session-memory"。

    .. image:: /img/openclaw/hooks2_open_claw.png


17. 安装完成。选择"Hatch in TUI"并按 Enter 即可启动 OpenClaw。

   .. image:: /img/openclaw/hatch_open_claw.png


.. note::

   您可以通过输入以下命令启动 OpenClaw：

    .. code-block:: bash

       openclaw tui

   按 Ctrl+C 两次可退出 tui 界面。

------------------------------------------------------------------------

让 OpenClaw 操控 PiCar-X
----------------------------------------------

**什么是 PiCar-X Skill？**

PiCar-X Skill 是 OpenClaw 的一个扩展，让您可以通过自然语言控制 SunFounder PiCar-X 机器人小车。无需编写 Python 脚本或记忆舵机角度，您只需告诉 OpenClaw 您想让 PiCar-X 做什么——比如"向前行驶"、"查看前方情况"或"左转"——OpenClaw 就会自动执行相应的 Python 代码。

以下是 PiCar-X Skill 可以做的事情：

* **行驶：** 前进、后退、通过方向舵机控制左右转向
* **摄像头云台：** 通过双轴摄像头云台左右/上下旋转
* **传感器：** 读取超声波距离、灰度传感器数据，用于巡线和悬崖检测
* **声音：** 通过小车扬声器播放音效和音乐
* **摄像头视觉：** 拍照、人脸检测、颜色追踪、二维码识别、手势识别和交通标志识别

----------------------------------------------------------------

前提条件
------------------------------

在使用 PiCar-X Skill 与 OpenClaw 之前，请确保您已具备：

1. **PiCar-X** 已正确组装并连接到 Raspberry Pi
2. **OpenClaw** 已安装并运行
3. 已安装以下 Python 库：

   - ``picarx``
   - ``robot_hat``
   - ``vilib``

您可以通过运行以下命令验证安装：

.. code-block:: bash

   python3 -c "import picarx"

如果此命令运行无报错，即可继续。

----------------------------------------------------------------

安装 PiCar-X Skill
------------------------------

按照以下步骤为 OpenClaw 安装 PiCar-X Skill：

1. **将 PiCar-X Skill 文件复制** 到 OpenClaw 技能目录：

   .. code-block:: bash

      cp -r ~/picar-x/picarx-control ~/.openclaw/workspace/skills/

2. **验证安装**，查看技能文件：

   .. code-block:: bash

      ls ~/.openclaw/workspace/skills/picarx-control/

   您应该看到 ``SKILL.md``、``install.sh``、``scripts/`` 和 ``references/`` 出现在输出中。

该技能的 ``SKILL.md`` 文件包含 OpenClaw 所需的所有指令——安全规则、每种功能的代码模板，以及从自然语言请求到 Python 代码的映射。OpenClaw 读取此文件并使用它来决定在 PiCar-X 上执行什么代码。

----------------------------------------------------------------

从命令行测试 PiCar-X Skill
----------------------------------------------

在使用该技能与 OpenClaw 之前，您可能想通过终端使用附带的 CLI 工具直接测试基本功能。

**检查超声波距离：**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/picarx-control/scripts/pc.py sensor distance

**前进：**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/picarx-control/scripts/pc.py move forward --speed 60

**后退：**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/picarx-control/scripts/pc.py move backward --speed 60

**左转：**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/picarx-control/scripts/pc.py turn left --angle 30

**右转：**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/picarx-control/scripts/pc.py turn right --angle 30

**设置摄像头水平角度：**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/picarx-control/scripts/pc.py cam pan --angle 30

**设置摄像头垂直角度：**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/picarx-control/scripts/pc.py cam tilt --angle 20

**播放音效：**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/picarx-control/scripts/pc.py sound play /path/to/sound.wav --volume 80

**读取灰度传感器数据（巡线）：**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/picarx-control/scripts/pc.py sensor grayscale

**运行舵机校准：**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/picarx-control/scripts/pc.py calibrate

----------------------------------------------------------------

在 OpenClaw 中使用 PiCar-X Skill
----------------------------------------------------

确认 PiCar-X Skill 可以从命令行正常工作后，即可在 OpenClaw 中使用它。

1. **启动 OpenClaw TUI**：

   .. code-block:: bash

      openclaw tui

2. **发送自然语言指令** 来控制 PiCar-X。以下是一些示例：

   * "向前行驶"
   * "后退"
   * "左转"
   * "右转"
   * "检查前方是否有障碍物"
   * "看向左边"
   * "向上看"
   * "向下看"
   * "拍张照片"
   * "检测人脸"
   * "找红色物体"
   * "跟随线路"
   * "检查前方是否有悬崖"

3. **OpenClaw 将自动** 将您的请求转换为相应的 Python 代码并在 PiCar-X 上执行。

----------------------------------------------------------------

可用操作和命令
-------------------------------------------

以下是 PiCar-X Skill 支持的完整功能列表：

行驶（``pc.py move``）
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - 操作
     - 描述
   * - ``forward``
     - 前进
   * - ``backward``
     - 后退

转向（``pc.py turn``）
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - 操作
     - 描述
   * - ``left``
     - 通过调整转向角度左转
   * - ``right``
     - 通过调整转向角度右转

摄像头云台（``pc.py cam``）
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - 功能
     - 描述
   * - 水平旋转
     - 水平旋转摄像头（-90° 至 90°）
   * - 垂直旋转
     - 垂直旋转摄像头（-35° 至 65°）

传感器
^^^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - 命令
     - 描述
   * - ``sensor distance``
     - 读取超声波距离传感器（返回厘米值）
   * - ``sensor grayscale``
     - 读取三通道灰度模块数值（用于巡线和悬崖检测）

声音（``pc.py sound``）
^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - 命令
     - 描述
   * - ``sound play <file>``
     - 播放音效文件
   * - ``sound music <file>``
     - 播放背景音乐
   * - ``sound volume <0-100>``
     - 设置扬声器音量
   * - ``sound stop``
     - 停止播放

.. note::

   声音文件可以是 Raspberry Pi 上可访问的任何 ``.wav`` 格式音频文件。您也可以使用 ``sound music`` 来播放背景音乐文件。

摄像头与视觉（通过自然语言 / exec）
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - 功能
     - 描述
   * - 拍照
     - 拍摄照片并保存到 ``~/Pictures/``
   * - 人脸检测
     - 检测人脸并报告位置
   * - 颜色检测
     - 按颜色定位物体（红、蓝、绿等）
   * - 手势识别
     - 识别石头/布/剪刀手势
   * - 交通标志检测
     - 识别停止/左转/右转/前进标志
   * - 二维码扫描
     - 读取二维码数据和位置

巡线与悬崖检测
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - 功能
     - 描述
   * - 巡线
     - 使用三通道灰度传感器在浅色表面上跟随黑线
   * - 悬崖检测
     - 使用灰度阈值检测边缘/落差

----------------------------------------------------------------

故障排除
------------------------------

OpenClaw 问题
^^^^^^^^^^^^^^^^^^^^^^^^

Q. 安装过程中出现错误 ``Error: systemctl is-enabled unavailable: Command failed: systemctl --user is-enabled openclaw-gateway.service``。该怎么办？

   暂时可以忽略，但在后续步骤中可能会遇到问题。届时请逐一参考解决。


Q. 运行 ``openclaw tui`` 时出现错误 ``-bash: openclaw: command not found``。该怎么办？

   执行以下命令：

   .. code-block:: bash

      echo 'export PATH="$HOME/.npm-global/bin:$PATH"' >> ~/.bashrc
      source ~/.bashrc

   现在您应该可以通过 ``openclaw tui`` 启动 tui 界面了。



Q. 在 ``openclaw tui`` 中遇到 ``not connected to gateway — message not sent`` 或 ``gateway disconnected: closed`` 消息。

   这是因为您的 OpenClaw Gateway 服务未启动。打开另一个终端，执行以下命令启动 OpenClaw Gateway：

   .. code-block:: bash

      openclaw gateway

   然后重新启动 ``openclaw tui``，即可正常使用。


Q. 我想将 OpenClaw Gateway 服务设置为后台运行 / 开机自启。该怎么做？

   通常情况下，OpenClaw Gateway 服务会在开机时自动启动。如果没有，您可以通过以下命令手动启动。

   1. 创建 ``~/.config/systemd/user`` 目录：

   .. code-block:: bash

      mkdir -p ~/.config/systemd/user


   2. 创建 ``openclaw-gateway.service`` 文件：

   .. code-block:: bash

      cat > ~/.config/systemd/user/openclaw-gateway.service << EOF
      [Unit]
      Description=OpenClaw Gateway
      After=network.target

      [Service]
      Type=simple
      ExecStart=$HOME/.npm-global/bin/openclaw gateway run
      Restart=on-failure
      RestartSec=10
      Environment="PATH=$HOME/.npm-global/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin"
      Environment="NODE_ENV=production"

      [Install]
      WantedBy=default.target
      EOF


   3. 然后重新加载 systemd 配置：

   .. code-block:: bash

      systemctl --user daemon-reload

   4. 启动服务：

   .. code-block:: bash

      systemctl --user start openclaw-gateway

   此时重新启动 ``openclaw tui``，即可正常使用。

   5. 设置开机自启：

   .. code-block:: bash

      systemctl --user enable openclaw-gateway


Q. 我的 OpenClaw 无法操作系统，该怎么办？

   新安装的 OpenClaw 可能默认没有操作 Raspberry Pi 系统的权限，只能聊天。我们需要手动配置权限。

   1.  打开 OpenClaw 配置文件：

      .. code-block:: bash

         nano ~/.openclaw/openclaw.json

   2.  找到 ``tools`` 选项，将 ``profile`` 和 ``exec`` 修改为如下所示。

      .. code-block:: json

        "tools": {
            "profile": "coding",
            "exec": {
                "secrity": "full"
            }
        },

   3.  保存并退出。

   4.  在终端输入以下命令重启 OpenClaw Gateway：

      .. code-block:: bash

         openclaw gateway restart

   现在，OpenClaw 应该具有读写权限，能够操作您的 Raspberry Pi 系统了。

PiCar-X 问题
^^^^^^^^^^^^^^^^^^^^^^^^


Q. PiCar-X 不响应命令。该怎么办？

   首先，确认 PiCar-X 已正确连接并通电。然后测试基本功能：

   .. code-block:: bash

      python3 ~/.openclaw/workspace/skills/picarx-control/scripts/pc.py sensor distance

   如果失败，请确保所需的 Python 库已安装：

   .. code-block:: bash

      python3 -c "import picarx; import robot_hat; import vilib"

Q. ``import picarx`` 测试失败。

   这意味着 PiCar-X Python 库未正确安装。请参考 PiCar-X 官方安装指南安装必要的库。您也可以运行附带的安装脚本：

   .. code-block:: bash

      bash ~/.openclaw/workspace/skills/picarx-control/install.sh

Q. OpenClaw 无法识别 PiCar-X Skill。

   在 TUI 中提醒 OpenClaw 同步技能，说：*"Please rsync my skills"* 或重启 OpenClaw Gateway：

   .. code-block:: bash

      openclaw gateway restart

Q. PiCar-X 动作显得突兀或转向偏斜。

   这通常是由于舵机校准值不正确导致的。运行校准脚本来调整方向舵机和摄像头云台：

   .. code-block:: bash

      python3 ~/.openclaw/workspace/skills/picarx-control/scripts/pc.py calibrate

   您也可以调整速度参数（例如使用 ``--speed 40``）来获得更平滑的移动，或在连续命令之间添加短暂延迟。

Q. 灰度传感器或巡线不工作。

   确保灰度模块已针对您的表面进行了正确校准。您可以使用配置设置巡线参考值。请参考 PiCar-X 主文档了解灰度校准步骤。

----------------------------------------------------------------

.. end_using_picarx
