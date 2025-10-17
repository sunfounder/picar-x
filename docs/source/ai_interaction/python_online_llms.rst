.. note::

    Ciao, benvenuto nella SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community su Facebook! Scopri di più su Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra comunità e del nostro team.
    - **Impara e Condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Accedi in anteprima agli annunci di nuovi prodotti e alle anticipazioni.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Giveaway Festivi**: Partecipa a giveaway e promozioni in occasione delle festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

.. _py_online_llm:

18. Connessione a LLM Online
=============================

In questa lezione impareremo come connettere il tuo PiCar-X (o Raspberry Pi) a diversi **modelli linguistici di grandi dimensioni online (LLM)**.  
Ogni fornitore richiede una chiave API e offre diversi modelli tra cui scegliere.  

Vedremo come:

* Creare e salvare le chiavi API in modo sicuro.  
* Scegliere un modello adatto alle tue esigenze.  
* Eseguire il nostro codice di esempio per chattare con i modelli.

Procediamo passo dopo passo per ogni fornitore.

----

OpenAI
----------

OpenAI fornisce potenti modelli come **GPT-4o** e **GPT-4.1** che possono essere utilizzati sia per attività di testo che di visione.

Ecco come configurarlo:

**Ottieni e salva la tua chiave API**

#. Vai su |link_openai_platform| ed effettua il login. Nella pagina **API keys**, clicca su **Create new secret key**.

   .. image:: img/llm_openai_create.png

#. Compila i dettagli (Proprietario, Nome, Progetto e permessi se necessari), quindi clicca su **Create secret key**.

   .. image:: img/llm_openai_create_confirm.png

#. Una volta creata la chiave, copiala subito — non potrai più visualizzarla. Se la perdi, dovrai generarne una nuova.

   .. image:: img/llm_openai_copy.png

#. Nella tua cartella di progetto (ad esempio: ``/picar-x/example``), crea un file chiamato ``secret.py``:

   .. code-block:: bash
   
       cd ~/picar-x/example
       sudo nano secret.py

#. Incolla la chiave nel file in questo modo:

   .. code-block:: python
   
       # secret.py
       # Store secrets here. Never commit this file to Git.
       OPENAI_API_KEY = "sk-xxx"

**Abilita la fatturazione e controlla i modelli**

#. Prima di usare la chiave, vai nella pagina **Billing** del tuo account OpenAI, aggiungi i dati di pagamento e ricarica un piccolo importo di crediti.

   .. image:: img/llm_openai_billing.png

#. Poi vai nella pagina **Limits** per controllare quali modelli sono disponibili per il tuo account e copia l'ID esatto del modello da usare nel codice.

   .. image:: img/llm_openai_models.png

**Test con codice di esempio**

#. Apri il nostro codice di esempio:

   .. code-block:: bash
   
       cd ~/picar-x/example
       sudo nano 18.online_llm_test.py

#. Sostituisci il contenuto con il codice seguente e aggiorna ``model="xxx"`` con il modello desiderato (ad esempio, ``gpt-4o``):

   .. code-block:: python
   
       from picarx.llm import OpenAI
       from secret import OPENAI_API_KEY
       
       INSTRUCTIONS = "You are a helpful assistant."
       WELCOME = "Hello, I am a helpful assistant. How can I help you?"
       
       llm = OpenAI(
           api_key=OPENAI_API_KEY,
           model="gpt-4o",
       )
  
   Salva ed esci (``Ctrl+X``, poi ``Y``, poi ``Enter``).

#. Infine, esegui il test:

   .. code-block:: bash
   
       sudo python3 18.online_llm_test.py
   

----

Gemini
------------------

Gemini è la famiglia di modelli AI di Google. È veloce e ideale per attività generiche.

**Ottieni e salva la tua chiave API**

#. Accedi a |link_google_ai|, quindi vai alla pagina API Keys.

   .. image:: img/llm_gemini_get.png

#. Clicca sul pulsante **Create API key** nell'angolo in alto a destra.

   .. image:: img/llm_gemini_create.png

#. Puoi creare una chiave per un progetto esistente o uno nuovo.

   .. image:: img/llm_gemini_choose.png

#. Copia la chiave API generata.

   .. image:: img/llm_gemini_copy.png

#. Nella tua cartella di progetto:

   .. code-block:: bash

       cd ~/picar-x/example
       sudo nano secret.py

#. Incolla la chiave:

   .. code-block:: python

        # secret.py
        # Store secrets here. Never commit this file to Git.
       GEMINI_API_KEY = "AIxxx"

