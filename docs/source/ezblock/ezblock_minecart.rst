.. note::

    Bonjour et bienvenue dans la communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Plongez-vous dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et relevez les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprenez & Partagez** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et à des avant-premières.
    - **Remises spéciales** : Profitez de réductions exclusives sur nos derniers produits.
    - **Promotions festives et concours** : Participez à des concours et à des promotions spéciales.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _ezb_minecart:

Chariot de mine
=====================

Créons un projet de chariot de mine ! Ce projet utilise le module de niveaux de gris pour faire avancer le PiCar-X le long d'une piste. Utilisez du ruban adhésif de couleur foncée pour tracer une piste au sol aussi droite que possible, et évitez les courbes trop prononcées. Quelques essais peuvent être nécessaires si le PiCar-X déraille.

En avançant le long de la piste, les sondes situées à gauche et à droite du module de niveaux de gris détecteront le sol clair, tandis que la sonde centrale détectera la piste. Si la piste présente une courbe, la sonde située à gauche ou à droite détectera le ruban de couleur foncée et orientera les roues dans cette direction. Si le chariot atteint la fin de la piste ou déraille, le module de niveaux de gris cessera de détecter le ruban de couleur foncée et le PiCar-X s'arrêtera.

**CONSEILS**

* Le bloc **Définir ref sur ()** est utilisé pour ajuster le seuil de niveaux de gris ; vous devrez le modifier en fonction de la situation réelle. Vous pouvez exécuter le test :ref:`test_grayscale` pour voir les valeurs du module de niveaux de gris sur des surfaces blanche et noire, puis remplir les valeurs intermédiaires dans ce bloc.

**EXEMPLE**

.. note::

    * Vous pouvez écrire le programme en suivant l'image ci-dessous, veuillez consulter le tutoriel : :ref:`ezblock:create_project_latest`.
    * Ou trouvez le code portant le même nom sur la page **Exemples** d'EzBlock Studio, puis cliquez sur **Exécuter** ou **Modifier** directement.

.. image:: img/sp210512_170342.png

.. image:: img/sp210512_171425.png

.. image:: img/sp210512_171454.png
