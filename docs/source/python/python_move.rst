.. note::

    Bonjour et bienvenue dans la communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Plongez dans l'univers du Raspberry Pi, de l'Arduino et de l'ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des conseils et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et à des avant-goûts exclusifs.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos derniers produits.
    - **Promotions et concours festifs** : Participez à des concours et promotions spéciales pendant les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_move:

1. Faites bouger PiCar-X
=============================

Voici le premier projet, testons les mouvements de base de PiCar-X.

**Exécuter le code**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 1.move.py

Après avoir exécuté le code, PiCar-X avancera, effectuera un virage en forme de S, s'arrêtera et secouera sa tête.

**Code**

.. note::
    Vous pouvez **Modifier/Réinitialiser/Copier/Exécuter/Arrêter** le code ci-dessous. Mais avant cela, vous devez vous rendre dans le chemin du code source, tel que ``picar-x/example``. Après avoir modifié le code, vous pouvez l'exécuter directement pour voir le résultat.

.. raw:: html

    <run></run>

.. code-block:: python

    from picarx import Picarx
    import time


    if __name__ == "__main__":
        try:
            px = Picarx()
            px.forward(30)
            time.sleep(0.5)
            for angle in range(0,35):
                px.set_dir_servo_angle(angle)
                time.sleep(0.01)
            for angle in range(35,-35,-1):
                px.set_dir_servo_angle(angle)
                time.sleep(0.01)        
            for angle in range(-35,0):
                px.set_dir_servo_angle(angle)
                time.sleep(0.01)
            px.forward(0)
            time.sleep(1)

            for angle in range(0,35):
                px.set_camera_servo1_angle(angle)
                time.sleep(0.01)
            for angle in range(35,-35,-1):
                px.set_camera_servo1_angle(angle)
                time.sleep(0.01)        
            for angle in range(-35,0):
                px.set_camera_servo1_angle(angle)
                time.sleep(0.01)
            for angle in range(0,35):
                px.set_camera_servo2_angle(angle)
                time.sleep(0.01)
            for angle in range(35,-35,-1):
                px.set_camera_servo2_angle(angle)
                time.sleep(0.01)        
            for angle in range(-35,0):
                px.set_camera_servo2_angle(angle)
                time.sleep(0.01)
                
        finally:
            px.forward(0)

**Comment ça fonctionne ?**

La fonctionnalité de base de PiCar-X se trouve dans le module ``picarx``, 
qui permet de contrôler le servo de direction et les roues,
et fait en sorte que PiCar-X avance, tourne en forme de S ou secoue sa tête.

Les bibliothèques pour supporter les fonctions de base de PiCar-X sont maintenant importées. 
Ces lignes apparaîtront dans tous les exemples impliquant le mouvement de PiCar-X.

.. code-block:: python
    :emphasize-lines: 0

    from picarx import Picarx
    import time

La fonction suivante avec la boucle ``for`` est ensuite utilisée pour faire avancer PiCar-X, changer de direction, et bouger la caméra en mode panoramique/inclinaison.

.. code-block:: python

    px.forward(speed)    
    px.set_dir_servo_angle(angle)
    px.set_camera_servo1_angle(angle)
    px.set_camera_servo2_angle(angle)

* ``forward()`` : Ordonne à PiCar-X d'avancer à une ``vitesse`` donnée.
* ``set_dir_servo_angle`` : Tourne le servo de direction à un ``angle`` spécifique.
* ``set_cam_pan_angle`` : Tourne le servo de panoramique à un ``angle`` spécifique.
* ``set_cam_tilt_angle`` : Tourne le servo d'inclinaison à un ``angle`` spécifique.

.. image:: img/pan_tilt_servo.png
    :width: 400
