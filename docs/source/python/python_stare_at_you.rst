.. note::

    Bonjour et bienvenue dans la communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Explorez plus en profondeur le Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus exclusifs.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos derniers produits.
    - **Promotions et concours festifs** : Participez à des concours et des promotions spéciales pendant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_stare:

8. Vous fixer du regard
=======================

Ce projet est également basé sur le projet :ref:`py_computer_vision`, avec l'ajout d'algorithmes de détection de visage.

Lorsque vous apparaissez devant la caméra, elle reconnaît votre visage et ajuste son cardan pour garder votre visage au centre du cadre.

Vous pouvez visionner l'écran à l'adresse ``http://<your IP>:9000/mjpg``.

**Exécuter le code**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 8.stare_at_you.py

Une fois le code exécuté, la caméra de la voiture suivra toujours votre visage.

**Code**

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
        Vilib.face_detect_switch(True)
        x_angle =0
        y_angle =0
        while True:
            if Vilib.detect_obj_parameter['human_n']!=0:
                coordinate_x = Vilib.detect_obj_parameter['human_x']
                coordinate_y = Vilib.detect_obj_parameter['human_y']
                
                # change the pan-tilt angle for track the object
                x_angle +=(coordinate_x*10/640)-5
                x_angle = clamp_number(x_angle,-35,35)
                px.set_cam_pan_angle(x_angle)

                y_angle -=(coordinate_y*10/480)-5
                y_angle = clamp_number(y_angle,-35,35)
                px.set_cam_tilt_angle(y_angle)

                sleep(0.05)

            else :
                pass
                sleep(0.05)

    if __name__ == "__main__":
        try:
            main()
        
        finally:
            px.stop()
            print("stop and exit")
            sleep(0.1)

**Comment ça fonctionne ?**

Ces lignes de code dans la boucle ``while True`` permettent à la caméra de suivre le visage.

.. code-block:: python

    while True:
        if Vilib.detect_obj_parameter['human_n']!=0:
            coordinate_x = Vilib.detect_obj_parameter['human_x']
            coordinate_y = Vilib.detect_obj_parameter['human_y']
            
            # modifier l'angle de panoramique/inclinaison pour suivre l'objet
            x_angle +=(coordinate_x*10/640)-5
            x_angle = clamp_number(x_angle,-35,35)
            px.set_cam_pan_angle(x_angle)

            y_angle -=(coordinate_y*10/480)-5
            y_angle = clamp_number(y_angle,-35,35)
            px.set_cam_tilt_angle(y_angle)

1. Vérifiez s'il y a un visage humain détecté

    .. code-block:: python

        Vilib.detect_obj_parameter['human_n'] != 0

2. Si un visage humain est détecté, obtenez les coordonnées (``coordinate_x`` et ``coordinate_y``) du visage détecté.

3. Calculez les nouveaux angles de panoramique et d'inclinaison (``x_angle`` et ``y_angle``) en fonction de la position du visage détecté et ajustez-les pour suivre le visage.

4. Limitez les angles de panoramique et d'inclinaison dans les plages spécifiées à l'aide de la fonction ``clamp_number``.

5. Réglez les angles de panoramique et d'inclinaison de la caméra à l'aide de ``px.set_cam_pan_angle()`` et ``px.set_cam_tilt_angle()``.
