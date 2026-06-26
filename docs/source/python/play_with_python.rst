.. note::

    Bonjour et bienvenue dans la communauté des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder sur Facebook ! Plongez au cœur du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et relevez les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprenez & Partagez** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux avant-goûts.
    - **Réductions exclusives** : Profitez de remises spéciales sur nos nouveaux produits.
    - **Promotions et concours festifs** : Participez à des concours et à des promotions lors des fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _play_python:

Jouer avec Python
=======================

Pour les débutants souhaitant programmer en **Python**, il est utile d’avoir quelques notions de base ainsi qu’une familiarité avec **Raspberry Pi OS**.  
Cette section vous guidera étape par étape — de la configuration de votre Raspberry Pi, aux mouvements de la PiCar-X, jusqu’à l’ajout de **vision par ordinateur** et d’**interaction vocale / IA**.

.. _quick_guide_python:

1. Guide Rapide Python
---------------------------

Apprenez à configurer votre environnement Raspberry Pi :  
installer Raspberry Pi OS, configurer le Wi-Fi et activer l’accès à distance pour exécuter facilement votre code Python.  
Si vous savez déjà utiliser le Raspberry Pi et accéder à sa ligne de commande, vous pouvez passer directement aux sections suivantes.

.. toctree::
    :maxdepth: 1

    ../_shared/pi_start/need_components
    ../_shared/pi_start/install_os_trixie
    ../_shared/pi_start/power_supply_robot_hat
    ../_shared/pi_start/set_up_pi
    install_all_modules
    py_servo_adjust

2. Mouvements de Base
-----------------------

Une fois votre PiCar-X assemblée, commencez par des programmes simples de **mouvement**.  
Vous apprendrez à **contrôler les moteurs**, à **avancer / reculer**, à **tourner**, et à utiliser des capteurs de base pour éviter les obstacles ou suivre une ligne.

.. toctree::
    :maxdepth: 1

    python_calibrate
    python_move
    python_keyboard
    python_avoid
    python_cliff
    python_line_track

3. Vision par Ordinateur
-------------------------

Donnez à votre PiCar-X la capacité de **voir** grâce à sa caméra.  
Cette section couvre des projets amusants basés sur la vision : suivi de visage, enregistrement vidéo, interactions avec des objets, ou encore **contrôle de la voiture via vidéo ou application mobile**.

.. toctree::
    :maxdepth: 1

    python_computer_vision
    python_stare_at_you
    python_record
    python_bull_fight
    python_video_car
    control_by_app

