.. _setup_pi:

4. 设置树莓派
============================

在开始编程和控制 PiCar-X 之前，你需要先访问你的树莓派。  
本节将介绍两种常见的连接方式：使用 **显示器、键盘和鼠标**，或者使用 **无屏幕（Headless）方式** 远程登录。

如果你有屏幕
-------------------------

.. note:: 安装在机器人上的 Raspberry Pi Zero 2W 不便于连接显示器，推荐使用 **无屏幕（Headless）** 方式。

**所需组件**

* Raspberry Pi  
* 电源适配器  
* Micro SD 卡  
* HDMI 线  
* 显示器  
* 鼠标  
* 键盘  

#. 将 microSD 卡插入树莓派。  
#. 连接鼠标、键盘和显示器（对于 Pi 4/5，使用靠近电源接口的 **HDMI0** 端口）。  
#. 给树莓派通电。  
#. 片刻后，你将看到 Raspberry Pi OS 桌面，可以打开终端输入命令。

    .. image:: img/bookwarm.png
        :align: center


如果你没有屏幕（Headless 无屏幕设置）
-----------------------------------------

没有显示器时，你可以通过网络远程登录树莓派，这是最方便的方式。

**所需组件**

* Raspberry Pi  
* 电源适配器  
* Micro SD 卡  
* 与树莓派在同一局域网内的电脑  

**提示**

* 设置正确的 **无线局域网国家代码** （使用 ISO/IEC alpha-2 代码，例如 ``US``、``UK``、``CN``），否则 Wi-Fi 可能无法正常工作。  
* 确保树莓派与电脑处于同一局域网。  
* 如有条件，使用网线连接更稳定。

**通过 SSH 连接**

1. 在电脑上打开终端（Windows：**PowerShell**，macOS/Linux：**Terminal**），输入：

   .. code-block::

      ssh <用户名>@<主机名>.local
      # 例如：
      ssh daisy@picarx.local

2. 或者，在路由器中查看 DHCP/客户端列表，找到树莓派的 IP，然后使用：

   .. code-block::

      ssh <用户名>@<IP>
      
      # 例如：
      ssh daisy@192.xxx.xx.xx

3. 首次登录时，会出现安全提示，输入 ``yes`` 继续。  

4. 输入你在 Raspberry Pi Imager 中设置的密码。（输入时不显示字符，这是正常的。）

   .. note::
      密码输入时不显示任何字符，这是标准的安全机制，只需认真输入即可。

5. 登录成功后，即可开始远程操作树莓派。

   .. image:: img/ssh_login.png
      :align: center

**故障排查**

* **ssh: Could not resolve hostname ...**  
  * 检查主机名是否输入正确。  
  * 如果仍然失败，使用 IP 地址代替 ``<hostname>.local``。

* **The term 'ssh' is not recognized...（Windows）**  
  * 系统未安装 OpenSSH。请手动安装（见 :ref:`openssh_powershell`），或使用第三方 SSH 客户端（见 :ref:`login_windows`）。

* **Permission denied (publickey,password)**  
  * 确保使用的是在 Raspberry Pi Imager 中设置的用户名和密码。

* **Connection refused**  
  * 通电后等待 1–2 分钟。  
  * 确认已在 Raspberry Pi Imager 中启用 SSH。

**图形界面访问方式**

如果你更喜欢图形界面而不是命令行，有两种方式可选：

    .. image:: img/bookwarm.png
        :align: center

* :ref:`remote_desktop`：启用 **VNC 虚拟网络计算**，即可像使用桌面一样访问树莓派。  
* |link_rpi_connect|：使用 **Raspberry Pi Connect**，通过浏览器从任何地方安全访问树莓派。

这样，你就可以在没有显示器的情况下，通过 **SSH 命令行** 或 **VNC / Raspberry Pi Connect 图形界面** 控制你的树莓派了。
