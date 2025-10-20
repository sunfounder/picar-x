
.. _py_online_llm:

18. 连接在线 LLM
================================

在本课中，我们将学习如何将你的 PiCar-X（或树莓派）连接到不同的 **在线大语言模型（LLM）**。  
每个提供商都需要一个 API key，并且提供不同的模型供你选择。

我们将逐步讲解以下内容：

* 如何安全地创建和保存 API key。  
* 如何选择适合你需求的模型。  
* 如何运行示例代码与模型进行对话。

接下来将针对每个提供商进行详细步骤说明。

----

开始之前
----------------

确保你已经准备好以下内容：

* :ref:`install_all_modules` — 安装 ``robot-hat``、 ``vilib``、 ``picar-x`` 模块，然后运行脚本 ``i2samp.sh``。

----

OpenAI
----------

OpenAI 提供了强大的模型，例如 **GPT-4o** 和 **GPT-4.1**，可用于文本和视觉任务。

以下是设置方法：

**获取并保存 API Key**

#. 打开 |link_openai_platform| 并登录。在 **API keys** 页面点击 **Create new secret key**。

   .. image:: img/llm_openai_create.png

#. 填写必要信息（Owner、Name、Project，如需可设置权限），然后点击 **Create secret key**。

   .. image:: img/llm_openai_create_confirm.png

#. 创建完成后请立即复制该密钥 —— 之后将无法再次查看。如果遗失，你需要重新生成一个。

   .. image:: img/llm_openai_copy.png

#. 在你的项目文件夹（例如：``/picar-x/example``）中创建一个名为 ``secret.py`` 的文件：

   .. code-block:: bash

       cd ~/picar-x/example
       sudo nano secret.py

#. 将密钥粘贴到文件中，如下所示：

   .. code-block:: python

       # secret.py
       # Store secrets here. Never commit this file to Git.
       OPENAI_API_KEY = "sk-xxx"

**开启计费并查看模型**

#. 在使用密钥前，进入 OpenAI 账号的 **Billing** 页面，添加支付方式并充值少量额度。

   .. image:: img/llm_openai_billing.png

#. 然后进入 **Limits** 页面，查看你的账号可使用的模型，并复制模型的精确 ID 以便在代码中使用。

   .. image:: img/llm_openai_models.png

**使用示例代码进行测试**

#. 打开我们的示例代码：

   .. code-block:: bash

       cd ~/picar-x/example
       sudo nano 18.online_llm_test.py

#. 将文件内容替换为以下代码，并将 ``model="xxx"`` 修改为你要使用的模型（例如 ``gpt-4o``）：

   .. code-block:: python

       from picarx.llm import OpenAI
       from secret import OPENAI_API_KEY
       
       INSTRUCTIONS = "You are a helpful assistant."
       WELCOME = "Hello, I am a helpful assistant. How can I help you?"
       
       llm = OpenAI(
           api_key=OPENAI_API_KEY,
           model="gpt-4o",
       )

   保存并退出（``Ctrl+X``，然后 ``Y``，再按 ``Enter``）。

#. 最后，运行测试：

   .. code-block:: bash
   
       sudo python3 18.online_llm_test.py
   

----

Gemini
------------------

Gemini 是 Google 推出的 AI 模型家族。它运行速度快，非常适合通用型任务。

**获取并保存 API Key**

#. 登录 |link_google_ai|，然后进入 API Keys 页面。

   .. image:: img/llm_gemini_get.png

#. 点击右上角的 **Create API key** 按钮。

   .. image:: img/llm_gemini_create.png

#. 你可以为已有项目或新项目创建密钥。

   .. image:: img/llm_gemini_choose.png

#. 复制生成的 API key。

   .. image:: img/llm_gemini_copy.png

#. 在你的项目文件夹中：

   .. code-block:: bash

       cd ~/picar-x/example
       sudo nano secret.py

