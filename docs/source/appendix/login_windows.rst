.. _login_windows:

PuTTY
=========================

Windowsユーザーの場合、SSHアプリケーションをいくつか使用することができます。ここでは、`PuTTY <https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html>`_ を推奨します。

**ステップ1**

PuTTYをダウンロードします。

**ステップ2**

PuTTYを開き、左側のツリー構造の **Session** をクリックします。 **Host Name (or IP address)** のテキストボックスにRPiのIPアドレスを、 **Port** の下には **22** を入力します（デフォルトでは22です）。

.. image:: img/image25.png
    :align: center

**ステップ3**

**Open** をクリックします。IPアドレスを使ってRaspberry Piに初めてログインする際、セキュリティリマインダーが表示されます。 **Yes** をクリックしてください。

**ステップ4**

PuTTYウィンドウが\"**login as:**\"と表示したら、\"**pi**\"（RPiのユーザー名）と **password** : \"raspberry\"（変更していない場合のデフォルト）を入力します。

.. note::

    パスワードを入力するとき、ウィンドウ上に文字が表示されないのは正常です。正しいパスワードを入力することが必要です。
    
    PuTTYの横に非アクティブと表示されている場合は、接続が切断されており、再接続する必要があります。
    
.. image:: img/image26.png
    :align: center

**ステップ5**

これでRaspberry Piに接続できました。次のステップを進める準備ができました。
