Raspberry pi OSのインストール
====================================

**必要なもの**

* Raspberry Pi 本体
* PC（Windows Mac Linux/UNIX）
* マイクロSDカード  8GB以上のもの


**ステップ1**

Raspberry Pi専用にSDカード書き込みツールが用意されました。Mac、WindowsならびにUbuntu 18.04で動作しますので、ほとんどの方にとって最も簡単なRaspberry pi用のSDカードの作成方法です。

ダウンロードページにアクセスしてください: 
https://www.raspberrypi.org/software/

お使いのパソコン用のRaspberry Pi Imagerのリンクをクリックしダウンロードし、完了したらそれをクリックしてインストーラーを起動します。

.. image:: img/image11.png
    :align: center


**ステップ2**

インストーラーを起動するとＯＳがインストーラーの実行を禁止しようとする場合があります。 たとえば、Windows では次のメッセージが表示されます。

このポップアップが表示された場合は、[**More info**] をクリックしてから [**Run anyway**] をクリックし指示に従ってRaspberry Pi Imagerをインストールします。

.. image:: img/image12.png
    :align: center

**ステップ3**

SDカードをパソコンのSDカード スロットに挿入します。（SDカードスロットが無いパソコンの場合USBマイクロSDカードアダプターを使用してください）
SDカードのフォーマットなどのメニュー画面が表示された場合、それらは無視して閉じてください。

**ステップ4**

Raspberry Pi Imagerで、インストールしたいOSとそれをインストールしたいSDカードを選択します。

.. image:: img/sp230607_161330.png
    :align: center

.. note:: 

    1) 初回はインターネットに接続する必要があります。

    2) そのOSは将来のオフライン使用のために保存されます(lastdownload.cache, C:/Users/yourname/AppData/Local/Raspberry Pi/Imager/cache)。したがって、次回ソフトウェアを開くときに再びダウンロードする必要はありません。


**ステップ5**

使用するSDカードを選択します。

.. image:: img/image14.png
    :align: center

**ステップ6**

 **設定** ボタン（画面右下のギアマーク：OSを選択すると表示される）をクリックして **詳細オプション** ページを開き、SSHを有効にしてWi-Fiを設定します。
 最低これら2つの項目を設定する必要があり他の項目は選択に応じて異なりますがパスワードはここで設定しておくと楽です。
 このカスタマイズ オプションを常に使用するように選択できます（次回利用時のデフォルトになる）。

.. image:: img/image15.png
    :align: center

下にスクロールしてWi-Fiの設定を完了し **SAVE** をクリックします。

.. note::

    **wifi country** には、2 文字の `ISO/IEC alpha2 コード <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements>`_ を設定する必要があります
    Raspberry Piを使用している国については、次のリンクを参照してください: https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2#Officially_assigned_code_elements
    
    日本国内で使用しているならば「JP」と設定してください。

.. image:: img/image16.png
    :align: center

**ステップ7**

**書き込む** ボタンをクリックしてください。

.. image:: img/image17.png
    :align: center

**ステップ8**

現在SDカードにファイルが保存されている場合はそれらのファイルを削除してしまわないように、事前にファイルをバックアップすることをお勧めします。
バックアップするファイルがない場合は、[**はい**] をクリックします。

.. image:: img/image18.png
    :align: center

**ステップ9**

しばらく待つと、次のウィンドウが表示され、書き込みが完了したことを示します。
そのままSDカードを取り出してRaspberry Pi Imagerを終了させます。

.. image:: img/image19.png
    :align: center