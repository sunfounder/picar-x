AI Interaction Using GPT-4O
=====================================================
In our previous projects, we used programming to direct PiCar-X in predetermined tasks, which could seem a bit tedious. This project introduces a thrilling leap towards dynamic engagement. Beware of trying to outsmart our car—as it's now equipped to understand far more than ever before!

This initiative details all the technical steps needed to integrate the GPT-4O into your system, including configuring the necessary virtual environments, installing crucial libraries, and setting up API keys and assistant IDs.

.. note::

   This project requires the use of |link_openai_platform|, and you need to pay for OpenAI. Additionally, the OpenAI API is billed separately from ChatGPT, with its own pricing available at https://openai.com/api/pricing/.

   Therefore, you need to decide whether to continue with this project or ensure you have funded the OpenAI API.

Whether you have a microphone to communicate directly or prefer typing into a command window, PiCar-X's responses powered by GPT-4O will surely astonish you!

Let's dive into this project and unleash a new level of interaction with PiCar-X!

1. Installing Required Packages and Dependencies
--------------------------------------------------------------
.. note::

   You need to install the necessary modules for PiCar-X first. For details, please refer to: :ref:`install_all_modules`.
   
In this section, we will create and activate a virtual environment, installing the required packages and dependencies within it. This ensures that the installed packages do not interfere with the rest of the system, maintaining project dependency isolation and preventing conflicts with other projects or system packages.

#. Use the ``python -m venv`` command to create a virtual environment named ``my_venv``, including system-level packages. The ``--system-site-packages`` option allows the virtual environment to access packages installed system-wide, which is useful when system-level libraries are needed.

   .. code-block:: shell

      python -m venv --system-site-packages my_venv

#. Switch to the ``my_venv`` directory and activate the virtual environment using the ``source bin/activate`` command. The command prompt will change to indicate that the virtual environment is active.

   .. code-block:: shell

      cd my_venv
      source bin/activate

#. Now, install the required Python packages within the activated virtual environment. These packages will be isolated to the virtual environment and will not affect other system packages.

   .. code-block:: shell

      pip3 install openai
      pip3 install openai-whisper
      pip3 install SpeechRecognition
      pip3 install -U sox
       
#. Finally, use the ``apt`` command to install system-level dependencies, which require administrator privileges.

   .. code-block:: shell

      sudo apt install python3-pyaudio
      sudo apt install sox


2. Obtain API Key and Assistant ID
-----------------------------------------

**Get API Key**

#. Visit |link_openai_platform| and click the **Create new secret key** button in the top right corner.

   .. image:: img/apt_create_api_key.png
      :width: 700
      :align: center

#. Select the Owner, Name, Project, and permissions as needed, and then click **Create secret key**.

   .. image:: img/apt_create_api_key2.png
      :width: 700
      :align: center

#. Once generated, save this secret key in a safe and accessible location. For security reasons, you will not be able to view it again through your OpenAI account. If you lose this secret key, you will need to generate a new one.

   .. image:: img/apt_create_api_key_copy.png
      :width: 700
      :align: center

**Get Assistant ID**

#. Next, click on **Assistants**, then click **Create**, making sure you are on the **Dashboard** page.

   .. image:: img/apt_create_assistant.png
      :width: 700
      :align: center

#. Move your cursor here to copy the **assistant ID**, then paste it into a text box or elsewhere. This is the unique identifier for this Assistant.

   .. image:: img/apt_create_assistant_id.png
      :width: 700
      :align: center

