.. _picarx_skill:

.. start_using_picarx

22. Utiliser OpenClaw pour contrôler le PiCar-X
=================================================


**Qu'est-ce qu'OpenClaw ?**

Considérez-le comme une version améliorée de ChatGPT. Alors que les chatbots traditionnels ne peuvent que parler (générer du texte), OpenClaw peut agir. Il comprend vos instructions en langage naturel et peut effectuer des opérations sur votre ordinateur, comme exécuter des commandes, gérer des fichiers et appeler divers outils.

Voici quelques scénarios d'application fantastiques :

* **Assistant personnel polyvalent :** Laissez-le vous aider à gérer votre emploi du temps, définir des rappels et suivre vos tâches. Il vous suffit de le lui dire dans une application de messagerie (comme Telegram, WhatsApp), et il s'en souviendra et exécutera.
* **« Colle » d'automatisation :** Il peut servir de liant pour vos différents services. Par exemple, vous pouvez lui demander de surveiller un site web pour détecter les changements de prix. Dès qu'une baisse de prix est détectée, il peut automatiquement déclencher un workflow d'automatisation n8n pour vous envoyer une notification par e-mail.
* **Assistant de développement dédié :** Demandez-lui de vous aider à gérer des serveurs, exécuter des scripts et vérifier les logs. Vous pouvez simplement dire : « Vérifie la charge du système pour moi », et il peut se connecter en SSH à votre serveur, exécuter la commande et renvoyer les résultats.
* **Compagnon matériel :** C'est un cas d'utilisation très intéressant. Vous pouvez demander à OpenClaw de contrôler du matériel connecté à un Raspberry Pi. Par exemple, un développeur l'a utilisé pour contrôler un aspirateur robotique avec un bras mécanique, ou même pour analyser les données d'un simulateur de course et les afficher sur un écran LED. L'équipe officielle de Raspberry Pi l'a même utilisé pour construire un photomaton automatique pour un mariage, simplement par conversation, sans écrire une seule ligne de code !


.. important::

   Le Raspberry Pi Zero 2W ne dispose que de 512 Mo de RAM, alors qu'OpenClaw nécessite un minimum de 1 Go. Il ne peut donc pas fonctionner correctement. Un Raspberry Pi 4/5 ou supérieur est recommandé.

Démarrage rapide d'OpenClaw
-------------------------------

Si vous souhaitez découvrir la puissance d'OpenClaw le plus rapidement possible, utilisez cette méthode. Elle installera et lancera automatiquement un assistant de configuration interactif.

1.  Ouvrez le terminal de votre Raspberry Pi et exécutez directement la commande suivante. Cette commande télécharge le script d'installation depuis le site officiel et l'exécute :

    .. code-block:: bash

       curl -fsSL https://openclaw.ai/install.sh | bash

    .. note:: Comme les nouvelles versions sont mises à jour rapidement, il est normal que vos étapes d'installation diffèrent légèrement.

2.  Le script téléchargera et installera automatiquement OpenClaw.

    .. image:: /img/openclaw/install_open_claw.png


3.  Vous verrez ensuite une invite de sécurité vous demandant si vous faites confiance à OpenClaw. Une fois que vous êtes sûr qu'il est sûr et fiable, utilisez les touches fléchées pour naviguer vers « Yes » et appuyez sur Entrée.

    .. image:: /img/openclaw/security_open_claw.png


4.  Sélectionnez Quick Start, puis appuyez sur Entrée.

    .. image:: /img/openclaw/quickstart_open_claw.png

5.  Sélectionnez votre modèle, puis appuyez sur Entrée. Nous utilisons OpenAI comme exemple ici.

    .. image:: /img/openclaw/model_provider_open_claw.png

6.  Sélectionnez OpenAI API Key.

    .. image:: /img/openclaw/api_key_open_claw.png

7.  Collez la clé API maintenant.

    .. image:: /img/openclaw/paste_api_key_open_claw.png

8.  Allez sur |link_openai_platform| et connectez-vous. Sur la page **API keys**, cliquez sur **Create new secret key**.

    .. image:: /img/openclaw/llm_openai_create.png

