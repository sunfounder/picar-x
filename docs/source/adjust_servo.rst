.. note::

    Bonjour et bienvenue dans la communauté des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder sur Facebook ! Plongez dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux avant-goûts.
    - **Réductions spéciales** : Bénéficiez de réductions exclusives sur nos derniers produits.
    - **Promotions et cadeaux festifs** : Participez à des concours et des promotions festives.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

Ajuster le servo pour l'assemblage
====================================

Avant d'assembler le servo, l'angle doit être réglé à zéro. En effet, 
le moteur du servo a une plage de mouvement limitée, et en réglant 
l'angle à zéro degré, cela garantit que le servo est en position initiale 
et ne dépasse pas sa plage de mouvement lorsqu'il est alimenté. Si le servo 
n'est pas réglé à zéro degré avant l'assemblage, il pourrait tenter de dépasser 
sa plage de mouvement une fois sous tension, risquant d'endommager le servo 
ou le système mécanique auquel il est connecté. Ainsi, régler l'angle à zéro 
est une étape cruciale pour assurer un fonctionnement sûr et normal du moteur 
du servo.

.. image:: img/IMG_9897.png


Pour les utilisateurs de Python
-------------------------------------

Veuillez consulter :ref:`quick_guide_python` pour finaliser l'installation de l'OS Raspberry Pi et ajuster l'angle des servos.


Pour les utilisateurs d'Ezblock
-------------------------------------

.. note::

    Si vous utilisez un Raspberry Pi 5, notre logiciel de programmation graphique, EzBlock, n'est pas compatible.


Après avoir installé le système Ezblock, la broche P11 peut être utilisée pour 
ajuster le servo. Veuillez consulter :ref:`ezb_servo_adjust` pour plus de détails.
