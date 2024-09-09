.. note::

    Bonjour et bienvenue dans la communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Plongez-vous dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et relevez les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprenez & Partagez** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et à des avant-premières.
    - **Remises spéciales** : Profitez de réductions exclusives sur nos nouveaux produits.
    - **Promotions festives et concours** : Participez à des tirages au sort et à des promotions durant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

4. Configurer votre Raspberry Pi
==================================
Si vous avez un écran
---------------------------

.. note:: Le Raspberry Pi ZERO installé sur le robot n'est pas facile à connecter à un écran. Veuillez utiliser la méthode sans écran pour le configurer.


Si vous avez un écran, il sera facile d'utiliser le Raspberry Pi.

**Composants nécessaires**

* Raspberry Pi
* Adaptateur secteur
* Carte Micro SD
* Adaptateur secteur de l'écran
* Câble HDMI
* Écran
* Souris
* Clavier

#. Branchez la souris et le clavier.

#. Connectez l'écran au port HDMI du Raspberry Pi et assurez-vous que votre écran est branché à une prise murale et allumé.

    .. note::

        Si vous utilisez un Raspberry Pi 4, vous devez connecter l'écran à HDMI0 (le plus proche du port d'alimentation).

#. Utilisez l'adaptateur secteur pour alimenter le Raspberry Pi.

#. Après quelques secondes, le bureau de Raspberry Pi OS s'affichera. Vous pouvez maintenant ouvrir le Terminal pour commencer à entrer des commandes.

    .. image:: img/bookwarm.png
        :align: center

Si vous n'avez pas d'écran
-------------------------------

Si vous n'avez pas d'écran, vous pouvez vous connecter à distance à votre Raspberry Pi.

**Composants nécessaires**

* Raspberry Pi
* Adaptateur secteur
* Carte Micro SD

Vous pouvez utiliser la commande SSH pour ouvrir le shell Bash de Raspberry Pi. Bash est le shell par défaut sous Linux. Le shell est une interface qui permet aux utilisateurs de communiquer avec le système via des commandes. La plupart de vos tâches peuvent être effectuées via le shell.

Si l'utilisation de la fenêtre de commande pour accéder à votre Raspberry Pi ne vous satisfait pas, vous pouvez également utiliser la fonctionnalité de bureau à distance pour gérer facilement vos fichiers sur le Raspberry Pi avec une interface graphique.

Voir ci-dessous les tutoriels détaillés pour chaque système.


.. toctree::

    remote_macosx
    remote_windows
    remote_linux
    remote_desktop
