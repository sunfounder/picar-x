.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 sur Facebook ! Plongez dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des conseils et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et aux avant-premières.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos derniers produits.
    - **Promotions et concours festifs** : Participez à des concours et à des promotions lors des fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

Détection de Visage
======================

En plus de la détection des couleurs, PiCar-X inclut également une fonction de détection de visage. Dans l'exemple suivant, le widget Joystick est utilisé pour ajuster l'orientation de la caméra, et le nombre de visages détectés sera affiché dans le moniteur de débogage.

Pour plus d'informations sur l'utilisation du widget Vidéo, veuillez consulter le tutoriel vidéo Ezblock ici : :ref:`ezblock:video_latest`.

.. image:: img/face_detection.PNG


**CONSEILS**

.. image:: img/sp210512_141947.png

Activez le widget **détection de visage** en le réglant sur **on** pour activer la détection faciale.

.. image:: img/sp210512_142327.png

Ces deux blocs sont utilisés pour ajuster l'orientation de la caméra panoramique, similaire à la conduite du PiCar-X dans le tutoriel :ref:`ezb_remote_control`. À mesure que la valeur augmente, la caméra pivote vers la droite ou vers le haut, et une diminution de la valeur la fait pivoter vers la gauche ou vers le bas.

.. image:: img/sp210512_142407.png

Les résultats de détection d'image sont donnés via le bloc **visage détecté**. Utilisez le menu déroulant pour choisir entre la lecture des coordonnées, la taille ou le nombre de résultats de la fonction de détection d'image.

.. image:: img/sp210512_142616.png

Utilisez le bloc **créer un texte avec** pour imprimer la combinaison de **texte** et des données de **visage détecté**.

**EXEMPLE**

.. note::

    * Vous pouvez écrire le programme en fonction de l'image ci-dessous, veuillez vous référer au tutoriel :ref:`ezblock:create_project_latest`.
    * Ou retrouvez le code du même nom sur la page **Exemples** d'EzBlock Studio et cliquez directement sur **Exécuter** ou **Modifier**.

.. image:: img/sp210512_142830.png