#. 将密钥粘贴进去：

   .. code-block:: python

        # secret.py
        # Store secrets here. Never commit this file to Git.
        GEMINI_API_KEY = "AIxxx"

**查看可用模型**

访问官方 |link_gemini_model| 页面，这里可以查看模型列表、对应的 API ID，以及每个模型适用的使用场景。

   .. image:: img/llm_gemini_model.png

**使用示例代码进行测试**

#. 打开测试文件：

   .. code-block:: bash

       cd ~/picar-x/example
       sudo nano 18.online_llm_test.py

#. 将文件内容替换为以下代码，并将 ``model="xxx"`` 修改为你要使用的模型（例如 ``gemini-2.5-flash``）：

   .. code-block:: python

       from picarx.llm import Gemini
       from secret import GEMINI_API_KEY

       INSTRUCTIONS = "You are a helpful assistant."
       WELCOME = "Hello, I am a helpful assistant. How can I help you?"

       llm = Gemini(
           api_key=GEMINI_API_KEY,
           model="gemini-2.5-flash",
       )

#. 保存并运行：


   .. code-block:: bash

       sudo python3 18.online_llm_test.py

----

Qwen
------------------

Qwen 是由阿里云提供的一系列大语言和多模态模型。  
这些模型支持文本生成、推理以及多模态理解（如图像分析）。

**获取 API Key**

要调用 Qwen 模型，你需要一个 **API Key**。  
国际用户通常使用 **DashScope International（Model Studio）** 控制台。  
中国大陆用户可以使用 **百炼（Bailian）** 控制台。

* **国际用户**

  #. 前往阿里云的 |link_qwen_inter| 官方页面。  
  #. 登录或注册一个 **Alibaba Cloud** 账号。  
  #. 进入 **Model Studio** （选择新加坡或北京区域）。  
    
     * 如果页面顶部出现“Activate Now”提示，点击它激活 Model Studio 并获得免费额度（仅限新加坡）。  
     * 激活是免费的，只有在用完免费额度后才会开始计费。  
     * 如果没有出现激活提示，说明服务已启用。
  
  #. 打开 **Key Management** 页面，在 **API Key** 标签页中点击 **Create API Key**。  
  #. 创建完成后，复制 API Key 并妥善保存。  
  
    .. image:: img/llm_qwen_api_key.png
        :width: 800
  
  .. note::
     香港、澳门和台湾的用户也应选择 **International (Model Studio)** 选项。

* **中国大陆用户**

  如果你在中国大陆，可以使用 **阿里云百炼（Bailian）** 控制台：

  #. 登录 |link_aliyun| （百炼控制台）并完成账号验证。  
  #. 选择 **Create API Key**。如果提示模型服务未激活，点击 **Activate**，同意条款并领取免费额度。激活完成后，“Create API Key” 按钮将可用。
  
     .. image:: img/llm_qwen_aliyun_create.png
  
  #. 再次点击 **Create API Key**，检查账户信息并点击 **Confirm**。
  
     .. image:: img/llm_qwen_aliyun_confirm.png
  
  #. 创建完成后，复制你的 API Key。
  
     .. image:: img/llm_qwen_aliyun_copy.png

**保存 API Key**

#. 在你的项目文件夹中：

   .. code-block:: bash

       cd ~/picar-x/example
       sudo nano secret.py

#. 将密钥粘贴进去，如下所示：

   .. code-block:: python

        # secret.py
        # Store secrets here. Never commit this file to Git.
        
        QWEN_API_KEY = "sk-xxx"

**使用示例代码进行测试**

#. 打开测试文件：

   .. code-block:: bash

       cd ~/picar-x/example
       sudo nano 18.online_llm_test.py
#. 将内容替换为以下代码，并将 ``model="xxx"`` 修改为你要使用的模型（例如 ``qwen-plus``）：

   .. code-block:: python
   
      from picarx.llm import Qwen
      from secret import QWEN_API_KEY

      INSTRUCTIONS = "You are a helpful assistant."
      WELCOME = "Hello, I am a helpful assistant. How can I help you?"

      llm = Qwen(
          api_key=QWEN_API_KEY,
          model="qwen-plus",
      )

