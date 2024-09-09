.. note::

    Bonjour et bienvenue dans la communauté des passionnés de Raspberry Pi, Arduino et ESP32 de SunFounder sur Facebook ! Plongez dans l'univers du Raspberry Pi, d'Arduino et de l'ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et surmontez les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprenez & Partagez** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux avant-goûts.
    - **Réductions exclusives** : Profitez de remises spéciales sur nos nouveaux produits.
    - **Promotions festives et concours** : Participez à des concours et à des promotions lors des fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_avoid:

4. Évitement d'obstacles
=============================

Dans ce projet, le PiCar-X détectera les obstacles devant lui pendant qu'il avance, 
et lorsque les obstacles seront trop proches, il changera de direction pour continuer à avancer.

**Exécution du code**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 4.avoiding_obstacles.py
    
Après avoir exécuté le code, le PiCar-X avancera.

S'il détecte que la distance de l'obstacle devant est inférieure à 20 cm, il reculera.

Si un obstacle se trouve à une distance comprise entre 20 et 40 cm, il tournera à gauche.

S'il n'y a pas d'obstacle après avoir tourné à gauche ou si la distance de l'obstacle est supérieure à 25 cm, 
il continuera d'avancer.

**Code**

.. note::
    Vous pouvez **Modifier/Réinitialiser/Copier/Exécuter/Arrêter** le code ci-dessous. Mais avant cela, vous devez vous rendre dans le chemin du code source comme ``picar-x/example``. Après avoir modifié le code, vous pouvez l'exécuter directement pour voir l'effet.

.. raw:: html

    <run></run>

.. code-block:: python

    from picarx import Picarx
    import time
    
    POWER = 50
    SafeDistance = 40   # > 40 sûr
    DangerDistance = 20 # > 20 && < 40 tourner, 
                        # < 20 reculer
    
    def main():
        try:
            px = Picarx()
            # px = Picarx(ultrasonic_pins=['D2','D3']) # déclencheur, écho
           
            while True:
                distance = round(px.ultrasonic.read(), 2)
                print("distance: ",distance)
                if distance >= SafeDistance:
                    px.set_dir_servo_angle(0)
                    px.forward(POWER)
                elif distance >= DangerDistance:
                    px.set_dir_servo_angle(30)
                    px.forward(POWER)
                    time.sleep(0.1)
                else:
                    px.set_dir_servo_angle(-30)
                    px.backward(POWER)
                    time.sleep(0.5)
    
        finally:
            px.forward(0)
    
    
    if __name__ == "__main__":
        main()

**Comment ça marche ?**

* Importation du module Picarx et initialisation des constantes :

    Cette section du code importe la classe ``Picarx`` du module ``picarx``, qui est essentielle pour contrôler le robot Picarx. Les constantes comme ``POWER``, ``SafeDistance`` et ``DangerDistance`` sont définies et seront utilisées plus tard dans le script pour contrôler le mouvement du robot en fonction des mesures de distance.

    .. code-block:: python

        from picarx import Picarx
        import time

        POWER = 50
        SafeDistance = 40 # > 40 sûr
        DangerDistance = 20 # > 20 && < 40 tourner,
        # < 20 reculer

* Définition de la fonction principale et lecture du capteur ultrasonique :

    La fonction ``main`` contrôle le robot Picarx. Une instance de ``Picarx`` est créée, ce qui active les fonctionnalités du robot. Le code entre dans une boucle infinie, lisant constamment la distance depuis le capteur ultrasonique. Cette distance est utilisée pour déterminer les mouvements du robot.

    .. code-block:: python
        
        def main():
        try:
        px = Picarx()

            while True:
                distance = round(px.ultrasonic.read(), 2)
                # [Rest du code]

* Logique de mouvement basée sur la distance :

    Le mouvement du robot est contrôlé en fonction de la distance lue par le capteur ultrasonique. Si la ``distance`` est supérieure à ``SafeDistance``, le robot avance. Si la distance est comprise entre ``DangerDistance`` et ``SafeDistance``, il tourne légèrement et avance. Si la ``distance`` est inférieure à ``DangerDistance``, le robot recule tout en tournant dans la direction opposée.

    .. code-block:: python

        if distance >= SafeDistance:
            px.set_dir_servo_angle(0)
            px.forward(POWER)
        elif distance >= DangerDistance:
            px.set_dir_servo_angle(30)
            px.forward(POWER)
            time.sleep(0.1)
        else:
            px.set_dir_servo_angle(-30)
            px.backward(POWER)
            time.sleep(0.5)

* Sécurité et nettoyage avec le bloc 'finally' :

    Le bloc ``try...finally`` garantit la sécurité en arrêtant le mouvement du robot en cas d'interruption ou d'erreur. Cela est essentiel pour éviter tout comportement incontrôlable du robot.

    .. code-block:: python
        
        try:
        # [Logique de contrôle]
        finally:
        px.forward(0)

* Point d'entrée de l'exécution :

    Le point d'entrée standard en Python ``if __name__ == "__main__":`` est utilisé pour exécuter la fonction principale lorsque le script est lancé en tant que programme autonome.

    .. code-block:: python
        
        if name == "main":
            main()

En résumé, le script utilise le module Picarx pour contrôler un robot, en utilisant un capteur ultrasonique pour mesurer les distances. Le mouvement du robot est adapté en fonction de ces mesures, garantissant un fonctionnement sécurisé grâce à un contrôle minutieux et à un mécanisme de sécurité dans le bloc finally.

