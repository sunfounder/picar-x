.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 sur Facebook ! Plongez plus profondément dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et avant-premières.
    - **Réductions exclusives** : Profitez de réductions exclusives sur nos nouveaux produits.
    - **Promotions festives et concours** : Participez à des concours et promotions lors des fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !


16. Voiture Commandée par la Voix avec Vosk (Hors ligne)
==============================================================

Vosk est un moteur de reconnaissance vocale (STT) léger qui prend en charge de nombreuses langues et fonctionne entièrement **hors ligne** sur Raspberry Pi.  
Vous n’avez besoin d’une connexion Internet qu’une seule fois pour télécharger un modèle linguistique. Ensuite, tout fonctionne sans réseau.

Dans cette leçon, nous allons :

* Vérifier le fonctionnement du microphone sur le Raspberry Pi.  
* Installer et tester Vosk avec un modèle linguistique choisi.  
* Construire une **voiture PiCar-X commandée par la voix** qui écoute un mot déclencheur puis répond à des commandes telles que **forward**, **backward**, **left** et **right**.

----

Avant de Commencer
-------------------

Assurez-vous d’avoir terminé :

* :ref:`install_all_modules` — Installe les modules ``robot-hat``, ``vilib``, ``picar-x``, puis exécute le script ``i2samp.sh``.

----

1. Vérifier votre microphone
------------------------------------

Avant d’utiliser la reconnaissance vocale, assurez-vous que votre microphone USB fonctionne correctement.

#. Listez les périphériques d’enregistrement disponibles :

   .. code-block:: bash

      arecord -l

   Recherchez une ligne comme ``card 1: ... device 0``.

#. Enregistrez un court échantillon (remplacez ``1,0`` par les numéros trouvés) :

   .. code-block:: bash

      arecord -D plughw:1,0 -f S16_LE -r 16000 -d 3 test.wav

   * Exemple : si votre périphérique est ``card 2, device 0``, utilisez :

   .. code-block:: bash

      arecord -D plughw:2,0 -f S16_LE -r 16000 -d 3 test.wav

#. Lisez l’enregistrement pour le vérifier :

   .. code-block:: bash

      aplay test.wav

#. Ajustez le volume du microphone si nécessaire :

   .. code-block:: bash

      alsamixer

   * Appuyez sur **F6** pour sélectionner votre microphone USB.  
   * Trouvez le canal **Mic** ou **Capture**.  
   * Assurez-vous qu’il n’est pas en mode muet (**[MM]** signifie muet, appuyez sur ``M`` pour réactiver → cela doit afficher **[OO]**).  
   * Utilisez les flèches ↑ / ↓ pour modifier le volume d’enregistrement.


.. _test_vosk:

2. Tester Vosk
--------------------------

**Étapes pour l’essayer** :

#. Créez un nouveau fichier :

   .. code-block:: bash

      cd ~/picar-x/example
      sudo nano test_stt_vosk.py

#. Copiez l’exemple de code ci-dessous, puis enregistrez avec ``Ctrl+X``, ``Y`` et ``Entrée`` :

   .. code-block:: python

      from picarx.stt import Vosk

      vosk = Vosk(language="en-us")

      print(vosk.available_languages)

      while True:
          print("Say something")
          result = vosk.listen(stream=False)
          print(result)

#. Exécutez le programme :

   .. code-block:: bash

      sudo python3 test_stt_vosk.py

#. La première fois que vous exécutez ce code avec une nouvelle langue, Vosk va **télécharger automatiquement le modèle linguistique** (par défaut, la version « small »).  
   En même temps, il affichera la liste des langues prises en charge. Ensuite vous verrez :

   .. code-block:: text

        vosk-model-small-en-us-0.15.zip: 100%|███████████████████| 39.3M/39.3M [00:05<00:00, 7.85MB/s]
        ['ar', 'ar-tn', 'ca', 'cn', 'cs', 'de', 'en-gb', 'en-in', 'en-us', 'eo', 'es', 'fa', 'fr', 'gu', 'hi', 'it', 'ja', 'ko', 'kz', 'nl', 'pl', 'pt', 'ru', 'sv', 'te', 'tg', 'tr', 'ua', 'uz', 'vn']
        Say something

   Cela signifie :

   * Le fichier modèle (``vosk-model-small-en-us-0.15``) a été téléchargé.  
   * La liste des langues disponibles a été affichée.  
   * Le système écoute maintenant — parlez dans le microphone du PiCar-X, et le texte reconnu apparaîtra dans le terminal.

   **Conseils** :

   * Placez le micro à environ 15–30 cm de votre bouche.  
   * Choisissez un modèle qui correspond à votre langue et à votre accent.

**Mode Streaming (optionnel)**

