.. note::

    Hola, ¡bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook! Sumérgete en el mundo de Raspberry Pi, Arduino y ESP32 con otros entusiastas.

    **¿Por qué unirte?**

    - **Soporte de expertos**: Resuelve problemas post-venta y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Obtén acceso anticipado a nuevos anuncios de productos y avances exclusivos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

.. _py_online_llm:

18. Conectarse a LLMs en Línea
================================

En esta lección, aprenderemos cómo conectar tu PiCar-X (o Raspberry Pi) a diferentes **Modelos de Lenguaje Grandes en línea (LLMs)**.  
Cada proveedor requiere una clave API y ofrece diferentes modelos que puedes elegir.  

Veremos cómo:

* Crear y guardar tus claves API de forma segura.  
* Elegir un modelo que se adapte a tus necesidades.  
* Ejecutar nuestro código de ejemplo para chatear con los modelos.

Vamos paso a paso con cada proveedor.

----

OpenAI
----------

OpenAI ofrece modelos potentes como **GPT-4o** y **GPT-4.1** que pueden usarse tanto para tareas de texto como de visión.  

Aquí te mostramos cómo configurarlo:

**Obtener y guardar tu clave API**

#. Ve a |link_openai_platform| e inicia sesión. En la página de **API keys**, haz clic en **Create new secret key**.

   .. image:: img/llm_openai_create.png

#. Rellena los detalles (Owner, Name, Project y permisos si es necesario), luego haz clic en **Create secret key**.

   .. image:: img/llm_openai_create_confirm.png

#. Una vez creada la clave, cópiala de inmediato — no podrás verla de nuevo. Si la pierdes, deberás generar una nueva.

   .. image:: img/llm_openai_copy.png

#. En tu carpeta del proyecto (por ejemplo: ``/picar-x/example``), crea un archivo llamado ``secret.py``:

   .. code-block:: bash
   
       cd ~/picar-x/example
       sudo nano secret.py

#. Pega tu clave en el archivo de esta manera:

   .. code-block:: python
   
       # secret.py
       # Guarda los secretos aquí. Nunca subas este archivo a Git.
       OPENAI_API_KEY = "sk-xxx"

**Habilitar facturación y verificar modelos**

#. Antes de usar la clave, ve a la página de **Billing** en tu cuenta de OpenAI, agrega tus detalles de pago y recarga una pequeña cantidad de créditos.  

   .. image:: img/llm_openai_billing.png

#. Luego ve a la página de **Limits** para verificar qué modelos están disponibles para tu cuenta y copia el ID exacto del modelo que usarás en tu código.  

   .. image:: img/llm_openai_models.png

**Probar con código de ejemplo**

#. Abre nuestro código de ejemplo:

   .. code-block:: bash
   
       cd ~/picar-x/example
       sudo nano 18.online_llm_test.py

#. Reemplaza el contenido con el código siguiente y actualiza ``model="xxx"`` con el modelo que quieras (por ejemplo, ``gpt-4o``):

   .. code-block:: python
   
       from picarx.llm import OpenAI
       from secret import OPENAI_API_KEY
       
       INSTRUCTIONS = "You are a helpful assistant."
       WELCOME = "Hello, I am a helpful assistant. How can I help you?"
       
       llm = OpenAI(
           api_key=OPENAI_API_KEY,
           model="gpt-4o",
       )
  
   Guarda y sal (``Ctrl+X``, luego ``Y``, luego ``Enter``).  

#. Finalmente, ejecuta la prueba:

   .. code-block:: bash
   
       sudo python3 18.online_llm_test.py


----

Gemini
------------------

Gemini es la familia de modelos de IA de Google. Es rápido y excelente para tareas de propósito general.  

**Obtener y guardar tu clave API**

#. Inicia sesión en |link_google_ai|, luego ve a la página de API Keys.

   .. image:: img/llm_gemini_get.png

#. Haz clic en el botón **Create API key** en la esquina superior derecha.

   .. image:: img/llm_gemini_create.png

#. Puedes crear una clave para un proyecto existente o uno nuevo.

   .. image:: img/llm_gemini_choose.png

#. Copia la clave API generada.

   .. image:: img/llm_gemini_copy.png

