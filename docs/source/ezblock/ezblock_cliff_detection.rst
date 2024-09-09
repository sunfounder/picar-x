.. note::

    Bonjour et bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 sur Facebook ! Plongez dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et aux avant-premières.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos nouveaux produits.
    - **Promotions festives et concours** : Participez à des concours et promotions lors des fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

Détection des falaises
===========================

Ce projet utilisera le **module de niveaux de gris** pour empêcher le PiCar-X de tomber d'une falaise lorsqu'il se déplace librement dans votre maison. Ce projet est essentiel pour les maisons avec des escaliers.

**CONSEILS**

.. image:: img/sp210512_164544.png

Le **module de niveaux de gris** effectuera la même opération plusieurs fois. Pour simplifier le programme, ce projet introduit une **fonction** qui renverra une variable de **liste** au bloc **faire en continu**.

**EXEMPLE**

.. note::

    * Vous pouvez écrire le programme selon l'image ci-dessous, veuillez vous référer au tutoriel :ref:`ezblock:create_project_latest`.
    * Ou retrouvez le code du même nom sur la page **Exemples** d'EzBlock Studio et cliquez directement sur **Exécuter** ou **Modifier**.

.. image:: img/sp210512_164755.png

.. image:: img/sp210512_164832.png
