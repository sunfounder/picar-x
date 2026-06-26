.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 sur Facebook ! Plongez plus profondément dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et avant-premières.
    - **Réductions exclusives** : Profitez de réductions exclusives sur nos nouveaux produits.
    - **Promotions festives et concours** : Participez à des concours et promotions lors des fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !


17. Vision et Langage avec Ollama
====================================

Dans cette leçon, vous allez apprendre à utiliser **Ollama**, un outil qui permet d'exécuter localement de grands modèles de langage et de vision.
Nous allons vous montrer comment installer Ollama, télécharger un modèle et connecter PiCar-X à ce modèle.

Grâce à cette configuration, PiCar-X peut prendre une photo avec sa caméra et le modèle pourra **voir et décrire** —
vous pourrez poser n'importe quelle question sur l'image, et le modèle répondra en langage naturel.

Avant de Commencer
-------------------

Assurez-vous d'avoir terminé :

* :ref:`install_all_modules` — Install ``robot-hat``, ``vilib``, ``picar-x`` modules, then run the script ``i2samp.sh``.

.. _download_ollama:

1. Installer Ollama (LLM) et Télécharger un Modèle
-----------------------------------------------------

Vous pouvez choisir où installer **Ollama** :

* Sur votre Raspberry Pi (exécution locale)
* Ou sur un autre ordinateur (Mac / Windows / Linux) dans le **même réseau local**

**Modèles recommandés selon le matériel**

Vous pouvez choisir n'importe quel modèle disponible sur |link_ollama_hub|.
Les modèles existent en différentes tailles (3B, 7B, 13B, 70B...).
Les petits modèles sont plus rapides et consomment moins de mémoire, tandis que les grands modèles offrent de meilleures réponses mais nécessitent un matériel plus puissant.

Consultez le tableau ci-dessous pour choisir la taille du modèle adaptée à votre appareil.

.. list-table::
   :header-rows: 1
   :widths: 20 20 40

   * - Taille du modèle
     - RAM minimale requise
     - Matériel recommandé
   * - ~3B paramètres
     - 8 Go (16 Go recommandé)
     - Raspberry Pi 5 (16 Go) ou PC/Mac milieu de gamme
   * - ~7B paramètres
     - 16 Go +
     - Pi 5 (16 Go, limite) ou PC/Mac milieu de gamme
   * - ~13B paramètres
     - 32 Go +
     - PC/Mac de bureau avec RAM importante
   * - 30B+ paramètres
     - 64 Go +
     - Station de travail / serveur / GPU recommandé
   * - 70B+ paramètres
     - 128 Go +
     - Serveur haut de gamme avec plusieurs GPU

**Installation sur Raspberry Pi**

Si vous souhaitez exécuter Ollama directement sur votre Raspberry Pi :

* Utilisez un **Raspberry Pi OS 64 bits**
* Fortement recommandé : **Raspberry Pi 5 (16 Go RAM)**

Exécutez les commandes suivantes :

.. code-block:: bash

   # Installer Ollama
   curl -fsSL https://ollama.com/install.sh | sh

   # Télécharger un modèle léger (bon pour les tests)
   ollama pull llama3.2:3b

   # Test rapide (tapez 'hi' et appuyez sur Entrée)
   ollama run llama3.2:3b

   # Démarrer l'API (port par défaut 11434)
   # Astuce : définissez OLLAMA_HOST=0.0.0.0 pour permettre l'accès via le LAN
   OLLAMA_HOST=0.0.0.0 ollama serve

**Installation sur Mac / Windows / Linux (application de bureau)**

1. Téléchargez et installez Ollama depuis |link_ollama|

   .. image:: img/llm_ollama_download.png

2. Ouvrez l'application Ollama, allez dans le **sélecteur de modèle**, et utilisez la barre de recherche pour trouver un modèle.
   Par exemple, tapez ``llama3.2:3b`` (un petit modèle léger pour commencer).

   .. image:: img/llm_ollama_choose.png

