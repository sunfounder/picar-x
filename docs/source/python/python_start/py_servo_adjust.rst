.. note::

    Bonjour et bienvenue dans la communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Plongez-vous dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et relevez les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprenez & Partagez** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et à des avant-premières.
    - **Remises spéciales** : Profitez de réductions exclusives sur nos nouveaux produits.
    - **Promotions festives et concours** : Participez à des tirages au sort et à des promotions durant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

7. Réglage du Servo (Important)
===================================

La plage d'angle du servo est de -90° à 90°, mais l'angle défini en usine est aléatoire, peut-être 0°, peut-être 45°. Si nous l'assemblons directement avec un tel angle, cela entraînera un dysfonctionnement lors de l'exécution du code par le robot, voire pire, cela pourrait bloquer le servo et l'endommager.

Nous devons donc régler tous les angles des servos à 0° avant de les installer, afin que l'angle du servo soit centré, quelle que soit la direction de rotation.

#. Pour vous assurer que le servo est correctement réglé à 0°, insérez d'abord le bras du servo dans l'axe du servo, puis faites doucement pivoter le bras à un autre angle. Ce bras de servo vous permet simplement de voir clairement que le servo tourne.

    .. image:: img/servo_arm.png

#. Maintenant, exécutez ``servo_zeroing.py`` dans le dossier ``example/``.

    .. raw:: html

        <run></run>

    .. code-block::

        cd ~/picar-x/example
        sudo python3 servo_zeroing.py

#. Ensuite, branchez le câble du servo dans le port P11 comme suit. En même temps, vous verrez le bras du servo tourner jusqu'à une position (Il s'agit de la position 0°, qui est une position aléatoire et peut ne pas être verticale ou parallèle.).


    .. image:: img/Z_P11.JPG

#. Maintenant, retirez le bras du servo, en veillant à ce que le fil du servo reste connecté, et ne coupez pas l'alimentation. Ensuite, poursuivez le montage en suivant les instructions papier.

.. note::

    * Ne débranchez pas le câble du servo avant de l'avoir fixé avec la vis du servo ; vous pouvez le débrancher après fixation.
    * Ne tournez pas le servo lorsqu'il est sous tension pour éviter tout dommage ; si l'axe du servo n'est pas inséré au bon angle, retirez le servo et réinsérez-le.
    * Avant d'assembler chaque servo, vous devez brancher le câble du servo dans le port P11 et allumer l'alimentation pour régler son angle à 0°.
