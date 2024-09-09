.. note::

    Bonjour et bienvenue dans la communauté des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder sur Facebook ! Plongez au cœur du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et relevez les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprenez & Partagez** : Échangez des conseils et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Obtenez un accès anticipé aux annonces de nouveaux produits et aux avant-premières.
    - **Remises spéciales** : Profitez de réductions exclusives sur nos nouveaux produits.
    - **Promotions festives et concours** : Participez à des concours et des promotions pendant les fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _control_by_app:

13. Contrôlé par l'application
==================================

Le contrôleur SunFounder est utilisé pour contrôler les robots basés sur Raspberry Pi/Pico.

L'application intègre des widgets tels que Bouton, Interrupteur, Joystick, Pavé directionnel, Curseur et Curseur de puissance ; des widgets d'entrée tels que l'affichage numérique, le radar ultrasonique, la détection de niveaux de gris et le compteur de vitesse.

Il y a 17 zones, de A à Q, où vous pouvez placer différents widgets pour personnaliser votre propre contrôleur.

De plus, cette application propose un service de streaming vidéo en direct.

Personnalisons un contrôleur PiCar-X à l'aide de cette application.

**Comment faire ?**

#. Installez le module ``sunfounder-controller``.

    Les modules ``robot-hat``, ``vilib`` et ``picar-x`` doivent être installés en premier, pour plus de détails, consultez : :ref:`install_all_modules`.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~
        git clone https://github.com/sunfounder/sunfounder-controller.git
        cd ~/sunfounder-controller
        sudo python3 setup.py install

#. Exécutez le code.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/picar-x/example
        sudo python3 13.app_control.py

#. Installez le `SunFounder Controller <https://docs.sunfounder.com/projects/sf-controller/en/latest/>`_ depuis **APP Store (iOS)** ou **Google Play (Android)**.

#. Ouvrez et créez un nouveau contrôleur.

    Créez un nouveau contrôleur en cliquant sur le signe + dans l'application SunFounder Controller.

    .. image:: img/app1.PNG

    Il existe des contrôleurs prédéfinis pour certains produits dans la section Prédéfinis, que vous pouvez utiliser selon vos besoins. Ici, nous sélectionnons **PiCar-X**.

    .. image:: img/app_control_preset.jpg

#. Connectez-vous au PiCar-X.

    Lorsque vous cliquez sur le bouton **Connecter**, il recherchera automatiquement les robots à proximité. Son nom est défini dans ``picarx_control.py`` et doit être en cours d'exécution en permanence.

    .. image:: img/app9.PNG

    Une fois que vous avez cliqué sur le nom du produit, le message "Connexion réussie" apparaîtra et le nom du produit s'affichera dans le coin supérieur droit.

    .. note::

        * Vous devez vous assurer que votre appareil mobile est connecté au même réseau LAN que PiCar-X.
        * Si la recherche ne se fait pas automatiquement, vous pouvez également entrer manuellement l'adresse IP pour vous connecter.

        .. image:: img/app11.PNG

#. Exécutez ce contrôleur.

    Cliquez sur le bouton **Exécuter** pour démarrer le contrôleur, vous verrez l'image capturée par la voiture, et vous pourrez maintenant contrôler votre PiCar-X avec ces widgets.

    .. image:: img/app12.PNG

    Voici les fonctions des widgets :

    * **A** : Affiche la vitesse actuelle de la voiture.
    * **E** : Active la fonction d'évitement d'obstacles.
    * **I** : Active la fonction de suivi de ligne.
    * **J** : Reconnaissance vocale, maintenez ce widget enfoncé pour parler, et il affichera la voix reconnue lorsque vous relâcherez. Nous avons défini les commandes ``forward``, ``backward``, ``left`` et ``right`` dans le code pour contrôler la voiture.
    * **K** : Contrôle les mouvements avant, arrière, gauche et droite de la voiture.
    * **Q** : Contrôle l'orientation de la tête (caméra) vers le haut, le bas, la gauche et la droite.
    * **N** : Active la fonction de reconnaissance des couleurs.
    * **O** : Active la fonction de reconnaissance faciale.
    * **P** : Active la fonction de reconnaissance d'objets, elle peut reconnaître près de 90 types d'objets. Pour la liste des modèles, veuillez consulter : https://github.com/sunfounder/vilib/blob/master/workspace/coco_labels.txt.
