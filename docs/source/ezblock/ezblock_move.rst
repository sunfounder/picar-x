.. note::

    Bonjour et bienvenue dans la communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Plongez-vous dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et relevez les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprenez & Partagez** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et à des avant-premières.
    - **Remises spéciales** : Profitez de réductions exclusives sur nos nouveaux produits.
    - **Promotions festives et concours** : Participez à des tirages au sort et à des promotions durant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

Mouvement
============

Ce premier projet vous apprend à programmer les actions de mouvement pour le PiCar-X. Dans ce projet, le programme ordonnera au PiCar-X d'exécuter cinq actions dans l'ordre : « avancer », « reculer », « tourner à gauche », « tourner à droite » et « s'arrêter ».

Pour apprendre les bases de l'utilisation d'Ezblock Studio, veuillez lire attentivement les deux sections suivantes :

* :ref:`ezblock:create_project_latest`

.. image:: img/move.png

**CONSEILS**

.. image:: img/sp210512_113300.png

Ce bloc fera avancer le PiCar-X à une vitesse basée sur un pourcentage de la puissance disponible. Dans l'exemple ci-dessous, « 50 » correspond à 50 % de la puissance, soit la moitié de la vitesse.

.. image:: img/sp210512_113418.png

Ce bloc fera reculer le PiCar-X à une vitesse basée sur un pourcentage de la puissance disponible.

.. image:: img/sp210512_113514.png

Ce bloc ajuste l'orientation des roues avant. La plage de valeurs est de « -45 » à « 45 ». Dans l'exemple ci-dessous, « -30 » signifie que les roues tourneront de 30° vers la gauche.

.. image:: img/BLK_Basic_delay.png
    :width: 200

Ce bloc introduira une pause temporaire entre les commandes, basée sur des millisecondes. Dans l'exemple ci-dessous, le PiCar-X attendra 1 seconde (1000 millisecondes) avant d'exécuter la commande suivante.

.. image:: img/sp210512_113550.png

Ce bloc arrêtera complètement le PiCar-X.

**EXEMPLE**

.. note::

    * Vous pouvez écrire le programme en suivant l'image ci-dessous, veuillez consulter le tutoriel : :ref:`ezblock:create_project_latest`.
    * Ou trouvez le code portant le même nom sur la page **Exemples** d'EzBlock Studio, puis cliquez sur **Exécuter** ou **Modifier** directement.

.. image:: img/sp210512_113827.png
