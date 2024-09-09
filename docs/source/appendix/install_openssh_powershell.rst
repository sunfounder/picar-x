.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 sur Facebook ! Plongez dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et vos défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et des avant-premières.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos nouveaux produits.
    - **Promotions festives et concours** : Participez à des concours et des promotions spéciales pendant les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _openssh_powershell:

Installer OpenSSH via Powershell
===================================

Lorsque vous utilisez ``ssh <nom_utilisateur>@<nom_hôte>.local`` (ou ``ssh <nom_utilisateur>@<adresse_IP>``) pour vous connecter à votre Raspberry Pi, mais que le message d'erreur suivant apparaît :

    .. code-block::

        ssh : Le terme 'ssh' n'est pas reconnu comme le nom d'une cmdlet, fonction, fichier de script ou programme exécutable. Vérifiez l'orthographe du nom, ou si un chemin a été inclus, assurez-vous que le chemin est correct et réessayez.

Cela signifie que votre système est trop ancien et ne dispose pas de `OpenSSH <https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=gui>`_ pré-installé. Vous devez suivre le tutoriel ci-dessous pour l'installer manuellement.

#. Tapez ``powershell`` dans la barre de recherche de votre bureau Windows, faites un clic droit sur ``Windows PowerShell``, puis sélectionnez ``Exécuter en tant qu'administrateur`` dans le menu qui apparaît.

    .. image:: img/powershell_ssh.png
        :align: center

#. Utilisez la commande suivante pour installer ``OpenSSH.Client``.

    .. code-block::

        Add-WindowsCapability -Online -Name OpenSSH.Client~~~~0.0.1.0

#. Après l'installation, la sortie suivante sera affichée.

    .. code-block::

        Path          :
        Online        : True
        RestartNeeded : False

#. Vérifiez l'installation avec la commande suivante.

    .. code-block::

        Get-WindowsCapability -Online | Where-Object Name -like 'OpenSSH*'

#. Vous verrez maintenant que ``OpenSSH.Client`` a bien été installé.

    .. code-block::

        Name  : OpenSSH.Client~~~~0.0.1.0
        State : Installed

        Name  : OpenSSH.Server~~~~0.0.1.0
        State : NotPresent

    .. warning:: 
        Si l'invite ci-dessus n'apparaît pas, cela signifie que votre système Windows est encore trop ancien. Il est recommandé d'installer un outil SSH tiers, tel que :ref:`login_windows`.

#. Redémarrez maintenant PowerShell et exécutez-le à nouveau en tant qu'administrateur. À ce stade, vous pourrez vous connecter à votre Raspberry Pi en utilisant la commande ``ssh``, où il vous sera demandé d'entrer le mot de passe que vous avez configuré précédemment.

    .. image:: img/powershell_login.png
