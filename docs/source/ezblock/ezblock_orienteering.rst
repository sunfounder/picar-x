.. note::

    Bonjour et bienvenue dans la communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Plongez-vous dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et relevez les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprenez & Partagez** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et à des avant-premières.
    - **Remises spéciales** : Profitez de réductions exclusives sur nos derniers produits.
    - **Promotions festives et concours** : Participez à des tirages au sort et à des promotions durant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

Course d'orientation
======================

Ce projet utilise la fonction de télécommande pour guider le PiCar-X dans une chasse au trésor compétitive !

Commencez par installer un parcours d'obstacles, un labyrinthe ou même une pièce vide dans laquelle le PiCar-X peut circuler. Ensuite, placez six marqueurs aléatoires le long de la route et placez une carte de couleur à chaque marqueur pour que le PiCar-X les trouve.

Les six modèles de couleurs pour le PiCar-X sont : rouge, orange, jaune, vert, bleu et violet, prêts à être imprimés à partir du fichier PDF suivant.

* :download:`[PDF]Color Cards <https://github.com/sunfounder/sf-pdf/raw/master/prop_card/object_detection/color-cards.pdf>`

.. image:: img/color_card.png

.. note::

    Les couleurs imprimées peuvent avoir une teinte légèrement différente des modèles de couleurs Ezblock en raison des différences de toner d'imprimante ou du support d'impression, comme un papier légèrement teinté. Cela peut entraîner une reconnaissance des couleurs moins précise.

Le PiCar-X sera programmé pour trouver trois des six couleurs dans un ordre aléatoire et utilisera la fonction TTS pour annoncer la couleur à rechercher ensuite.

L'objectif est d'aider le PiCar-X à trouver chacune des trois couleurs dans le temps le plus court possible.

Placez le PiCar-X au centre du terrain et cliquez sur le bouton de la page Télécommande pour commencer le jeu.

.. image:: img/orienteering.png

Jouez à tour de rôle avec des amis pour voir qui peut aider le PiCar-X à atteindre l'objectif le plus rapidement !

**EXEMPLE**

.. note::

    * Vous pouvez écrire le programme en suivant l'image ci-dessous, veuillez consulter le tutoriel : :ref:`ezblock:create_project_latest`.
    * Ou trouvez le code portant le même nom sur la page **Exemples** d'EzBlock Studio, puis cliquez sur **Exécuter** ou **Modifier** directement.

.. image:: img/sp210513_154117.png
    :width: 800

.. image:: img/sp210513_154256.png
    :width: 800

.. image:: img/sp210513_154425.png
    :width: 800
