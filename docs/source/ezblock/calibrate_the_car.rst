.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 sur Facebook ! Plongez dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des conseils et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et aux avant-premières.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos nouveaux produits.
    - **Promotions festives et concours** : Participez à des concours et à des promotions spéciales lors des fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

Calibration de la voiture
==============================

Après avoir connecté le PiCar-X, vous passerez par une étape de calibration. Cela est nécessaire en raison des éventuelles déviations lors de l'installation ou des limitations des servos eux-mêmes, ce qui peut entraîner une légère inclinaison des angles des servos. Vous pouvez donc les calibrer à cette étape.

Cependant, si vous pensez que l'assemblage est parfait et qu'aucune calibration n'est nécessaire, vous pouvez également ignorer cette étape.

.. note::
    Si vous souhaitez recalibrer le robot pendant son utilisation, veuillez suivre les étapes ci-dessous.
    
    #. Vous pouvez ouvrir la page de détails du produit en cliquant sur l'icône de connexion dans le coin supérieur gauche.

        .. image:: img/calibrate0.png

    #. Cliquez sur le bouton **Paramètres**.

        .. image:: img/calibrate1.png

    #. Sur cette page, vous pouvez modifier le nom du produit, le type de produit, voir la version de l'application ou calibrer le robot. Une fois que vous cliquez sur **Calibrer**, vous accéderez à la page de calibration.

        .. image:: img/calibrate2.png

Les étapes de calibration sont les suivantes :

#. Une fois sur la page de calibration, deux points de repère vous indiqueront où calibrer.

    .. note::
        La calibration est un processus de micro-ajustement. Il est recommandé de démonter et de réassembler la pièce si, après avoir cliqué plusieurs fois sur un bouton, la pièce reste décalée.

    .. image:: img/calibrate3.png

#. Cliquez sur le point de repère de gauche pour calibrer le Pan-Tilt du PiCar-X (la partie caméra). En utilisant les deux ensembles de boutons à droite, vous pouvez ajuster lentement l'orientation du Pan-Tilt, ainsi que vérifier les angles. Une fois l'ajustement terminé, cliquez sur **Confirmer**.

    .. image:: img/calibrate4.png

#. Pour calibrer l'orientation des roues avant, cliquez sur le point de repère de droite. Utilisez les deux boutons à droite pour aligner les roues avant vers l'avant. Lorsque l'ajustement est terminé, cliquez sur **Confirmer**.

    .. image:: img/calibrate5.png
