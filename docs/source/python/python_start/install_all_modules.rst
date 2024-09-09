.. note::

    Bonjour et bienvenue dans la communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Plongez-vous dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et relevez les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprenez & Partagez** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et à des avant-premières.
    - **Remises spéciales** : Profitez de réductions exclusives sur nos nouveaux produits.
    - **Promotions festives et concours** : Participez à des tirages au sort et à des promotions durant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _install_all_modules:


5. Installer tous les modules (Important)
=============================================

Assurez-vous d'être connecté à Internet et mettez à jour votre système :

.. raw:: html

    <run></run>

.. code-block::

    sudo apt update
    sudo apt upgrade

.. note::

    Les paquets liés à Python3 doivent être installés si vous utilisez la version Lite de l'OS.

    .. raw:: html

        <run></run>

    .. code-block::
    
        sudo apt install git python3-pip python3-setuptools python3-smbus


Installez ``robot-hat``.

.. raw:: html

    <run></run>

.. code-block::

    cd ~/
    git clone -b v2.0 https://github.com/sunfounder/robot-hat.git
    cd robot-hat
    sudo python3 setup.py install


Ensuite, téléchargez et installez le module ``vilib``.

.. raw:: html

    <run></run>

.. code-block::

    cd ~/
    git clone -b picamera2 https://github.com/sunfounder/vilib.git
    cd vilib
    sudo python3 install.py

Téléchargez et installez le module ``picar-x``.

.. raw:: html

    <run></run>

.. code-block::

    cd ~/
    git clone -b v2.0 https://github.com/sunfounder/picar-x.git
    cd picar-x
    sudo python3 setup.py install

Cette étape prendra un certain temps, soyez patient.

Enfin, vous devez exécuter le script ``i2samp.sh`` pour installer les composants requis par l'amplificateur i2s, sinon le Picar-X n'aura pas de son.

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x
    sudo bash i2samp.sh
	
.. image:: img/i2s.png

Tapez ``y`` et appuyez sur Entrée pour continuer à exécuter le script.

.. image:: img/i2s2.png

Tapez ``y`` et appuyez sur Entrée pour exécuter ``/dev/zero`` en arrière-plan.

.. image:: img/i2s3.png

Tapez ``y`` et appuyez sur Entrée pour redémarrer le Picar-X.

.. note::
    S'il n'y a pas de son après le redémarrage, vous devrez peut-être exécuter le script i2samp.sh plusieurs fois.
