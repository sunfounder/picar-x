.. note::

    Bonjour, bienvenue dans la communauté des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder sur Facebook ! Explorez en profondeur le Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux nouvelles annonces de produits et à des aperçus exclusifs.
    - **Réductions spéciales** : Bénéficiez de réductions exclusives sur nos derniers produits.
    - **Promotions et concours festifs** : Participez à des concours et promotions spéciales pendant les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_video:

9. Enregistrer une vidéo
=============================

Cet exemple vous guidera dans l'utilisation de la fonction d'enregistrement.

**Exécuter le code**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 9.record_video.py

Après l'exécution du code, vous pouvez entrer ``http://<your IP>:9000/mjpg`` dans le navigateur pour voir l'écran vidéo, par exemple : ``http://192.168.18.113:9000/mjpg``.

.. image:: img/display.png

L'enregistrement peut être démarré ou arrêté en appuyant sur les touches du clavier.

* Appuyez sur ``q`` pour commencer à enregistrer, mettre en pause ou continuer, ``e`` pour arrêter l'enregistrement ou sauvegarder.
* Si vous souhaitez quitter le programme, appuyez sur ``ctrl+c``.

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

**Comment ça fonctionne ?**


Les fonctions liées à l'enregistrement incluent les suivantes :


* ``Vilib.rec_video_run(video_name)`` : Lance le thread pour enregistrer la vidéo. ``video_name`` est le nom du fichier vidéo, qui doit être une chaîne de caractères.
* ``Vilib.rec_video_start()`` : Démarrer ou continuer l'enregistrement vidéo.
* ``Vilib.rec_video_pause()`` : Mettre en pause l'enregistrement.
* ``Vilib.rec_video_stop()`` : Arrêter l'enregistrement.

``Vilib.rec_video_set["path"] = f"/home/{username}/Videos/"`` définit l'emplacement de stockage des fichiers vidéo.
