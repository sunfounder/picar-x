.. note::

    Bonjour, bienvenue dans la communauté SunFounder Raspberry Pi & Arduino & ESP32 sur Facebook ! Plongez plus profondément dans l'univers du Raspberry Pi, Arduino et ESP32 avec d'autres passionnés.

    **Pourquoi nous rejoindre ?**

    - **Support d'experts** : Résolvez vos problèmes après-vente et défis techniques grâce à l'aide de notre communauté et de notre équipe.
    - **Apprendre et partager** : Échangez des astuces et des tutoriels pour améliorer vos compétences.
    - **Aperçus exclusifs** : Bénéficiez d'un accès anticipé aux annonces de nouveaux produits et avant-premières.
    - **Réductions exclusives** : Profitez de réductions exclusives sur nos nouveaux produits.
    - **Promotions festives et concours** : Participez à des concours et promotions lors des fêtes.

    👉 Prêt à explorer et créer avec nous ? Cliquez sur [|link_sf_facebook|] et rejoignez-nous dès aujourd'hui !


19. Chatbot Vocal Local
===========================

Dans cette leçon, vous combinerez tout ce que vous avez appris — **reconnaissance vocale (STT)**,
**synthèse vocale (TTS)** et un **LLM local (Ollama)** — pour créer un **chatbot vocal** entièrement hors ligne
qui s'exécute sur votre système PiCar-X.

Le flux de travail est simple :

#. **Écouter** — Le microphone capte votre voix et la transcrit avec **Vosk**.
#. **Penser** — Le texte est envoyé à un **LLM** local exécuté via Ollama (par ex., ``llama3.2:3b``).
#. **Parler** — Le chatbot répond à voix haute grâce à **Piper TTS**.

Cela crée un **robot conversationnel mains libres** capable de comprendre et de répondre en temps réel.

----

Avant de Commencer
------------------

Assurez-vous d'avoir préparé les éléments suivants :

* :ref:`install_all_modules` — Install ``robot-hat``, ``vilib``, ``picar-x`` modules, then run the script ``i2samp.sh``.
* Avoir testé **Piper TTS** (:ref:`test_piper`) et choisi un modèle de voix fonctionnel.
* Avoir testé **Vosk STT** (:ref:`test_vosk`) et choisi le bon pack de langue (par ex., ``en-us``).
* Avoir installé **Ollama** (:ref:`download_ollama`) sur votre Pi ou un autre ordinateur, et téléchargé un modèle tel que ``llama3.2:3b`` (ou un plus petit comme ``moondream:1.8b`` si la mémoire est limitée).

Exécuter le Code
------------------

#. Ouvrez le script d'exemple :

   .. code-block:: bash

      cd ~/picar-x/example
      sudo nano 19.local_voice_chatbot.py

#. Mettez à jour les paramètres selon vos besoins :

   * ``stt = Vosk(language="en-us")`` : Modifiez ceci pour correspondre à votre accent/pack de langue (par ex., ``en-us``, ``zh-cn``, ``es``).
   * ``tts.set_model("en_US-amy-low")`` : Remplacez par le modèle de voix Piper que vous avez validé dans :ref:`test_piper`.
   * ``llm = Ollama(ip="localhost", model="llama3.2:3b")`` : Adaptez ``ip`` et ``model`` à votre configuration.

     * ``ip`` : Si Ollama s'exécute sur le **même Pi**, utilisez ``localhost``. Si Ollama tourne sur un autre ordinateur de votre LAN, activez **Expose to network** dans Ollama et réglez ``ip`` sur l'adresse IP LAN de cet ordinateur.
     * ``model`` : Doit correspondre exactement au nom du modèle que vous avez téléchargé/activé dans Ollama.

#. Exécutez le script :

   .. code-block:: bash

      cd ~/picar-x/example
      sudo python3 19.local_voice_chatbot.py

#. Après lancement, vous devriez observer :

   * Le bot vous salue avec un message de bienvenue parlé.
   * Il attend une entrée vocale.
   * Vosk transcrit votre voix en texte.
   * Le texte est envoyé à Ollama, qui renvoie une réponse en streaming.
   * La réponse est nettoyée (suppression du raisonnement caché) puis prononcée par Piper.
   * Arrêtez le programme à tout moment avec ``Ctrl+C``.

----

Code
----

