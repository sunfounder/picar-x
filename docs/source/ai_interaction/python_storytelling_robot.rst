.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 sur Facebook ! Plongez plus profondément dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et avant-premières.
    - **Réductions exclusives** : Profitez de réductions exclusives sur nos nouveaux produits.
    - **Promotions festives et concours** : Participez à des concours et promotions lors des fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !


15. Robot Conteur avec Piper et OpenAI
========================================================

Dans la leçon précédente, nous avons testé deux moteurs TTS intégrés sur Raspberry Pi (**Espeak** et **Pico2Wave**).
Explorons maintenant deux options plus puissantes : **Piper** (hors ligne, basé sur des réseaux neuronaux) et **OpenAI TTS** (en ligne, basé sur le cloud).

* **Piper** : un moteur TTS local qui fonctionne hors ligne sur Raspberry Pi.
* **OpenAI TTS** : un service en ligne offrant des voix très naturelles et humaines.

À la fin, votre PiCar-X roulera tout en racontant des blagues comme un petit conteur.

Avant de Commencer
-------------------

Assurez-vous d'avoir terminé :

* :ref:`install_all_modules` — Install ``robot-hat``, ``vilib``, ``picar-x`` modules, then run the script ``i2samp.sh``.

.. _test_piper:

1. Tester Piper
------------------

**Étapes à suivre** :

#. Créez un nouveau fichier :

   .. code-block:: bash

      cd ~/picar-x/example
      sudo nano test_tts_piper.py

