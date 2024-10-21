.. note::

    Bonjour et bienvenue dans la communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Plongez-vous dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et relevez les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprenez & Partagez** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et à des avant-premières.
    - **Remises spéciales** : Profitez de réductions exclusives sur nos derniers produits.
    - **Promotions festives et concours** : Participez à des tirages au sort et à des promotions durant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _ezb_servo_adjust:

Guide rapide sur EzBlock
===========================

.. note::

    Si vous utilisez un Raspberry Pi 5, notre logiciel de programmation graphique, EzBlock, n'est pas compatible.
    
La plage d'angle du servo est de -90° à 90°, mais l'angle défini en usine est aléatoire, peut-être 0°, peut-être 45°. Si nous l'assemblons directement avec un tel angle, cela entraînera un état chaotique lorsque le robot exécutera le code, voire pire, cela pourrait bloquer le servo et le brûler.

Nous devons donc régler tous les angles des servos à 0° avant de les installer, de sorte que l'angle du servo soit au milieu, quelle que soit la direction de rotation.

#. Tout d'abord, :ref:`ezblock:install_ezblock_os_latest` (les tutoriels d'EzBlock) sur une carte Micro SD, une fois l'installation terminée, insérez-la dans le Raspberry Pi.

    .. note::
        Une fois l'installation terminée, veuillez revenir à cette page.

    .. image:: img/insert_sd_card.png
        :width: 500
        :align: center

#. Pour vous assurer que le servo a été correctement réglé à 0°, insérez d'abord le bras du servo dans l'axe du servo, puis faites doucement pivoter le bras à un angle différent. Ce bras de servo vous permet de voir clairement que le servo tourne.

    .. image:: img/servo_arm.png

#. Suivez les instructions sur le dépliant de montage, insérez le câble de la batterie et mettez l'interrupteur d'alimentation sur ON. Ensuite, branchez un câble USB-C alimenté pour activer la batterie. Attendez 1 à 2 minutes, un son indiquera que le Raspberry Pi a démarré avec succès.

    .. image:: img/Z_BTR.JPG
        :width: 800
        :align: center

#. Ensuite, branchez le câble du servo dans le port P11 comme suit.

    .. image:: img/Z_P11.JPG

#. Appuyez et maintenez la touche **USR**, puis appuyez sur la touche **RST** pour exécuter le script de mise à zéro du servo dans le système. Lorsque vous voyez le bras du servo tourner à une position (c'est la position 0°, qui est une position aléatoire et peut ne pas être verticale ou parallèle), cela indique que le programme a été exécuté.

    .. note::

        Cette étape ne doit être effectuée qu'une seule fois ; par la suite, il suffit d'insérer d'autres fils de servos, et ils se mettront automatiquement à zéro.

    .. image:: img/Z_P11_BT.png
        :width: 400
        :align: center
    
#. Maintenant, retirez le bras du servo, en veillant à ce que le fil du servo reste connecté, et ne coupez pas l'alimentation. Ensuite, poursuivez le montage en suivant les instructions papier de montage.

.. note::

    * Ne débranchez pas ce câble de servo avant d'avoir fixé ce servo avec la vis du servo, vous pouvez le débrancher après fixation.
    * Ne tournez pas le servo lorsqu'il est sous tension pour éviter d'endommager le servo ; si l'axe du servo est inséré à un mauvais angle, retirez le servo et réinsérez-le.
    * Avant d'assembler chaque servo, vous devez brancher le câble du servo dans le port P11 et allumer l'alimentation pour régler son angle à 0°.
    * Cette fonction de mise à zéro sera désactivée si vous téléchargez un programme sur le robot plus tard avec l'application EzBlock.
