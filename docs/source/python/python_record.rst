.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _py_video:

9. Videoaufnahme
==================

Diese Anleitung zeigt Ihnen, wie Sie die Aufnahmefunktion nutzen können.

**Code ausführen**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 9.record_video.py

Nachdem der Code ausgeführt wurde, können Sie ``http://<Ihre IP>:9000/mjpg`` in Ihren Browser eingeben, um das Video zu sehen. Zum Beispiel: ``http://192.168.18.113:9000/mjpg``

.. image:: img/display.png

Die Aufnahme kann durch Drücken der Tasten auf der Tastatur gestartet oder gestoppt werden.

* Drücken Sie ``q``, um die Aufnahme zu starten oder zu pausieren/fortzusetzen, ``e``, um die Aufnahme zu stoppen oder zu speichern.
* Um das Programm zu beenden, drücken Sie ``ctrl+c``.


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

**Wie funktioniert des?**

Die Funktionen zur Videoaufnahme umfassen Folgendes:

* ``Vilib.rec_video_run(video_name)``: Startet den Thread für die Videoaufnahme. ``video_name`` ist der Name der Videodatei, es sollte ein String sein.
* ``Vilib.rec_video_start()``: Startet oder setzt die Videoaufnahme fort.
* ``Vilib.rec_video_pause()``: Pausiert die Aufnahme.
* ``Vilib.rec_video_stop()``: Stoppt die Aufnahme.

``Vilib.rec_video_set["path"] = f"/home/{username}/Videos/"`` legt den Speicherort der Videodateien fest.