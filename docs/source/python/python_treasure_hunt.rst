.. note::

    Bonjour et bienvenue dans la communauté des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder sur Facebook ! Plongez dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour perfectionner vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et à des aperçus exclusifs.
    - **Réductions spéciales** : Bénéficiez de réductions exclusives sur nos nouveaux produits.
    - **Promotions et concours festifs** : Participez à des concours et promotions spéciales pendant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_treasure:

12. Chasse au trésor
============================

Disposez un labyrinthe dans votre pièce et placez six cartes de couleurs différentes dans six coins. Ensuite, contrôlez PiCar-X pour rechercher ces cartes de couleurs une par une !

.. note:: Vous pouvez télécharger et imprimer les :download:`cartes de couleur en PDF <https://github.com/sunfounder/sf-pdf/raw/master/prop_card/object_detection/color-cards.pdf>` pour la détection de couleur.

**Exécuter le code**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 12.treasure_hunt.py

**Voir l'image**

Après l'exécution du code, le terminal affichera l'invite suivante :

.. code-block::

    No desktop !
    * Serving Flask app "vilib.vilib" (lazy loading)
    * Environment: production
    WARNING: Do not use the development server in a production environment.
    Use a production WSGI server instead.
    * Debug mode: off
    * Running on http://0.0.0.0:9000/ (Press CTRL+C to quit)

Vous pouvez ensuite entrer ``http://<your IP>:9000/mjpg`` dans le navigateur pour voir l'écran vidéo, par exemple : ``http://192.168.18.113:9000/mjpg``.

.. image:: img/display.png

**Code**

.. code-block:: python

    from picarx import Picarx
    from time import sleep
    from robot_hat import Music,TTS
    from vilib import Vilib
    import readchar
    import random
    import threading
    
    px = Picarx()
    
    music = Music()
    tts = TTS()
    
    manual = '''
    Press keys on keyboard to control Picar-X!
        w: Forward
        a: Turn left
        s: Backward
        d: Turn right
        space: Say the target again
        ctrl+c: Quit
    '''
    
    color = "red"
    color_list=["red","orange","yellow","green","blue","purple"]
    
    def renew_color_detect():
        global color
        color = random.choice(color_list)
        Vilib.color_detect(color)
        tts.say("Look for " + color)
    
    key = None
    lock = threading.Lock()
    def key_scan_thread():
        global key
        while True:
            key_temp = readchar.readkey()
            print('\r',end='')
            with lock:
                key = key_temp.lower()
                if key == readchar.key.SPACE:
                    key = 'space'
                elif key == readchar.key.CTRL_C:
                    key = 'quit'
                    break
            sleep(0.01)
    
    def car_move(key):
        if 'w' == key:
            px.set_dir_servo_angle(0)
            px.forward(80)
        elif 's' == key:
            px.set_dir_servo_angle(0)
            px.backward(80)
        elif 'a' == key:
            px.set_dir_servo_angle(-30)
            px.forward(80)
        elif 'd' == key:
            px.set_dir_servo_angle(30)
            px.forward(80)
    
    
    def main():
        global key
        Vilib.camera_start(vflip=False,hflip=False)
        Vilib.display(local=False,web=True)
        sleep(0.8)
        print(manual)
    
        sleep(1)
        _key_t = threading.Thread(target=key_scan_thread)
        _key_t.setDaemon(True)
        _key_t.start()
    
        tts.say("game start")
        sleep(0.05)
        renew_color_detect()
        while True:
    
            if Vilib.detect_obj_parameter['color_n']!=0 and Vilib.detect_obj_parameter['color_w']>100:
                tts.say("will done")
                sleep(0.05)
                renew_color_detect()
    
            with lock:
                if key != None and key in ('wsad'):
                    car_move(key)
                    sleep(0.5)
                    px.stop()
                    key =  None
                elif key == 'space':
                    tts.say("Look for " + color)
                    key =  None
                elif key == 'quit':
                    _key_t.join()
                    print("\n\rQuit")
                    break
    
            sleep(0.05)
    
    if __name__ == "__main__":
        try:
            main()
        except KeyboardInterrupt:
            pass
        except Exception as e:
            print(f"ERROR: {e}")
        finally:
            Vilib.camera_close()
            px.stop()
            sleep(.2)

**Comment ça fonctionne ?**

Pour comprendre la logique de base de ce code, vous pouvez vous concentrer sur les parties clés suivantes :

1. **Initialisation et importations :**
   Les instructions d'importation au début du code vous permettent de comprendre les bibliothèques utilisées.

2. **Variables globales :**
   Les définitions des variables globales, telles que ``color`` et ``key``, qui sont utilisées dans tout le code pour suivre la couleur cible et les entrées du clavier.

3. ``renew_color_detect()`` :
   Cette fonction sélectionne une couleur aléatoire dans une liste et la définit comme couleur cible à détecter. Elle utilise également la synthèse vocale pour annoncer la couleur sélectionnée.

4. ``key_scan_thread()`` :
   Cette fonction s'exécute dans un thread séparé et scanne continuellement les entrées du clavier, mettant à jour la variable ``key`` avec la touche pressée. Elle utilise un verrou pour garantir un accès sécurisé aux threads.

5. ``car_move(key)`` :
   Cette fonction contrôle les mouvements du PiCar-X en fonction des entrées du clavier (``key``). Elle définit la direction et la vitesse du déplacement du robot.

6. ``main()`` : La fonction principale qui orchestre la logique générale du code. Elle fait les actions suivantes :

    * Initialise la caméra et démarre l'affichage du flux vidéo.
    * Crée un thread séparé pour scanner les entrées du clavier.
    * Annonce le début du jeu avec la synthèse vocale.
    * Entre dans une boucle continue pour :

        * Vérifier la détection d'objets colorés et déclencher des actions lorsqu'un objet valide est détecté.
        * Gérer les entrées du clavier pour contrôler le robot et interagir avec le jeu.
    * Gère la sortie du jeu et les exceptions comme l'interruption clavier (KeyboardInterrupt).
    * S'assure que la caméra est fermée et que PiCar-X s'arrête à la sortie.

En comprenant ces parties clés du code, 
vous pouvez saisir la logique fondamentale de la manière dont le robot PiCar-X réagit aux entrées du clavier et détecte/interagit avec les objets d'une couleur spécifique en utilisant les capacités de la caméra et de la sortie audio.
