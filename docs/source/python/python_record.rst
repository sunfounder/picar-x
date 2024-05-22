.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _py_video:

9. Record Video
==================

This example will guide you how to use the recording function.

**Run the Code**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 9.record_video.py


After the code runs, you can enter ``http://<your IP>:9000/mjpg`` in the browser to view the video screen. such as:  ``http://192.168.18.113:9000/mjpg``

.. image:: img/display.png

Recording can be stopped or started by pressing the keys on the keyboard.

* Press ``q`` to begin recording or pause/continue, ``e`` to stop recording or save.
* If you want to exit the program, press ``ctrl+c``.


**Code** 

.. code-block:: python

    from time import sleep,strftime,localtime
    from vilib import Vilib
    import readchar
    import os

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
        username = os.getlogin()
        
        Vilib.rec_video_set["path"] = f"/home/{username}/Videos/" # set path

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

**How it works?**

Functions related to recording include the following:

* ``Vilib.rec_video_run(video_name)`` : Started the thread to record the video. ``video_name`` is the name of the video file, it should be a string.
* ``Vilib.rec_video_start()``: Start or continue video recording.
* ``Vilib.rec_video_pause()``: Pause recording.
* ``Vilib.rec_video_stop()``: Stop recording.

``Vilib.rec_video_set["path"] = f"/home/{username}/Videos/"`` sets the storage location of video files.