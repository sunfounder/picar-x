.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 sur Facebook ! Plongez plus profondément dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et avant-premières.
    - **Réductions exclusives** : Profitez de réductions exclusives sur nos nouveaux produits.
    - **Promotions festives et concours** : Participez à des concours et promotions lors des fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_treasure:

20. Chasse au Trésor
============================

Dans cette leçon, vous allez transformer votre PiCar-X en **robot chasseur de trésor**.  
Aménagez un petit labyrinthe dans votre pièce et placez six cartes de couleurs différentes dans chaque coin.  
Votre PiCar-X va **chercher, reconnaître et célébrer** lorsqu’il trouvera la couleur cible.  

Ce projet combine trois compétences que vous avez déjà apprises :

* **Vision par ordinateur** – détection des cartes colorées avec la caméra Pi.  
* **Contrôle au clavier** – conduire le robot manuellement à travers le labyrinthe.  
* **Retour vocal** – Pico2Wave annonce la couleur cible et le succès.  

C’est un jeu amusant qui montre comment les robots peuvent **voir, réfléchir et agir** comme de vrais chasseurs de trésors !

.. note::  
   Vous pouvez télécharger et imprimer les :download:`Cartes couleur PDF <https://github.com/sunfounder/sf-pdf/raw/master/prop_card/object_detection/color-cards.pdf>` pour une détection plus fiable.

Exécuter le code
---------------------

.. raw:: html

    <run></run>

.. code-block:: bash

    cd ~/picar-x/example
    sudo python3 20.treasure_hunt.py

Après l’exécution, vous verrez un message comme celui-ci :

.. code-block:: text

    * Running on http://0.0.0.0:9000/ (Press CTRL+C to quit)

Ensuite, ouvrez ``http://<votre IP>:9000/mjpg`` dans votre navigateur pour voir le flux vidéo en direct.  
Exemple : ``http://192.168.18.113:9000/mjpg``

.. image:: img/display.png

Règles du jeu
----------------------

1. Le robot sélectionne aléatoirement une **couleur cible** et dit : **« Cherche le rouge ! »**  
2. Vous conduisez le PiCar-X avec le clavier :

   * ``w`` = avancer  
   * ``a`` = tourner à gauche  
   * ``s`` = reculer  
   * ``d`` = tourner à droite  
   * ``space`` = répéter la couleur cible  
   * ``Ctrl+C`` = quitter

3. Lorsque la caméra voit la carte de couleur cible, PiCar-X dit **« Bravo ! »**  
4. Une nouvelle couleur cible est choisie et la chasse continue !

Code
----


