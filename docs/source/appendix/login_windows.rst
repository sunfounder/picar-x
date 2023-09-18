.. _login_windows:

PuTTY
=========================

Windowsユーザーの場合、SSHのいくつかのアプリケーションを使用できます。ここでは、 `PuTTY <https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html>`_ をおすすめします。

**ステップ1**

PuTTYをダウンロードします。

**ステップ2**

PuTTYを開き、左のツリー構造で **Session** をクリックします。 **Host Name（またはIPアドレス）** のテキストボックスにRPiのIPアドレスを入力し、 **Port** に **22** を入力します（デフォルトでは22）。

.. image:: img/image25.png
    :align: center

**ステップ3**

**Open** をクリックします。IPアドレスでRaspberry Piに初めてログインすると、セキュリティのリマインダが表示されます。 **Yes** をクリックしてください。

**ステップ4**

PuTTYのウィンドウで「login as:」と表示されたら、
「pi」（RPiのユーザー名）を入力し、 **password** に「raspberry」を入力します（変更していない場合はデフォルト）。

.. note::

    パスワードを入力すると、キャラクタはウィンドウには表示されませんが、これは正常です。正しいパスワードを入力する必要があります。
    
    PuTTYの横に非アクティブが表示される場合、接続が切断されて再接続が必要であることを意味します。
    
.. image:: img/image26.png
    :align: center

**ステップ5**

ここで、Raspberry Piに接続したので、次の手順を実行する準備が整いました。
