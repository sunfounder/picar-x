.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 sur Facebook ! Plongez plus profondément dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et avant-premières.
    - **Réductions exclusives** : Profitez de réductions exclusives sur nos nouveaux produits.
    - **Promotions festives et concours** : Participez à des concours et promotions lors des fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !


.. _ai_voice_assistant_car:

21. Voiture Assistante Vocale IA
=============================================

Cette leçon transforme votre PiCar-X en **assistant vocal mobile alimenté par l’IA**.  
Le robot peut se réveiller à votre voix, reconnaître ce que vous dites, répondre avec émotion,  
et exprimer ses “sentiments” à travers des mouvements, des gestes et des lumières.

Vous allez construire une **voiture assistante vocale entièrement interactive** en utilisant :

* **LLM** - Large Language Model (OpenAI GPT ou Doubao).  
* **STT** - Speech-to-Text (voix vers texte).  
* **TTS** - Text-to-Speech (texte vers voix).  
* **Capteurs + Actions** - Ultrason, caméra et actions expressives intégrées.

----

Avant de Commencer
-------------------

Assurez-vous d’avoir terminé :

* :ref:`install_all_modules` — Installe les modules ``robot-hat``, ``vilib``, ``picar-x``, puis exécute le script ``i2samp.sh``.
* :ref:`test_piper` — Vérifiez les langues prises en charge par **Piper TTS**.  
* :ref:`test_vosk` — Vérifiez les langues prises en charge par **Vosk STT**.  
* :ref:`py_online_llm` — Cette étape est **très importante** : obtenez votre clé API **OpenAI** ou **Doubao**, ou la clé API d’un autre LLM pris en charge.

Vous devez déjà disposer de :

* Un **microphone** et un **haut-parleur** fonctionnels sur votre PiCar-X.  
* Une **clé API valide** enregistrée dans ``secret.py``.  
* Une connexion réseau stable (une **connexion filaire** est recommandée pour une meilleure stabilité).

----

Exécuter l’Exemple
-------------------

Les deux versions linguistiques sont placées dans le même répertoire :

.. code-block:: bash

   cd ~/picar-x/example

**Version anglaise** (OpenAI GPT, instructions en anglais) :

.. code-block:: bash

   sudo python3 21.voice_active_car_gpt.py

* LLM : ``OpenAI GPT-4o-mini``  
* TTS : ``en_US-ryan-low`` (Piper)  
* STT : Vosk (``en-us``)

Mot d’activation :

.. code-block::

   "Hey buddy"

---

**Version chinoise** (Doubao, instructions en chinois) :

.. code-block:: bash

   sudo python3 21.voice_active_car_doubao_cn.py

* LLM : ``Doubao-seed-1-6-250615``  
* TTS : ``zh_CN-huayan-x_low`` (Piper)  
* STT : Vosk (``cn``)

Mot d’activation :

.. code-block::

   "你好 滴滴"

.. note::

   Vous pouvez modifier le **mot d’activation** et le **nom du robot** dans le code :  
   ``NAME = "Buddy"`` ou ``NAME = "滴滴"``  
   ``WAKE_WORD = ["hey buddy"]`` ou ``WAKE_WORD = ["你好 滴滴"]``

----

Ce Qui Va se Passer
--------------------

Lorsque vous exécutez cet exemple avec succès :

* Le robot **attend le mot d’activation** (par ex. “Hey Buddy” / “你好 滴滴”).  
* Lorsqu’il entend le mot d’activation :

  * Les LED **clignotent** puis restent allumées.  
  * Le robot vous **salue** avec une voix joyeuse.

* Il commence ensuite à **écouter votre voix** en temps réel.  
* Après avoir reconnu ce que vous avez dit, il :

  * Envoie votre parole au **LLM** (OpenAI ou Doubao).  
  * **Réfléchit** et fait clignoter les LED pendant le traitement.  
  * Répond avec une **voix TTS**.  
  * Exécute les **actions correspondantes** (par ex. hochement de tête, rotation, célébration).

* Si vous vous approchez trop près, le capteur à ultrasons :

  * Déclenche un mouvement automatique de **recul** pour la sécurité.  
  * Interrompt le cycle en cours avec une réponse d’avertissement.

**Exemple d’interaction**

.. code-block:: text

   Vous : Hey Buddy
   Robot : Salut !

   Vous : Tourne à gauche et regarde autour.
   Robot : Bien reçu, je tourne la tête à gauche comme un chat curieux !
   ACTIONS : turn_left, look_left

----

Basculer vers d’Autres LLM ou TTS
---------------------------------------------

Vous pouvez facilement passer à d’autres LLM, TTS ou langues STT en effectuant seulement quelques modifications :

* LLM pris en charge :

  * OpenAI
  * Doubao
  * Deepseek
  * Gemini
  * Qwen
  * Grok

* :ref:`test_piper` — Vérifiez les langues prises en charge par **Piper TTS**.  
* :ref:`test_vosk` — Vérifiez les langues prises en charge par **Vosk STT**.  

Pour changer, modifiez simplement la partie d’initialisation dans le code :

.. code-block:: python

   from picarx.llm import Gemini as LLM
   llm = LLM(api_key="YOUR_KEY", model="gemini-pro")

   # Définir les modèles et les langues
   TTS_MODEL = "en_US-ryan-low"
   STT_LANGUAGE = "en-us"

