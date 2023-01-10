Windows ユーザ
=====================

Windowsユーザーの場合は **Windows PowerShell** を利用できます。

#. ``windows`` + ``R`` キーを押し入力ウィンドウに **powershell** と入力してPowerShellを起動してください。

    .. image:: img/sp221221_135900.png
        :align: center

#. 後は Mac や Linux のターミナル操作と同じで開かれたPowerShellの画面で ``ssh <username>@<hostname>.local`` と入力します。

    .. code-block::

        ssh pi@raspberrypi.local


#. 以下のメッセージが表示されます.

    .. code-block::

        The authenticity of host 'raspberrypi.local (192.168.6.116)' can't be established.
        ECDSA key fingerprint is SHA256:7ggckKZ2EEgS76a557cddfxFNDOBBuzcJsgaqA/igz4.
        Are you sure you want to continue connecting (yes/no/[fingerprint])? 

    \"yes\" と入力してください。

#. パスワードを入力してください。 (デフォルトの場合は ``raspberry`` です。)

    .. note::
        When you input the password, the characters do not display on
        window accordingly, which is normal. What you need is to input the
        correct password.

#. これでRaspberry piに正常にログインできましたので、OSのアップデートを行います。

    .. image:: img/sp221221_140628.png
        :width: 550
        :align: center


リモート・デスクトップ 
-----------------------------

VNCでリモート・デスクトップを利用できます。

 **VNCサービスの有効化** 

VNCは標準でインストールされておりますが、デフォルトでは無効化されていますので、有効化する必要があります。

#. 以下のコマンドを入力します:

    .. raw:: html

        <run></run>

    .. code-block:: 

        $ sudo raspi-config

    .. image:: img/image287.png
        :align: center

#. **3** の **Interfacing Options** を下矢印で選択してリターン機を押します。

    .. image:: img/image282.png
        :align: center

#. **P3 VNC** を矢印キーで選択してリターンキーを押します。

    .. image:: img/image288.png
        :align: center

#. **Yes → OK -> Finish** と順番に選択して設定を終了させます。

    .. image:: img/image289.png
        :align: center

**VNCによるログイン**

#. 先ず `VNC Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ をダウンロードしてファイルを開き、指示に従いインストールします。インストールしたら起動します。

#. メニューのファイルから **New connection** を選択します。

    .. image:: img/image290.png
        :align: center

#. Raspberry piのIPアドレスを入力します。 **Name** には好きな名前を付けます。（Raspberry piの名前と同じが良いかもしれません） 「OK」をクリックします。

    .. image:: img/image291.png
        :align: center

#. 作成した **接続先** をダブルクリックします。:

    .. image:: img/image292.png
        :align: center

#. ログイン・ユーザー名 ( **pi** ) とSDカードを作成した際に指定したパスワード (デフォルトでは **raspberry** )を入力します。

    .. image:: img/image293.png
        :align: center

#. Raspberry Piのデスクトップ画面が表示されるはずです。:

    .. image:: img/image294.png
        :align: center





.. XRDP
.. ^^^^^^^^^^^^^^^^^^^^^^^

.. **XRDPのインストール** 

.. もう一つの手法はXRDPを使うことです。これはマイクロソフトが提供するRDPというプロトコルを使用する方法です。

.. #. SSHを利用してRaspberry piにログインします。

.. #. 以下の手順に従いXRDPをインストールします。

..     .. raw:: html

..         <run></run>

..     .. code-block:: 

..         sudo apt-get update
..         sudo apt-get install xrdp

.. #. 以下の表示が表示されるので、「Y」と入力して「Enterキーを押します。

..     .. image:: img/image295.png
..         :align: center

.. #. インストールが完了したら、Windows リモート デスクトップ アプリケーションを使用して Raspberry Pi にログインしてください。

.. **XRDPでのログイン**


.. Windows ユーザーの場合は、Windows に付属のリモート デスクトップ機能を使用できます。
.. Macユーザーの場合は、APP Store から Microsoftリモート デスクトップをダウンロードして使用できます。
.. この 2 つの間に大きな違いはありません。
.. 次の例は、Windows リモート デスクトップです。

.. **ステップ2**

.. ファイル名を指定して実行 (WIN+R) に「 ``mstsc`` 」と入力してリモート デスクトップ接続を開き、Raspberry Pi の IP アドレスを入力して、「Connect」をクリックします。


.. .. image:: img/image296.png
..     :align: center

.. **ステップ3**

.. 次にxrdp ログイン ページが表示されます。
.. ユーザー名とパスワードを入力して「OK」をクリックしてください。
.. ユーザー名は ( **pi** ) とSDカードを作成した際に指定したパスワード (デフォルトでは **raspberry** )になります。

.. .. image:: img/image297.png
..     :align: center

.. **Step 4**

.. Raspberry Piのデスクトップ画面が表示されるはずです。

.. .. image:: img/image20.png
..     :align: center