**Controlla i modelli disponibili**

Vai alla pagina ufficiale |link_gemini_model|: qui vedrai l'elenco dei modelli, i relativi ID API esatti e per quali casi d'uso sono ottimizzati.

   .. image:: img/llm_gemini_model.png

**Test con codice di esempio**

#. Apri il file di test:

   .. code-block:: bash

       cd ~/picar-x/example
       sudo nano 18.online_llm_test.py

#. Sostituisci il contenuto con il codice seguente e aggiorna ``model="xxx"`` con il modello desiderato (ad esempio, ``gemini-2.5-flash``):

   .. code-block:: python

       from picarx.llm import Gemini
       from secret import GEMINI_API_KEY

       INSTRUCTIONS = "You are a helpful assistant."
       WELCOME = "Hello, I am a helpful assistant. How can I help you?"

       llm = Gemini(
           api_key=GEMINI_API_KEY,
           model="gemini-2.5-flash",
       )

#. Salva ed esegui:

   .. code-block:: bash

       sudo python3 18.online_llm_test.py

----

Qwen
------------------

Qwen è una famiglia di modelli linguistici di grandi dimensioni e multimodali fornita da Alibaba Cloud.  
Questi modelli supportano generazione di testo, ragionamento e comprensione multimodale (come l’analisi di immagini).

**Ottieni una chiave API**

Per utilizzare i modelli Qwen, hai bisogno di una **API Key**.  
La maggior parte degli utenti internazionali dovrebbe usare la console **DashScope International (Model Studio)**.  
Gli utenti nella Cina continentale possono invece utilizzare la console **Bailian (百炼)**.

* **Per utenti internazionali**

  #. Vai alla pagina ufficiale |link_qwen_inter| su **Alibaba Cloud**.  
  #. Accedi o crea un account **Alibaba Cloud**.  
  #. Vai su **Model Studio** (scegli la regione Singapore o Beijing).  
    
      * Se appare un messaggio “Activate Now” in alto, clicca per attivare Model Studio e ricevere la quota gratuita (solo Singapore).  
      * L’attivazione è gratuita — pagherai solo dopo aver consumato la quota gratuita.  
      * Se non appare alcun messaggio di attivazione, il servizio è già attivo.
  
  #. Vai nella pagina **Key Management**. Nella scheda **API Key**, clicca **Create API Key**.  
  #. Dopo la creazione, copia la tua API Key e conservala in un luogo sicuro.  
  
    .. image:: img/llm_qwen_api_key.png
        :width: 800
  
  .. note::
     Gli utenti di Hong Kong, Macao e Taiwan devono anch’essi scegliere l’opzione **International (Model Studio)**.
  
* **Per utenti della Cina continentale**

  Se ti trovi nella Cina continentale, puoi usare la console **Alibaba Cloud Bailian (百炼)**:
  
  #. Accedi a |link_aliyun| (console Bailian) e completa la verifica dell’account.  
  #. Seleziona **Create API Key**. Se appare un messaggio che indica che i servizi modello non sono attivati, clicca **Activate**, accetta i termini e richiedi la quota gratuita. Dopo l’attivazione, il pulsante **Create API Key** sarà abilitato.  
  
     .. image:: img/llm_qwen_aliyun_create.png
  
  #. Clicca nuovamente **Create API Key**, controlla l’account e clicca **Confirm**.  
  
     .. image:: img/llm_qwen_aliyun_confirm.png
  
  #. Una volta creata, copia la tua API Key.  
  
     .. image:: img/llm_qwen_aliyun_copy.png

**Salva la tua API Key**

#. Nella cartella del tuo progetto:

   .. code-block:: bash

       cd ~/picar-x/example
       sudo nano secret.py

#. Incolla la chiave così:

   .. code-block:: python

        # secret.py
        # Store secrets here. Never commit this file to Git.
        
        QWEN_API_KEY = "sk-xxx"

**Test con codice di esempio**

#. Apri il file di test:

   .. code-block:: bash

       cd ~/picar-x/example
       sudo nano 18.online_llm_test.py
       
#. Sostituisci il contenuto con il codice qui sotto e aggiorna ``model="xxx"`` con il modello desiderato (ad esempio, ``qwen-plus``):

   .. code-block:: python
   
      from picarx.llm import Qwen
      from secret import QWEN_API_KEY

      INSTRUCTIONS = "You are a helpful assistant."
      WELCOME = "Hello, I am a helpful assistant. How can I help you?"

      llm = Qwen(
          api_key=QWEN_API_KEY,
          model="qwen-plus",
      )


