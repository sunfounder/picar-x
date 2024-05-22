.. note::

    こんにちは、SunFounderのRaspberry Pi & Arduino & ESP32愛好家コミュニティへようこそ！Facebook上でRaspberry Pi、Arduino、ESP32についてもっと深く掘り下げ、他の愛好家と交流しましょう。

    **参加する理由は？**

    - **エキスパートサポート**：コミュニティやチームの助けを借りて、販売後の問題や技術的な課題を解決します。
    - **学び＆共有**：ヒントやチュートリアルを交換してスキルを向上させましょう。
    - **独占的なプレビュー**：新製品の発表や先行プレビューに早期アクセスしましょう。
    - **特別割引**：最新製品の独占割引をお楽しみください。
    - **祭りのプロモーションとギフト**：ギフトや祝日のプロモーションに参加しましょう。

    👉 私たちと一緒に探索し、創造する準備はできていますか？[|link_sf_facebook|]をクリックして今すぐ参加しましょう！

.. _installing_the_os:

OSのインストール
=======================

**必要なコンポーネント**

* Raspberry Pi 4B/Zero 2 w/3B 3B+/2B/Zero W
* 1 x パーソナルコンピュータ
* 1 x マイクロSDカード 

**手順**


#. Raspberry Piのソフトウェアダウンロードページにアクセスします： `Raspberry Pi Imager <https://www.raspberrypi.org/software/>`_。ご使用のオペレーティングシステムに合わせたImagerバージョンを選択します。ダウンロード後、ファイルを開いてインストールを開始します。

    .. image:: img/os_install_imager.png


#. インストーラを起動すると、OSがセキュリティ警告を表示する場合があります。たとえば、Windowsでは警告メッセージが表示されることがあります。このような場合は、 **More info** を選択し、その後 **Run anyway** を選択します。画面の指示に従ってRaspberry Pi Imagerをインストールします。

    .. image:: img/os_info.png


#. SDカードをコンピュータまたはラップトップのSDカードスロットに挿入します。

#. Raspberry Pi Imagerアプリケーションをアイコンをクリックするか、端末で ``rpi-imager`` を実行して開きます。

    .. image:: img/os_open_imager.png

#. **CHOOSE DEVICE** をクリックし、リストから特定のRaspberry Piモデルを選択します（注意：Raspberry Pi 5は適用されません）。

    .. image:: img/os_choose_device.png

#. **CHOOSE OS** を選択し、次に **Raspberry Pi OS (Legacy)** を選択します。

    .. warning::
        * スピーカーが動作しないため、 **Bookworm** バージョンをインストールしないでください。
        * **Raspberry Pi OS (Legacy)** バージョン - **Debian Bullseye** をインストールする必要があります。

    .. image:: img/os_choose_os.png


#. **Choose Storage** をクリックし、インストール用の正しいストレージデバイスを選択します。

    .. note::

        複数のストレージデバイスが接続されている場合は、特に正しいデバイスを選択してください。不確かな場合は他のデバイスを切断してください。

    .. image:: img/os_choose_sd.png

#. **NEXT** を押し、 **EDIT SETTINGS** を選択してOSの設定をカスタマイズします。

    .. image:: img/os_enter_setting.png

#. Raspberry Piの **hostname** を設定します。

    .. note::

        ホスト名は、Raspberry Piがネットワーク上で自身を識別するために使用するものです。 `<hostname>.local` または `<hostname>.lan` を使用してPiに接続できます。

    .. image:: img/os_set_hostname.png

#. Raspberry Piの管理者アカウント用に **Username** と **Password** を作成します。

    .. note::

        Raspberry Piにはデフォルトのパスワードがないため、セキュリティのためにユニークなユーザー名とパスワードを設定することが重要です。

    .. image:: img/os_set_username.png

#. ワイヤレスLANを設定するために、ネットワークの **SSID** と **Password** を入力します。

    .. note::

        ``Wireless LAN country`` は、Raspberry Piを使用している国の2文字の `ISO/IEC alpha2コード <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ に設定する必要があります。

    .. image:: img/os_set_wifi.png


#. **SERVICES** をクリックし、パスワードベースのリモートアクセスのために **SSH** を有効にします。 **Save** をクリックすることを忘れないでください。

    .. image:: img/os_enable_ssh.png

#. **Yes** をクリックして選択を確認します。

    .. image:: img/os_click_yes.png

#. SDカードに既存のファイルがある場合は、データ損失を避けるためにバックアップを行ってください。バックアップが不要な場合は **Yes** をクリックして続行します。

    .. image:: img/os_continue.png

#. OSがSDカードに書き込まれるのを待ちます。完了すると、確認ウィンドウが表示されます。

    .. image:: img/os_finish.png
        :align: center
