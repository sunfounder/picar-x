.. note::

    Bonjour et bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 sur Facebook ! Plongez dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et aux avant-premières.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos nouveaux produits.
    - **Promotions festives et concours** : Participez à des concours et promotions lors des fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

Détection des couleurs
===========================

Le PiCar-X est une voiture autonome équipée d'une caméra intégrée, permettant aux programmes Ezblock d'utiliser le code de détection d'objets et de reconnaissance des couleurs. Dans cette section, nous allons utiliser Ezblock pour créer un programme de détection des couleurs.

.. note:: 

    Avant de commencer cette section, assurez-vous que le câble FFC de la caméra Raspberry Pi est correctement connecté. Pour des instructions détaillées sur la connexion sécurisée du câble FCC, consultez :ref:`assembly_instructions`.

Dans ce programme, Ezblock se verra d'abord indiquer la plage de valeurs de Teinte-Saturation-Valeur (HSV) de la couleur à détecter, puis utilisera OpenCV pour traiter les couleurs dans cette plage HSV afin de supprimer les bruits de fond, et enfin encadrera la couleur correspondante.

Ezblock inclut 6 modèles de couleurs pour le PiCar-X : "rouge", "orange", "jaune", "vert", "bleu" et "violet". Des cartes de couleurs ont été préparées dans le PDF suivant et devront être imprimées sur une imprimante couleur.

* :download:`[PDF]Color Cards <https://github.com/sunfounder/sf-pdf/raw/master/prop_card/object_detection/color-cards.pdf>`

.. image:: img/color_card.png
    :width: 600

.. note::

    Les couleurs imprimées peuvent légèrement différer des modèles de couleurs Ezblock en raison des variations de toners d'imprimante ou du support d'impression, comme un papier de couleur beige. Cela peut entraîner une reconnaissance des couleurs moins précise.


.. image:: img/ezblock_color_detect.PNG

**CONSEILS**

.. image:: img/sp210512_121105.png

Glissez le widget Vidéo depuis la page de télécommande, et il générera un moniteur vidéo. Pour plus d'informations sur l'utilisation du widget Vidéo, veuillez consulter le tutoriel vidéo Ezblock ici : :ref:`ezblock:video_latest`.

.. image:: img/sp210512_121125.png

Activez le moniteur vidéo en réglant le bloc **moniteur de caméra** sur **activé**. Remarque : Désactiver le **moniteur de caméra** fermera le moniteur, mais la détection d'objets restera disponible.

.. image:: img/sp210512_134133.png

Utilisez le bloc **détection de couleurs** pour activer la détection de couleurs. Remarque : une seule couleur peut être détectée à la fois.

**EXEMPLE**

.. note::

    * Vous pouvez écrire le programme selon l'image ci-dessous, veuillez vous référer au tutoriel :ref:`ezblock:create_project_latest`.
    * Ou retrouvez le code du même nom sur la page **Exemples** d'EzBlock Studio et cliquez directement sur **Exécuter** ou **Modifier**.

.. image:: img/sp210512_134636.png
