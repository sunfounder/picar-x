.. note::

    Bonjour et bienvenue dans la communauté des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder sur Facebook ! Plongez au cœur du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et relevez les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprenez & Partagez** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux avant-goûts.
    - **Réductions exclusives** : Profitez de remises spéciales sur nos nouveaux produits.
    - **Promotions et concours festifs** : Participez à des concours et à des promotions lors des fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _install_all_modules:


Installer tous les modules (Important)
=========================================

#. **Préparer le système**

   Assurez-vous que votre Raspberry Pi est connecté à Internet, puis mettez le système à jour :

   .. raw:: html

      <run></run>

   .. code-block::

      sudo apt update
      sudo apt upgrade

   .. note::
      Si vous utilisez Raspberry Pi OS Lite, installez d’abord les paquets Python 3 requis :

   .. raw:: html

      <run></run>

   .. code-block::

         sudo apt install git python3-pip python3-setuptools python3-smbus

#. **Installer robot-hat**

   Téléchargez et installez le module ``robot-hat`` :

   .. raw:: html

      <run></run>

   .. code-block::

      cd ~/
      git clone -b 2.5.x https://github.com/sunfounder/robot-hat.git --depth 1
      cd robot-hat
      sudo python3 install.py

#. **Installer vilib**

   Téléchargez et installez le module ``vilib`` :

   .. raw:: html

      <run></run>

   .. code-block::

      cd ~/
      git clone https://github.com/sunfounder/vilib.git --depth 1
      cd vilib
      sudo python3 install.py

#. **Installer picar-x**

   Téléchargez et installez le module ``picar-x`` :

   .. raw:: html

      <run></run>

   .. code-block::

      cd ~/
      git clone -b 2.1.x https://github.com/sunfounder/picar-x.git --depth 1
      cd picar-x
      sudo pip3 install . --break

   Cette étape peut prendre un certain temps. Veuillez être patient.

#. **Activer le son (amplificateur I2S)**

   Pour activer la sortie audio, exécutez le script ``i2samp.sh`` afin d’installer les composants nécessaires de l’amplificateur I2S :

   .. raw:: html

      <run></run>

   .. code-block::   

      cd ~/robot-hat
      sudo bash i2samp.sh

   Suivez les instructions affichées à l’écran en tapant ``y`` puis en appuyant sur Entrée pour continuer, exécutez ``/dev/zero`` en arrière-plan et redémarrez le Picar-X.

   .. note::

      S’il n’y a toujours pas de son après le redémarrage, essayez d’exécuter le script ``i2samp.sh`` plusieurs fois.