3. Une fois le téléchargement terminé, tapez quelque chose de simple comme "Hi" dans la fenêtre de chat — Ollama lancera automatiquement le modèle au premier usage.

   .. image:: img/llm_olama_llama_download.png

4. Allez dans **Settings** → activez **Expose Ollama to the network**.
   Cela permet à votre Raspberry Pi de s'y connecter via le réseau local.

   .. image:: img/llm_olama_windows_enable.png

.. warning::

   Si vous voyez une erreur comme :

   ``Error: model requires more system memory ...``

   Cela signifie que le modèle est trop volumineux pour votre machine.
   Utilisez un **modèle plus petit** ou passez à un ordinateur avec plus de RAM.

2. Tester Ollama
------------------------

Une fois Ollama installé et votre modèle prêt, vous pouvez le tester rapidement avec une simple boucle de chat minimale.

**Étapes**

#. Créez un nouveau fichier :

   .. code-block:: bash

      cd ~/picar-x/example
      nano test_llm_ollama.py

#. Collez le code suivant et enregistrez (``Ctrl+X`` → ``Y`` → ``Entrée``) :

   .. code-block:: python

      from picarx.llm import Ollama

      INSTRUCTIONS = "You are a helpful assistant."
      WELCOME = "Hello, I am a helpful assistant. How can I help you?"

      # If Ollama runs on the same Raspberry Pi, use "localhost".
      # If it runs on another computer in your LAN, replace with that computer's IP address.
      llm = Ollama(
          ip="localhost",
          model="llama3.2:3b"   # you can replace with any model
      )

      # Basic configuration
      llm.set_max_messages(20)
      llm.set_instructions(INSTRUCTIONS)
      llm.set_welcome(WELCOME)

      print(WELCOME)

      while True:
          text = input(">>> ")
          if text.strip().lower() in {"exit", "quit"}:
              break

          # Response with streaming output
          response = llm.prompt(text, stream=True)
          for token in response:
              if token:
                  print(token, end="", flush=True)
          print("")

#. Exécutez le programme :

   .. code-block:: bash

      python3 test_llm_ollama.py

#. Vous pouvez maintenant discuter avec PiCar-X directement depuis le terminal.

   * Vous pouvez choisir **n'importe quel modèle** disponible sur |link_ollama_hub|, mais les petits modèles (par ex. ``moondream:1.8b``, ``phi3:mini``) sont recommandés si vous n'avez que 8 à 16 Go de RAM.
   * Assurez-vous que le modèle spécifié dans le code correspond bien à celui que vous avez déjà téléchargé dans Ollama.
   * Tapez ``exit`` ou ``quit`` pour arrêter le programme.
   * Si la connexion échoue, vérifiez qu'Ollama est en cours d'exécution et que les deux appareils sont bien sur le même réseau local si vous utilisez un hôte distant.



3. Vision et Dialogue avec Ollama
-------------------------------------------

Dans cette démo, la caméra du Pi prend une photo **chaque fois que vous tapez une question**.
Le programme envoie **votre texte + la nouvelle photo** à un modèle de vision local via Ollama,
puis diffuse la réponse du modèle en anglais simple.
C'est une base minimale de type "voir et raconter" que vous pourrez ensuite enrichir avec des détections de couleur/visage/QR code.

**Avant de Commencer**

#. Ouvrez l'application **Ollama** (ou lancez le service) et assurez-vous qu'un **modèle compatible vision** est téléchargé.

   * Si vous avez suffisamment de mémoire (≥16 Go RAM), vous pouvez essayer ``llava:7b``.
   * Si vous n'avez que **8 Go RAM**, préférez un modèle plus léger comme ``moondream:1.8b`` ou ``granite3.2-vision:2b``.

   .. image:: img/llm_ollama_image_model.png

**Lancer la Démo**

#. Accédez au dossier des exemples et lancez le script :

   .. code-block:: bash

      cd ~/picar-x/example
      python3 17.text_vision_talk.py

