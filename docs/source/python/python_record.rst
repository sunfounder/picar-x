.. _py_video:

9. ビデオ録画
==================

この例では、録画機能の使用方法を案内します。

**コードの実行**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 9.record_video.py


コードを実行した後、ブラウザで ``http://<your IP>:9000/mjpg`` にアクセスして、ビデオ画面を表示できます。例えば： ``http://192.168.18.113:9000/mjpg``

.. image:: img/display.png

キーボードのキーを押すことで、録画を停止または開始できます。

* ``q`` を押して録画を開始または一時停止/続行し、 ``e`` を押して録画を停止または保存します。
* プログラムを終了したい場合は、 ``ctrl+c`` を押してください。


**コード** 

.. code-block:: python

    from time import sleep,strftime,localtime
    from vilib import Vilib
    import readchar 

    manual = '''
    Press keys on keyboard to control recording:
        Q: record/pause/continue
        E: stop
        Ctrl + C: Quit
    '''

    def print_overwrite(msg,  end='', flush=True):
        print('\r\033[2K', end='',flush=True)
        print(msg, end=end, flush=True)

    def main():
        rec_flag = 'stop' # start,pause,stop
        vname = None
        Vilib.rec_video_set["path"] = "/home/pi/Videos/" # set path

        Vilib.camera_start(vflip=False,hflip=False) 
        Vilib.display(local=True,web=True)
        sleep(0.8)  # wait for startup

        print(manual)
        while True:
            # read keyboard
            key = readchar.readkey()
            key = key.lower()
            # start,pause
            if key == 'q':
                key = None
                if rec_flag == 'stop':            
                    rec_flag = 'start'
                    # set name
                    vname = strftime("%Y-%m-%d-%H.%M.%S", localtime())
                    Vilib.rec_video_set["name"] = vname
                    # start record
                    Vilib.rec_video_run()
                    Vilib.rec_video_start()
                    print_overwrite('rec start ...')
                elif rec_flag == 'start':
                    rec_flag = 'pause'
                    Vilib.rec_video_pause()
                    print_overwrite('pause')
                elif rec_flag == 'pause':
                    rec_flag = 'start'
                    Vilib.rec_video_start()
                    print_overwrite('continue')
            # stop       
            elif key == 'e' and rec_flag != 'stop':
                key = None
                rec_flag = 'stop'
                Vilib.rec_video_stop()
                print_overwrite("The video saved as %s%s.avi"%(Vilib.rec_video_set["path"],vname),end='\n')  
            # quit
            elif key == readchar.key.CTRL_C:
                Vilib.camera_close()
                print('\nquit')
                break 

            sleep(0.1)

    if __name__ == "__main__":
        main()

**どのように動作するのか？**

録画に関連する機能は以下の通りです：

* ``Vilib.rec_video_run(video_name)`` ：ビデオの録画を開始するスレッドを開始します。 ``video_name`` はビデオファイルの名前で、文字列である必要があります。
* ``Vilib.rec_video_start()`` ：ビデオ録画を開始または続行します。
* ``Vilib.rec_video_pause()`` ：録画を一時停止します。
* ``Vilib.rec_video_stop()`` ：録画を停止します。

``Vilib.rec_video_set["path"] = f"/home/{username}/Videos/"`` はビデオファイルの保存場所を設定します。