.. code-block:: python

   import re
   import time
   from picarx.llm import Ollama
   from picarx.stt import Vosk
   from picarx.tts import Piper

   # Initialize speech recognition
   stt = Vosk(language="en-us")

   # Initialize TTS
   tts = Piper()
   tts.set_model("en_US-amy-low")

   # Instructions for the LLM
   INSTRUCTIONS = (
       "You are a helpful assistant. Answer directly in plain English. "
       "Do NOT include any hidden thinking, analysis, or tags like <think>."
   )
   WELCOME = "Hello! I'm your voice chatbot. Speak when you're ready."

   # Initialize Ollama connection
   llm = Ollama(ip="localhost", model="llama3.2:3b")
   llm.set_max_messages(20)
   llm.set_instructions(INSTRUCTIONS)

   # Utility: clean hidden reasoning
   def strip_thinking(text: str) -> str:
       if not text:
           return ""
       text = re.sub(r"<\s*think[^>]*>.*?<\s*/\s*think\s*>", "", text, flags=re.DOTALL|re.IGNORECASE)
       text = re.sub(r"<\s*thinking[^>]*>.*?<\s*/\s*thinking\s*>", "", text, flags=re.DOTALL|re.IGNORECASE)
       text = re.sub(r"```(?:\s*thinking)?\s*.*?```", "", text, flags=re.DOTALL|re.IGNORECASE)
       text = re.sub(r"\[/?thinking\]", "", text, flags=re.IGNORECASE)
       return re.sub(r"\s+\n", "\n", text).strip()

   def main():
       print(WELCOME)
       tts.say(WELCOME)

       try:
           while True:
               print("\n🎤 Listening... (Press Ctrl+C to stop)")

               # Collect final transcript from Vosk
               text = ""
               for result in stt.listen(stream=True):
                   if result["done"]:
                       text = result["final"].strip()
                       print(f"[YOU] {text}")
                   else:
                       print(f"[YOU] {result['partial']}", end="\r", flush=True)

               if not text:
                   print("[INFO] Nothing recognized. Try again.")
                   time.sleep(0.1)
                   continue

               # Query Ollama with streaming
               reply_accum = ""
               response = llm.prompt(text, stream=True)
               for next_word in response:
                   if next_word:
                       print(next_word, end="", flush=True)
                       reply_accum += next_word
               print("")

               # Clean and speak
               clean = strip_thinking(reply_accum)
               if clean:
                   tts.say(clean)
               else:
                   tts.say("Sorry, I didn't catch that.")

               time.sleep(0.05)

       except KeyboardInterrupt:
           print("\n[INFO] Stopping...")
       finally:
           tts.say("Goodbye!")
           print("Bye.")

   if __name__ == "__main__":
       main()

----

Analyse du Code
---------------

**Imports et configuration globale**

.. code-block:: python

   import re
   import time
   from picarx.llm import Ollama
   from picarx.stt import Vosk
   from picarx.tts import Piper

Fait venir les trois sous-systèmes que vous avez construits plus tôt :
**Vosk** pour la reconnaissance vocale (STT), **Ollama** pour le LLM, et **Piper** pour la synthèse vocale (TTS).



**Initialiser la STT (Vosk)**

.. code-block:: python

   stt = Vosk(language="en-us")

Charge le modèle Vosk pour l'anglais américain.
Changez le code de langue (p. ex., ``zh-cn``, ``es``) pour correspondre à votre pack vocal afin d'améliorer la précision.



**Initialiser la TTS (Piper)**

.. code-block:: python

   tts = Piper()
   tts.set_model("en_US-amy-low")

Crée un moteur Piper et sélectionne une voix spécifique.
Choisissez un modèle que vous avez testé dans :ref:`test_piper`. Les voix de plus faible qualité sont plus rapides et utilisent moins de CPU.



**Instructions du LLM et phrase d'accueil**

.. code-block:: python

   INSTRUCTIONS = (
       "You are a helpful assistant. Answer directly in plain English. "
       "Do NOT include any hidden thinking, analysis, or tags like <think>."
   )
   WELCOME = "Hello! I'm your voice chatbot. Speak when you're ready."

Deux choix UX clés :

* Garder des **réponses courtes et directes** (cela aide à la clarté en TTS).
* Interdire explicitement les balises de "chaîne de pensée" cachée pour réduire le bruit dans les sorties.



**Connexion à Ollama et portée de conversation**

.. code-block:: python

   llm = Ollama(ip="localhost", model="llama3.2:3b")
   llm.set_max_messages(20)
   llm.set_instructions(INSTRUCTIONS)

* ``ip="localhost"`` suppose que le serveur Ollama s'exécute sur le même Pi. S'il tourne sur une autre machine du LAN, mettez l'**IP LAN** de cet ordinateur et activez *Expose to network* dans Ollama.
* ``set_max_messages(20)`` conserve un historique de conversation court. Diminuez-le si la mémoire/la latence est tendue.

**Supprimer le raisonnement caché / les balises avant de parler**