#. Copiez le code ci-dessous dans le fichier. Appuyez sur ``Ctrl+X``, puis ``Y`` et enfin ``Entrée`` pour sauvegarder et quitter.

   .. code-block:: python

       from picarx.tts import Piper

       tts = Piper()

       # Liste les langues prises en charge
       print(tts.available_countrys())

       # Liste les modèles pour l'anglais (en_us)
       print(tts.available_models('en_us'))

       # Définit un modèle vocal (téléchargement automatique s'il n'est pas présent)
       tts.set_model("en_US-amy-low")

       # Prononce une phrase
       tts.say("Hello! I'm Piper TTS.")

   * ``available_countrys()`` : affiche les langues prises en charge.
   * ``available_models()`` : liste les modèles disponibles pour cette langue.
   * ``set_model()`` : définit le modèle vocal (téléchargé automatiquement s'il est absent).
   * ``say()`` : convertit le texte en parole et le lit à voix haute.

#. Exécutez le programme :

   .. code-block:: bash

      sudo python3 test_tts_piper.py

#. Lors de la première exécution, le modèle vocal sélectionné sera téléchargé automatiquement.

   * Vous devriez alors entendre le PiCar-X dire : ``Hello! I'm Piper TTS.``

   * Vous pouvez changer de modèle linguistique en appelant ``set_model()`` avec un autre nom.


2. Tester OpenAI TTS
-------------------------------

**Obtenir et enregistrer votre clé API**

#. Rendez-vous sur |link_openai_platform| et connectez-vous. Sur la page **API keys**, cliquez sur **Create new secret key**.

   .. image:: img/llm_openai_create.png

#. Remplissez les informations (Propriétaire, Nom, Projet et permissions si nécessaire), puis cliquez sur **Create secret key**.

   .. image:: img/llm_openai_create_confirm.png

#. Une fois la clé créée, copiez-la immédiatement — vous ne pourrez plus la revoir. Si vous la perdez, vous devrez en générer une nouvelle.

   .. image:: img/llm_openai_copy.png

#. Dans votre dossier de projet (par exemple : ``/picar-x/example``), créez un fichier appelé ``secret.py`` :

   .. code-block:: bash

       cd ~/picar-x/example
       sudo nano secret.py

#. Collez votre clé dans le fichier comme ceci :

   .. code-block:: python

       # secret.py
       # Stockez les clés ici. Ne jamais valider ce fichier dans Git.
       OPENAI_API_KEY = "sk-xxx"

**Écrire et exécuter un programme de test**

#. Créez un nouveau fichier :

   .. code-block:: bash

       cd ~/picar-x/example
       sudo nano test_tts_openai.py

#. Copiez le code ci-dessous dans le fichier. Appuyez sur ``Ctrl+X``, puis ``Y`` et enfin ``Entrée`` pour sauvegarder et quitter.

   .. code-block:: python

      from picarx.tts import OpenAI_TTS
      from secret import OPENAI_API_KEY   # ou utilisez la version try/except montrée plus haut

      # Initialiser OpenAI TTS
      tts = OpenAI_TTS(api_key=OPENAI_API_KEY)
      tts.set_model('gpt-4o-mini-tts')  # modèle TTS à faible latence
      tts.set_voice('alloy')            # choisir une voix

      # Petit test de vérification
      tts.say("Hello! I'm OpenAI TTS.")

#. Exécutez le programme :

   .. code-block:: bash

       sudo python3 test_tts_openai.py

#. Vous devriez entendre le PiCar-X dire :

   ``Hello! I'm OpenAI TTS.``


3. Robot Conteur
------------------------

Maintenant que nous avons testé **Piper** et **OpenAI TTS**, utilisons-les dans un vrai projet :
un **robot conteur** qui se déplace tout en racontant des blagues.

Dans ce programme, le PiCar-X va :

* Vous saluer avec une synthèse vocale au démarrage.
* Avancer et raconter une première blague.
* Avancer à nouveau et raconter une deuxième blague.
* Enfin, reculer, revenir « à la maison » et dire au revoir.

C'est comme avoir un petit robot conteur sur roues !

**Exécuter le code**

.. code-block:: bash

    cd ~/picar-x/example
    sudo python3 15.storytelling_robot.py

**Code**


.. code-block:: python

   from picarx import Picarx
   import time

   # === TTS Configuration ===
   # Default: Piper
   from picarx.tts import Piper
   tts = Piper()
   tts.set_model("en_US-amy-low")  # use the voice model you installed

   # Optional: switch to OpenAI TTS
   # from picarx.tts import OpenAI_TTS
   # from secret import OPENAI_API_KEY
   # tts = OpenAI_TTS(api_key=OPENAI_API_KEY)
   # tts.set_model("gpt-4o-mini-tts")  # low-latency TTS model
   # tts.set_voice("alloy")            # choose a voice

   # === PiCar-X Setup ===
   px = Picarx()

   # Quick hello (sanity check)
   tts.say("Hello! I'm PiCar-X speaking with Piper.")

   def main():
       try:
           # Leg 1
           px.forward(30)
           time.sleep(3)
           px.stop()
           tts.say("Why can't your nose be twelve inches long? Because then it would be a foot!")

           # Leg 2
           px.forward(30)
           time.sleep(3)
           px.stop()
           tts.say("Why did the cow go to outer space? To see the moooon!")

           # Wrap-up
           tts.say("That's all for today. Goodbye, let's go home and sleep.")
           px.backward(30)
           time.sleep(6)
           px.stop()

       except KeyboardInterrupt:
           px.stop()
       finally:
           px.stop()
           px.set_dir_servo_angle(0)

   if __name__ == "__main__":
       main()

----

Dépannage
-------------------

* **No module named 'secret'**

  Cela signifie que ``secret.py`` n'est pas dans le même dossier que votre fichier Python.
  Déplacez ``secret.py`` dans le même répertoire que celui où vous exécutez le script, par exemple :

  .. code-block:: bash

     ls ~/picar-x/example
     # Assurez-vous que vous voyez à la fois : secret.py et votre fichier .py

* **OpenAI : Invalid API key / 401**

  * Vérifiez que vous avez bien collé la clé complète (elle commence par ``sk-``) et qu'il n'y a pas d'espaces ou de retours à la ligne en trop.
  * Assurez-vous que votre code l'importe correctement :

    .. code-block:: python

       from secret import OPENAI_API_KEY

  * Confirmez que votre Raspberry Pi a accès au réseau (essayez ``ping api.openai.com``).

* **OpenAI : Quota dépassé / erreur de facturation**

  * Vous devrez peut-être ajouter un moyen de paiement ou augmenter votre quota dans le tableau de bord OpenAI.
  * Réessayez après avoir résolu le problème de facturation.

* **Piper : tts.say() s'exécute mais aucun son**

  * Assurez-vous qu'un modèle vocal est bien présent :

    .. code-block:: bash

       ls ~/.local/share/piper/voices

  * Vérifiez que le nom du modèle correspond exactement dans votre code :

    .. code-block:: python

       tts.set_model("en_US-amy-low")

  * Vérifiez le périphérique de sortie audio / le volume sur votre Pi (``alsamixer``) et que les haut-parleurs sont correctement branchés et alimentés.

* **Erreurs ALSA / périphérique audio (par ex. « Audio device busy » ou « No such file or directory »)**

  * Fermez les autres programmes utilisant l'audio.
  * Redémarrez le Raspberry Pi si le périphérique reste occupé.
  * Pour HDMI vs prise jack, sélectionnez le bon périphérique dans les paramètres audio de Raspberry Pi OS.

* **Permission denied lors de l'exécution de Python**

  * Essayez avec ``sudo`` si votre environnement l'exige :

    .. code-block:: bash

       sudo python3 test_tts_piper.py



Comparaison des moteurs TTS
-----------------------------------

.. list-table:: Comparatif des fonctionnalités : Espeak vs Pico2Wave vs Piper vs OpenAI TTS
   :header-rows: 1
   :widths: 18 18 20 22 22

   * - Élément
     - Espeak
     - Pico2Wave
     - Piper
     - OpenAI TTS
   * - Fonctionne sur
     - Intégré au Raspberry Pi (hors ligne)
     - Intégré au Raspberry Pi (hors ligne)
     - Raspberry Pi / PC (hors ligne, nécessite un modèle)
     - Cloud (en ligne, nécessite une clé API)
   * - Qualité de la voix
     - Robotique
     - Plus naturelle qu'Espeak
     - Naturelle (TTS neuronal)
     - Très naturelle / humaine
   * - Contrôles
     - Vitesse, hauteur, volume
     - Contrôles limités
     - Choix de différentes voix/modèles
     - Choix de modèles et de voix
   * - Langues
     - Nombreuses (qualité variable)
     - Ensemble limité
     - Nombreuses voix/langues disponibles
     - Meilleure en anglais (autres langues selon disponibilité)
   * - Latence / vitesse
     - Très rapide
     - Rapide
     - Temps réel sur Pi 4/5 avec modèles « low »
     - Dépend du réseau (généralement faible latence)
   * - Installation
     - Minimale
     - Minimale
     - Télécharger les modèles ``.onnx`` + ``.onnx.json``
     - Créer une clé API, installer le client
   * - Idéal pour
     - Tests rapides, invites simples
     - Voix hors ligne légèrement meilleure
     - Projets locaux avec meilleure qualité vocale
     - Qualité maximale, nombreuses options vocales