#. Esegui con:

   .. code-block:: bash
   
       sudo python3 18.online_llm_test.py

----

Grok (xAI)
------------------
Grok è l’IA conversazionale di xAI, creata dal team di Elon Musk. Puoi connetterti ad essa tramite l’API xAI.

**Ottieni e salva la tua chiave API**

#. Registrati qui: |link_grok_ai|. Aggiungi prima dei crediti al tuo account — altrimenti l’API non funzionerà.

#. Vai nella pagina API Keys, clicca su **Create API key**.  

   .. image:: img/llm_grok_create.png

#. Inserisci un nome per la chiave, poi clicca **Create API key**. 

   .. image:: img/llm_grok_name.png

#. Copia la chiave generata e conservala in un luogo sicuro. 

   .. image:: img/llm_grok_copy.png

#. Nella cartella del tuo progetto:

   .. code-block:: bash

       cd ~/picar-x/example
       sudo nano secret.py

#. Incolla la chiave così:

   .. code-block:: python

        # secret.py
        # Store secrets here. Never commit this file to Git.
        
        GROK_API_KEY = "xai-xxx"

**Controlla i modelli disponibili**

Vai alla pagina Models nella console xAI. Qui puoi vedere tutti i modelli disponibili per il tuo team, insieme ai relativi ID API esatti — usa questi ID nel tuo codice.

   .. image:: img/llm_grok_model.png

**Test con codice di esempio**

#. Apri il file di test:

   .. code-block:: bash

       cd ~/picar-x/example
       sudo nano 18.online_llm_test.py
       
#. Sostituisci il contenuto con il codice qui sotto e aggiorna ``model="xxx"`` con il modello desiderato (ad esempio, ``grok-4-latest``):

   .. code-block:: python
   
       from picarx.llm import Grok
       from secret import GROK_API_KEY
   
       INSTRUCTIONS = "You are a helpful assistant."
       WELCOME = "Hello, I am a helpful assistant. How can I help you?"
   
       llm = Grok(
           api_key=GROK_API_KEY,
           model="grok-4-latest",
       )

#. Esegui con:

   .. code-block:: bash
   
       sudo python3 18.online_llm_test.py

----

DeepSeek
------------------

DeepSeek è un provider cinese di LLM che offre modelli potenti e a prezzi accessibili.

**Ottieni e salva la tua chiave API**

#. Accedi a |link_deepseek|. 

#. Nel menu in alto a destra, seleziona **API Keys → Create API Key**. 

   .. image:: img/llm_deepseek_create.png

#. Inserisci un nome, clicca su **Create**, poi copia la chiave.

   .. image:: img/llm_deepseek_copy.png

#. Nella tua cartella di progetto:

   .. code-block:: bash

       cd ~/picar-x/example
       sudo nano secret.py

#. Aggiungi la tua chiave:

   .. code-block:: python

       # secret.py
       DEEPSEEK_API_KEY = "sk-xxx"

**Abilita la fatturazione**

Dovrai ricaricare il tuo account. Inizia con un piccolo importo (ad esempio ¥10 RMB). 

   .. image:: img/llm_deepseek_chognzhi.png

**Modelli disponibili**

Alla data di stesura (2025-09-12), DeepSeek offre:  

* ``deepseek-chat``  
* ``deepseek-reasoner``  

**Test con codice di esempio**

#. Apri il file di test:

   .. code-block:: bash

       cd ~/picar-x/example
       sudo nano 18.online_llm_test.py
       
#. Sostituisci il contenuto con il codice seguente e aggiorna ``model="xxx"`` con il modello desiderato (ad esempio, ``deepseek-chat``):

   .. code-block:: python
   
       from picarx.llm import Deepseek
       from secret import DEEPSEEK_API_KEY
   
       INSTRUCTIONS = "You are a helpful assistant."
       WELCOME = "Hello, I am a helpful assistant. How can I help you?"
   
       llm = Deepseek(
           api_key=DEEPSEEK_API_KEY,
           model="deepseek-chat",
           max_messages=20,
       )

#. Esegui:

   .. code-block:: bash
   
       sudo python3 18.online_llm_test.py

----

Doubao
------------------
Doubao è la piattaforma di modelli AI di ByteDance (Volcengine Ark).

**Ottieni e salva la tua chiave API**

#. Accedi a |link_doubao|.

