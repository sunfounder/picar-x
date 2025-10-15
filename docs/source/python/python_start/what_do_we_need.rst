.. note::

    Bonjour et bienvenue dans la communauté Facebook des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder ! Plongez-vous dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et relevez les défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprenez & Partagez** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et à des avant-premières.
    - **Remises spéciales** : Profitez de réductions exclusives sur nos nouveaux produits.
    - **Promotions festives et concours** : Participez à des tirages au sort et à des promotions durant les fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

1. De Quoi Avez-Vous Besoin ?
=================================

Avant de commencer à jouer avec la **PiCar-X**, préparons le matériel essentiel.  
Pensez à ces composants comme au **cerveau**, au **cœur** et aux **sens** de la PiCar-X — sans eux, la voiture ne peut pas fonctionner correctement.

Composants Requis
-----------------------------

* **Raspberry Pi**

  Le Raspberry Pi agit comme le **cerveau** de la PiCar-X, en gérant tous les calculs, capteurs et commandes.

  .. image:: img/need_pi.jpg

  * **Modèles compatibles** : Raspberry Pi 5, 4, 3, et Raspberry Pi Zero 2 W (fonctionne mieux avec Pi 5 ou Pi 4).  
  * **Minimum** : **2 Go de RAM** — suffisant pour toutes les fonctions standard de la PiCar-X (mouvements, capteurs, streaming caméra) et pour utiliser des services d’IA en ligne tels que OpenAI Whisper, TTS ou LLMs.  
  * **Recommandé** : **4 Go de RAM ou plus** — assure de meilleures performances lors de l’exécution de modèles d’IA locaux (par ex. Vosk pour la reconnaissance vocale, Piper TTS ou de petits LLMs) en même temps que le streaming caméra et les commandes.

----

* **Adaptateur Secteur**

  La PiCar-X est livrée avec un pack de batteries **18650** et une carte **Robot HAT** avec un circuit de charge intégré.

  .. image:: img/need_power.png
    :width: 400

  * Pour la charge, il est recommandé d’utiliser une **alimentation 5V 3A**, telle que l’adaptateur USB-C officiel Raspberry Pi 15W.  
  * Vous pouvez également utiliser un chargeur USB-C **Power Delivery (PD)** ou **QC 2.0**.  
  * Une charge complète prend environ **2 heures** (de 0 % à 100 %).

----

* **Carte Micro SD**

  Le Raspberry Pi n’a pas de disque dur intégré. Il démarre et stocke tout sur une **carte Micro SD**.

  .. image:: img/need_sd.jpg
    :width: 200

  * Minimum : **16 Go**  
  * Recommandé : **32 Go** pour plus de stabilité  
  * Marque conseillée : **SanDisk** ou **Samsung** pour éviter les erreurs de lecture/écriture.

----

Composants Optionnels
-----------------------------

Bien qu’ils ne soient pas strictement nécessaires, les périphériques suivants améliorent considérablement l’expérience d’apprentissage et de débogage :

* **Moniteur (HDMI ou TV)**

  Idéal pour les débutants, un écran avec entrée HDMI facilite la configuration de Raspberry Pi OS et l’exécution de programmes graphiques.

  .. image:: img/need_screen.png
    :width: 400

* **Câble HDMI (Standard / Mini / Micro)**

  Les différents modèles de Raspberry Pi utilisent des connecteurs HDMI différents — vérifiez le vôtre avant achat.

  * **Raspberry Pi 4 / 5** : Micro HDMI  
  * **Raspberry Pi 3** : HDMI Standard  
  * **Raspberry Pi Zero 2W** : Mini HDMI

  .. image:: img/need_hdmi.png
    :width: 400

* **Clavier & Souris**

  Très utiles pour la configuration initiale de Raspberry Pi OS.  
  Par la suite, vous pourrez passer à un accès à distance (SSH / VNC), mais pour débuter un simple clavier USB ou sans fil est recommandé.

  .. image:: img/need_keyboard_mouse.png
    :width: 500

----

**Conseils de Préparation**

* Si vous avez acheté un **kit PiCar-X**, la plupart des accessoires sont inclus.  
  Mais vous devez préparer séparément la carte Raspberry Pi, la carte Micro SD et l’adaptateur secteur.  
* Pas sûr de quoi acheter ? 👉 Le choix le plus simple et fiable est :  
  **Raspberry Pi 4 (2 Go) + Alimentation officielle + Carte Micro SD 32 Go**.
