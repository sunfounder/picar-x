.. note::

    Bonjour et bienvenue dans la communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Plongez-vous dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et relevez les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprenez & Partagez** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et à des avant-premières.
    - **Remises spéciales** : Profitez de réductions exclusives sur nos derniers produits.
    - **Promotions festives et concours** : Participez à des tirages au sort et à des promotions durant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

Module Caméra
====================================


**Description**

.. image:: img/camera_module_pic.png
   :width: 200
   :align: center

Il s'agit d'un module caméra Raspberry Pi de 5MP avec capteur OV5647. Il est plug and play, connectez le câble ruban inclus au port CSI (Interface Série Caméra) sur votre Raspberry Pi et il est prêt à être utilisé.

La carte est petite, environ 25 mm x 23 mm x 9 mm, et pèse 3 g, ce qui la rend idéale pour les applications mobiles ou autres applications critiques en termes de taille et de poids. Le module caméra a une résolution native de 5 mégapixels et dispose d'un objectif à focale fixe intégré qui capture des images fixes en 2592 x 1944 pixels et prend également en charge les vidéos 1080p30, 720p60 et 640x480p90.

.. note:: 

   Le module est uniquement capable de capturer des images et des vidéos, pas de son.


**Spécifications**

* **Résolution des Images Statiques**: 2592×1944 
* **Résolution Vidéo Prise en Charge**: 1080p/30 fps, 720p/ 60fps et enregistrement vidéo 640 x 480p 60/90 
* **Ouverture (F)**: 1.8 
* **Angle de Vue**: 65 degrés 
* **Dimensions**: 24mmx23.5mmx8mm 
* **Poids**: 3g 
* **Interface**: Connecteur CSI 
* **Système d'Exploitation Supporté**: Raspberry Pi OS (dernière version recommandée)


**Assembler le Module Caméra**

Sur le module caméra ou le Raspberry Pi, vous trouverez un connecteur en plastique plat. Tirez doucement sur le commutateur de fixation noir jusqu'à ce qu'il soit partiellement sorti. Insérez le câble FFC dans le connecteur en plastique dans la direction indiquée et repoussez le commutateur de fixation en place.

Si le câble FFC est correctement installé, il sera droit et ne se retirera pas lorsque vous le tirerez doucement. Sinon, réinstallez-le.

.. image:: img/connect_ffc.png
.. image:: img/1.10_camera.png
   :width: 700

.. warning::

   N'installez pas la caméra avec l'alimentation allumée, cela pourrait endommager votre caméra.

.. **Activer l'interface de la caméra**

.. Exécutez la commande suivante pour activer l'interface de la caméra de votre Raspberry Pi. Si elle est déjà activée, ignorez cette étape ; si vous ne savez pas si elle l'est ou non, veuillez continuer.

.. .. raw:: html

..    <run></run>

.. .. code-block::

..    sudo raspi-config

.. **3 Options d'interface**

.. .. image:: img/image282.png
..    :align: center

.. **P1 Camera**

.. .. image:: img/camera_config1.png
..    :align: center

.. **<Oui>, puis <Ok> -> <Finish>**

.. .. image:: img/camera_config2.png
..    :align: center

.. Une fois la configuration terminée, il est recommandé de redémarrer le Raspberry Pi.

.. .. raw:: html

..    <run></run>

.. .. code-block::

..    sudo reboot