#. 运行：

   .. code-block:: bash
   
       sudo python3 18.online_llm_test.py

Grok (xAI)
------------------
Grok 是由埃隆·马斯克团队开发的 xAI 对话式 AI。你可以通过 xAI 的 API 来连接它。

**获取并保存 API Key**

#. 在 |link_grok_ai| 注册账户。首先为你的账户充值一些额度，否则 API 无法使用。

#. 进入 API Keys 页面，点击 **Create API key**。

   .. image:: img/llm_grok_create.png

#. 输入一个名称，然后点击 **Create API key**。

   .. image:: img/llm_grok_name.png

#. 复制生成的密钥并妥善保存。

   .. image:: img/llm_grok_copy.png

#. 在你的项目文件夹中：

   .. code-block:: bash

       cd ~/picar-x/example
       sudo nano secret.py

#. 将密钥粘贴进去：

   .. code-block:: python

        # secret.py
        # Store secrets here. Never commit this file to Git.
        
        GROK_API_KEY = "xai-xxx"

**查看可用模型**

进入 xAI 控制台的 Models 页面。这里可以查看你团队可使用的所有模型及其 API ID —— 你需要在代码中使用这些 ID。

   .. image:: img/llm_grok_model.png

**使用示例代码进行测试**

#. 打开测试文件：

   .. code-block:: bash

       cd ~/picar-x/example
       sudo nano 18.online_llm_test.py

#. 将文件内容替换为以下代码，并将 ``model="xxx"`` 修改为你要使用的模型（例如 ``grok-4-latest``）：

   .. code-block:: python
   
       from picarx.llm import Grok
       from secret import GROK_API_KEY
   
       INSTRUCTIONS = "You are a helpful assistant."
       WELCOME = "Hello, I am a helpful assistant. How can I help you?"
   
       llm = Grok(
           api_key=GROK_API_KEY,
           model="grok-4-latest",
       )

#. 运行：

   .. code-block:: bash
   
       sudo python3 18.online_llm_test.py

----

DeepSeek
------------------

DeepSeek 是一家中国的大语言模型提供商，提供高性价比且功能强大的模型。

**获取并保存 API Key**

#. 登录 |link_deepseek|。

#. 在右上角菜单中，选择 **API Keys → Create API Key**。

   .. image:: img/llm_deepseek_create.png

#. 输入名称，点击 **Create**，然后复制密钥。

   .. image:: img/llm_deepseek_copy.png

#. 在你的项目文件夹中：

   .. code-block:: bash

       cd ~/picar-x/example
       sudo nano secret.py

#. 添加密钥：

   .. code-block:: python

       # secret.py
       DEEPSEEK_API_KEY = "sk-xxx"

**开启计费**

你需要先给账户充值。建议先充值少量金额（例如 ¥10 元人民币）。

   .. image:: img/llm_deepseek_chognzhi.png

**可用模型**

截至 2025-09-12，DeepSeek 提供的模型包括：

* ``deepseek-chat``  
* ``deepseek-reasoner``

**使用示例代码进行测试**

#. 打开测试文件：

   .. code-block:: bash

       cd ~/picar-x/example
       sudo nano 18.online_llm_test.py
#. 将文件内容替换为以下代码，并将 ``model="xxx"`` 修改为你要使用的模型（例如 ``deepseek-chat``）：

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

#. 运行：

   .. code-block:: bash
   
       sudo python3 18.online_llm_test.py

----

Doubao
------------------
Doubao 是字节跳动旗下的 AI 模型平台（Volcengine Ark）。

**获取并保存 API Key**

#. 登录 |link_doubao|。

#. 在左侧菜单中，找到 **API Key Management → Create API Key**。

   .. image:: img/llm_doubao_create.png

