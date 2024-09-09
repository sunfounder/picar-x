.. note::

    Bonjour et bienvenue dans la communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Plongez-vous dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et relevez les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprenez & Partagez** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et à des avant-premières.
    - **Remises spéciales** : Profitez de réductions exclusives sur nos nouveaux produits.
    - **Promotions festives et concours** : Participez à des tirages au sort et à des promotions durant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

3. Alimentation pour le Raspberry Pi (Important)
=====================================================

Chargement
-------------------

Insérez le câble de la batterie. Ensuite, insérez le câble USB-C pour charger la batterie.
Vous devrez fournir votre propre chargeur ; nous recommandons un chargeur 5V 3A, ou un chargeur de smartphone courant fera l'affaire.

.. image:: img/BTR_IMG_1096.png

.. note::
    Connectez une source d'alimentation externe Type-C au port Type-C sur le robot hat ; la batterie commencera immédiatement à se charger, et un indicateur rouge s'allumera.\
    Lorsque la batterie est complètement chargée, la lumière rouge s'éteindra automatiquement.


Mise sous tension
----------------------

Allumez l'interrupteur. Le voyant d'alimentation et l'indicateur de niveau de batterie s'allumeront.

.. image:: img/BTR_IMG_1097.png


Attendez quelques secondes, et vous entendrez un léger bip, indiquant que le Raspberry Pi a démarré avec succès.

.. note::
    Si les deux voyants de niveau de batterie sont éteints, veuillez charger la batterie.
    Si vous avez besoin de programmer ou de déboguer pendant de longues sessions, vous pouvez maintenir le Raspberry Pi en marche en insérant le câble USB-C pour charger la batterie simultanément.

Batterie 18650
-----------------------------------

.. image:: img/3pin_battery.jpg

* VCC : Borne positive de la batterie, ici il y a deux ensembles de VCC et GND pour augmenter le courant et réduire la résistance.
* Milieu : Pour équilibrer la tension entre les deux cellules et ainsi protéger la batterie.
* GND : Borne négative de la batterie.

Ceci est un pack de batteries personnalisé fabriqué par SunFounder, composé de deux batteries 18650 d'une capacité de 2000mAh. Le connecteur est XH2.54 3P, qui peut être chargé directement après avoir été inséré dans le shield.

**Caractéristiques**

* Charge de la batterie : 5V/2A
* Sortie de la batterie : 5V/5A
* Capacité de la batterie : 3,7V 2000mAh x 2
* Autonomie de la batterie : 90 min
* Temps de charge de la batterie : 130 min
* Connecteur : XH2.54 3P
