.. note::

    Bonjour, bienvenue dans la communauté des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder sur Facebook ! Plongez dans l'univers de Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des conseils et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et à des aperçus exclusifs.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos derniers produits.
    - **Promotions et cadeaux festifs** : Participez à des concours et à des promotions festives.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

Introduction 
====================


L'histoire des voitures autonomes
----------------------------------------

Des expériences sur les voitures autonomes sont menées depuis au moins les 
années 1920. Des essais prometteurs ont eu lieu dans les années 1950, et les 
travaux ont progressé depuis lors. Les premières voitures réellement autonomes 
sont apparues dans les années 1980, avec les projets Navlab et ALV de l'Université 
Carnegie Mellon en 1984, ainsi que le projet Eureka Prometheus de Mercedes-Benz et 
de l'Université de la Bundeswehr Munich en 1987. Depuis la fin des années 1980, de 
nombreuses organisations de recherche et grands constructeurs automobiles ont 
développé des véhicules autonomes fonctionnels, notamment : Mercedes-Benz, General 
Motors, Continental Automotive Systems, Autoliv Inc., Bosch, Nissan, Toyota, Audi, 
Volvo, Vislab de l'Université de Parme, l'Université d'Oxford et Google. En juillet 
2013, Vislab a démontré BRAiVE, un véhicule qui s'est déplacé de manière autonome 
sur une route ouverte au trafic mixte. En 2019, vingt-neuf États américains avaient 
déjà adopté des lois autorisant les voitures autonomes sur les routes publiques.

Certains membres de la CEE-ONU et de l'UE, dont le Royaume-Uni, ont mis en place 
des règles et des règlements relatifs aux voitures automatisées et entièrement 
automatisées. En Europe, des villes en Belgique, France, Italie et au Royaume-Uni 
prévoient de mettre en place des systèmes de transport pour voitures autonomes, 
tandis que l'Allemagne, les Pays-Bas et l'Espagne ont déjà autorisé les tests de 
voitures robotisées en circulation publique. En 2020, le Royaume-Uni, l'UE et le 
Japon étaient en bonne voie pour réglementer les voitures automatisées.

* Référence : `History of self-driving cars - Wikipedia <https://en.wikipedia.org/wiki/History_of_self-driving_carss>`_


Aujourd'hui, les voitures autonomes représentent la prochaine grande révolution technologique. Certains experts prédisent qu'à l'horizon 2025, les voitures de niveau 4 pourraient entrer sur le marché. Ces véhicules de niveau 4 permettront aux conducteurs de détourner leur attention de la conduite, rendant inutile la surveillance constante des conditions de circulation tant que le système fonctionne correctement.

Référence sur le niveau 4 :

* `SAE Levels of Driving Automation™  <https://www.sae.org/blog/sae-j3016-update>`_
* `ABI Research Forecasts 8 Million Vehicles to Ship with SAE Level 3, 4 and 5 Autonomous Technology in 2025 <https://www.abiresearch.com/press/abi-research-forecasts-8-million-vehicles-ship-sae-level-3-4-and-5-autonomous-technology-2025/>`_

.. image:: img/self_driving_car.jpeg

Les récentes avancées rapides dans les domaines des logiciels (intelligence artificielle, apprentissage automatique), du matériel (GPU, FPGA, accéléromètres, etc.) et du cloud computing accélèrent cette révolution technologique.

* En octobre 2010, un camion autonome conçu par l'entreprise italienne **Vislab** a mis trois mois pour `travel from Italy to China <http://edition.cnn.com/2010/TECH/innovation/10/27/driverless.car/>`_, soit un total de 13 000 kilomètres.
* En avril 2015, une voiture conçue par **Delphi Automotive** a voyagé de `San Francisco à New York <https://money.cnn.com/2015/04/03/autos/delphi-driverless-car-cross-country- trip/>`_, parcourant 5 470 kilomètres, dont 99 % sous contrôle informatique.
* En décembre 2018, **Waymo**, la filiale de **Alphabet**, a lancé un `level 4 self-driving taxi service in Arizona <https://www.reuters.com/article/us-waymo-selfdriving-focus/waymo-unveils-self- driving-taxi-service-in-arizona-for-paying-customers-idUSKBN1O41M2>`_, où ils testaient déjà des voitures autonomes depuis 2008. Les véhicules, sans conducteur, ont roulé plus d'une année et parcouru plus de 16 millions de kilomètres.
* En octobre 2020, **Baidu** a lancé son service `Apollo Robotaxi self-driving cab service <http://autonews.gasgoo.com/icv/70017615.html>`_  à Pékin. Les trajets couvrent les zones résidentielles, commerciales et industrielles, offrant un système de conduite entièrement autonome.

