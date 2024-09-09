.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 sur Facebook ! Plongez dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et vos défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et des avant-premières.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos nouveaux produits.
    - **Promotions festives et concours** : Participez à des concours et des promotions spéciales pendant les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _login_windows:

PuTTY
=========================

Si vous êtes un utilisateur de Windows, vous pouvez utiliser certaines applications SSH. Nous vous recommandons ici `PuTTY <https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html>`_.

**Étape 1**

Téléchargez PuTTY.

**Étape 2**

Ouvrez PuTTY et cliquez sur **Session** dans la structure en arborescence à gauche. Entrez
l'adresse IP du Raspberry Pi dans la case sous **Host Name (ou adresse IP)** et **22** sous **Port** (par défaut, c'est 22).

.. image:: img/image25.png
    :align: center

**Étape 3**

Cliquez sur **Open**. Notez que lors de votre première connexion au Raspberry Pi avec
l'adresse IP, une alerte de sécurité s'affichera. Cliquez simplement sur **Yes**.

**Étape 4**

Lorsque la fenêtre PuTTY affiche \"**login as:**\", tapez \"**pi**\" (le nom 
d'utilisateur du Raspberry Pi), et **mot de passe** : \"raspberry\"
(par défaut, si vous ne l'avez pas changé).

.. note::

    Lorsque vous saisissez le mot de passe, les caractères ne s'affichent pas dans la fenêtre, ce qui est normal. Vous devez simplement entrer le mot de passe correct.
    
    Si « inactif » apparaît à côté de PuTTY, cela signifie que la connexion a été rompue et doit être rétablie.
    
.. image:: img/image26.png
    :align: center

**Étape 5**


Nous avons maintenant connecté le Raspberry Pi, et il est temps de passer aux étapes suivantes.
