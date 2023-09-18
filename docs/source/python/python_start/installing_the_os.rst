OSのインストール
=======================

**必要な部品**

================== ======================
Raspberry Pi        パーソナルコンピュータ
Micro SDカード 
================== ======================

**ステップ1**

Raspberry Piは、Mac OS、Ubuntu 18.04、Windowsで動作するグラフィカルなSDカード書き込みツールを開発しています。これは、イメージをダウンロードしてSDカードに自動的にインストールするため、ほとんどのユーザーにとって最も簡単なオプションです。

ダウンロードページを訪れます: https://www.raspberrypi.org/software/. あなたのオペレーティングシステムに合わせたRaspberry Pi Imagerのリンクをクリックし、ダウンロードが完了したらインストーラを起動します。

.. image:: img/image11.png
    :align: center

**ステップ2**

インストーラを起動すると、オペレーティングシステムがそれを実行するのをブロックしようとする場合があります。例えば、Windowsでは以下のメッセージが表示されます:

このポップアップが表示されたら、 **詳細情報** をクリックしてから **とにかく実行** をクリックし、Raspberry Pi Imagerをインストールする手順に従います。

.. image:: img/image12.png
    :align: center

**ステップ3**

SDカードをコンピュータまたはラップトップのSDカードスロットに挿入します。

**ステップ4**

Raspberry Pi Imagerで、インストールしたいOSとそれをインストールしたいSDカードを選択します。

.. image:: img/sp230607_161330.png
    :align: center

.. note:: 

    1) 初回はインターネットに接続する必要があります。

    2) そのOSは将来のオフライン使用のために保存されます(lastdownload.cache, C:/Users/yourname/AppData/Local/Raspberry Pi/Imager/cache)。したがって、次回ソフトウェアを開くときに再びダウンロードする必要はありません。

**ステップ5**

使用するSDカードを選択してください。

.. image:: img/image14.png
    :align: center

**ステップ6**

高度なオプションページを開くには、OSを選択後に表示される設定ボタンをクリックするか、Ctrl+Shift+Xを押してください。
SSHを有効にし、ユーザー名と名前を設定してください。この画像のカスタマイズオプションを常に使用することも選択できます。

.. note::
    「ホスト名の設定」のボックスがチェックされていない場合、デフォルトのホスト名は引き続き ``raspberrypi`` となります。このホスト名を使ってRaspberry Piにリモートでアクセスします。

.. image:: img/image15.png
    :align: center

その後、wifiの設定を完了させるために下にスクロールし、 **保存** をクリックします。

.. note::

    **wifiの国** は、Raspberry Piを使用している国の2文字の `ISO/IEC alpha2コード <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ に設定する必要があります。以下のリンクを参照してください: https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements

.. image:: img/image16.png
    :align: center

**ステップ7**

**書き込み** ボタンをクリックしてください。

.. image:: img/image17.png
    :align: center

**ステップ8**

現在、SDカードにファイルがある場合は、それらのファイルを永久に失うことなくバックアップすることを検討したいかもしれません。バックアップするファイルがない場合は、 **はい** をクリックしてください。

.. image:: img/image18.png
    :align: center

**ステップ9**

一定の時間を待った後、書き込みの完了を示す次のウィンドウが表示されます。

.. image:: img/image19.png
    :align: center