----

Référence des Actions et Sons
-----------------------------

Voici les **mots-clés d’action** que le LLM peut renvoyer (après la ligne ``ACTIONS:``) et leur effet sur le robot.

.. list-table::
   :header-rows: 1
   :widths: 20 55 25

   * - **Action**
     - **Ce qu’elle fait (selon preset_actions.py)**
     - **Effet / Remarques**
   * - ``shake head``
     - Balance rapidement l’angle de panoramique de la caméra de droite à gauche en mouvements décroissants, puis se recentre.
     - Geste de “Non” ; les roues restent immobiles.
   * - ``nod``
     - Fait basculer la caméra vers le haut et le bas deux fois, puis se recentre.
     - Geste de “Oui” ; les roues restent immobiles.
   * - ``wave hands``
     - Incline la caméra, puis tourne le volant à gauche/droite deux fois (±25°), puis revient au centre.
     - Salutation ludique (utilise le servo de direction comme des “bras”).
   * - ``resist``
     - Petite inclinaison ; alterne (direction ±15°, panoramique ±15°) 3 fois ; s’arrête et se recentre.
     - Mouvement de “refus” ou défensif.
   * - ``act cute``
     - Incline la tête vers le bas ; petits allers-retours rapides (courtes impulsions moteurs), puis réinitialisation.
     - Mouvement “mignon” rebondissant ; très courtes actions.
   * - ``rub hands``
     - Petites oscillations répétées de la direction (±6°) cinq fois ; réinitialisation.
     - Imite le geste de “frotter les mains”.
   * - ``think``
     - Panoramique fluide vers la droite + inclinaison vers le bas + direction à droite ; courte pause ; pose réfléchie ; réinitialisation.
     - Utilisé comme animation unique de “réflexion”.
   * - ``twist body``
     - Trois cycles de court mouvement avant / arrêt / pan gauche / direction gauche, puis court mouvement arrière / arrêt / pan droit / direction droite.
     - Donne une impression de “torsion” du corps.
   * - ``celebrate``
     - Inclinaison vers le haut ; deux mouvements pan/direction vers la droite, puis deux vers la gauche ; retour au centre.
     - Mouvement festif et symétrique.
   * - ``depressed``
     - Série d’inclinaisons vers le bas avec des angles et des pauses variés ; se termine après un long battement et se réinitialise.
     - Séquence de posture “triste”.


Mouvements & Utilitaires
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 22 58 20

   * - **Action**
     - **Ce qu’elle fait**
     - **Remarques**
   * - ``forward``
     - Avance à basse vitesse pendant environ 1 seconde, puis s’arrête.
     - Implémenté par ``forward(car)`` (5 % de vitesse + 1 s).
   * - ``backward``
     - Recule à basse vitesse pendant environ 1 seconde, puis s’arrête.
     - Implémenté par ``backward(car)`` (5 % de vitesse + 1 s).

Effets Sonores
~~~~~~~~~~~~~~

.. list-table::
   :header-rows: 1
   :widths: 24 56 20

   * - **Son**
     - **Ce qu’il fait**
     - **Remarques**
   * - ``honking``
     - Joue ``car-double-horn.wav`` de manière asynchrone (volume ~100).
     - Déclenché via ``Music.sound_play_threading``.
   * - ``start engine``
     - Joue ``car-start-engine.wav`` de manière asynchrone (volume ~50).
     - Signal de démarrage / prêt.

Déclencheurs Capteurs (Automatiques)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Proximité ultrasonique**  

  * Déclenchement : distance < 10 cm  
  * Effet secondaire : mouvement automatique ``backward`` + désactivation de l’image pour ce tour  
  * Message injecté : ``<<<Ultrasonic sense too close: {distance}cm>>>``

Hooks du Cycle de Vie (Indicateurs LED)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* ``before_listen`` → clignote deux fois (prêt à écouter)  
* ``before_think`` → clignotement continu (réflexion)  
* ``before_say`` → LED allumée (parole)  
* ``after_say`` → attend les actions → LED éteinte  
* ``on_stop`` → arrêt des actions, fermeture des périphériques


----

Dépannage
---------

* **Le robot ne réagit pas au mot d’activation**  

  * Vérifiez si le microphone fonctionne.  
  * Assurez-vous que ``WAKE_ENABLE = True``.  
  * Ajustez le mot d’activation pour correspondre à votre prononciation.

* **Aucun son ne sort du haut-parleur**
 
  * Vérifiez la configuration du modèle TTS.  
  * Testez Piper ou Espeak manuellement.  
  * Vérifiez la connexion et le volume du haut-parleur.

* **Erreur ou délai d’expiration de la clé API** 
 
  * Vérifiez votre clé dans ``secret.py``.  
  * Assurez-vous que la connexion réseau est active.  
  * Confirmez que le LLM est pris en charge.

* **Le PiCar-X ne bouge pas ou n’exécute pas les actions**
 
  * Vérifiez que le nom de l’action correspond à ``actions_dict``.  
  * Vérifiez les connexions moteur et servomoteur.

* **Le capteur à ultrasons se déclenche de manière inattendue.**  

  * Vérifiez la hauteur et l’angle d’installation du capteur.  
  * Ajustez le seuil de distance ``TOO_CLOSE`` dans le code.
