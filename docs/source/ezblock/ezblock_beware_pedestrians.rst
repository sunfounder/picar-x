.. note::

    Bonjour et bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 sur Facebook ! Plongez dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et aux avant-premières.
    - **Réductions spéciales** : Profitez de remises exclusives sur nos derniers produits.
    - **Promotions festives et concours** : Participez à des concours et des promotions lors des fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

Attention aux piétons
=============================

Ce projet vise à faire en sorte que le PiCar-X prenne des mesures appropriées en fonction des conditions routières. Pendant la conduite, le PiCar-X s'arrêtera complètement si un piéton est détecté sur son chemin.

Une fois le programme lancé, tenez une photo d'une personne devant le PiCar-X. Le moniteur vidéo détectera le visage de la personne et le PiCar-X s'arrêtera automatiquement.

Pour simuler les protocoles de sécurité routière, une procédure de jugement est créée pour envoyer une valeur **[count]** à un bloc **if do else**. Cette procédure vérifiera 10 fois la présence d'un visage humain, et si un visage est détecté, **[count]** sera incrémenté de +1. Lorsque **[count]** dépasse 3, le PiCar-X cessera de se déplacer.

* :ref:`ezblock:remote_control_latest`

.. image:: img/face_detection.PNG


**EXEMPLE**

.. note::

    * Vous pouvez écrire le programme en vous basant sur l'image suivante. Veuillez vous référer au tutoriel :ref:`ezblock:create_project_latest`.
    * Ou trouvez le code portant le même nom sur la page **Exemples** de l'EzBlock Studio et cliquez directement sur **Exécuter** ou **Modifier**.

.. image:: img/sp210512_185509.png
