.. note::

    Bonjour et bienvenue dans la communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Plongez-vous dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et relevez les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprenez & Partagez** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et à des avant-premières.
    - **Remises spéciales** : Profitez de réductions exclusives sur nos derniers produits.
    - **Promotions festives et concours** : Participez à des tirages au sort et à des promotions durant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

6. Activer l'interface I2C (Important)
==========================================

Nous utiliserons l'interface I2C du Raspberry Pi. Cette interface devrait avoir été activée lors de l'installation du module ``robot-hat`` plus tôt. Pour vous assurer que tout fonctionne correctement, vérifions si elle est bien activée.

#. Entrez la commande suivante :

    .. raw:: html

        <run></run>

    .. code-block:: 

        sudo raspi-config

#. Sélectionnez **Options d'interface** en appuyant sur la flèche bas de votre clavier, puis appuyez sur la touche **Entrée**.

    .. image:: img/image282.png
        :align: center

#. Ensuite, sélectionnez **I2C**.

    .. image:: img/image283.png
        :align: center

#. Utilisez les flèches de votre clavier pour sélectionner **<Oui>** -> **<OK>** afin de finaliser la configuration de l'I2C.

    .. image:: img/image284.png
        :align: center

#. Après avoir sélectionné **<Finish>**, une fenêtre contextuelle vous rappellera que vous devez redémarrer pour que les paramètres prennent effet, sélectionnez **<Oui>**.

    .. image:: img/camera_enable2.png
        :align: center
