.. note::

    Bonjour et bienvenue dans la communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Plongez-vous dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et relevez les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprenez & Partagez** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et à des avant-premières.
    - **Remises spéciales** : Profitez de réductions exclusives sur nos nouveaux produits.
    - **Promotions festives et concours** : Participez à des tirages au sort et à des promotions durant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _install_os_sd:

2. Installation de l'OS
============================================================


**Composants requis**

* Un ordinateur personnel
* Une carte Micro SD et un lecteur

1. Installer Raspberry Pi Imager
----------------------------------------

#. Rendez-vous sur la page de téléchargement du logiciel Raspberry Pi à `Raspberry Pi Imager <https://www.raspberrypi.org/software/>`_. Choisissez la version d'Imager compatible avec votre système d'exploitation. Téléchargez et ouvrez le fichier pour lancer l'installation.

    .. image:: img/os_install_imager.png
        :align: center

#. Une invite de sécurité peut apparaître lors de l'installation, selon votre système d'exploitation. Par exemple, Windows peut afficher un message d'avertissement. Dans ce cas, sélectionnez **Plus d'infos** puis **Exécuter quand même**. Suivez les instructions à l'écran pour terminer l'installation du Raspberry Pi Imager.

    .. image:: img/os_info.png
        :align: center

#. Lancez l'application Raspberry Pi Imager en cliquant sur son icône ou en tapant ``rpi-imager`` dans votre terminal.

    .. image:: img/os_open_imager.png
        :align: center

2. Installer l'OS sur la carte Micro SD
---------------------------------------------

#. Insérez votre carte SD dans votre ordinateur ou portable à l'aide d'un lecteur.

#. Dans l'Imager, cliquez sur **Raspberry Pi Device** et sélectionnez le modèle de Raspberry Pi dans la liste déroulante.

    .. image:: img/os_choose_device.png
        :align: center

#. Sélectionnez **Système d'exploitation** et optez pour la version recommandée de l'OS.

    .. image:: img/os_choose_os.png
        :align: center

#. Cliquez sur **Choisir le stockage** et sélectionnez le périphérique de stockage approprié pour l'installation.

    .. note::

        Assurez-vous de sélectionner le bon périphérique de stockage. Pour éviter toute confusion, déconnectez les autres périphériques de stockage si plusieurs sont connectés.

    .. image:: img/os_choose_sd.png
        :align: center

#. Cliquez sur **NEXT** puis sur **MODIFIER LES PARAMÈTRES** pour personnaliser les paramètres de votre OS.

    .. note::

        Si vous avez un écran pour votre Raspberry Pi, vous pouvez ignorer les étapes suivantes et cliquer sur 'Oui' pour commencer l'installation. Vous pourrez ajuster les autres paramètres plus tard sur l'écran.

    .. image:: img/os_enter_setting.png
        :align: center

#. Définissez un **nom d'hôte** pour votre Raspberry Pi.

    .. note::

        Le nom d'hôte est l'identifiant réseau de votre Raspberry Pi. Vous pouvez accéder à votre Pi en utilisant ``<hostname>.local`` ou ``<hostname>.lan``.

    .. image:: img/os_set_hostname.png
        :align: center

#. Créez un **Nom d'utilisateur** et un **Mot de passe** pour le compte administrateur du Raspberry Pi.

    .. note::

        Il est essentiel de définir un nom d'utilisateur et un mot de passe uniques pour sécuriser votre Raspberry Pi, qui n'a pas de mot de passe par défaut.

    .. image:: img/os_set_username.png
        :align: center

#. Configurez le réseau LAN sans fil en fournissant le **SSID** et le **Mot de passe** de votre réseau.

    .. note::

        Réglez le ``pays du réseau sans fil`` sur le code à deux lettres `ISO/IEC alpha2 <https://fr.wikipedia.org/wiki/ISO_3166-1_alpha-2#Table_de_codage>`_ correspondant à votre localisation.

    .. image:: img/os_set_wifi.png
        :align: center


#. Pour vous connecter à distance à votre Raspberry Pi, activez SSH dans l'onglet Services.

    * Pour l'**authentification par mot de passe**, utilisez le nom d'utilisateur et le mot de passe de l'onglet Général.
    * Pour l'authentification par clé publique, choisissez "Autoriser uniquement l'authentification par clé publique". Si vous avez une clé RSA, elle sera utilisée. Sinon, cliquez sur "Exécuter SSH-keygen" pour générer une nouvelle paire de clés.

    .. image:: img/os_enable_ssh.png
        :align: center

#. Le menu **Options** vous permet de configurer le comportement de l'Imager pendant l'écriture, y compris jouer un son à la fin, éjecter le média à la fin et activer la télémétrie.

    .. image:: img/os_options.png
        :align: center

    
#. Lorsque vous avez terminé de saisir les paramètres de personnalisation de l'OS, cliquez sur **Enregistrer** pour sauvegarder vos personnalisations. Ensuite, cliquez sur **Oui** pour les appliquer lors de l'écriture de l'image.

    .. image:: img/os_click_yes.png
        :align: center

#. Si la carte SD contient des données existantes, assurez-vous de les sauvegarder pour éviter toute perte de données. Cliquez sur **Oui** si aucune sauvegarde n'est nécessaire.

    .. image:: img/os_continue.png
        :align: center

#. Lorsque vous voyez la fenêtre contextuelle "Écriture réussie", cela signifie que votre image a été complètement écrite et vérifiée. Vous êtes maintenant prêt à démarrer un Raspberry Pi à partir de la carte Micro SD !

    .. image:: img/os_finish.png
        :align: center

#. Vous pouvez maintenant insérer la carte SD configurée avec Raspberry Pi OS dans l'emplacement microSD situé sous le Raspberry Pi.

    .. image:: img/os_sd_to_pi.jpg
        :width: 500
        :align: center