Vous pouvez aussi utiliser le mode de streaming pour voir les résultats partiels pendant que vous parlez :

.. code-block:: python

   from picarx.stt import Vosk

   vosk = Vosk(language="en-us")

   while True:
       print("Say something")
       for result in vosk.listen(stream=True):
           if result["done"]:
               print(f"final:   {result['final']}")
           else:
               print(f"partial: {result['partial']}", end="\r", flush=True)


3. Voiture Commandée par la Voix
-------------------------------------

Nous allons maintenant connecter la reconnaissance vocale au PiCar-X !

Nous utiliserons un **mot déclencheur** (« hey robot ») afin que la voiture n’écoute les commandes qu’après activation.  
Cela économise des ressources CPU et évite les déclenchements accidentels.

**Exécuter le code**

.. code-block:: bash

   cd ~/picar-x/example
   sudo python3 16.voice_controlled_car.py

Dans ce programme, la voiture :

* Attend le mot déclencheur **« hey robot »**.  
* Ensuite, vous pouvez parler naturellement — tant que votre phrase contient un des mots-clés (**forward**, **backward**, **left**, **right**), la voiture réagit.  

  Par exemple :

  * « Can you move forward a little? » → la voiture avance.  
  * « Please turn left now. » → la voiture tourne à gauche.

* La commande **« sleep »** arrête la boucle de commande et remet la voiture en mode veille.

**Code**

.. code-block:: python

   from picarx import Picarx
   from picarx.stt import Vosk
   import time

   px = Picarx()
   stt = Vosk(language="en-us")

   WAKE_WORDS = ["hey robot"]

   print('Say "hey robot" to wake me up! Then say: forward / backward / left / right. Say "sleep" to stop listening.')

   try:
       while True:
           # --- wait for wake word once ---
           stt.wait_until_heard(WAKE_WORDS)
           print("Wake word detected. Listening for commands... (say 'sleep' to pause)")

           # --- command loop: multiple commands after one wake ---
           while True:
               res = stt.listen(stream=False)
               text = res.get("text", "") if isinstance(res, dict) else str(res)
               text = text.lower().strip()
               if not text:
                   continue

               print("Heard:", text)

               if "sleep" in text:
                   # pause command mode; go back to wait for wake word
                   px.stop(); px.set_dir_servo_angle(0)
                   print("Sleeping. Say 'hey robot' to wake me again.")
                   break

               elif "forward" in text:
                   px.set_dir_servo_angle(0)
                   px.forward(30); time.sleep(1); px.stop()

               elif "backward" in text:
                   px.set_dir_servo_angle(0)
                   px.backward(30); time.sleep(1); px.stop()

               elif "left" in text:
                   px.set_dir_servo_angle(-25)
                   px.forward(30); time.sleep(1)
                   px.stop(); px.set_dir_servo_angle(0)

               elif "right" in text:
                   px.set_dir_servo_angle(25)
                   px.forward(30); time.sleep(1)
                   px.stop(); px.set_dir_servo_angle(0)
               # (ignore other words)

   except KeyboardInterrupt:
       pass
   finally:
       px.stop(); px.set_dir_servo_angle(0)
       print("Stopped and centered. Bye.")

Dépannage
-----------------

* **No such file or directory (lors de l’exécution de `arecord`)**

  Vous avez peut-être utilisé un mauvais numéro de carte/périphérique.  
  Exécutez :

  .. code-block:: bash

     arecord -l

  puis remplacez ``1,0`` par les numéros indiqués pour votre microphone USB.

* **Le fichier enregistré est silencieux**

  Ouvrez le mixeur et vérifiez le volume du micro :

  .. code-block:: bash

     alsamixer

  * Appuyez sur **F6** pour sélectionner votre micro USB.  
  * Assurez-vous que **Mic/Capture** n’est pas en mode muet (**[OO]** au lieu de **[MM]**).  
  * Augmentez le niveau avec la flèche ↑.

* **Vosk ne reconnaît pas la parole**

  * Assurez-vous que le **code de langue** correspond au modèle (par ex. ``en-us`` pour l’anglais, ``zh-cn`` pour le chinois).  
  * Tenez le micro à 15–30 cm et évitez les bruits de fond.  
  * Parlez clairement et lentement.

* **Le mot déclencheur (“hey robot”) ne fonctionne pas**

  * Dites-le d’un ton naturel, pas trop vite.  
  * Vérifiez que le programme affiche bien le texte reconnu. Sinon, le microphone ne fonctionne probablement pas.

* **Latence élevée / reconnaissance lente**

  * Le téléchargement par défaut utilise un **petit modèle** (plus rapide, mais moins précis).  
  * Si c’est encore lent, fermez d’autres programmes pour libérer du CPU.
