.. note::

    Bonjour et bienvenue dans la communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Plongez-vous dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et relevez les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprenez & Partagez** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et à des avant-premières.
    - **Remises spéciales** : Profitez de réductions exclusives sur nos nouveaux produits.
    - **Promotions festives et concours** : Participez à des tirages au sort et à des promotions durant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _setup_pi:

4. Configurer votre Raspberry Pi
==================================

Pour commencer à programmer et contrôler votre **PiCar-X**, vous devez d’abord accéder à votre Raspberry Pi.  
Cette section vous guide à travers deux méthodes courantes :  

* utiliser un **écran**, un clavier et une souris ;  
* ou configurer une **connexion sans écran (headless)** afin de vous connecter à distance depuis un autre ordinateur.

Si Vous Avez un Écran
-------------------------

.. note:: Le Raspberry Pi Zero 2W installé sur le robot n’est pas simple à connecter à un écran. Nous recommandons donc la méthode **sans écran**.

**Composants requis**

* Raspberry Pi  
* Adaptateur secteur  
* Carte Micro SD  
* Câble HDMI  
* Écran  
* Souris  
* Clavier

#. Insérez la carte microSD dans votre Raspberry Pi.  
#. Branchez la souris, le clavier et l’écran (pour Pi 4/5, utilisez **HDMI0**, le port le plus proche de l’alimentation).  
#. Allumez le Raspberry Pi.  
#. Après quelques instants, le bureau Raspberry Pi OS s’affichera et vous pourrez ouvrir un Terminal pour saisir des commandes.

    .. image:: img/bookwarm.png
        :align: center

----

Si Vous N’Avez Pas d’Écran (Mode Headless)
---------------------------------------------

Sans moniteur, vous pouvez configurer et vous connecter à votre Raspberry Pi **à distance**.  
C’est la manière la plus pratique de démarrer.

**Composants requis**

* Raspberry Pi  
* Adaptateur secteur  
* Carte Micro SD  
* Un ordinateur sur le même réseau

**Conseils**

* Configurez correctement le **pays du réseau Wi-Fi** en utilisant le code ISO/IEC alpha-2 (par ex. ``US``, ``UK``, ``CN``), sinon le Wi-Fi ne fonctionnera pas.  
* Assurez-vous que votre Raspberry Pi et votre ordinateur sont sur le même réseau local.  
* Pour une connexion plus stable, utilisez un câble Ethernet si possible.

----

**Connexion via SSH**

1. Sur votre ordinateur, ouvrez un terminal (Windows : **PowerShell**, macOS/Linux : **Terminal**) et tapez :

   .. code-block::

      ssh <nom_utilisateur>@<nom_hôte>.local
      # Exemple :
      ssh daisy@picarx.local

2. Vous pouvez également consulter la liste des clients DHCP sur votre routeur, trouver l’adresse IP de votre Pi, puis vous connecter ainsi :

   .. code-block::

      ssh <nom_utilisateur>@<IP>
      
      # Exemple :
      ssh daisy@192.xxx.xx.xx

3. Lors de la première connexion, un message de sécurité s’affichera. Tapez ``yes`` pour continuer.

4. Saisissez le mot de passe défini dans Raspberry Pi Imager. (Aucun caractère ne s’affichera pendant la saisie — c’est normal.)

   .. note::
      L’absence de caractères visibles pendant la saisie du mot de passe est une **mesure de sécurité standard**. Tapez simplement avec soin.

5. Une fois connecté, votre Raspberry Pi est prêt à être utilisé à distance.

   .. image:: img/ssh_login.png
      :align: center

----

**Dépannage**

* **ssh: Could not resolve hostname ...**  
  * Vérifiez que le nom d’hôte est correct.  
  * Si cela ne fonctionne pas, utilisez l’adresse IP du Pi à la place de ``<hostname>.local``.

* **The term 'ssh' is not recognized... (Windows)**  
  * Votre système n’a pas OpenSSH installé. Installez-le manuellement (voir :ref:`openssh_powershell`) ou utilisez un client SSH tiers (voir :ref:`login_windows`).

* **Permission denied (publickey,password)**  
  * Assurez-vous d’utiliser le bon nom d’utilisateur et mot de passe configurés dans Raspberry Pi Imager.

* **Connection refused**  
  * Patientez 1 à 2 minutes après l’allumage.  
  * Vérifiez que SSH a bien été activé dans Raspberry Pi Imager.

----

**Options d’Accès Graphique**

Si vous préférez une **interface graphique** plutôt que la ligne de commande, vous avez deux options :

    .. image:: img/bookwarm.png
        :align: center

* :ref:`remote_desktop` : Activez **VNC (Virtual Network Computing)** pour accéder à tout le bureau du Pi à distance.  
* |link_rpi_connect| : Utilisez **Raspberry Pi Connect** pour un accès sécurisé depuis n’importe où, directement dans un navigateur.

Vous pouvez maintenant **contrôler votre Raspberry Pi sans écran**, soit par SSH pour la ligne de commande, soit avec **VNC / Raspberry Pi Connect** pour une interface graphique complète.