.. code-block:: python

    #!/usr/bin/env python3

    from picarx import Picarx
    from vilib import Vilib
    from picarx.tts import Pico2Wave

    from time import sleep
    import threading
    import readchar
    import random

    # -----------------------
    # Settings
    # -----------------------
    COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
    DETECTION_WIDTH_THRESHOLD = 100  # how wide the color blob must be
    DRIVE_SPEED = 80
    TURN_ANGLE = 30

    MANUAL = """
    Press keys to control PiCar-X:
      w: forward    a: turn left    s: backward    d: turn right
      space: repeat target          Ctrl+C: quit
    """

    # -----------------------
    # Init
    # -----------------------
    px = Picarx()

    tts = Pico2Wave()
    tts.set_lang("en-US")

    current_color = "red"
    key = None
    lock = threading.Lock()

    def say(line: str):
        print(f"[SAY] {line}")
        tts.say(line)

    def renew_color_detect():
        """Choose a new target color and start detection."""
        global current_color
        current_color = random.choice(COLORS)
        Vilib.color_detect(current_color)
        say(f"Look for {current_color}!")

    def key_scan_thread():
        """Background thread reading keys."""
        global key
        while True:
            k = readchar.readkey()
            # Map special keys before lowercasing
            if k == readchar.key.SPACE:
                mapped = "space"
            elif k == readchar.key.CTRL_C:
                mapped = "quit"
            else:
                mapped = k.lower()

            with lock:
                key = mapped

            if mapped == "quit":
                return
            sleep(0.01)

    def car_move(k: str):
        if k == "w":
            px.set_dir_servo_angle(0)
            px.forward(DRIVE_SPEED)
        elif k == "s":
            px.set_dir_servo_angle(0)
            px.backward(DRIVE_SPEED)
        elif k == "a":
            px.set_dir_servo_angle(-TURN_ANGLE)
            px.forward(DRIVE_SPEED)
        elif k == "d":
            px.set_dir_servo_angle(TURN_ANGLE)
            px.forward(DRIVE_SPEED)

    def main():
        global key

        # Start camera and web preview
        Vilib.camera_start(vflip=False, hflip=False)
        Vilib.display(local=False, web=True)
        sleep(0.8)

        print(MANUAL.strip())
        say("Game start!")
        sleep(0.1)
        renew_color_detect()

        # Start keyboard thread (modern style)
        key_thread = threading.Thread(target=key_scan_thread, daemon=True)
        key_thread.start()

        try:
            while True:
                # Check detection: if target color present and wide enough
                if (Vilib.detect_obj_parameter.get("color_n", 0) != 0 and
                    Vilib.detect_obj_parameter.get("color_w", 0) > DETECTION_WIDTH_THRESHOLD):
                    say("Well done!")
                    sleep(0.1)
                    renew_color_detect()

                # Take a snapshot of the last key (and clear it)
                with lock:
                    k = key
                    key = None

                # Handle movement / actions
                if k in ("w", "a", "s", "d"):
                    car_move(k)
                    sleep(0.5)
                    px.stop()
                elif k == "space":
                    say(f"Look for {current_color}!")
                elif k == "quit":
                    print("\n[INFO] Quit requested.")
                    break

                sleep(0.05)

        except KeyboardInterrupt:
            print("\n[INFO] Stopped by user.")
        finally:
            try:
                Vilib.camera_close()
            except Exception:
                pass
            px.stop()
            say("Goodbye!")
            sleep(0.2)

    if __name__ == "__main__":
        main()

Comment ça marche
-----------------------------

1. **Initialisation**

   * Importer les modules et configurer PiCar-X, la caméra et la synthèse vocale TTS.  
   * Définir la liste des couleurs, la vitesse et l’angle de direction.

2. **Sélection de la couleur cible**

   * ``renew_color_detect()`` choisit aléatoirement une couleur cible.  
   * Le robot annonce la couleur cible avec Pico2Wave.

3. **Contrôle au clavier**

   * ``key_scan_thread()`` s’exécute en arrière-plan pour capturer les touches.  
   * Les touches ``w, a, s, d`` contrôlent le mouvement ; ``space`` répète la couleur cible.

4. **Détection de couleur**

   * La caméra vérifie en continu si la couleur cible est visible.  
   * Si la zone détectée est suffisamment grande, PiCar-X célèbre la trouvaille.

5. **Boucle principale**

   * Gère en continu le mouvement, la détection et le retour vocal.  
   * Arrête proprement le robot et la caméra lors de la sortie.

Dépannage
---------------

* **Le flux de la caméra ne fonctionne pas ?**  

  Exécutez ``libcamera-hello`` pour vérifier si la caméra Pi est correctement connectée.

* **Le robot ne détecte pas les couleurs ?**

  Assurez-vous que les cartes sont bien imprimées et placées dans un bon éclairage. Essayez d’ajuster ``DETECTION_WIDTH_THRESHOLD``.

* **Pas de retour vocal ?**

  Vérifiez que ``pico2wave`` est installé et que votre sortie audio est bien configurée.

* **La voiture ne bouge pas ?**

  Vérifiez que l’alimentation de PiCar-X est allumée et que la calibration des moteurs est correcte.

----

En terminant cette leçon, vous avez construit un **mini-jeu de chasse au trésor** avec PiCar-X,  
en combinant **vision**, **contrôle** et **interaction** dans un seul projet !
