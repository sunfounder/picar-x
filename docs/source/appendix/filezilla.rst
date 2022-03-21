.. _filezilla:

Filezilla 软件
==========================

.. image:: img/filezilla_icon.png

文件传输协议 (FTP) 是一种标准通信协议，用于在计算机网络上将计算机文件从服务器传输到客户端。

Filezilla 是一款开源软件，不仅支持 FTP，还支持 FTP over TLS (FTPS) 和 SFTP。 我们可以使用 Filezilla 将本地文件（如图片和音频等）上传到树莓派，或者从树莓派下载文件到本地。

**第1步**:下载 Filezilla。

在 `Filezilla 官方网站 <https://filezilla-project.org/>`_ 下载客户端, Filezilla 有一个很好的教程，请参考: `Filezilla文档 <https://wiki.filezilla-project.org/Documentation>`_ 。

**第2步**: 连接树莓派

快速安装后打开它，现在 `连接到 FTP 服务器 <https://wiki.filezilla-project.org/Using#Connecting_to_an_FTP_server>`_。

它有 3 种连接方式，这里我们使用 **快速连接** 栏。 输入 **主机名/IP** 、 **用户名** 、 **密码** 和 **端口（22）** ，然后点击 **快速连接** 或按 **回车** 连接到服务器。

.. image:: img/filezilla_connect.png

.. note::

    快速连接是测试您的登录信息的好方法。 如果要创建永久条目，可以在快速连接成功后选择 **File**-> **Copy Current Connection to Site Manager** （文件->将当前连接复制到站点管理器），输入名称并单击 **确定**。 
    下次您将能够通过在 **File** -> **Site Manager** (文件-> 站点管理器。)中选择先前保存的站点进行连接。

    .. image:: img/ftp_site.png

**第3步**: 上传/下载文件。

您可以通过拖放将本地文件上传到树莓派，也可以将树莓派文件中的文件下载到本地。

.. image:: img/upload_ftp.png
