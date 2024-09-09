.. note::

    Bonjour et bienvenue dans la communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Plongez-vous dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et relevez les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprenez & Partagez** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et à des avant-premières.
    - **Remises spéciales** : Profitez de réductions exclusives sur nos produits les plus récents.
    - **Promotions festives et tirages au sort** : Participez à des tirages au sort et à des promotions durant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _test_grayscale:

Test du module de niveaux de gris
====================================

Le PiCar-X est équipé d'un module de niveaux de gris pour implémenter le suivi de ligne, la détection de falaises et d'autres expériences amusantes. Ce module possède trois capteurs qui renvoient chacun une valeur en fonction de la nuance de couleur détectée. Par exemple, un capteur lisant une nuance de noir pur renverra une valeur de "0".

**CONSEILS**

.. image:: img/sp210512_115406.png

Utilisez le bloc **module de niveaux de gris** pour lire la valeur de l'un des capteurs. Dans l'exemple ci-dessus, le capteur “A0” est celui situé à l'extrême gauche du PiCar-X. Utilisez la flèche déroulante pour changer le capteur en “A1” (capteur central) ou en “A2” (capteur à l'extrême droite).

.. image:: img/sp210512_120023.png

Le programme est simplifié avec un bloc **créer une liste avec**. 
Une **Liste** est utilisée de la même manière qu'une seule **Variable**, mais dans ce cas, une **Liste** est plus efficace qu'une seule **Variable** car le module de niveaux de gris renverra plusieurs valeurs de capteurs.
Le bloc **créer une liste avec** créera des **Variables** séparées pour chaque capteur, puis les placera dans une Liste.

**EXEMPLE**

.. note::

    * Vous pouvez écrire le programme en suivant l'image ci-dessous, veuillez consulter le tutoriel : :ref:`ezblock:create_project_latest`.
    * Ou trouvez le code portant le même nom sur la page **Exemples** d'EzBlock Studio, puis cliquez sur **Exécuter** ou **Modifier** directement.

.. image:: img/sp210512_120508.png