#. Ce qu'il se passe à l'exécution :

   * Le programme affiche une ligne d'accueil et attend votre saisie (``>>>``).
   * **Chaque fois que vous tapez quelque chose** (par ex. "hello", "Y a-t-il du jaune ?", "Des visages ?", "Qu'y a-t-il sur le bureau ?"), il :

     * **capture une photo** avec la caméra du Pi (enregistrée dans ``/tmp/llm-img.jpg``),
     * **envoie votre texte + la photo** au modèle de vision via Ollama,
     * **diffuse en retour** la réponse du modèle dans le terminal.

   * Tapez ``exit`` ou ``quit`` pour quitter le programme.

**Code**


.. code-block:: python

   from picarx.llm import Ollama
   from picamera2 import Picamera2
   import time

   """
   You need to set up Ollama first.

   Note: At least 8GB RAM is recommended for small vision models (e.g., moondream:1.8b).
         For llava:7b, more memory is preferred (>=16GB).
   """

   INSTRUCTIONS = "You are a helpful assistant."
   WELCOME = "Hello, I am a helpful assistant. How can I help you?"

   # If Ollama runs on the same Pi, use "localhost".
   # If it runs on another computer in your LAN, replace with that computer's IP.
   llm = Ollama(
       ip="localhost",          # e.g., "192.168.100.145" if remote
       model="llava:7b"         # change to "moondream:1.8b" or "granite3.2-vision:2b" for 8GB RAM
   )

   # Basic configuration
   llm.set_max_messages(20)
   llm.set_instructions(INSTRUCTIONS)
   llm.set_welcome(WELCOME)

   # Init camera
   camera = Picamera2()
   config = camera.create_still_configuration(
       main={"size": (1280, 720)},
   )
   camera.configure(config)
   camera.start()
   time.sleep(2)

   print(WELCOME)

   while True:
       input_text = input(">>> ")
       if input_text.strip().lower() in {"exit", "quit"}:
           break

       # Capture image
       img_path = "/tmp/llm-img.jpg"
       camera.capture_file(img_path)

       # Response with stream (text + image)
       response = llm.prompt(input_text, stream=True, image_path=img_path)
       for next_word in response:
           if next_word:
               print(next_word, end="", flush=True)
       print("")

Dépannage
---------------

* **J'obtiens une erreur du type : `model requires more system memory ...`.**

  * Cela signifie que le modèle est trop volumineux pour votre appareil.
  * Utilisez un modèle plus petit comme ``moondream:1.8b`` ou ``granite3.2-vision:2b``.
  * Ou passez à une machine avec plus de RAM et activez l'option **Expose to network** dans Ollama.

* **Le code ne peut pas se connecter à Ollama (connexion refusée).**

  Vérifiez les points suivants :

  * Assurez-vous qu'Ollama est en cours d'exécution (``ollama serve`` ou que l'application de bureau est ouverte).
  * Si vous utilisez un ordinateur distant, activez **Expose to network** dans les paramètres Ollama.
  * Vérifiez que l'adresse ``ip="..."`` dans votre code correspond bien à l'adresse IP LAN correcte.
  * Confirmez que les deux appareils sont sur le même réseau local.

* **Ma caméra Pi ne capture rien.**

  * Vérifiez que ``Picamera2`` est installé et fonctionne à l'aide d'un script de test simple.
  * Assurez-vous que le câble de la caméra est correctement connecté et activé dans ``raspi-config``.
  * Vérifiez que votre script a la permission d'écrire dans le chemin cible (``/tmp/llm-img.jpg``).

* **La sortie est trop lente.**

  * Les petits modèles répondent plus rapidement, mais avec des réponses plus simples.
  * Vous pouvez réduire la résolution de la caméra (par exemple 640×480 au lieu de 1280×720) pour accélérer le traitement d'image.
  * Fermez les autres programmes sur votre Pi pour libérer du CPU et de la RAM.
