.. note::

    Bonjour et bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 sur Facebook ! Plongez dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour perfectionner vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et aux avant-premières.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos derniers produits.
    - **Promotions festives et concours** : Participez à des concours et à des promotions spéciales lors des fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

Musique de fond
======================

En plus de programmer le PiCar-X pour jouer des effets sonores ou utiliser la synthèse vocale (TTS), le PiCar-X peut également diffuser de la musique de fond. Ce projet utilisera également un widget **Slider** pour ajuster le volume de la musique.

* :ref:`ezblock:remote_control_latest`

Pour un tutoriel détaillé sur les fonctions de contrôle à distance d'Ezblocks, veuillez consulter le tutoriel :ref:`ezb_remote_control`.

**ASTUCES**

.. image:: img/sp210512_152803.png

Le bloc **jouer la musique de fond** doit être ajouté à la fonction **Start**. Utilisez le menu déroulant pour choisir la musique de fond que le PiCar-X diffusera.

.. image:: img/sp210512_153123.png

Le bloc **définir le volume de la musique de fond à** permet d'ajuster le volume dans une plage de 0 à 100.

.. image:: img/sp210512_154708.png

Faites glisser une barre **Slider** depuis la page **Remote Control** pour régler le volume de la musique.

.. image:: img/sp210512_154259.png

Le bloc **slider [A] obtenir la valeur** lira la valeur du curseur. Dans l'exemple ci-dessus, le curseur ‘A’ est sélectionné. S'il y a plusieurs curseurs, utilisez le menu déroulant pour choisir celui qui convient.

**EXEMPLE**

.. note::

    * Vous pouvez écrire le programme en suivant l'image ci-dessous. Veuillez vous référer au tutoriel :ref:`ezblock:create_project_latest`.
    * Ou trouvez le code du même nom sur la page **Exemples** de l'EzBlock Studio et cliquez sur **Exécuter** ou **Modifier** directement.

.. image:: img/sp210512_155406.png
