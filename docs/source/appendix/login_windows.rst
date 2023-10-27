.. _login_windows:

PuTTY
=========================
 
如果你是Windows用户，你可以使用一些SSH应用程序。在这里，我们推荐 `PuTTY <https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html>`_。

**步骤1**

下载PuTTY。

**步骤2**

打开PuTTY，点击左侧的树状结构中的 **会话(Session)**。在 **主机名(或IP地址)（Host Name (or IP address)）** 下的文本框中输入RPi的IP地址，并在 **端口(Port)** 下输入 **22** （默认为22）。

.. image:: img/image25.png
    :align: center

**步骤3**

点击 **打开(Open)**。请注意，当你首次使用IP地址登录树莓派时，会提示一个安全提醒。只需点击 **是(Yes)**。

**步骤4**

当PuTTY窗口提示 **登录为(login as):**，输入 **pi** （RPi的用户名）和 **密码(password)**。

.. note::

    当你输入密码时，字符不会在窗口上显示，这是正常的。你需要做的是输入正确的密码。
    
    如果PuTTY旁边显示为不活动(inactive)，意味着连接已经断开，需要重新连接。
    
.. image:: img/image26.png
    :align: center

**步骤5**

在这里，我们已经连接上了树莓派，现在是进行下一步的时候了。
