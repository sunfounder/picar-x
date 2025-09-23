.. note::

    Hello, welcome to the SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasts Community on Facebook! Dive deeper into Raspberry Pi, Arduino, and ESP32 with fellow enthusiasts.

    **Why Join?**

    - **Expert Support**: Solve post-sale issues and technical challenges with help from our community and team.
    - **Learn & Share**: Exchange tips and tutorials to enhance your skills.
    - **Exclusive Previews**: Get early access to new product announcements and sneak peeks.
    - **Special Discounts**: Enjoy exclusive discounts on our newest products.
    - **Festive Promotions and Giveaways**: Take part in giveaways and holiday promotions.

    👉 Ready to explore and create with us? Click [|link_sf_facebook|] and join today!

1. What Else Do You Need?
===============================

Before we start playing with PiCar-X, let’s prepare the essential hardware.  
Think of these components as the **brain, heart, and senses** of PiCar-X — without them, the car cannot run properly.

Required Components
------------------------------

* **Raspberry Pi**

  The Raspberry Pi acts as the **brain** of PiCar-X, handling all computing, sensing, and control tasks.  
  
  .. image:: img/need_pi.jpg

  * **Compatible models**: Raspberry Pi 5, Raspberry Pi 4, 3, or Raspberry Pi Zero 2W  
  * **Minimum**: **2GB RAM** — sufficient for all PiCar-X standard functions (movement, sensors, camera streaming) and for using **online AI services** such as OpenAI Whisper, TTS, or LLMs.  
  * **Recommended**: **4GB RAM or more** — ensures smoother performance when running **local AI models** (e.g., Vosk speech recognition, Piper TTS, or lightweight LLMs) alongside camera streaming and control tasks.  
  

* **Power Adapter**

  PiCar-X comes with an **18650 battery pack** and a **Robot HAT** board featuring a built-in charging circuit.
  
  .. image:: img/need_power.png
    :width: 400

  * For charging, it is recommended to use a **5V 3A power supply**, such as the official **Raspberry Pi 15W USB-C adapter**.  
  * You may also use a **USB-C Power Delivery (PD) charger** or a **QC 2.0 fast charger**.  
  * A full charge typically takes about **2 hours** (from 0% to 100%).  


* **Micro SD Card**

  The Raspberry Pi does not have a built-in hard drive. It boots and stores all files on a **Micro SD card**.  
  
  .. image:: img/need_sd.jpg
    :width: 200

  * Minimum: **16GB**  
  * Recommended: **32GB** for better stability  
  * Brand: Use reliable options such as **SanDisk** or **Samsung** to avoid read/write errors  
  
Optional Components
------------------------

Although not strictly required, the following peripherals will greatly improve your learning and debugging experience:

* **Monitor (HDMI or TV)** 

  For beginners, we strongly recommend a display with an HDMI input, so you can easily configure Raspberry Pi OS and run graphical programs.  

  .. image:: img/need_screen.png
    :width: 400

* **HDMI Cable (Standard / Mini / Micro)**
 
  Different Raspberry Pi models use different HDMI connectors, be sure to check your Pi model and prepare the correct cable. 
  
  * **Raspberry Pi 4 / 5**: Micro HDMI  
  * **Raspberry Pi 3**: Standard HDMI  
  * **Raspberry Pi Zero 2W**: Mini HDMI 

  .. image:: img/need_hdmi.png
    :width: 400

* **Keyboard & Mouse**

  Very useful during the initial setup of Raspberry Pi OS. Later, you may switch to remote access (SSH/VNC), but for beginners we recommend preparing a basic USB or wireless set.  

  .. image:: img/need_keyboard_mouse.png
    :width: 500
 

**Tips for Preparation**

* If you purchased the **PiCar-X kit**, most accessories are included, but you still need to prepare the Raspberry Pi board, Micro SD card, and power adapter separately.  
* Not sure what to buy? 👉 The most stable and universal choice is:  
  **Raspberry Pi 4 (2GB) + Official Power Supply + 32GB Micro SD card**.  