.. code-block:: python

   def strip_thinking(text: str) -> str:
       if not text:
           return ""
       text = re.sub(r"<\s*think[^>]*>.*?<\s*/\s*think\s*>", "", text, flags=re.DOTALL|re.IGNORECASE)
       text = re.sub(r"<\s*thinking[^>]*>.*?<\s*/\s*thinking\s*>", "", text, flags=re.DOTALL|re.IGNORECASE)
       text = re.sub(r"```(?:\s*thinking)?\s*.*?```", "", text, flags=re.DOTALL|re.IGNORECASE)
       text = re.sub(r"\[/?thinking\]", "", text, flags=re.IGNORECASE)
       return re.sub(r"\s+\n", "\n", text).strip()

Certains modèles peuvent émettre des balises de style interne (p. ex., ``<think>...``).
Cette fonction les supprime pour que votre TTS **ne prononce que** la réponse finale.

**Astuce :** Si vous voyez d'autres artefacts à l'écran (parce que vous streamez des tokens bruts), cette fonction garantit déjà que la sortie **parlée** reste propre.

**Boucle principale : saluer une fois, puis écouter → penser → parler**

.. code-block:: python

   print(WELCOME)
   tts.say(WELCOME)

Salue l'utilisateur via le terminal et le haut-parleur. Se produit une fois au démarrage.

**Écouter (STT en streaming avec partiels en direct)**

.. code-block:: python

   print("\n🎤 Listening... (Press Ctrl+C to stop)")

   text = ""
   for result in stt.listen(stream=True):
       if result["done"]:
           text = result["final"].strip()
           print(f"[YOU] {text}")
       else:
           print(f"[YOU] {result['partial']}", end="\r", flush=True)

* ``stream=True`` fournit des transcriptions **partielles** pour un retour immédiat et une transcription **finale** lorsque l'énoncé se termine.
* Le texte final reconnu est stocké dans ``text`` et affiché une fois.

**Garde-fou :** Si rien n'a été reconnu, vous passez l'appel au LLM :

.. code-block:: python

   if not text:
       print("[INFO] Nothing recognized. Try again.")
       time.sleep(0.1)
       continue

Cela évite d'envoyer des invites vides au modèle (économie de temps et de tokens).

**Penser (LLM) avec impression en streaming**

.. code-block:: python

   reply_accum = ""
   response = llm.prompt(text, stream=True)
   for next_word in response:
       if next_word:
           print(next_word, end="", flush=True)
           reply_accum += next_word
   print("")

* Envoie la transcription finale au LLM local et **affiche les tokens à l'arrivée** pour une faible latence.
* Pendant ce temps, vous accumulez la réponse complète dans ``reply_accum`` pour post-traitement.

**Remarque :** Si vous préférez **ne pas** afficher les tokens bruts, définissez ``stream=False`` et affichez simplement la chaîne finale.

**Parler (nettoyer d'abord, puis TTS en une seule fois)**

.. code-block:: python

   clean = strip_thinking(reply_accum)
   if clean:
       tts.say(clean)
   else:
       tts.say("Sorry, I didn't catch that.")

* Nettoie le texte final pour supprimer les balises cachées, puis **parle une seule fois**.
* Limiter la TTS à un seul passage évite les invites répétées comme "[LLM] / [SAY]".

**Sortie et arrêt**

.. code-block:: python

   except KeyboardInterrupt:
       print("\n[INFO] Stopping...")
   finally:
       tts.say("Goodbye!")
       print("Bye.")

Utilisez **Ctrl+C** pour arrêter. Le bot prononce un court au revoir pour signaler un arrêt propre.


----

Dépannage & FAQ
--------------------

* **Le modèle est trop volumineux (erreur mémoire)**

  Utilisez un modèle plus petit comme ``moondream:1.8b`` ou exécutez Ollama sur un ordinateur plus puissant.

* **Aucune réponse d'Ollama**

  Assurez-vous qu'Ollama est en cours d'exécution (``ollama serve`` ou application de bureau ouverte).
  Si Ollama est distant, activez **Expose to network** et vérifiez l'adresse IP.

* **Vosk ne reconnaît pas la parole**

  Vérifiez le bon fonctionnement de votre microphone. Essayez un autre pack de langue (``zh-cn``, ``es``, etc.) si nécessaire.

* **Piper est silencieux ou affiche des erreurs**

  Vérifiez que le modèle vocal choisi est bien téléchargé et testé dans :ref:`test_piper`.

* **Les réponses sont trop longues ou hors sujet**

  Modifiez ``INSTRUCTIONS`` et ajoutez : **« Keep answers short and to the point. »** (Gardez les réponses courtes et concises).
