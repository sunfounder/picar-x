.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 sur Facebook ! Plongez plus profondément dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et avant-premières.
    - **Réductions exclusives** : Profitez de réductions exclusives sur nos nouveaux produits.
    - **Promotions festives et concours** : Participez à des concours et promotions lors des fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !


14. Voiture à Annonces Vocales avec Espeak et Pico2Wave
===============================================================

Dans cette leçon, nous allons utiliser deux moteurs de synthèse vocale (TTS) intégrés à Raspberry Pi — **Espeak** et **Pico2Wave** — pour faire parler la PiCar-X.

Ces deux moteurs sont simples et fonctionnent hors ligne, mais leurs voix sont très différentes :

* **Espeak** : très léger et rapide, mais la voix est robotique. Vous pouvez régler la vitesse, la hauteur, le volume, etc.
* **Pico2Wave** : produit une voix plus fluide et naturelle qu'Espeak, mais avec moins d'options de configuration.

Vous allez entendre la différence en termes de **qualité de voix** et de **fonctionnalités**, puis créer une « voiture à annonces vocales » qui annonce ses actions avant de bouger.

----

Avant de Commencer
-------------------

Assurez-vous d'avoir terminé :

* :ref:`install_all_modules` — Install ``robot-hat``, ``vilib``, ``picar-x`` modules, then run the script ``i2samp.sh``.

----

1. Tester Espeak
--------------------

Espeak est un moteur TTS léger inclus dans Raspberry Pi OS.
Sa voix est robotique mais hautement configurable : vous pouvez ajuster le volume, la vitesse, la hauteur, et plus encore.

**Étapes à suivre** :

* Créez un nouveau fichier avec la commande :

  .. code-block:: bash

      cd ~/picar-x/example
      sudo nano test_tts_espeak.py

* Copiez ensuite l'exemple de code ci-dessous. Appuyez sur ``Ctrl+X``, puis ``Y``, et enfin ``Entrée`` pour enregistrer et quitter.

  .. code-block:: python

      from picarx.tts import Espeak

      tts = Espeak()

      # Optional voice tuning
      # tts.set_amp(100)   # 0 to 200
      # tts.set_speed(150) # 80 to 260
      # tts.set_gap(5)     # 0 to 200
      # tts.set_pitch(50)  # 0 to 99

      # Quick hello (sanity check)
      tts.say("Hello! I'm Espeak TTS.")


* Exécutez le programme avec :

  .. code-block:: bash

     sudo python3 test_tts_espeak.py

* Vous devriez entendre la PiCar-X dire : "Hello! I'm Espeak TTS."
* Décommentez les lignes de réglage vocal dans le code pour expérimenter l'effet de ``amp``, ``speed``, ``gap`` et ``pitch`` sur la voix.

----

2. Tester Pico2Wave
---------------------

Pico2Wave produit une voix plus naturelle et humaine qu'Espeak.
Il est plus simple à utiliser mais moins flexible — vous ne pouvez changer que la langue, pas la hauteur ou la vitesse.

**Étapes à suivre** :

* Créez un nouveau fichier avec la commande :

  .. code-block:: bash

      cd ~/picar-x/example
      sudo nano test_tts_pico2wave.py

* Copiez ensuite l'exemple de code dans ce fichier. Appuyez sur ``Ctrl+X``, puis ``Y``, et enfin ``Entrée`` pour enregistrer et quitter.

  .. code-block:: python

      from picarx.tts import Pico2Wave

      tts = Pico2Wave()

      tts.set_lang('en-US')  # en-US, en-GB, de-DE, es-ES, fr-FR, it-IT

      # Quick hello (sanity check)
      tts.say("Hello! I'm Pico2Wave TTS.")

* Exécutez le programme avec :

  .. code-block::

    sudo python3 test_tts_pico2wave.py

* Vous devriez entendre la PiCar-X dire : "Hello! I'm Pico2Wave TTS."
* Essayez de changer la langue (par exemple, ``es-ES`` pour l'espagnol) et écoutez la différence.

----

3. Voiture à Annonces Vocales
-----------------------------------

Nous allons maintenant combiner **Pico2Wave** ou **Espeak** avec le code de conduite de la PiCar-X pour créer une « voiture à annonces vocales » :
avant chaque action, la voiture annoncera ce qu'elle est sur le point de faire.

**Exécuter le code**

.. code-block:: bash

    cd ~/picar-x/example
    sudo python3 14.voice_promt_car.py

Lorsque vous exécutez ce code, votre PiCar-X avancera, reculera et tournera, en annonçant chaque mouvement à l'avance.
Cela rend votre voiture plus sûre, plus conviviale et plus interactive.

**Code**

.. code-block:: python

  from picarx import Picarx
  from picarx.tts import Espeak
  import time

  # If you want to try Pico2Wave instead of Espeak, uncomment below:
  # from picarx.tts import Pico2Wave
  # tts = Pico2Wave()
  # tts.set_lang('en-US')  # Options: en-US, en-GB, de-DE, es-ES, fr-FR, it-IT

  px = Picarx()
  tts = Espeak()

  # Quick hello (test)
  tts.say("Hello! I'm PiCar-X.")

  def main():
      try:
          # Forward
          tts.say("Moving forward")
          px.forward(30)
          time.sleep(2)
          px.stop()

          # Backward
          tts.say("Moving backward")
          px.backward(30)
          time.sleep(2)
          px.stop()

          # Turn left
          tts.say("Turning left")
          px.set_dir_servo_angle(-20)
          px.forward(30)
          time.sleep(2)
          px.stop()
          px.set_dir_servo_angle(0)

          # Turn right
          tts.say("Turning right")
          px.set_dir_servo_angle(20)
          px.forward(30)
          time.sleep(2)
          px.stop()
          px.set_dir_servo_angle(0)

      except KeyboardInterrupt:
          # Stop if interrupted
          px.stop()
      finally:
          # Reset to safe state
          px.stop()
          px.set_dir_servo_angle(0)

  if __name__ == "__main__":
      main()

----


Dépannage
-------------------

* **Aucun son lors de l'exécution d'Espeak ou Pico2Wave**

  * Vérifiez que vos haut-parleurs/casque sont bien branchés et que le volume n'est pas coupé.
  * Faites un test rapide dans le terminal :

    .. code-block:: bash

       espeak "Hello world"
       pico2wave -w test.wav "Hello world" && aplay test.wav

  Si vous n'entendez rien, le problème vient de la sortie audio, pas de votre code Python.

* **La voix d'Espeak est trop rapide ou trop robotique**

  * Essayez d'ajuster les paramètres dans votre code :

    .. code-block:: python

       tts.set_speed(120)   # plus lent
       tts.set_pitch(60)    # hauteur différente

* **Permission refusée lors de l'exécution du code**

  * Essayez d'exécuter avec ``sudo`` :

    .. code-block:: bash

       sudo python3 test_tts_espeak.py


Comparaison : Espeak vs Pico2Wave
-------------------------------------

.. list-table::
   :widths: 20 40 40
   :header-rows: 1

   * - Fonctionnalité
     - Espeak
     - Pico2Wave
   * - Qualité de la voix
     - Robotique, synthétique
     - Plus naturelle, proche de la voix humaine
   * - Langues
     - Anglais par défaut
     - Moins nombreuses, mais les plus courantes
   * - Réglages possibles
     - Oui (vitesse, hauteur, etc.)
     - Non (langue uniquement)
   * - Performances
     - Très rapide, léger
     - Un peu plus lent, plus lourd
