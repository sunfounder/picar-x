.. note::

    Bonjour, bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino & ESP32 sur Facebook ! Explorez plus en profondeur l'univers de Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et surmontez les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprenez & Partagez** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux avant-goûts.
    - **Réductions exclusives** : Profitez de remises spéciales sur nos nouveaux produits.
    - **Promotions festives et concours** : Participez à des concours et à des promotions pendant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_bull_fight:

10. Combat de Taureau
=============================


Transformez le PiCar-X en un taureau enragé ! Utilisez sa caméra pour suivre et charger vers un tissu rouge !

**Exécution du code**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 10.bull_fight.py


**Visualisation de l'image**

Après l'exécution du code, le terminal affichera l'invite suivante :

.. code-block::

    No desktop !
    * Serving Flask app "vilib.vilib" (lazy loading)
    * Environment: production
    WARNING: Do not use the development server in a production environment.
    Use a production WSGI server instead.
    * Debug mode: off
    * Running on http://0.0.0.0:9000/ (Press CTRL+C to quit)

Vous pouvez alors entrer ``http://<your IP>:9000/mjpg`` dans le navigateur pour visualiser le flux vidéo. Par exemple : ``https://192.168.18.113:9000/mjpg``

.. image:: img/display.png

**Code**

.. note::
    Vous pouvez **Modifier/Réinitialiser/Copier/Exécuter/Arrêter** le code ci-dessous. Mais avant cela, vous devez vous rendre dans le chemin du code source tel que ``picar-x\examples``. Après modification, exécutez directement pour observer les résultats.

.. raw:: html

    <run></run>

.. code-block:: python

    from picarx import Picarx
    from time import sleep
    from vilib import Vilib

    px = Picarx()

    def clamp_number(num,a,b):
    return max(min(num, max(a, b)), min(a, b))

    def main():
        Vilib.camera_start()
        Vilib.display()
        Vilib.color_detect("red")
        speed = 50
        dir_angle=0
        x_angle =0
        y_angle =0
        while True:
            if Vilib.detect_obj_parameter['color_n']!=0:
                coordinate_x = Vilib.detect_obj_parameter['color_x']
                coordinate_y = Vilib.detect_obj_parameter['color_y']
                
                # ajuster l'angle de la caméra pour suivre l'objet
                x_angle +=(coordinate_x*10/640)-5
                x_angle = clamp_number(x_angle,-35,35)
                px.set_cam_pan_angle(x_angle)

                y_angle -=(coordinate_y*10/480)-5
                y_angle = clamp_number(y_angle,-35,35)
                px.set_cam_tilt_angle(y_angle)

                # mouvement
                # La direction du mouvement change plus lentement que celle de la caméra 
                # pour éviter la confusion lors de changements rapides.
                if dir_angle > x_angle:
                    dir_angle -= 1
                elif dir_angle < x_angle:
                    dir_angle += 1
                px.set_dir_servo_angle(x_angle)
                px.forward(speed)
                sleep(0.05)

            else :
                px.forward(0)
                sleep(0.05)


    if __name__ == "__main__":
        try:
        main()
        
        finally:
            px.stop()
            print("stop and exit")
            sleep(0.1)

**Comment ça fonctionne ?**

Vous devez prêter attention aux trois parties suivantes de cet exemple :

1. Définir la fonction principale :

    * Démarrer la caméra avec ``Vilib.camera_start()``.
    * Afficher le flux vidéo avec ``Vilib.display()``.
    * Activer la détection de couleur et spécifier la couleur cible comme "rouge" avec ``Vilib.color_detect("red")``.
    * Initialiser les variables : ``speed`` pour la vitesse de déplacement du véhicule, ``dir_angle`` pour l'angle de direction du mouvement, ``x_angle`` pour l'angle de rotation de la caméra, et ``y_angle`` pour l'angle d'inclinaison de la caméra.

2. Entrer dans une boucle continue (while True) pour suivre l'objet de couleur rouge :

    * Vérifier s'il y a un objet rouge détecté (``Vilib.detect_obj_parameter['color_n'] != 0``).
    * Si un objet rouge est détecté, obtenir ses coordonnées (``coordinate_x`` et ``coordinate_y``).
    * Calculer de nouveaux angles de rotation et d'inclinaison (``x_angle`` et ``y_angle``) en fonction de la position de l'objet détecté et les ajuster pour suivre l'objet.
    * Limiter les angles de rotation et d'inclinaison dans une plage spécifiée avec la fonction ``clamp_number``.
    * Régler les angles de rotation et d'inclinaison de la caméra avec ``px.set_cam_pan_angle()`` et ``px.set_cam_tilt_angle()`` pour garder l'objet en vue.

3. Contrôler le mouvement du véhicule en fonction de la différence entre ``dir_angle`` et ``x_angle`` :

    * Si ``dir_angle`` est supérieur à ``x_angle``, décrémenter ``dir_angle`` de 1 pour changer progressivement la direction.
    * Si ``dir_angle`` est inférieur à ``x_angle``, incrémenter ``dir_angle`` de 1.
    * Régler l'angle du servo de direction avec ``px.set_dir_servo_angle()`` pour ajuster les roues du véhicule en conséquence.
    * Faire avancer le véhicule à la vitesse spécifiée avec ``px.forward(speed)``.
