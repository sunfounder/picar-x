.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 sur Facebook ! Plongez au cœur de l'univers Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour développer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux aperçus exclusifs.
    - **Réductions exclusives** : Profitez de remises exclusives sur nos derniers produits.
    - **Promotions festives et concours** : Participez à des concours et promotions spéciales lors des fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _filezilla:

Logiciel Filezilla
==========================

.. image:: img/filezilla_icon.png

Le File Transfer Protocol (FTP) est un protocole de communication standard utilisé pour transférer des fichiers informatiques d'un serveur à un client sur un réseau.

Filezilla est un logiciel open source qui prend en charge non seulement FTP, mais aussi FTP sur TLS (FTPS) et SFTP. Nous pouvons utiliser Filezilla pour télécharger des fichiers locaux (comme des images, de l'audio, etc.) vers le Raspberry Pi, ou pour télécharger des fichiers depuis le Raspberry Pi vers un ordinateur local.

**Étape 1** : Télécharger Filezilla.

Téléchargez le client depuis le  `Filezilla’s official website <https://filezilla-project.org/>`_, Filezilla propose également un excellent tutoriel, veuillez vous référer à : `Documentation - Filezilla <https://wiki.filezilla-project.org/Documentation>`_.

**Étape 2** : Connectez-vous à Raspberry Pi.

Après une installation rapide, ouvrez Filezilla et  `connect it to an FTP server <https://wiki.filezilla-project.org/Using#Connecting_to_an_FTP_server>`_. Il y a 3 façons de se connecter, ici nous utilisons la barre de **Connexion rapide**. Entrez le **nom d'hôte/IP**, **nom d'utilisateur**, **mot de passe** et **port (22)**, puis cliquez sur **Connexion rapide** ou appuyez sur **Entrée** pour vous connecter au serveur.

.. image:: img/filezilla_connect.png

.. note::

    La Connexion rapide est un bon moyen de tester vos informations de connexion. Si vous souhaitez créer une entrée permanente, vous pouvez sélectionner **Fichier** -> **Copier la connexion actuelle dans le gestionnaire de sites** après une Connexion rapide réussie, entrez le nom et cliquez sur **OK**. La prochaine fois, vous pourrez vous connecter en sélectionnant le site enregistré dans **Fichier** -> **Gestionnaire de sites**.

    .. image:: img/ftp_site.png

**Étape 3** : Télécharger ou téléverser des fichiers.

Vous pouvez téléverser des fichiers locaux sur le Raspberry Pi en les faisant glisser et en les déposant, ou télécharger des fichiers du Raspberry Pi vers votre ordinateur.

.. image:: img/upload_ftp.png
