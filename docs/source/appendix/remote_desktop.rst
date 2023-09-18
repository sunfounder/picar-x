.. _remote_desktop:


リモートデスクトップ 
===============================

Raspberry Piのデスクトップをリモートで制御する方法は2つあります:

**VNC** と **XRDP** 、どちらかを使用できます。

VNC 
--------------

VNCを使用してリモートデスクトップの機能を使用できます。

**VNCサービスの有効化**

VNCサービスはシステムにインストールされています。デフォルトでは、
VNCは無効になっています。設定で有効にする必要があります。

**ステップ 1**

以下のコマンドを入力します:

.. raw:: html

    <run></run>

.. code-block:: 

    sudo raspi-config

.. image:: img/image287.png
   :align: center

**ステップ 2**

キーボードの下矢印キーを押して **3 Interfacing Options** を選択し、 **Enter** キーを押します。

.. image:: img/image282.png
   :align: center

**ステップ 3**

**P3 VNC**

.. image:: img/image288.png
   :align: center

**ステップ 4**

**Yes -> OK -> Finish** を選択して設定を終了します。

.. image:: img/image289.png
   :align: center

**VNCへのログイン**

**ステップ 1**

パーソナルコンピュータに `VNC Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ をダウンロードしてインストールする必要があります。
インストールが完了したら、それを開きます。

**ステップ 2**

次に、 **新しい接続** を選択します。

.. image:: img/image290.png
   :align: center

**ステップ 3**

Raspberry Piの ``<Hostname>.local`` または ``<IP address>`` と任意の **名前** を入力します。

.. image:: img/image291.png
   :align: center

**ステップ 4**

作成した接続をダブルクリックします:

.. image:: img/image292.png
   :align: center

**ステップ 5**

ユーザー名とパスワードを入力します。

.. image:: img/image293.png
   :align: center

**ステップ 6**

これでRaspberry Piのデスクトップが表示されます:

.. image:: img/image294.png
   :align: center

VNCの部分はここまでです。


XRDP
-----------------------

もう1つのリモートデスクトップの方法はXRDPで、
RDP（Microsoft Remote Desktop Protocol）を使用してリモートマシンにグラフィカルにログインする機能を提供します。

**XRDPのインストール**

**ステップ 1**

SSHを使用してRaspberry Piにログインします。

**ステップ 2**

XRDPをインストールするための以下の指示を入力します。

.. raw:: html

    <run></run>

.. code-block:: 

   sudo apt-get update
   sudo apt-get install xrdp

**ステップ 3**

その後、インストールが開始されます。

``Y`` を入力し、 ``Enter`` キーを押して確認します。

.. image:: img/image295.png
   :align: center

**ステップ 4**

インストールが完了したら、Windowsのリモートデスクトップアプリケーションを
使用してRaspberry Piにログインする必要があります。

**XRDPへのログイン**

**ステップ 1**

Windowsユーザーの場合、Windowsに付属するリモートデスクトップ機能を使用できます。
Macユーザーの場合、APP StoreからMicrosoft Remote Desktopをダウンロードして使用できます。
両方の違いはあまりありません。次の例はWindowsのリモートデスクトップです。

**ステップ 2**

Run（ ``WIN+R`` ）に ``mstsc`` と入力して、リモートデスクトップ接続を開き、
Raspberry Piの ``<Hostname>.local`` または ``<IP address>`` を入力し、 **接続** をクリックします。

.. image:: img/image296.png
   :align: center

**ステップ 3**

次に、xrdpのログインページが表示されます。ユーザー名とパスワードを入力してください。
その後、 **OK** をクリックしてください。

.. image:: img/image297.png
   :align: center

**ステップ 4**

ここで、リモートデスクトップを使用してRPiに正常にログインしました。

.. image:: img/image20.png
   :align: center
