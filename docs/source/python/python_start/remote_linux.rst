
Linux / UNIX ユーザー
===========================


#. ターミナルを開いて ``ssh <username>@<hostname>.local`` と入力してください。

    .. code-block::

        ssh pi@raspberrypi.local

#. 以下のメッセージが表示されます。

    .. code-block::

        The authenticity of host 'raspberrypi.local (192.168.6.116)' can't be established.
        ECDSA key fingerprint is SHA256:7ggckKZ2EEgS76a557cddfxFNDOBBuzcJsgaqA/igz4.
        Are you sure you want to continue connecting (yes/no/[fingerprint])? 

#. \"yes\" と入力してください。

    .. image:: img/mac-ssh-login.png
        :width: 550
        :align: center


#. パスワードを入力してください。 (デフォルトの場合は ``raspberry`` です。)

    .. .. image:: img/image23.png
    ..     :align: center

        .. note::
            パスワードは入力しても表示されませんので入力を間違えないように注意してください。 


#. これでRaspberry piに正常にログインできましたので、OSのアップデートを行います。

    .. image:: img/mac-ssh-terminal.png
        :width: 550
        :align: center