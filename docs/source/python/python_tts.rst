.. note::

    Bonjour et bienvenue dans la communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Plongez dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux nouvelles annonces de produits et à des avant-goûts exclusifs.
    - **Réductions spéciales** : Bénéficiez de réductions exclusives sur nos nouveaux produits.
    - **Promotions et concours festifs** : Participez à des concours et promotions pendant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_tts:

3. Synthèse vocale & Effet sonore
====================================

Dans cet exemple, nous utilisons les effets sonores de PiCar-X (ou plus précisément, de Robot HAT).
Cela comprend trois parties : la Musique, les Sons et la Synthèse vocale (TTS).

.. image:: img/how_are_you.jpg

**Installer i2samp**

Avant d'utiliser les fonctions de Synthèse vocale (TTS) et d'Effet sonore, 
vous devez d'abord activer le haut-parleur pour qu'il soit fonctionnel et émette des sons.

Exécutez ``i2samp.sh`` dans le dossier **picar-x**,
ce script installera tout ce qui est nécessaire pour utiliser l'amplificateur i2s.

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x
    sudo bash i2samp.sh 

.. image:: img/tt_bash.png

Il y aura plusieurs invites demandant de confirmer l'action. Répondez à toutes avec **Y**. Après que les modifications ont été effectuées sur le système Raspberry Pi, l'ordinateur devra redémarrer pour que ces changements prennent effet.

Après le redémarrage, exécutez à nouveau le script ``i2samp.sh`` pour tester l'amplificateur. Si un son est joué correctement à partir du haut-parleur, la configuration est terminée.

**Exécuter le code**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 3.tts_example.py

Après avoir exécuté le code, suivez les instructions affichées dans le terminal.

Appuyez sur une touche pour appeler la fonction !

    * espace : Jouer l'effet sonore (Klaxon de voiture)
    * c : Jouer l'effet sonore avec des threads
    * t : Parler un texte (Dire Bonjour)
    * q : Lire/Arrêter la musique

**Code**

.. code-block:: python

    from time import sleep
    from robot_hat import Music,TTS
    import readchar

    music = Music()
    tts = TTS()

    manual = '''
    Input key to call the function!
        space: Play sound effect (Car horn)
        c: Play sound effect with threads
        t: Text to speak
        q: Play/Stop Music
    '''

    def main():
        print(manual)

        flag_bgm = False
        music.music_set_volume(20)
        tts.lang("en-US")


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

            elif key == "t":
                words = "Hello"
                tts.say(words)

    if __name__ == "__main__":
        main()

**Comment ça fonctionne ?**

Les fonctions liées à la musique de fond incluent :

* ``music = Music()`` : Déclare l'objet.
* ``music.music_set_volume(20)`` : Définit le volume, l'intervalle est de 0 à 100.
* ``music.music_play('../musics/slow-trail-Ahjay_Stelino.mp3')`` : Joue des fichiers musicaux, ici le fichier **slow-trail-Ahjay_Stelino.mp3** situé dans le dossier ``../musics``.
* ``music.music_stop()`` : Arrête la lecture de la musique de fond.

.. note::

    Vous pouvez ajouter différents effets sonores ou musiques dans les dossiers ``musics`` ou ``sounds`` via :ref:`filezilla`.

Les fonctions liées aux effets sonores incluent :

* ``music = Music()``
* ``music.sound_play('../sounds/car-double-horn.wav')`` : Joue le fichier sonore.
* ``music.sound_play_threading('../sounds/car-double-horn.wav')`` : Joue le fichier sonore dans un mode thread sans suspendre le thread principal.

Le logiciel `eSpeak <http://espeak.sourceforge.net/>`_ est utilisé pour implémenter les fonctions de synthèse vocale.

Importez le module TTS de robot_hat, qui encapsule les fonctions convertissant du texte en parole.

Les fonctions liées à la Synthèse vocale incluent :

* ``tts = TTS()``
* ``tts.say(words)`` : Joue un fichier audio de texte.
* ``tts.lang("en-US")`` : Définit la langue.

.. note:: 

    Définissez la langue en paramétrant ``lang("")`` avec les caractères suivants.

.. list-table:: Langue
    :widths: 15 50

    *   - zh-CN 
        - Mandarin (Chinois)
    *   - en-US 
        - Anglais (États-Unis)
    *   - en-GB     
        - Anglais (Royaume-Uni)
    *   - de-DE     
        - Allemand
    *   - es-ES     
        - Espagnol
    *   - fr-FR  
        - Français
    *   - it-IT  
        - Italien
