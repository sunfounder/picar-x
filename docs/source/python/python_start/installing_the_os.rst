OSのインストール
=======================

**必要なコンポーネント**


* 任意のRaspberry Pi 
* 1 x 個人用コンピュータ
* 1 x Micro SDカード 


**ステップ 1**

Raspberry Piは、Mac OS、Ubuntu 18.04、Windowsで動作するグラフィカルなSDカードライティングツールを開発しました。これはほとんどのユーザーにとって最も簡単なオプションです。イメージをダウンロードしてSDカードに自動的にインストールします。

ダウンロードページを訪れてください: https://www.raspberrypi.org/software/。あなたのオペレーティングシステムに合ったRaspberry Pi Imagerのリンクをクリックし、ダウンロードが完了したらそれをクリックしてインストーラを起動してください。

.. image:: img/image11.png
    :align: center


**ステップ 2**

インストーラを起動すると、オペレーティングシステムが実行をブロックしようとする場合があります。例えば、Windowsでは次のようなメッセージが表示されます。

このようなポップアップが表示された場合は、 **詳細情報** をクリックし、次に **とにかく実行** をクリックして、Raspberry Pi Imagerをインストールする手順に従ってください。

.. image:: img/image12.png
    :align: center

**ステップ 3**

SDカードをコンピュータまたはラップトップのSDカードスロットに挿入します。

**ステップ 4**

Raspberry Pi Imagerで、 **CHOOSE OS** -> **Raspberry Pi OS(Legacy)** をクリックします。

.. warning::
    * **Bookworm** バージョンをインストールしないでください。それではスピーカーが動作しません。
    * **Raspberry Pi OS (Legacy)** バージョン - **Debian Bullseye** をインストールする必要があります。

.. image:: img/3d33.png
    :align: center


**ステップ 5**

使用するSDカードを選択します。

.. image:: img/image14.png
    :align: center

**ステップ 6**

詳細オプションページを開くには、オペレーティングシステムを選択した後に表示される **設定** ボタンをクリックするか、 **Ctrl+Shift+X** を押します。

ここで、ホスト名を設定し、sshを有効にし、ユーザー名とパスワードを設定します。

.. warning::

    リモートでRaspberry Piにアクセスするためには、 ``hostname``、 ``username``、 ``password`` を必ずメモしておいてください。これらは後で非常に重要になります。

.. image:: img/image15.png
    :align: center

その後、下にスクロールしてwifi設定を完了し、 **SAVE** をクリックします。

.. note::

    **wifi country** は、あなたがRaspberry Piを使用している国の2文字の `ISO/IEC alpha2コード <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ に設定してください。次のリンクを参照してください: https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements。

.. image:: img/image16.png
    :align: center

**ステップ 7**

**WRITE** ボタンをクリックします。

.. image:: img/image17.png
    :align: center

**ステップ 8**

現在SDカードにファイルがある場合は、それらのファイルをまずバックアップして、永久に失うことがないようにしたいでしょう。バックアップするファイルがない場合は、 **Yes** をクリックします。

.. image:: img/image18.png
    :align: center

**ステップ 9**

しばらく待った後、書き込みが完了したことを表す以下のウィンドウが表示されます。

.. image:: img/image19.png
    :align: center
