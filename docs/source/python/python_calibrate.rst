.. note::

    Bonjour et bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez plus profondément dans l'univers de Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et surmontez les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour perfectionner vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et à des avant-premières.
    - **Réductions exclusives** : Profitez de remises exclusives sur nos nouveaux produits.
    - **Promotions festives et concours** : Participez à des concours et à des promotions spéciales pendant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_calibrate:

0. Calibration du PiCar-X
=============================

Calibration des moteurs et du servo
--------------------------------------

Certains angles des servos peuvent être légèrement inclinés en raison de possibles écarts pendant l'installation du PiCar-X ou de limitations propres aux servos. Vous pouvez donc les calibrer.

Bien entendu, vous pouvez passer cette étape si vous estimez que l'assemblage est parfait et qu'aucune calibration n'est nécessaire.

#. Exécutez le fichier ``calibration.py``.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/picar-x/example/calibration
        sudo python3 calibration.py

#. Après l'exécution du code, vous verrez l'interface suivante s'afficher dans le terminal.

    .. image:: img/calibrate1.png

#. La touche ``R`` permet de tester si les 3 servos fonctionnent correctement. Après avoir sélectionné un servo avec les touches ``1``, ``2`` ou ``3``, appuyez sur la touche ``R`` pour tester le servo correspondant.

#. Appuyez sur la touche numérique ``1`` pour sélectionner le servo des roues avant, puis appuyez sur ``W/S`` pour aligner les roues avant le plus droit possible sans incliner à gauche ou à droite.

    .. image:: img/calibrate2.png

#. Appuyez sur la touche numérique ``2`` pour sélectionner le **servo panoramique**, puis appuyez sur ``W/S`` pour que la plateforme de la caméra soit orientée droit devant, sans incliner à gauche ou à droite.

    .. image:: img/calibrate3.png

#. Appuyez sur la touche numérique ``3`` pour sélectionner le **servo d'inclinaison**, puis appuyez sur ``W/S`` pour que la plateforme soit bien droite, sans inclinaison vers le haut ou le bas.

    .. image:: img/calibrate4.png

#. Comme les câblages des moteurs peuvent être inversés lors de l'installation, vous pouvez appuyer sur ``E`` pour vérifier si la voiture avance normalement. Si ce n'est pas le cas, utilisez les touches numériques ``4`` et ``5`` pour sélectionner les moteurs gauche et droit, puis appuyez sur la touche ``Q`` pour calibrer le sens de rotation.

    .. image:: img/calibrate6.png

#. Lorsque la calibration est terminée, appuyez sur la **barre d'espace** pour sauvegarder les paramètres de calibration. Une invite vous demandera de saisir ``y`` pour confirmer, puis appuyez sur **Ctrl+C** pour quitter le programme et terminer la calibration.

    .. image:: img/calibrate5.png


Calibration du module de niveaux de gris
-------------------------------------------

En raison des conditions environnementales et de l'éclairage variables, 
les paramètres prédéfinis pour le module de niveaux de gris peuvent ne 
pas être optimaux. Vous pouvez ajuster ces paramètres via ce programme 
pour obtenir de meilleurs résultats.

#. Déroulez une bande de ruban adhésif noir d'environ 15 cm de long sur 
un sol clair. Centrez votre PiCar-X de manière à ce qu'il chevauche le 
ruban. Dans cette configuration, le capteur central du module de niveaux 
de gris doit se trouver directement au-dessus du ruban, tandis que les 
deux capteurs latéraux doivent survoler la surface plus claire.

#. Exécutez le fichier ``grayscale_calibration.py``.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/picar-x/example/calibration
        sudo python3 grayscale_calibration.py

#. Après l'exécution du code, l'interface suivante s'affichera dans le terminal.

    .. image:: img/calibrate_g1.png

#. Appuyez sur la touche "Q" pour lancer la calibration des niveaux de gris. Vous observerez alors que le PiCar-X effectue de petits mouvements vers la gauche et vers la droite. Pendant ce processus, chacun des trois capteurs doit balayer le ruban adhésif au moins une fois.

#. De plus, vous verrez apparaître trois paires de valeurs significativement différentes dans la section "valeurs seuils", tandis que la "référence de ligne" affichera deux valeurs intermédiaires, chacune représentant la moyenne d'une de ces paires.

    .. image:: img/calibrate_g2.png

#. Ensuite, soulevez le PiCar-X en l'air (ou positionnez-le au-dessus d'un rebord) et appuyez sur la touche "E". Vous verrez que les valeurs de la "référence de falaise" sont également mises à jour en conséquence.

    .. image:: img/calibrate_g3.png

#. Une fois que vous avez vérifié l'exactitude des valeurs, appuyez sur la touche "espace" pour sauvegarder les données. Vous pouvez ensuite quitter le programme en appuyant sur **Ctrl+C**.

