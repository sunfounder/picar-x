.. note::

    Bonjour et bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 sur Facebook ! Plongez dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et aux avant-premières.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos nouveaux produits.
    - **Promotions festives et concours** : Participez à des concours et promotions lors des fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

Corrida
==============

Transformez le PiCar-X en un taureau enragé ! Préparez un tissu rouge, comme un mouchoir, et devenez un matador. Lorsque le PiCar-X poursuivra le tissu rouge, faites attention à ne pas vous faire percuter !

.. note::

    Ce projet est plus avancé que les précédents. Le PiCar-X devra utiliser la fonction de détection de couleur pour maintenir la caméra orientée vers le tissu rouge, puis ajuster automatiquement l'orientation du corps en fonction de la direction de la caméra.

**CONSEILS**

.. image:: img/sp210512_174650.png

Commencez par ajouter le bloc **détection de couleur [rouge]** au widget **Démarrer** pour que le PiCar-X recherche un objet de couleur rouge. Dans la boucle infinie, ajoutez le bloc **[largeur] de la couleur détectée** pour transformer l'entrée en une grille de “détection d'objet”.

.. image:: img/sp210512_174807.png

La “détection d'objet” fournira les coordonnées détectées en valeurs (x, y), 
basées sur le point central de l'image de la caméra. 
L'écran est divisé en une grille 3x3, comme illustré ci-dessous, 
donc si le tissu rouge est dans le coin supérieur gauche de l'image de la caméra, les coordonnées (x, y) seront (-1, 1).

.. image:: img/sp210512_174956.png

La “détection d'objet” détectera la largeur et la hauteur du graphique.
Si plusieurs cibles sont identifiées, les dimensions de la plus grande seront enregistrées.

**EXEMPLE**

.. note::

    * Vous pouvez écrire le programme selon l'image ci-dessous, veuillez vous référer au tutoriel :ref:`ezblock:create_project_latest`.
    * Ou retrouvez le code du même nom sur la page **Exemples** d'EzBlock Studio et cliquez directement sur **Exécuter** ou **Modifier**.

.. image:: img/sp210512_175519.png
    :width: 800