#. En tu carpeta de proyecto:

   .. code-block:: bash

       cd ~/picar-x/example
       sudo nano secret.py

#. Pega la clave:

   .. code-block:: python

        # secret.py
        # Guarda los secretos aquí. Nunca subas este archivo a Git.
       GEMINI_API_KEY = "AIxxx"

**Verificar modelos disponibles**

Ve a la página oficial |link_gemini_model|, allí verás la lista de modelos, sus IDs exactos de API y para qué caso de uso está optimizado cada uno.

   .. image:: img/llm_gemini_model.png

**Probar con código de ejemplo**

#. Abre el archivo de prueba:

   .. code-block:: bash

       cd ~/picar-x/example
       sudo nano 18.online_llm_test.py

#. Reemplaza el contenido con el código a continuación y actualiza ``model="xxx"`` con el modelo que desees (por ejemplo, ``gemini-2.5-flash``):

   .. code-block:: python

       from picarx.llm import Gemini
       from secret import GEMINI_API_KEY

       INSTRUCTIONS = "You are a helpful assistant."
       WELCOME = "Hello, I am a helpful assistant. How can I help you?"

       llm = Gemini(
           api_key=GEMINI_API_KEY,
           model="gemini-2.5-flash",
       )

#. Guarda y ejecuta:

   .. code-block:: bash

       sudo python3 18.online_llm_test.py

----

Qwen
------------------

Qwen es una familia de modelos grandes de lenguaje y multimodales proporcionados por Alibaba Cloud.  
Estos modelos admiten generación de texto, razonamiento y comprensión multimodal (como análisis de imágenes).

**Obtener una clave API**

Para usar los modelos Qwen, necesitas una **clave API**.  
La mayoría de los usuarios internacionales deben usar la consola **DashScope International (Model Studio)**.  
Los usuarios en China continental pueden usar la consola **Bailian (百炼)**.

* **Para usuarios internacionales**

  #. Ve a la página oficial |link_qwen_inter| en **Alibaba Cloud**.  
  #. Inicia sesión o crea una cuenta en **Alibaba Cloud**.  
  #. Navega a **Model Studio** (elige región de Singapur o Beijing).  
    
      * Si aparece un mensaje “Activate Now” en la parte superior, haz clic para activar Model Studio y obtener la cuota gratuita (solo Singapur).  
      * La activación es gratuita — solo se te cobrará cuando uses toda la cuota gratuita.  
      * Si no aparece el mensaje de activación, el servicio ya está activo. 
   
  #. Ve a la página **Key Management**. En la pestaña **API Key**, haz clic en **Create API Key**.  
  #. Después de crearla, copia tu clave API y guárdala de forma segura.  
  
    .. image:: img/llm_qwen_api_key.png
        :width: 800
  
  .. note::
     Los usuarios en Hong Kong, Macao y Taiwán también deben elegir la opción **International (Model Studio)**.
  
* **Para usuarios en China continental**

  Si estás en China continental, puedes usar la consola **Alibaba Cloud Bailian (百炼)**:

  #. Inicia sesión en |link_aliyun| (consola Bailian) y completa la verificación de cuenta.  
  #. Selecciona **Create API Key**. Si aparece un aviso de que los servicios de modelo no están activados, haz clic en **Activate**, acepta los términos y reclama tu cuota gratuita. Después de la activación, el botón **Create API Key** estará habilitado.  
  
     .. image:: img/llm_qwen_aliyun_create.png
  
  #. Haz clic en **Create API Key** nuevamente, verifica tu cuenta y luego haz clic en **Confirm**.  
  
     .. image:: img/llm_qwen_aliyun_confirm.png
  
  #. Una vez creada, copia tu clave API.  
  
     .. image:: img/llm_qwen_aliyun_copy.png

**Guardar tu clave API**

#. En tu carpeta de proyecto:

   .. code-block:: bash

       cd ~/picar-x/example
       sudo nano secret.py

#. Pega tu clave así:

   .. code-block:: python

        # secret.py
        # Guarda los secretos aquí. Nunca subas este archivo a Git.
        
        QWEN_API_KEY = "sk-xxx"

**Probar con código de ejemplo**

