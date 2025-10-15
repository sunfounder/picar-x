.. note::

    Bonjour, bienvenue dans la communauté SunFounder pour les passionnés de Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez plus profondément dans l'univers du Raspberry Pi, d'Arduino et de l'ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et relevez les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprendre & Partager** : Échangez des conseils et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces de nouveaux produits et aux avant-premières.
    - **Réductions spéciales** : Profitez de réductions exclusives sur nos derniers produits.
    - **Promotions festives et concours** : Participez à des concours et des promotions spéciales lors des fêtes.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_line_tracking:

6. Suivi de ligne
====================================

Dans ce projet, nous allons utiliser le module de détection de niveaux de 
gris pour faire avancer le PiCar-X le long d'une ligne. Utilisez un ruban adhésif de couleur sombre pour tracer une ligne aussi droite que possible, et évitez les courbes trop prononcées. Quelques ajustements peuvent être nécessaires si le PiCar-X déraille.

**Exécuter le code**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 6.line_tracking.py
    
Après avoir exécuté le code, le PiCar-X se déplacera le long de la ligne.

**Code**

.. note::
    Vous pouvez **Modifier/Réinitialiser/Copier/Exécuter/Arrêter** le code ci-dessous. Mais avant cela, vous devez aller dans le chemin du code source, comme ``picar-x/example``. Après avoir modifié le code, vous pouvez l'exécuter directement pour voir le résultat.

.. raw:: html

    <run></run>

.. code-block:: python

    from picarx import Picarx
    from time import sleep

    px = Picarx()
    # px = Picarx(grayscale_pins=['A0', 'A1', 'A2'])

    # Veuillez exécuter ./calibration/grayscale_calibration.py pour calibrer automatiquement les valeurs de niveaux de gris
    # ou modifiez manuellement la valeur de référence avec le code suivant
    # px.set_line_reference([1400, 1400, 1400])

    current_state = None
    px_power = 10
    offset = 20
    last_state = "stop"

    def outHandle():
        global last_state, current_state
        if last_state == 'left':
            px.set_dir_servo_angle(-30)
            px.backward(10)
        elif last_state == 'right':
            px.set_dir_servo_angle(30)
            px.backward(10)
        while True:
            gm_val_list = px.get_grayscale_data()
            gm_state = get_status(gm_val_list)
            print("outHandle gm_val_list: %s, %s"%(gm_val_list, gm_state))
            currentSta = gm_state
            if currentSta != last_state:
                break
        sleep(0.001)

    def get_status(val_list):
        _state = px.get_line_status(val_list)  # [bool, bool, bool], 0 means line, 1 means background
        if _state == [0, 0, 0]:
            return 'stop'
        elif _state[1] == 1:
            return 'forward'
        elif _state[0] == 1:
            return 'right'
        elif _state[2] == 1:
            return 'left'

    if __name__=='__main__':
        try:
            while True:
                gm_val_list = px.get_grayscale_data()
                gm_state = get_status(gm_val_list)
                print("gm_val_list: %s, %s"%(gm_val_list, gm_state))

                if gm_state != "stop":
                    last_state = gm_state

                if gm_state == 'forward':
                    px.set_dir_servo_angle(0)
                    px.forward(px_power) 
                elif gm_state == 'left':
                    px.set_dir_servo_angle(offset)
                    px.forward(px_power) 
                elif gm_state == 'right':
                    px.set_dir_servo_angle(-offset)
                    px.forward(px_power) 
                else:
                    outHandle()

        except KeyboardInterrupt:
            print("\nKeyboardInterrupt: stop and exit")
            
        finally:
            px.stop()
            print("stop and exit")
            sleep(0.1)
       

**Comment ça fonctionne ?**

Ce script Python contrôle une voiture robot PiCarx en utilisant des capteurs de niveaux de gris pour la navigation. Voici une explication de ses principales composantes :

* Importation et initialisation :

    Le script importe la classe Picarx pour contrôler la voiture robot et la fonction sleep du module time pour ajouter des délais.

    Une instance de Picarx est créée, avec une ligne commentée montrant une autre initialisation avec des broches de capteurs de niveaux de gris spécifiques.

    .. code-block:: python
        
        from picarx import Picarx
        from time import sleep

        px = Picarx()

* Configuration et variables globales :

    ``current_state``, ``px_power``, ``offset``, et ``last_state`` sont des variables globales utilisées pour suivre et contrôler les mouvements de la voiture. ``px_power`` définit la puissance du moteur, et ``offset`` est utilisé pour ajuster l'angle de direction.

    .. code-block:: python

        current_state = None
        px_power = 10
        offset = 20
        last_state = "stop"

* Fonction ``outHandle`` :

    Cette fonction est appelée lorsque la voiture doit gérer un scénario de "sortie de ligne".

    Elle ajuste la direction de la voiture en fonction de ``last_state`` et vérifie les valeurs des capteurs de niveaux de gris pour déterminer le nouvel état.

    .. code-block:: python

        def outHandle():
            global last_state, current_state
            if last_state == 'left':
                px.set_dir_servo_angle(-30)
                px.backward(10)
            elif last_state == 'right':
                px.set_dir_servo_angle(30)
                px.backward(10)
            while True:
                gm_val_list = px.get_grayscale_data()
                gm_state = get_status(gm_val_list)
                print("outHandle gm_val_list: %s, %s"%(gm_val_list, gm_state))
                currentSta = gm_state
                if currentSta != last_state:
                    break
            sleep(0.001)

* Fonction ``get_status`` :

    Cette fonction interprète les données du capteur de niveaux de gris (``val_list``) pour déterminer l'état de navigation de la voiture.

    L'état de la voiture peut être "forward", "left", "right" ou "stop", selon le capteur qui détecte la ligne.

    .. code-block:: python
        
        def get_status(val_list):
            _state = px.get_line_status(val_list)  # [bool, bool, bool], 0 means line, 1 means background
            if _state == [0, 0, 0]:
                return 'stop'
            elif _state[1] == 1:
                return 'forward'
            elif _state[0] == 1:
                return 'right'
            elif _state[2] == 1:
                return 'left'

* Boucle principale :

    La boucle ``while True`` vérifie continuellement les données des capteurs de niveaux de gris et ajuste les mouvements de la voiture en conséquence.

    En fonction de l'état ``gm_state``, elle définit l'angle de direction et la direction du mouvement.

    .. code-block:: python

        if __name__=='__main__':
            try:
                while True:
                    gm_val_list = px.get_grayscale_data()
                    gm_state = get_status(gm_val_list)
                    print("gm_val_list: %s, %s"%(gm_val_list, gm_state))

                    if gm_state != "stop":
                        last_state = gm_state

                    if gm_state == 'forward':
                        px.set_dir_servo_angle(0)
                        px.forward(px_power) 
                    elif gm_state == 'left':
                        px.set_dir_servo_angle(offset)
                        px.forward(px_power) 
                    elif gm_state == 'right':
                        px.set_dir_servo_angle(-offset)
                        px.forward(px_power) 
                    else:
                        outHandle()

* Sécurité et nettoyage :

    Le bloc ``try...finally`` garantit que la voiture s'arrête lorsque le script est interrompu ou terminé.

    .. code-block:: python
        
        finally:
        px.stop()
        print("stop and exit")
        sleep(0.1)

En résumé, le script utilise des capteurs de niveaux de gris pour naviguer avec la voiture robot PiCarx. Il lit continuellement les données des capteurs pour déterminer la direction et ajuste les mouvements et la direction de la voiture en conséquence. La fonction outHandle fournit une logique supplémentaire pour les situations où la voiture doit ajuster son chemin de manière significative.
