.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

.. _remote_desktop:

Accès à Distance au Bureau pour Raspberry Pi
==================================================

Pour ceux qui préfèrent une interface graphique (GUI) plutôt que l’accès en ligne de commande, le Raspberry Pi prend en charge l’accès à distance via le **bureau à distance VNC**.  
Ce guide vous montre comment configurer et utiliser **VNC (Virtual Network Computing)** pour contrôler votre Raspberry Pi depuis un autre ordinateur.

Nous recommandons d’utiliser `VNC® Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ pour cette tâche.

**Activer le Service VNC sur le Raspberry Pi**

Le service VNC est préinstallé dans Raspberry Pi OS, mais désactivé par défaut.  
Suivez ces étapes pour l’activer :

#. Saisissez la commande suivante dans le terminal de votre Raspberry Pi :

    .. raw:: html

        <run></run>

    .. code-block:: 

        sudo raspi-config

#. Naviguez jusqu’à **Interfacing Options** à l’aide de la flèche bas, puis appuyez sur **Entrée**.

    .. image:: img/config_interface.png
        :align: center

#. Sélectionnez **VNC** dans la liste des options.

    .. image:: img/vnc.png
        :align: center

#. Utilisez les flèches pour choisir **<Yes>** → **<OK>** → **<Finish>** afin d’activer définitivement le service VNC.

    .. image:: img/vnc_yes.png
        :align: center

----

**Se Connecter via VNC Viewer**

#. Téléchargez et installez `VNC Viewer <https://www.realvnc.com/en/connect/download/viewer/>`_ sur votre ordinateur personnel.

#. Une fois installé, lancez **VNC Viewer**. Entrez le nom d’hôte ou l’adresse IP de votre Raspberry Pi, puis appuyez sur **Entrée**.

    .. image:: img/vnc_viewer1.png
        :align: center

#. Lorsqu’on vous le demande, saisissez le **nom d’utilisateur** et le **mot de passe** de votre Raspberry Pi, puis cliquez sur **OK**.

    .. image:: img/vnc_viewer2.png
        :align: center

#. Après quelques secondes, le bureau Raspberry Pi OS s’affiche à distance. Vous pouvez maintenant ouvrir le terminal et exécuter des commandes comme si vous étiez devant le Pi.

    .. image:: img/bookwarm.png
        :align: center