#. Reemplaza el contenido con el siguiente código y actualiza ``model="xxx"`` con el modelo que desees (por ejemplo, ``qwen-plus``):

   .. code-block:: python
   
      from picarx.llm import Qwen
      from secret import QWEN_API_KEY

      INSTRUCTIONS = "You are a helpful assistant."
      WELCOME = "Hello, I am a helpful assistant. How can I help you?"

      llm = Qwen(
          api_key=QWEN_API_KEY,
          model="qwen-plus",
      )

#. Ejecuta con:

   .. code-block:: bash
   
       sudo python3 18.online_llm_test.py

       
Grok (xAI)
------------------
Grok es la IA conversacional de xAI, creada por el equipo de Elon Musk. Puedes conectarte a ella a través de la API de xAI.

**Obtener y guardar tu clave API**

#. Regístrate para obtener una cuenta aquí: |link_grok_ai|. Agrega algunos créditos a tu cuenta primero — de lo contrario, la API no funcionará.

#. Ve a la página de API Keys y haz clic en **Create API key**.  

   .. image:: img/llm_grok_create.png

#. Escribe un nombre para la clave y haz clic en **Create API key**. 

   .. image:: img/llm_grok_name.png

#. Copia la clave generada y guárdala en un lugar seguro. 

   .. image:: img/llm_grok_copy.png

#. En tu carpeta de proyecto:

   .. code-block:: bash

       cd ~/picar-x/example
       sudo nano secret.py

#. Pega tu clave de esta manera:

   .. code-block:: python

        # secret.py
        # Guarda los secretos aquí. Nunca subas este archivo a Git.
        
        GROK_API_KEY = "xai-xxx"

**Verificar modelos disponibles**

Ve a la página de **Models** en la consola de xAI. Allí puedes ver todos los modelos disponibles para tu equipo, junto con sus IDs exactos de API — usa estos IDs en tu código.

   .. image:: img/llm_grok_model.png

**Probar con código de ejemplo**

#. Reemplaza el contenido con el siguiente código y actualiza ``model="xxx"`` con el modelo que desees (por ejemplo, ``grok-4-latest``):

   .. code-block:: python
   
       from picarx.llm import Grok
       from secret import GROK_API_KEY
   
       INSTRUCTIONS = "You are a helpful assistant."
       WELCOME = "Hello, I am a helpful assistant. How can I help you?"
   
       llm = Grok(
           api_key=GROK_API_KEY,
           model="grok-4-latest",
       )

#. Ejecuta con:

   .. code-block:: bash
   
       sudo python3 18.online_llm_test.py

----

DeepSeek
------------------

DeepSeek es un proveedor chino de LLM que ofrece modelos accesibles y potentes.  

**Obtener y guardar tu clave API**

#. Inicia sesión en |link_deepseek|. 

#. En el menú superior derecho, selecciona **API Keys → Create API Key**. 

   .. image:: img/llm_deepseek_create.png

#. Escribe un nombre, haz clic en **Create** y luego copia la clave.

   .. image:: img/llm_deepseek_copy.png

#. En tu carpeta de proyecto:

   .. code-block:: bash

       cd ~/picar-x/example
       sudo nano secret.py

#. Agrega tu clave:

   .. code-block:: python

       # secret.py
       DEEPSEEK_API_KEY = "sk-xxx"

**Habilitar facturación**

Necesitarás recargar tu cuenta primero. Comienza con una pequeña cantidad (por ejemplo, ¥10 RMB).

   .. image:: img/llm_deepseek_chognzhi.png

**Modelos disponibles**

En el momento de redactar esto (2025-09-12), DeepSeek ofrece:  

* ``deepseek-chat``  
* ``deepseek-reasoner``  

**Probar con código de ejemplo**

#. Reemplaza el contenido con el siguiente código y actualiza ``model="xxx"`` con el modelo que desees (por ejemplo, ``deepseek-chat``):

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

#. Ejecuta:

   .. code-block:: bash
   
       sudo python3 18.online_llm_test.py

----

Doubao
------------------
Doubao es la plataforma de modelos de IA de ByteDance (Volcengine Ark).  

**Obtener y guardar tu clave API**

#. Inicia sesión en |link_doubao|.