9.  Remplissez les détails (Owner, Name, Project et permissions si nécessaire), puis cliquez sur **Create secret key**.

    .. image:: /img/openclaw/llm_openai_create_confirm.png

10. Une fois la clé créée, copiez-la immédiatement — vous ne pourrez plus la revoir. Si vous la perdez, vous devrez en générer une nouvelle.

    .. image:: /img/openclaw/llm_openai_copy.png

11. Collez la clé dans la configuration d'OpenClaw.

    .. image:: /img/openclaw/paste_api_key_enter_open_claw.png

12. Sélectionnez le modèle que vous souhaitez utiliser. Dans cet exemple, nous allons utiliser **Keep current**.

    .. image:: /img/openclaw/model_config_open_claw.png

13. Ensuite vient la sélection du canal. Les canaux font référence aux services de communication pris en charge par OpenClaw, tels que Telegram, WhatsApp, Discord, etc. Utilisez la flèche vers le bas pour sélectionner l'option « Skip for now », puis appuyez sur Entrée.

    .. image:: /img/openclaw/channel_open_claw.png

14. Ensuite, vous serez invité à configurer les compétences immédiatement. Sélectionnez « Yes » et appuyez sur Entrée.

    .. image:: /img/openclaw/config_skill_open_claw.png

15. Installez les compétences dont vous avez besoin. Dans l'exemple suivant, nous sélectionnons l'option « Skip for now » (appuyez sur la barre d'espace pour sélectionner), puis appuyez sur Entrée.

    .. image:: /img/openclaw/install_skill_open_claw.png

16. Ensuite viennent les Hooks ; nous allons cocher « command-logger » et « session-memory ».

    .. image:: /img/openclaw/hooks2_open_claw.png


17. L'installation est maintenant terminée. Vous pouvez démarrer OpenClaw en sélectionnant « Hatch in TUI » et en appuyant sur Entrée.

   .. image:: /img/openclaw/hatch_open_claw.png


.. note::

   Vous pouvez démarrer OpenClaw en entrant la commande suivante :

    .. code-block:: bash

       openclaw tui

   Et vous pouvez appuyer deux fois sur ctrl+c pour quitter l'interface TUI.

------------------------------------------------------------------------

Faire fonctionner le PiCar-X avec OpenClaw
----------------------------------------------

**Qu'est-ce que la compétence PiCar-X ?**

La compétence PiCar-X est une extension pour OpenClaw qui vous permet de contrôler votre voiture robot SunFounder PiCar-X en langage naturel. Au lieu d'écrire des scripts Python ou de mémoriser des angles de servo, vous pouvez simplement dire à OpenClaw ce que vous voulez que le PiCar-X fasse — comme « avance », « vérifie ce qu'il y a devant » ou « tourne à gauche » — et OpenClaw exécutera automatiquement le code Python approprié.

Voici quelques choses que vous pouvez faire avec la compétence PiCar-X :

* **Conduite :** Avancer, reculer, tourner à gauche/droite avec le contrôle du servo de direction
* **Caméra orientable :** Panoramique gauche/droite, inclinaison haut/bas via la caméra 2 axes
* **Capteurs :** Lire la distance ultrasonique, les données du capteur de niveaux de gris pour le suivi de ligne et la détection de falaise
* **Son :** Jouer des effets sonores et de la musique via le haut-parleur de la voiture
* **Vision par caméra :** Prendre des photos, détecter des visages, suivre des couleurs, reconnaître des QR codes, des gestes et des panneaux de signalisation

----------------------------------------------------------------

Prérequis
------------------------------

Avant de pouvoir utiliser la compétence PiCar-X avec OpenClaw, assurez-vous d'avoir :

1. **PiCar-X** correctement assemblé et connecté à votre Raspberry Pi
2. **OpenClaw** installé et en cours d'exécution
3. Les bibliothèques Python suivantes installées :

   - ``picarx``
   - ``robot_hat``
   - ``vilib``

Vous pouvez vérifier l'installation en exécutant :

.. code-block:: bash

   python3 -c "import picarx"

Si cette commande s'exécute sans erreur, vous êtes prêt à continuer.

----------------------------------------------------------------

Installer la compétence PiCar-X
---------------------------------

Suivez ces étapes pour installer la compétence PiCar-X pour OpenClaw :

1. **Copiez les fichiers de la compétence PiCar-X** dans le répertoire des compétences d'OpenClaw :

   .. code-block:: bash

      cp -r ~/picar-x/picarx-control ~/.openclaw/workspace/skills/

2. **Vérifiez l'installation** en consultant les fichiers de la compétence :

   .. code-block:: bash

      ls ~/.openclaw/workspace/skills/picarx-control/

   Vous devriez voir ``SKILL.md``, ``install.sh``, ``scripts/`` et ``references/`` dans la sortie.

Le fichier ``SKILL.md`` de la compétence contient toutes les instructions dont OpenClaw a besoin — règles de sécurité, modèles de code pour chaque capacité et une correspondance entre les demandes en langage naturel et le code Python. OpenClaw lit ce fichier et l'utilise pour décider quel code exécuter sur votre PiCar-X.

----------------------------------------------------------------

Tester la compétence PiCar-X depuis la CLI
----------------------------------------------

Avant d'utiliser la compétence avec OpenClaw, vous pouvez tester les fonctionnalités de base directement depuis le terminal en utilisant l'outil CLI inclus.

**Vérifier la distance ultrasonique :**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/picarx-control/scripts/pc.py sensor distance

**Avancer :**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/picarx-control/scripts/pc.py move forward --speed 60

**Reculer :**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/picarx-control/scripts/pc.py move backward --speed 60

**Tourner à gauche :**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/picarx-control/scripts/pc.py turn left --angle 30

**Tourner à droite :**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/picarx-control/scripts/pc.py turn right --angle 30

**Régler l'angle de panoramique de la caméra :**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/picarx-control/scripts/pc.py cam pan --angle 30

**Régler l'angle d'inclinaison de la caméra :**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/picarx-control/scripts/pc.py cam tilt --angle 20

**Jouer un effet sonore :**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/picarx-control/scripts/pc.py sound play /path/to/sound.wav --volume 80

**Lire les données du capteur de niveaux de gris (suivi de ligne) :**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/picarx-control/scripts/pc.py sensor grayscale

**Lancer l'étalonnage des servos :**

.. code-block:: bash

   python3 ~/.openclaw/workspace/skills/picarx-control/scripts/pc.py calibrate

----------------------------------------------------------------

Utiliser la compétence PiCar-X dans OpenClaw
----------------------------------------------------

Une fois que vous avez vérifié que la compétence PiCar-X fonctionne depuis la ligne de commande, vous pouvez commencer à l'utiliser dans OpenClaw.

1. **Lancez OpenClaw TUI** :

   .. code-block:: bash

      openclaw tui

2. **Envoyez des commandes en langage naturel** pour contrôler le PiCar-X. Voici quelques exemples :

   * « Avance »
   * « Recule »
   * « Tourne à gauche »
   * « Tourne à droite »
   * « Vérifie s'il y a quelque chose devant »
   * « Regarde à gauche »
   * « Regarde en haut »
   * « Regarde en bas »
   * « Prends une photo »
   * « Détecte les visages »
   * « Trouve la couleur rouge »
   * « Suis la ligne »
   * « Vérifie s'il y a une falaise devant »

3. **OpenClaw traduira automatiquement** votre demande en code Python approprié et l'exécutera sur le PiCar-X.

----------------------------------------------------------------

Actions et commandes disponibles
-------------------------------------------

Voici la liste complète des capacités prises en charge par la compétence PiCar-X :

Conduite (``pc.py move``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Action
     - Description
   * - ``forward``
     - Avancer
   * - ``backward``
     - Reculer

Direction (``pc.py turn``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Action
     - Description
   * - ``left``
     - Tourner à gauche en ajustant l'angle de direction
   * - ``right``
     - Tourner à droite en ajustant l'angle de direction

Caméra orientable (``pc.py cam``)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Capacité
     - Description
   * - Panoramique
     - Faire pivoter la caméra horizontalement (-90° à 90°)
   * - Inclinaison
     - Incliner la caméra verticalement (-35° à 65°)

Capteurs
^^^^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Commande
     - Description
   * - ``sensor distance``
     - Lire le capteur de distance ultrasonique (retourne en cm)
   * - ``sensor grayscale``
     - Lire les valeurs du module de niveaux de gris à 3 canaux (pour le suivi de ligne et la détection de falaise)

Son (``pc.py sound``)
^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Commande
     - Description
   * - ``sound play <fichier>``
     - Jouer un fichier d'effet sonore
   * - ``sound music <fichier>``
     - Jouer de la musique de fond
   * - ``sound volume <0-100>``
     - Régler le volume du haut-parleur
   * - ``sound stop``
     - Arrêter la lecture

.. note::

   Les fichiers son peuvent être n'importe quel fichier audio au format ``.wav`` accessible sur votre Raspberry Pi. Vous pouvez également utiliser ``sound music`` pour lire des fichiers de musique de fond.

Caméra et vision (via langage naturel / exec)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Capacité
     - Description
   * - Prendre une photo
     - Capturer et enregistrer une photo dans ``~/Pictures/``
   * - Détection de visage
     - Détecter les visages humains et indiquer leur position
   * - Détection de couleur
     - Localiser des objets par couleur (rouge, bleu, vert, etc.)
   * - Reconnaissance de gestes
     - Reconnaître les gestes pierre/feuille/ciseaux
   * - Détection de panneaux
     - Reconnaître les panneaux stop/gauche/droite/tout droit
   * - Lecture de QR code
     - Lire les données et la position des QR codes

Suivi de ligne et détection de falaise
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Capacité
     - Description
   * - Suivi de ligne
     - Suivre une ligne noire sur une surface claire en utilisant le capteur de niveaux de gris à 3 canaux
   * - Détection de falaise
     - Détecter les bords/chutes en utilisant les seuils du capteur de niveaux de gris

----------------------------------------------------------------

Dépannage
------------------------------

Problèmes avec OpenClaw
^^^^^^^^^^^^^^^^^^^^^^^^

Q. Pendant l'installation, j'obtiens l'erreur ``Error: systemctl is-enabled unavailable: Command failed: systemctl --user is-enabled openclaw-gateway.service``. Que dois-je faire ?

   Vous pouvez ignorer cela pour le moment, mais vous pourriez rencontrer des problèmes lors des prochaines étapes. Veuillez vous y référer un par un à ce moment-là.


Q. Lorsque j'exécute ``openclaw tui``, j'obtiens l'erreur ``-bash: openclaw: command not found``. Que dois-je faire ?

   Exécutez la commande suivante :

   .. code-block:: bash

      echo 'export PATH="$HOME/.npm-global/bin:$PATH"' >> ~/.bashrc
      source ~/.bashrc

   Vous devriez maintenant pouvoir démarrer l'interface TUI avec ``openclaw tui``.



Q. Dans ``openclaw tui``, je rencontre ``not connected to gateway — message not sent`` ou le message ``gateway disconnected: closed``.

   Cela signifie que votre service OpenClaw Gateway n'est pas démarré. Ouvrez un autre terminal et exécutez la commande suivante pour démarrer l'OpenClaw Gateway :

   .. code-block:: bash

      openclaw gateway

   Ensuite, redémarrez ``openclaw tui``, et vous pourrez l'utiliser directement.


Q. Je souhaite configurer le service OpenClaw Gateway pour qu'il s'exécute en arrière-plan / démarre automatiquement au démarrage. Comment faire ?

   Normalement, votre service OpenClaw Gateway devrait démarrer automatiquement au démarrage. Si ce n'est pas le cas, vous pouvez le démarrer manuellement avec la commande suivante.

   1. Créez le répertoire ``~/.config/systemd/user`` :

   .. code-block:: bash

      mkdir -p ~/.config/systemd/user


   2. Créez le fichier ``openclaw-gateway.service`` :

   .. code-block:: bash

      cat > ~/.config/systemd/user/openclaw-gateway.service << EOF
      [Unit]
      Description=OpenClaw Gateway
      After=network.target

      [Service]
      Type=simple
      ExecStart=$HOME/.npm-global/bin/openclaw gateway run
      Restart=on-failure
      RestartSec=10
      Environment="PATH=$HOME/.npm-global/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin"
      Environment="NODE_ENV=production"

      [Install]
      WantedBy=default.target
      EOF


   3. Ensuite, rechargez la configuration systemd :

   .. code-block:: bash

      systemctl --user daemon-reload

   4. Démarrez le service :

   .. code-block:: bash

      systemctl --user start openclaw-gateway

   À ce stade, redémarrez ``openclaw tui``, et vous pourrez l'utiliser directement.

   5. Activez-le pour qu'il démarre au démarrage :

   .. code-block:: bash

      systemctl --user enable openclaw-gateway


Q. Mon OpenClaw ne peut pas interagir avec le système, que dois-je faire ?

   Un OpenClaw nouvellement installé peut ne pas avoir la permission d'interagir avec votre système Raspberry Pi par défaut ; il peut seulement discuter. Nous devons configurer manuellement les permissions.

   1.  Ouvrez le fichier de configuration d'OpenClaw :

      .. code-block:: bash

         nano ~/.openclaw/openclaw.json

   2.  Trouvez l'option ``tools`` et modifiez ``profile`` et ``exec`` comme indiqué.

      .. code-block:: json

        "tools": {
            "profile": "coding",
            "exec": {
                "secrity": "full"
            }
        },

   3.  Enregistrez et quittez.

   4.  Entrez la commande suivante dans le terminal pour redémarrer l'OpenClaw Gateway :

      .. code-block:: bash

         openclaw gateway restart

   Maintenant, OpenClaw devrait avoir les permissions de lecture et d'écriture et pouvoir interagir avec votre système Raspberry Pi.

Problèmes avec le PiCar-X
^^^^^^^^^^^^^^^^^^^^^^^^^^^^


Q. Le PiCar-X ne répond pas aux commandes. Que dois-je faire ?

   Tout d'abord, vérifiez que le PiCar-X est correctement connecté et allumé. Ensuite, testez les fonctionnalités de base :

   .. code-block:: bash

      python3 ~/.openclaw/workspace/skills/picarx-control/scripts/pc.py sensor distance

   Si cela échoue, assurez-vous que les bibliothèques Python requises sont installées :

   .. code-block:: bash

      python3 -c "import picarx; import robot_hat; import vilib"

Q. Le test ``import picarx`` échoue.

   Cela signifie que la bibliothèque Python PiCar-X n'est pas correctement installée. Veuillez consulter le guide d'installation officiel du PiCar-X pour installer les bibliothèques nécessaires. Vous pouvez également exécuter le script d'installation inclus :

   .. code-block:: bash

      bash ~/.openclaw/workspace/skills/picarx-control/install.sh

Q. OpenClaw ne reconnaît pas la compétence PiCar-X.

   Rappelez à OpenClaw de synchroniser les compétences en disant dans le TUI : *« Please rsync my skills »* ou redémarrez l'OpenClaw Gateway :

   .. code-block:: bash

      openclaw gateway restart

Q. Les mouvements du PiCar-X semblent saccadés ou la direction est décentrée.

   Cela est généralement dû à des valeurs d'étalonnage des servos incorrectes. Exécutez le script d'étalonnage pour ajuster le servo de direction et la caméra orientable :

   .. code-block:: bash

      python3 ~/.openclaw/workspace/skills/picarx-control/scripts/pc.py calibrate

   Vous pouvez également ajuster le paramètre de vitesse (par exemple, utilisez ``--speed 40``) pour un mouvement plus fluide, ou ajouter de courtes pauses entre les commandes consécutives.

Q. Le suivi de ligne ou les niveaux de gris ne fonctionnent pas correctement.

   Assurez-vous que le module de niveaux de gris est correctement étalonné pour votre surface. Vous pouvez définir les valeurs de référence de ligne à l'aide de la configuration. Consultez la documentation principale du PiCar-X pour les procédures d'étalonnage des niveaux de gris.

----------------------------------------------------------------

.. end_using_picarx