#. Randomly set a name, then copy the following content into the **Instructions** box to describe your Assistant.

   .. image:: img/apt_create_assistant_instructions.png
      :width: 700
      :align: center

   .. code-block::

         You are a small car with AI capabilities named PaiCar-X. You can engage in conversations with people and react accordingly to different situations with actions or sounds. You are driven by two rear wheels, with two front wheels that can turn left and right, and equipped with a camera mounted on a 2-axis gimbal.

         ## Response with Json Format, eg:
         {"actions": ["start engine", "honking", "wave hands"], "answer": "Hello, I am PaiCar-X, your good friend."}

         ## Response Style
         Tone: Cheerful, optimistic, humorous, childlike
         Preferred Style: Enjoys incorporating jokes, metaphors, and playful banter; prefers responding from a robotic perspective
         Answer Elaboration: Moderately detailed

         ## Actions you can do:
         ["shake head", "nod", "wave hands", "resist", "act cute", "rub hands", "think", "twist body", "celebrate, "depressed"]
         ## Sound effects:
         ["honking", "start engine"]


#. PiCar-X is equipped with a camera module that you can enable to capture images of what it sees and upload them to GPT using our example code. Therefore, we recommend choosing GPT-4O, which has image analysis capabilities. Of course, you can also choose gpt-3.5-turbo or other models.

   .. image:: img/apt_create_assistant_model.png
      :width: 700
      :align: center

#. Now, click **Playground** to see if your account is functioning properly.

   .. image:: img/apt_playground.png

#. If your messages or uploaded images are sent successfully and you receive replies, it means your account has not reached the usage limit.


   .. image:: img/apt_playground_40.png
      :width: 700
      :align: center

#. If you encounter an error message after inputting information, you may have reached your usage limit. Please check your usage dashboard or billing settings.

   .. image:: img/apt_playground_40mini_3.5.png
      :width: 700
      :align: center

3. Fill in API Key and Assistant ID
--------------------------------------------------

#. Use the command to open the ``keys.py`` file.

   .. code-block:: shell

      nano ~/picar-x/gpt_examples/keys.py

#. Fill in the API Key and Assistant ID you just copied.

   .. code-block:: shell

      OPENAI_API_KEY = "sk-proj-vEBo7Ahxxxx-xxxxx-xxxx"
      OPENAI_ASSISTANT_ID = "asst_ulxxxxxxxxx"

#. Press ``Ctrl + X``, ``Y``, and then ``Enter`` to save the file and exit.

4. Running the Example
----------------------------------
Text Communication
^^^^^^^^^^^^^^^^^^^^^^^^^^

If your PiCar-X does not have a microphone, you can use keyboard input text to interact with it by running the following commands.

#. Now, run the following commands using sudo, as PiCar-X's speaker will not function without it. The process will take some time to complete.

   .. code-block:: shell

      cd ~/picar-x/gpt_examples/
      sudo ~/my_venv/bin/python3 gpt_car.py --keyboard

#. Once the commands have executed successfully, you will see the following output, indicating that all components of PiCar-X are ready.

   .. code-block:: shell

      vilib 0.3.8 launching ...
      picamera2 0.3.19

      Web display on:
         http://rpi_ip:9000/mjpg

      Starting web streaming ...
      * Serving Flask app 'vilib.vilib'
      * Debug mode: off

      input:

#. You will also be provided with a link to view PiCar-X's camera feed on your web browser: ``http://rpi_ip:9000/mjpg``.

   .. image:: img/apt_ip_camera.png
      :width: 700
      :align: center

#. You can now type your commands into the terminal window, and press Enter to send them. PiCar-X's responses may surprise you.

   .. note::
      
      PiCar-X needs to receive your input, send it to GPT for processing, receive the response, and then play it back via speech synthesis. This entire process takes some time, so please be patient.

   .. image:: img/apt_keyboard_input.png
      :width: 700
      :align: center

#. If you are using the GPT-4O model, you can also ask questions based on what PiCar-X sees.

Voice Communication
^^^^^^^^^^^^^^^^^^^^^^^^

If your PiCar-X is equipped with a microphone, or you can purchase one by clicking |link_microphone|, you can interact with PiCar-X using voice commands.

#. First, verify that the Raspberry Pi has detected the microphone.

   .. code-block:: shell

      arecord -l

   If successful, you will receive the following information, indicating that your microphone has been detected.

   .. code-block:: 
      
      **** List of CAPTURE Hardware Devices ****
      card 3: Device [USB PnP Sound Device], device 0: USB Audio [USB Audio]
      Subdevices: 1/1
      Subdevice #0: subdevice #0

#. Run the following command, then speak to PiCar-X or make some sounds. The microphone will record the sounds into the ``op.wav`` file. Press ``Ctrl + C`` to stop recording.

   .. code-block:: shell

      rec op.wav

#. Finally, use the command below to play back the recorded sound, confirming that the microphone is functioning properly.

   .. code-block:: shell

      sudo play op.wav

#. Now, run the following commands using sudo, as PiCar-X's speaker will not function without it. The process will take some time to complete.

   .. code-block:: shell

      cd ~/picar-x/gpt_examples/
      sudo ~/my_venv/bin/python3 gpt_car.py

#. Once the commands have executed successfully, you will see the following output, indicating that all components of PiCar-X are ready.

   .. code-block:: shell
      
      vilib 0.3.8 launching ...
      picamera2 0.3.19

      Web display on:
         http://rpi_ip:9000/mjpg

      Starting web streaming ...
      * Serving Flask app 'vilib.vilib'
      * Debug mode: off

      listening ...

#. You will also be provided with a link to view PiCar-X's camera feed on your web browser: ``http://rpi_ip:9000/mjpg``.

   .. image:: img/apt_ip_camera.png
      :width: 700
      :align: center

#. You can now speak to PiCar-X, and its responses may surprise you.

   .. note::
      
      PiCar-X needs to receive your input, convert it to text, send it to GPT for processing, receive the response, and then play it back via speech synthesis. This entire process takes some time, so please be patient.

   .. image:: img/apt_speech_input.png
      :width: 700
      :align: center

#. If you are using the GPT-4O model, you can also ask questions based on what PiCar-X sees.


5. Modify parameters [optional]
-------------------------------------------

In the ``gpt_car.py`` file, locate the following lines. You can modify these parameters to configure the STT language, TTS volume gain, and voice role.

* **STT (Speech to Text)** refers to the process where the PiCar-X microphone captures speech and converts it into text to be sent to GPT. You can specify the language for better accuracy and latency in this conversion.

* **TTS (Text to Speech)** is the process of converting GPT's text responses into speech, which is played through the PiCar-X speaker. You can adjust the volume gain and select a voice role for the TTS output.

.. code-block:: python

   # openai assistant init
   # =================================================================
   openai_helper = OpenAiHelper(OPENAI_API_KEY, OPENAI_ASSISTANT_ID, 'picrawler')

   # LANGUAGE = ['zh', 'en'] # config stt language code, https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes
   LANGUAGE = []

   VOLUME_DB = 3 # tts voloume gain, preferably less than 5db

   # select tts voice role, counld be "alloy, echo, fable, onyx, nova, and shimmer"
   # https://platform.openai.com/docs/guides/text-to-speech/supported-languages
   TTS_VOICE = 'nova'


* ``LANGUAGE`` variable: 

  * Improves Speech-to-Text (STT) accuracy and response time.
  * ``LANGUAGE = []`` means supporting all languages, but this may reduce STT accuracy and increase latency.
  * It's recommended to set the specific language(s) using |link_iso_language_code| language codes to improve performance.

* ``VOLUME_DB`` variable:

  * Controls the gain applied to Text-to-Speech (TTS) output.
  * Increasing the value will boost the volume, but it's best to keep the value below 5dB to prevent audio distortion.

* ``TTS_VOICE`` variable:

  * Select the voice role for the Text-to-Speech (TTS) output.
  * Available options: ``alloy, echo, fable, onyx, nova, shimmer``.
  * You can experiment with different voices from |link_voice_options| to find one that suits your desired tone and audience. The available voices are currently optimized for English.
