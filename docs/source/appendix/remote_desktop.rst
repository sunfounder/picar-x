.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _remote_desktop:

Raspberry Pi のリモートデスクトップアクセス
==================================================

コマンドラインよりも **GUI（グラフィカルユーザーインターフェース）** を好む場合、  
Raspberry Pi ではリモートデスクトップ機能を利用できます。  
このガイドでは、リモートアクセスのための **VNC（Virtual Network Computing）** の設定と使用方法を紹介します。

この目的には `VNC® Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ の使用をおすすめします。

**Raspberry Pi で VNC サービスを有効にする**

VNC サービスは Raspberry Pi OS に標準でインストールされていますが、デフォルトでは無効になっています。  
以下の手順で有効にします：

#. Raspberry Pi のターミナルで次のコマンドを入力します：

    .. raw:: html

        <run></run>

    .. code-block::

        sudo raspi-config

#. ↓キーで **Interfacing Options（インターフェイス設定）** を選択し、**Enter** を押します。

    .. image:: img/config_interface.png
        :align: center

#. オプションから **VNC** を選択します。

    .. image:: img/vnc.png
        :align: center

#. 矢印キーで **<Yes>** → **<OK>** → **<Finish>** を選択し、VNC サービスを有効にします。

    .. image:: img/vnc_yes.png
        :align: center

**VNC Viewer でログイン**

#. `VNC Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ を PC にダウンロードしてインストールします。

#. VNC Viewer を起動し、Raspberry Pi のホスト名または IP アドレスを入力して Enter を押します。

    .. image:: img/vnc_viewer1.png
        :align: center

#. プロンプトが表示されたら、Raspberry Pi のユーザー名とパスワードを入力し、**OK** をクリックします。

    .. image:: img/vnc_viewer2.png
        :align: center

#. 数秒後、Raspberry Pi OS のデスクトップが表示されます。  
   ここからターミナルを開いてコマンドを実行できます。

    .. image:: img/bookwarm.png
        :align: center