#. 输入一个名称并点击 **Create**。

   .. image:: img/llm_doubao_name.png

#. 点击 **Show API Key** 图标并复制密钥。

   .. image:: img/llm_doubao_copy.png

#. 在你的项目文件夹中：

   .. code-block:: bash

       cd ~/picar-x/example
       sudo nano secret.py

#. 添加密钥：

   .. code-block:: python

       # secret.py
       DOUBAO_API_KEY = "xxx"

**选择模型**

#. 前往模型市场，选择你要使用的模型。

   .. image:: img/llm_doubao_model_select.png

#. 例如，选择 **Doubao-seed-1.6**，然后点击 **API 接入**。

   .. image:: img/llm_doubao_model.png

#. 选择你的 API Key 并点击 **Use API**。

   .. image:: img/llm_doubao_use_api.png

#. 点击 **Enable Model**。

   .. image:: img/llm_doubao_kaitong.png

#. 将鼠标悬停在模型 ID 上并复制它。

   .. image:: img/llm_doubao_copy_id.png

**使用示例代码进行测试**

#. 打开测试文件：

   .. code-block:: bash

       cd ~/picar-x/example
       sudo nano 18.online_llm_test.py

#. 将文件内容替换为以下代码，并将 ``model="xxx"`` 修改为你要使用的模型（例如 ``doubao-seed-1-6-250615``）：

   .. code-block:: python
   
       from picarx.llm import Doubao
       from secret import DOUBAO_API_KEY
   
       INSTRUCTIONS = "You are a helpful assistant."
       WELCOME = "Hello, I am a helpful assistant. How can I help you?"
   
       llm = Doubao(
           api_key=DOUBAO_API_KEY,
           model="doubao-seed-1-6-250615",
       )

#. 运行：

   .. code-block:: bash
   
       sudo python3 18.online_llm_test.py

General
--------------

本项目支持通过统一接口连接多个 LLM 平台，已内置兼容以下服务：

* **OpenAI** （ChatGPT / GPT-4o、GPT-4、GPT-3.5）  
* **Gemini** （Google AI Studio / Vertex AI）  
* **Grok** （xAI）  
* **DeepSeek**  
* **Qwen（通义千问）**  
* **Doubao（豆包）**

此外，还可以连接 **任何符合 OpenAI API 格式的其他 LLM 服务**。  
对于这类平台，你需要手动获取 **API Key** 和正确的 **base_url**。

**获取并保存 API Key**

#. 从你要使用的平台获取 **API Key**。（可参考各平台官方控制台。）

#. 在你的项目文件夹中创建一个新文件：

   .. code-block:: bash

      cd ~/picar-x/example
      nano secret.py

#. 将密钥添加到 ``secret.py`` 中：

   .. code-block:: python

      # secret.py
      API_KEY = "your_api_key_here"

.. warning::

   请妥善保管你的 API Key，不要将 ``secret.py`` 上传至公共仓库。

**使用示例代码进行测试**

#. 打开测试文件：

   .. code-block:: bash

       cd ~/picar-x/example
       sudo nano 18.online_llm_test.py
#. 将 Python 文件内容替换为以下示例代码，并填写你所用平台的正确 ``base_url`` 和 ``model``：

   .. note::

      关于 ``base_url``：  
      我们支持 **OpenAI API 格式** 以及任何与之 **兼容** 的接口。  
      每个平台的 ``base_url`` 各不相同，请查看对应的官方文档。

   .. code-block:: python

      from picarx.llm import LLM
      from secret import API_KEY

      INSTRUCTIONS = "You are a helpful assistant."
      WELCOME = "Hello, I am a helpful assistant. How can I help you?"

      llm = LLM(
          base_url="https://api.example.com/v1",  # 填写你所用平台的 base_url
          api_key=API_KEY,
          model="your-model-name-here",           # 填写模型名称
      )

#. 运行程序：


   .. code-block:: bash

      python3 18.online_llm_test.py



