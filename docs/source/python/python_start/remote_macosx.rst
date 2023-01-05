
Mac OS X ユーザ
==========================

しかしMacユーザーの場合は可能であれば一時的にでもモニター、キーボード、マウスをセットしてRspberry pi側のVNCの設定を行った方が楽です。
まずはその方法から説明いたします。

なお予め断っておきますが、この方法の場合MacとRaspberry piの間の通信は暗号化による保護がなされません。
実際の利用に際しては個人宅もしくは社内のネットワーク内での通信となるので保護がなくても問題にはならないでしょう。
しかし気になる方は別途記述するVNCアプリを導入してご利用ください。

Mac OS X ユーザーで一時的にモニター（あるいはTV）を利用できる方
---------------------------------------------------------------------

#. Raspberry Piにディスプレイ、マウス、キーボードを接続し、電源を入れる。図の番号に従ってメニューを選択します。


    .. image:: img/mac_vnc1.png
        :align: center

#. 以下の画面が表示されるので **Interfaces** タブをクリックし、さらに **VNC** を **Enabled** に設定してから画面右下の **OK** ボタンをクリックします。

    .. image:: img/mac_vnc2.png
        :align: center


#. 画面右上に **VNC** のアイコンが表示されVNCサーバーが起動します。

    .. image:: img/mac_vnc3.png
        :align: center


#. 表示された **VNC** アイコンをクリックしてVNC Serverウィンドウを表示し、さらに右上のメニューボタンをクリック、続いて **Options** をクリックします

    .. image:: img/mac_vnc4.png
        :align: center

#. 以下の画面が表示されるのでオプションを変更します。

    .. image:: img/mac_vnc5.png
        :align: center

    Encryptionを **Prefer offon** に、Authenticationを **VNC password** に設定してください。
    **OK** ボタンをクリックするとパスワードの入力画面が表示されるのでRaspberry piのパスワードと同じでも、別のパスワードでも構わないので入力して **OK** をクリックしてください。これでMacから接続できる準備が整いました。もうモニターなどは接続を外しても大丈夫です。

**ここからはMac側での操作になります。**

#. ファインダーの移動メニューからサーバーへ接続を選択します。

    .. image:: img/mac_vnc10.png
        :align: center

#. Raspberry pi のアドレスを入力します。以下のように **Raspberri piの名前** ＋ **.local** でアドレスを指定します。

        .. image:: img/mac_vnc11.png
            :align: center

      **接続** ボタンをクリックします。

#. パスワードを聞いてくるので入力してください。

        .. image:: img/mac_vnc12.png
            :align: center

#. Raspberry pi のデスクトップが表示され、Mac上からそのまま操作ができるようになります。

        .. image:: img/mac_vnc13.png
            :align: center


Mac OS X ユーザーで一時的であってもモニター（あるいはTV）を利用できない方
---------------------------------------------------------------------------

 * SSHコマンドを適用してRaspberry PiのBash Shellを開くことができます。
 * BashはLinuxの標準のデフォルト・シェルです。
 * シェル自体はユーザーがUnix/Linuxを利用する際のコマンド（命令）です。
 * シェルを通して必要な作業のほとんどが行えます。
 * Raspberry pi 側の設定が終われば前述の **Mac** からファインダーを使ってRaspberry piのデスクトップにアクセスできます。


#. Raspberry Pi への **SSH** 接続 ``ssh <username>@<hostname>.local`` と入力して ``リターンキー`` を押します。


    .. code-block::

        ssh pi@raspberrypi.local


    .. image:: img/mac_vnc14.png


#. 最初にログインするときだけ以下のメッセージが表示されるので **yes** と入力してください。

    .. code-block::

        The authenticity of host 'raspberrypi.local (2400:2410:2101:5800:635b:f0b6:2662:8cba)' can't be established.
        ED25519 key fingerprint is SHA256:oo7x3ZSgAo032wD1tE8eW0fFM/kmewIvRwkBys6XRwg.
        This key is not known by any other names
        Are you sure you want to continue connecting (yes/no/[fingerprint])?


#. Raspberry pi の **パスワード** を入力します。パスワードは入力しても表示されませんので入力を間違えないように注意してください。

    .. code-block::

        pi@raspberrypi.local's password: 
        Linux raspberrypi 5.15.61-v8+ #1579 SMP PREEMPT Fri Aug 26 11:16:44 BST 2022 aarch64

        The programs included with the Debian GNU/Linux system are free software;
        the exact distribution terms for each program are described in the
        individual files in /usr/share/doc/*/copyright.

        Debian GNU/Linux comes with ABSOLUTELY NO WARRANTY, to the extent
        permitted by applicable law.
        Last login: Thu Sep 22 12:18:22 2022
        pi@raspberrypi:~ $ 


    

#. これでRaspberry piに正常にログインできましたので、MacからVNCでログイン出来るように設定します。まずはOSのアップデートを行います。以下のコマンドを入力します。

    .. code-block::

        sudo apt update
        sudo apt upgrade


    ``Do you want to continue? [Y/n]`` が表示されたら **Y** を入力します。

    アップデートが終わるまでしばし時間がかかりることがあります。（その時のアップデート量によります。）


#. VNC を有効化して VNC サーバーを起動します。以下のコマンドを入力します。

    .. code-block::

        sudo raspi-config

#. 以下の画面が表示されますので、キーボードの矢印キーで **3 Interface Options** を選択してリターンキーを押します。

    .. image:: img/image282.png
        :align: center

#. 以下の画面が表示されますので、キーボードの矢印キーで **P3 VNC** を選択してリターンキーを押します。

    .. image:: img/image288.png
        :align: center

#. 以下の画面が表示されますので、キーボードの矢印キーで **<Yes>** を選択してリターンキーを押します。

    .. image:: img/mac_vnc8.png
        :align: center

#. 以下の画面が表示されますので、キーボードの矢印キーで **<Ok>** を選択してリターンキーを押します。

    .. image:: img/mac_vnc7.png
        :align: center

#. 最後にキーボードの矢印キーで **<Finish>** を選択してリターンキーを押します。

    .. image:: img/mac_vnc6.png
        :align: center

#. VNCサーバーが起動するようになったので、今度はMacからの接続様の設定を変更します。

    .. code-block::

        sudo nano /etc/vnc/config.d/common.custom

    以下のような画面になるので ``Authentication=VncAuth`` と入力し、 ``Ctl + o`` を押し、リターンキーを押し、さらに ``Ctl + x`` を押します。

    .. image:: img/mac_vnc15.png
        :align: center

#. さらにMacからVNCでログインするときのパスワードを設定します。Raspberry pi のパスワードと同じで問題はないはずです。

    .. code-block::

        sudo vncpasswd -service
        password: (パスワードを入力)

#. これで設定が出来ましたので設定を反映させるためにRaspberry piを再起動します。

    .. code-block::

        sudo sudo reboot

#. ファインダーの移動メニューからサーバーへ接続を選択します。

    .. image:: img/mac_vnc10.png
        :align: center

#. Raspberry pi のアドレスを入力します。以下のように **Raspberri piの名前** ＋ **.local** でアドレスを指定します。

        .. image:: img/mac_vnc11.png
            :align: center

      **Connect** ボタンをクリックします。

#. パスワードを聞いてくるので入力してください。

        .. image:: img/mac_vnc12.png
            :align: center

#. Raspberry pi のデスクトップが表示され、Mac上からそのまま操作ができるようになります。

        .. image:: img/mac_vnc13.png
            :align: center
