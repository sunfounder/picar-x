.. note::

    Bonjour et bienvenue dans la communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Plongez-vous dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et relevez les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprenez & Partagez** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et à des avant-premières.
    - **Remises spéciales** : Profitez de réductions exclusives sur nos nouveaux produits.
    - **Promotions festives et concours** : Participez à des tirages au sort et à des promotions durant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _remote_desktop:

Accès au bureau à distance pour Raspberry Pi
==================================================

Pour ceux qui préfèrent une interface graphique (GUI) à l'accès en ligne de commande, le Raspberry Pi prend en charge la fonctionnalité de bureau à distance. Ce guide vous expliquera comment configurer et utiliser VNC (Virtual Network Computing) pour accéder à distance à votre Raspberry Pi.

Nous recommandons d'utiliser `VNC® Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ pour cette tâche.

**Activation du service VNC sur le Raspberry Pi**

Le service VNC est pré-installé dans le système d'exploitation Raspberry Pi OS mais est désactivé par défaut. Suivez ces étapes pour l'activer :

#. Saisissez la commande suivante dans le terminal du Raspberry Pi :

    .. raw:: html

        <run></run>

    .. code-block:: 

        sudo raspi-config

#. Naviguez jusqu'à **Options d'interface** à l'aide de la touche fléchée vers le bas, puis appuyez sur **Entrée**.

    .. image:: img/config_interface.png
        :align: center

#. Sélectionnez **VNC** dans les options.

    .. image:: img/vnc.png
        :align: center

#. Utilisez les touches fléchées pour choisir **<Yes>** -> **<OK>** -> **<Finish>** et finalisez l'activation du service VNC.

    .. image:: img/vnc_yes.png
        :align: center

**Connexion via VNC Viewer**

#. Téléchargez et installez `VNC Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ sur votre ordinateur personnel.

#. Une fois installé, lancez VNC Viewer. Saisissez le nom d'hôte ou l'adresse IP de votre Raspberry Pi et appuyez sur Entrée.

    .. image:: img/vnc_viewer1.png
        :align: center

#. Lorsque vous y êtes invité, entrez le nom d'utilisateur et le mot de passe de votre Raspberry Pi, puis cliquez sur **OK**.

    .. image:: img/vnc_viewer2.png
        :align: center

#. Après quelques secondes, le bureau de Raspberry Pi OS s'affichera. Vous pouvez maintenant ouvrir le terminal pour commencer à saisir des commandes.

    .. image:: img/bookwarm.png
        :align: center