#. Nel menu a sinistra, scorri fino a **API Key Management → Create API Key**. 

   .. image:: img/llm_doubao_create.png

#. Scegli un nome e clicca su **Create**.  

   .. image:: img/llm_doubao_name.png

#. Clicca sull’icona **Show API Key** e copia la chiave. 

   .. image:: img/llm_doubao_copy.png

#. Nella tua cartella di progetto:

   .. code-block:: bash

       cd ~/picar-x/example
       sudo nano secret.py

#. Aggiungi la tua chiave:

   .. code-block:: python

       # secret.py
       DOUBAO_API_KEY = "xxx"

**Scegli un modello**

#. Vai al marketplace dei modelli e scegli un modello.  

   .. image:: img/llm_doubao_model_select.png

#. Ad esempio, scegli **Doubao-seed-1.6**, poi clicca **API 接入**. 

   .. image:: img/llm_doubao_model.png

#. Seleziona la tua API Key e clicca **Use API**. 

   .. image:: img/llm_doubao_use_api.png

#. Clicca su **Enable Model**. 

   .. image:: img/llm_doubao_kaitong.png

#. Passa con il mouse sopra l’ID del modello per copiarlo. 

   .. image:: img/llm_doubao_copy_id.png

**Test con codice di esempio**

#. Apri il file di test:

   .. code-block:: bash

       cd ~/picar-x/example
       sudo nano 18.online_llm_test.py
       
#. Sostituisci il contenuto con il codice seguente e aggiorna ``model="xxx"`` con il modello desiderato (ad esempio, ``doubao-seed-1-6-250615``):

   .. code-block:: python
   
       from picarx.llm import Doubao
       from secret import DOUBAO_API_KEY
   
       INSTRUCTIONS = "You are a helpful assistant."
       WELCOME = "Hello, I am a helpful assistant. How can I help you?"
   
       llm = Doubao(
           api_key=DOUBAO_API_KEY,
           model="doubao-seed-1-6-250615",
       )

#. Esegui con:

   .. code-block:: bash
   
       sudo python3 18.online_llm_test.py

----

General
--------------

Questo progetto supporta la connessione a più piattaforme LLM tramite un’interfaccia unificata.  
Abbiamo una compatibilità integrata con:

* **OpenAI** (ChatGPT / GPT-4o, GPT-4, GPT-3.5)  
* **Gemini** (Google AI Studio / Vertex AI)  
* **Grok** (xAI)  
* **DeepSeek**  
* **Qwen (通义千问)**  
* **Doubao (豆包)**  

Inoltre, puoi connetterti a **qualsiasi altro servizio LLM compatibile con il formato dell’API di OpenAI**.  
Per queste piattaforme, dovrai ottenere manualmente la tua **API Key** e la corretta **base_url**.

**Ottieni e salva la tua chiave API**

#. Ottieni una **API Key** dalla piattaforma che desideri utilizzare. (Consulta la console ufficiale di ogni piattaforma per i dettagli.)  

#. Nella cartella del tuo progetto, crea un nuovo file:

   .. code-block:: bash

      cd ~/picar-x/example
      nano secret.py

#. Aggiungi la tua chiave in ``secret.py``:

   .. code-block:: python

      # secret.py
      API_KEY = "your_api_key_here"

.. warning::

   Mantieni la tua API Key privata. Non caricare ``secret.py`` in repository pubblici.

**Test con codice di esempio**

#. Apri il file di test:

   .. code-block:: bash

       cd ~/picar-x/example
       sudo nano 18.online_llm_test.py
       
#. Sostituisci il contenuto di un file Python con il seguente esempio e inserisci la corretta ``base_url`` e ``model`` per la tua piattaforma:

   .. note::

      Informazioni su ``base_url``:  
      Supportiamo il **formato API di OpenAI**, oltre a qualsiasi API **compatibile**.  
      Ogni fornitore ha la propria ``base_url``. Controlla la loro documentazione.  

   .. code-block:: python

      from picarx.llm import LLM
      from secret import API_KEY

      INSTRUCTIONS = "You are a helpful assistant."
      WELCOME = "Hello, I am a helpful assistant. How can I help you?"

      llm = LLM(
          base_url="https://api.example.com/v1",  # inserisci la base_url del tuo fornitore
          api_key=API_KEY,
          model="your-model-name-here",           # scegli un modello dal tuo fornitore
      )

#. Esegui il programma:

   .. code-block:: bash

      python3 18.online_llm_test.py

      python3 18.online_llm_test.py
