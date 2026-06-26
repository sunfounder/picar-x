.. note::

    Hallo und willkommen in der SunFounder Raspberry Pi & Arduino & ESP32 Enthusiasten-Gemeinschaft auf Facebook! Tauchen Sie tiefer ein in die Welt von Raspberry Pi, Arduino und ESP32 mit anderen Enthusiasten.

    **Warum beitreten?**

    - **Expertenunterstützung**: Lösen Sie Nachverkaufsprobleme und technische Herausforderungen mit Hilfe unserer Gemeinschaft und unseres Teams.
    - **Lernen & Teilen**: Tauschen Sie Tipps und Anleitungen aus, um Ihre Fähigkeiten zu verbessern.
    - **Exklusive Vorschauen**: Erhalten Sie frühzeitigen Zugang zu neuen Produktankündigungen und exklusiven Einblicken.
    - **Spezialrabatte**: Genießen Sie exklusive Rabatte auf unsere neuesten Produkte.
    - **Festliche Aktionen und Gewinnspiele**: Nehmen Sie an Gewinnspielen und Feiertagsaktionen teil.

    👉 Sind Sie bereit, mit uns zu erkunden und zu erschaffen? Klicken Sie auf [|link_sf_facebook|] und treten Sie heute bei!

.. _install_all_modules:


Alle Module installieren (Wichtig)
==================================

#. **System vorbereiten**

   Stellen Sie sicher, dass Ihr Raspberry Pi mit dem Internet verbunden ist, und aktualisieren Sie anschließend das System:

   ::

      sudo apt update
      sudo apt upgrade

   .. note::
      Wenn Sie **Raspberry Pi OS Lite** verwenden, installieren Sie zunächst die erforderlichen Python-3-Pakete:

      ::

         sudo apt install git python3-pip python3-setuptools python3-smbus

#. **robot-hat installieren**

   Laden Sie das Modul ``robot-hat`` herunter und installieren Sie es:

   ::

      cd ~/
      git clone -b 2.5.x https://github.com/sunfounder/robot-hat.git --depth 1
      cd robot-hat
      sudo python3 install.py

#. **vilib installieren**

   Laden Sie das Modul ``vilib`` herunter und installieren Sie es:

   ::

      cd ~/
      git clone https://github.com/sunfounder/vilib.git --depth 1
      cd vilib
      sudo python3 install.py

#. **picar-x installieren**

   Laden Sie das Modul ``picar-x`` herunter und installieren Sie es:

   ::

      cd ~/
      git clone -b 2.1.x https://github.com/sunfounder/picar-x.git --depth 1
      cd picar-x
      sudo pip3 install . --break

   Dieser Schritt kann etwas Zeit in Anspruch nehmen. Bitte haben Sie Geduld.

#. **Sound aktivieren (I2S-Verstärker)**

   Um die Audioausgabe zu aktivieren, führen Sie das Skript ``i2samp.sh`` aus, um die erforderlichen I2S-Verstärkerkomponenten zu installieren:

   ::

      cd ~/robot-hat
      sudo bash i2samp.sh

   Folgen Sie den Anweisungen auf dem Bildschirm, indem Sie ``y`` eingeben und die Eingabetaste drücken, um fortzufahren, ``/dev/zero`` im Hintergrund auszuführen und den PiCar-X neu zu starten.

   .. note::
      Wenn nach dem Neustart kein Ton zu hören ist, versuchen Sie, das Skript ``i2samp.sh`` mehrmals auszuführen.
