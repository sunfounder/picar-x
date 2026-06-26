.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 sur Facebook ! Plongez plus profondément dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et avant-premières.
    - **Réductions exclusives** : Profitez de réductions exclusives sur nos nouveaux produits.
    - **Promotions festives et concours** : Participez à des concours et promotions lors des fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_tts:

13. Jouer de la Musique et des Effets Sonores
================================================

Dans ce projet, vous apprendrez à faire jouer au PiCar-X de la musique de fond ou des effets sonores.
Vous pouvez également lire des fichiers audio que vous avez enregistrés.

**Avant de Commencer**

Assurez-vous d'avoir terminé :

* :ref:`install_all_modules` — Install ``robot-hat``, ``vilib``, ``picar-x`` modules, then run the script ``i2samp.sh``.

**Exécuter le Code**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 13.sound_background_music.py

Après l'exécution du code, veuillez suivre les instructions affichées dans le terminal.

Appuyez sur une touche pour appeler une fonction !

    * space: Joue un effet sonore (klaxon de voiture)
    * c: Joue un effet sonore avec des threads
    * q: Lecture/Arrêt de la musique

**Code**

.. code-block:: python

    from time import sleep
    from picarx.music import Music
    import readchar

    music = Music()

    manual = '''
    Input key to call the function!
        space: Play sound effect (Car horn)
        c: Play sound effect with threads
        q: Play/Stop Music
    '''

    def main():
        print(manual)

        flag_bgm = False
        music.music_set_volume(20)


        while True:
            key = readchar.readkey()
            key = key.lower()
            if key == "q":
                flag_bgm = not flag_bgm
                if flag_bgm is True:
                    music.music_play('../musics/slow-trail-Ahjay_Stelino.mp3')
                else:
                    music.music_stop()

            elif key == readchar.key.SPACE:
                music.sound_play('../sounds/car-double-horn.wav')
                sleep(0.05)

            elif key == "c":
                music.sound_play_threading('../sounds/car-double-horn.wav')
                sleep(0.05)


    if __name__ == "__main__":
        main()

**Comment ça fonctionne ?**

Les fonctions liées à la musique de fond incluent les suivantes :

* ``music = Music()`` : Déclare l'objet.
* ``music.music_set_volume(20)`` : Définit le volume, la plage est de 0 à 100.
* ``music.music_play('../musics/slow-trail-Ahjay_Stelino.mp3')`` : Lit un fichier musical, ici le fichier **slow-trail-Ahjay_Stelino.mp3** situé dans le dossier ``../musics``.
* ``music.music_stop()`` : Arrête la lecture de la musique de fond.

.. note::

    Vous pouvez ajouter différents effets sonores ou musiques dans le dossier ``musics`` ou ``sounds`` via :ref:`filezilla`.
