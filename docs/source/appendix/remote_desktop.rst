.. _remote_desktop:


リモート・デスクトップ 
==========================

Rspberry piのデスクトップをリモートで利用する方法は２つあります:

 **VNC** と **XRDP** で、どちらでも利用可能です。
 
 なお、Macユーザーの場合は :ref:`set_up_raspberrypi` を先にご参照ください。より簡単に設定できると思います。

VNC 
--------------

VNCでリモート・デスクトップを利用できます。

 **VNCサービスの有効化** 

VNCは標準でインストールされておりますが、デフォルトでは無効化されていますので、有効化する必要があります。

 **ステップ1** 

以下のコマンドを入力します:

.. raw:: html

    <run></run>

.. code-block:: 

    $ sudo raspi-config

.. image:: img/image287.png
   :align: center

**ステップ２** 

**3** の **Interfacing Options** を下矢印で選択してリターン機を押します。

.. image:: img/image282.png
   :align: center

**ステップ3** 

**P3 VNC** を矢印キーで選択してリターンキーを押します。

.. image:: img/image288.png
   :align: center

**ステップ4** 

**Yes → OK -> Finish** と順番に選択して設定を終了させます。

.. image:: img/image289.png
   :align: center

**VNCによるログイン** （Windowsの場合）

**ステップ1** 

先ず `VNC Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ をダウンロードしてファイルを開き、指示に従いインストールします。
インストールしたら起動します。

**Stepステップ2**

メニューのファイルから **New connection** を選択します。

.. image:: img/image290.png
   :align: center

**ステップ3** 

Raspberry piのIPアドレスを入力します。 **Name** には好きな名前を付けます。（Raspberry piの名前と同じが良いかもしれません） 「OK」をクリックします。

.. image:: img/image291.png
   :align: center

**ステップ4** 

作成した **接続先** をダブルクリックします。:

.. image:: img/image292.png
   :align: center

**ステップ5** 

ログイン・ユーザー名 ( **pi** ) とSDカードを作成した際に指定したパスワード (デフォルトでは **raspberry** )を入力します。

.. image:: img/image293.png
   :align: center

**ステップ6** 

Raspberry Piのデスクトップ画面が表示されるはずです。:

.. image:: img/image294.png
   :align: center

これでVNCの説明は終わりになります。
なお、Macの場合はファインダーの「移動」から「サーバーへ接続」を選択し「vnc://pi@サーバー名.local」と入力します。


XRDP
-----------------------

**XRDPのインストール** 

もう一つの手法はXRDPを使うことです。これはマイクロソフトが提供するRDPというプロトコルを使用する方法です。

**ステップ1**

SSHを利用してRaspberry piにログインします。

**ステップ2**

以下の手順に従いXRDPをインストールします。

.. raw:: html

    <run></run>

.. code-block:: 

   sudo apt-get update
   sudo apt-get install xrdp

**ステップ3**

以下の表示が表示されるので、

「Y」と入力して「Enterキーを押します。

.. image:: img/image295.png
   :align: center

**ステップ4**

インストールが完了したら、Windows リモート デスクトップ アプリケーションを使用して Raspberry Pi にログインしてください。

**XRDPでのログイン**

**ステップ1**

Windows ユーザーの場合は、Windows に付属のリモート デスクトップ機能を使用できます。
Macユーザーの場合は、APP Store から Microsoftリモート デスクトップをダウンロードして使用できます。
この 2 つの間に大きな違いはありません。
次の例は、Windows リモート デスクトップです。

**ステップ2**

ファイル名を指定して実行 (WIN+R) に「 ``mstsc`` 」と入力してリモート デスクトップ接続を開き、Raspberry Pi の IP アドレスを入力して、「Connect」をクリックします。


.. image:: img/image296.png
   :align: center

**ステップ3**

次にxrdp ログイン ページが表示されます。
ユーザー名とパスワードを入力して「OK」をクリックしてください。
ユーザー名は ( **pi** ) とSDカードを作成した際に指定したパスワード (デフォルトでは **raspberry** )になります。

.. image:: img/image297.png
   :align: center

**Step 4**

Raspberry Piのデスクトップ画面が表示されるはずです。

.. image:: img/image20.png
   :align: center