Cependant, malgré les énormes quantités de données recueillies quotidiennement, notamment des enregistrements de conduite réels et des scénarios simulés, la complexité des modèles d'IA pour les voitures autonomes n'a pas encore été entièrement maîtrisée.

Selon le `RAND's report <https://www.rand.org/pubs/research_reports/RR1478.html>`_, atteindre un niveau d'apprentissage autonome suffisant nécessite des données d'entraînement issues de centaines de millions, voire de milliards de kilomètres, pour garantir un niveau de fiabilité adéquat.

Ainsi, bien que l'avenir des voitures autonomes soit prometteur et excitant, il reste encore de nombreuses années de développement avant que la technologie ne soit suffisamment mature pour être accessible au grand public.

La manière la plus efficace de permettre à une technologie émergente de mûrir rapidement est de la rendre facilement accessible à tous, en minimisant les barrières à l'entrée sur le marché. C'est pourquoi SunFounder a lancé PiCar-X.

L'objectif de SunFounder est d'aider les débutants, les novices et ceux qui souhaitent simplement découvrir la conduite autonome à comprendre le processus de développement, la technologie et les innovations les plus récentes dans ce domaine.


À propos du PiCar-X
-----------------------

.. .. image:: img/picar-x.jpg

Le PiCar-X est une voiture robot autonome, contrôlée par IA, conçue pour la plateforme Raspberry Pi, où le Raspberry Pi sert de centre de contrôle. Le module caméra à deux axes, le module ultrason et les modules de suivi de ligne du PiCar-X permettent des fonctions telles que la détection de couleurs, de visages et de panneaux de signalisation, l'évitement automatique des obstacles et le suivi automatique de ligne.

Grâce à la carte Robot HAT conçue par SunFounder, le PiCar-X intègre des moteurs pour la conduite gauche/droite, des servomoteurs pour la direction et les mouvements de la caméra (panoramique/inclinaison), et préconfigure les broches ADC, PWM et Digital I2C du Robot HAT pour permettre des extensions à la fonctionnalité standard du Raspberry Pi. Un haut-parleur et une puce bluetooth ont également été intégrés dans le Robot HAT pour le contrôle à distance de la synthèse vocale, des effets sonores ou même des fonctionnalités de musique d'ambiance.

Toutes les fonctions du PiCar-X, y compris le contrôle GPIO, la vision par ordinateur et l'apprentissage profond, sont mises en œuvre grâce au langage de programmation Python open source, à la bibliothèque de vision par ordinateur OpenCV, ainsi qu'à TensorFlow de Google pour les frameworks d'apprentissage profond. D'autres logiciels sont inclus pour optimiser les capacités du PiCar-X, offrant à l'utilisateur un environnement d'apprentissage quasi illimité.


Apprentissage profond et réseaux neuronaux
-------------------------------------------------
Pour en savoir plus sur l'apprentissage profond et les réseaux neuronaux, SunFounder recommande les ressources suivantes :

`Machine Learning - Andrew Ng <https://www.coursera.org/learn/machine-learning>`_ : Ce cours propose une introduction large à l'apprentissage automatique, à l'exploration de données et à la reconnaissance des motifs statistiques.

`Neural Networks and Deep Learning <http://neuralnetworksanddeeplearning.com/>`_ : Ce livre numérique couvre les réseaux neuronaux, un paradigme de programmation inspiré de la biologie, permettant à un ordinateur d'apprendre à partir de données d'observation, ainsi que l'apprentissage profond, un ensemble puissant de techniques d'apprentissage automatique dans les réseaux neuronaux.

`Repenser l'architecture Inception pour la vision par ordinateur <https://arxiv.org/abs/1512.00567>`_ : Ce livre blanc explore des méthodes permettant d'augmenter l'efficacité des réseaux en optimisant les calculs grâce à des convolutions factorisées et à une régularisation agressive.
