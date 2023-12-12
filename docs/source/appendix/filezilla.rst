.. _filezilla:

Filezillaソフトウェア
==========================

.. image:: img/filezilla_icon.png

ファイル転送プロトコル（FTP）は、コンピュータネットワーク上のサーバーからクライアントへコンピュータファイルを転送するために使用される標準的な通信プロトコルです。

Filezillaはオープンソースソフトウェアで、FTPだけでなく、TLS上のFTP（FTPS）やSFTPにも対応しています。Filezillaを使用して、ローカルファイル（写真や音声など）をラズベリーパイにアップロードしたり、ラズベリーパイからローカルにファイルをダウンロードすることができます。

**ステップ1**：Filezillaをダウンロードする。

`Filezillaの公式ウェブサイト <https://filezilla-project.org/>`_ からクライアントをダウンロードしてください。Filezillaには非常に良いチュートリアルがありますので、こちらを参照してください： `Documentation - Filezilla <https://wiki.filezilla-project.org/Documentation>`_。

**ステップ2**：ラズベリーパイに接続する

簡単なインストール後、開いて `FTPサーバーに接続する <https://wiki.filezilla-project.org/Using#Connecting_to_an_FTP_server>`_。接続する方法は3つありますが、ここでは **Quick Connect** バーを使用します。 **hostname/IP**、 **username**、 **password**、 **port (22)** を入力し、 **Quick Connect** をクリックするか **Enter** を押してサーバーに接続します。

.. image:: img/filezilla_connect.png

.. note::

    クイック接続は、ログイン情報をテストする良い方法です。恒久的なエントリーを作成したい場合は、成功したクイック接続後に **File**-> **Copy Current Connection to Site Manager** を選択し、名前を入力して **OK** をクリックします。次回は **File** -> **Site Manager** 内で以前に保存したサイトを選択することで接続できます。
    
    .. image:: img/ftp_site.png

**ステップ3**：ファイルをアップロード/ダウンロードする。

ラズベリーパイにローカルファイルをドラッグアンドドロップでアップロードするか、ラズベリーパイ内のファイルをローカルにダウンロードします。

.. image:: img/upload_ftp.png