#. En el menú de la izquierda, desplázate hacia abajo hasta **API Key Management → Create API Key**. 

   .. image:: img/llm_doubao_create.png

#. Elige un nombre y haz clic en **Create**.  

   .. image:: img/llm_doubao_name.png

#. Haz clic en el ícono **Show API Key** y copia la clave. 

   .. image:: img/llm_doubao_copy.png

#. En tu carpeta de proyecto:

   .. code-block:: bash

       cd ~/picar-x/example
       sudo nano secret.py

#. Agrega tu clave:

   .. code-block:: python

       # secret.py
       DOUBAO_API_KEY = "xxx"

**Elegir un modelo**

#. Ve al marketplace de modelos y selecciona un modelo.  

   .. image:: img/llm_doubao_model_select.png

#. Por ejemplo, selecciona **Doubao-seed-1.6**, luego haz clic en **API 接入**. 

   .. image:: img/llm_doubao_model.png

#. Selecciona tu clave API y haz clic en **Use API**. 

   .. image:: img/llm_doubao_use_api.png

#. Haz clic en **Enable Model**. 

   .. image:: img/llm_doubao_kaitong.png

#. Pasa el cursor sobre el ID del modelo para copiarlo. 

   .. image:: img/llm_doubao_copy_id.png

**Probar con código de ejemplo**

#. Reemplaza el contenido con el siguiente código y actualiza ``model="xxx"`` con el modelo que desees (por ejemplo, ``doubao-seed-1-6-250615``):

   .. code-block:: python
   
       from picarx.llm import Doubao
       from secret import DOUBAO_API_KEY
   
       INSTRUCTIONS = "You are a helpful assistant."
       WELCOME = "Hello, I am a helpful assistant. How can I help you?"
   
       llm = Doubao(
           api_key=DOUBAO_API_KEY,
           model="doubao-seed-1-6-250615",
       )

#. Ejecuta con:

   .. code-block:: bash
   
       sudo python3 18.online_llm_test.py


General
--------------

Este proyecto admite la conexión a múltiples plataformas LLM mediante una interfaz unificada.  
Tiene compatibilidad integrada con:

* **OpenAI** (ChatGPT / GPT-4o, GPT-4, GPT-3.5)  
* **Gemini** (Google AI Studio / Vertex AI)  
* **Grok** (xAI)  
* **DeepSeek**  
* **Qwen (通义千问)**  
* **Doubao (豆包)**  

Además, puedes conectarte a **cualquier otro servicio LLM que sea compatible con el formato de la API de OpenAI**.  
Para esas plataformas, deberás obtener manualmente tu **API Key** y el **base_url** correcto.

**Obtener y guardar tu clave API**

#. Obtén una **API Key** de la plataforma que deseas usar. (Consulta la consola oficial de cada plataforma para más detalles.)  

#. En tu carpeta de proyecto, crea un nuevo archivo:

   .. code-block:: bash

      cd ~/picar-x/example
      nano secret.py

#. Agrega tu clave en ``secret.py``:

   .. code-block:: python

      # secret.py
      API_KEY = "your_api_key_here"

.. warning::

   Mantén tu clave API en privado. No subas ``secret.py`` a repositorios públicos.

**Probar con código de ejemplo**

#. Reemplaza el contenido de un archivo Python con el siguiente ejemplo y completa ``base_url`` y ``model`` correctamente para tu plataforma:

   .. note::

      Acerca de ``base_url``:  
      Admitimos el **formato de API de OpenAI**, así como cualquier API que sea **compatible** con este.  
      Cada proveedor tiene su propio ``base_url``. Revisa su documentación oficial.  

   .. code-block:: python

      from picarx.llm import LLM
      from secret import API_KEY

      INSTRUCTIONS = "You are a helpful assistant."
      WELCOME = "Hello, I am a helpful assistant. How can I help you?"

      llm = LLM(
          base_url="https://api.example.com/v1",  # coloca aquí el base_url de tu proveedor
          api_key=API_KEY,
          model="your-model-name-here",           # elige un modelo de tu proveedor
      )

#. Ejecuta el programa:

   .. code-block:: bash

      python3 18.online_llm_test.py



