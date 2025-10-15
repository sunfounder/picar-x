.. note::

    Bonjour et bienvenue dans la communauté des passionnés de SunFounder Raspberry Pi, Arduino et ESP32 sur Facebook ! Plongez au cœur des projets avec Raspberry Pi, Arduino et ESP32 aux côtés d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez les problèmes après-vente et surmontez les défis techniques avec l'aide de notre communauté et de notre équipe.
    - **Apprenez et partagez** : Échangez des conseils et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Accédez en avant-première aux annonces et aperçus de nouveaux produits.
    - **Réductions spéciales** : Bénéficiez de remises exclusives sur nos produits les plus récents.
    - **Promotions festives et concours** : Participez à des promotions et à des concours lors d'événements spéciaux.

    👉 Prêt à explorer et à créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !

.. _py_cliff:

5. Détection de Falaise 
===========================

Apprenons à PiCar-X un peu de conscience de protection pour qu'il utilise son module de niveaux de gris afin d'éviter de tomber d'une falaise.

Dans cet exemple, la voiture restera en mode veille.  
Si vous la poussez vers une falaise, elle se réveillera immédiatement et reculera.

**Exécution du Code**

.. raw:: html

    <run></run>

.. code-block::

    cd ~/picar-x/example
    sudo python3 5.cliff_detection.py
    
**Code**

.. note::
    Vous pouvez **Modifier/Réinitialiser/Copier/Exécuter/Arrêter** le code ci-dessous. Avant cela, vous devez vous rendre dans le répertoire du code source comme ``picar-x/example``. Après avoir modifié le code, vous pouvez l'exécuter directement pour voir l'effet.

.. raw:: html

    <run></run>

.. code-block:: python


    from picarx import Picarx
    from time import sleep

    px = Picarx()
    # px = Picarx(grayscale_pins=['A0', 'A1', 'A2'])
    # manual modify reference value
    px.set_cliff_reference([200, 200, 200])

    last_state = "safe"

    if __name__ == '__main__':
        try:
            while True:
                gm_val_list = px.get_grayscale_data()
                gm_state = px.get_cliff_status(gm_val_list)
                # print("cliff status is: %s" % gm_state)

                if gm_state is False:
                    state = "safe"
                    px.stop()
                else:
                    state = "danger"
                    px.backward(80)
                    if last_state == "safe":
                        sleep(0.1)

                last_state = state

        except KeyboardInterrupt:
            print("\nKeyboardInterrupt: stop and exit")

        finally:
            px.stop()
            sleep(0.1)

**Comment ça fonctionne ?** 

La fonction de détection de falaise fonctionne comme suit :



* ``get_grayscale_data()`` : Cette méthode renvoie directement les relevés des trois capteurs, de droite à gauche. Plus la zone est lumineuse, plus la valeur obtenue est grande.

* ``get_cliff_status(gm_val_list)`` : Cette méthode compare les relevés des trois sondes et donne un résultat. Si le résultat est vrai, une falaise est détectée devant la voiture.

