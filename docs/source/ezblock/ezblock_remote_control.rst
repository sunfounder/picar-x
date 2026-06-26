.. note::

    Bonjour et bienvenue dans la communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Plongez-vous dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et relevez les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprenez & Partagez** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et à des avant-premières.
    - **Remises spéciales** : Profitez de réductions exclusives sur nos derniers produits.
    - **Promotions festives et concours** : Participez à des tirages au sort et à des promotions durant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _ezb_remote_control:

Télécommande
=======================

Ce projet vous apprendra à contrôler à distance le PiCar-X avec le widget Joystick.
Remarque : Après avoir glissé-déposé le widget Joystick depuis la page Télécommande, utilisez la fonction "Map" pour calibrer les lectures des axes X et Y du joystick. Pour plus d'informations sur la fonction Télécommande, veuillez consulter le lien suivant :


* :ref:`ezblock:remote_control_latest`


.. image:: img/remote_control23.png

**CONSEILS**

.. image:: img/sp210512_114004.png

Pour utiliser la fonction de télécommande, ouvrez la page Télécommande depuis le côté gauche de la page principale.

.. image:: img/sp210512_114042.png

Glissez un Joystick vers la zone centrale de la page Télécommande. En basculant le point blanc au centre et en le faisant glisser doucement dans n'importe quelle direction, vous obtiendrez une coordonnée (X,Y). La plage des axes X et Y est par défaut réglée de “-100” à “100”. En basculant le point blanc et en le faisant glisser complètement à gauche du joystick, vous obtiendrez une valeur de X égale à “-100” et une valeur de Y égale à “0”.

.. image:: img/sp210512_114136.png

Après avoir glissé-déposé un widget sur la page Télécommande, une nouvelle catégorie - Remote - apparaîtra avec le bloc ci-dessus.
Ce bloc lit la valeur du joystick sur la page Télécommande. Vous pouvez utiliser le menu déroulant pour passer à la lecture de l'axe Y.

.. image:: img/sp210512_114235.png

Le bloc de valeur de mappage permet de remapper un nombre d'une plage à une autre. Si la plage est réglée de 0 à 100 et que la valeur de mappage est de 50, alors elle est à 50 % de la plage, soit “50”. Si la plage est réglée de 0 à 255 et que la valeur de mappage est de 50, alors elle est à 50 % de la plage, soit “127,5”.

**EXEMPLE**

.. note::

    * Vous pouvez écrire le programme en suivant l'image ci-dessous, veuillez consulter le tutoriel : :ref:`ezblock:create_project_latest`.
    * Ou trouvez le code portant le même nom sur la page **Exemples** d'EzBlock Studio, puis cliquez sur **Exécuter** ou **Modifier** directement.

.. image:: img/sp210512_114416.png
