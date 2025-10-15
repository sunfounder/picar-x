.. note::

    Ciao, benvenuto nella Community SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Approfondisci le tue conoscenze su Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato ai nuovi annunci di prodotto e alle anteprime esclusive.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni e Giveaway Festivi**: Partecipa a promozioni e omaggi durante le festività.

    👉 Sei pronto per esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti oggi stesso!

1. Di cos’altro hai bisogno?
===============================

Prima di iniziare a giocare con PiCar-X, prepariamo l’hardware essenziale.  
Pensa a questi componenti come al **cervello, cuore e sensi** di PiCar-X — senza di essi, l’auto non può funzionare correttamente.

Componenti richiesti
------------------------------

* **Raspberry Pi**

  Il Raspberry Pi funge da **cervello** di PiCar-X, gestendo tutte le operazioni di calcolo, rilevamento e controllo.
  
  .. image:: img/need_pi.jpg

  * **Modelli compatibili**: Compatibile con Raspberry Pi 5, 4, 3 e Raspberry Pi Zero 2 W (migliori prestazioni con Pi 5 o Pi 4).  
  * **Minimo**: **2GB di RAM** — sufficiente per tutte le funzioni standard di PiCar-X (movimento, sensori, streaming della fotocamera) e per l’utilizzo di **servizi AI online** come OpenAI Whisper, TTS o LLM.  
  * **Consigliato**: **4GB di RAM o più** — garantisce prestazioni più fluide quando si eseguono **modelli AI locali** (es. Vosk per il riconoscimento vocale, Piper TTS o LLM leggeri) insieme a streaming e controllo della fotocamera.  
  

* **Alimentatore**

  PiCar-X è dotato di un **pacchetto batterie 18650** e di una scheda **Robot HAT** con circuito di ricarica integrato.
  
  .. image:: img/need_power.png
    :width: 400

  * Per la ricarica si consiglia di utilizzare un alimentatore da **5V 3A**, come l’**adattatore USB-C ufficiale da 15W** per Raspberry Pi.  
  * È anche possibile utilizzare un **caricatore USB-C Power Delivery (PD)** o un **caricatore QC 2.0**.  
  * Una carica completa richiede circa **2 ore** (dallo 0% al 100%).  


* **Scheda Micro SD**

  Il Raspberry Pi non dispone di un disco rigido integrato. Si avvia e archivia tutti i file su una **scheda Micro SD**.
  
  .. image:: img/need_sd.jpg
    :width: 200

  * Minimo: **16GB**  
  * Consigliato: **32GB** per una maggiore stabilità  
  * Marca: Usa opzioni affidabili come **SanDisk** o **Samsung** per evitare errori di lettura/scrittura  
  

Componenti opzionali
------------------------

Sebbene non strettamente necessari, i seguenti accessori miglioreranno notevolmente la tua esperienza di apprendimento e debug:

* **Monitor (HDMI o TV)** 

  Per i principianti, consigliamo vivamente un display con ingresso HDMI, in modo da poter configurare facilmente Raspberry Pi OS ed eseguire programmi grafici.

  .. image:: img/need_screen.png
    :width: 400

* **Cavo HDMI (Standard / Mini / Micro)**
 
  I diversi modelli di Raspberry Pi utilizzano connettori HDMI diversi: assicurati di controllare il modello del tuo Pi e preparare il cavo corretto.
  
  * **Raspberry Pi 4 / 5**: Micro HDMI  
  * **Raspberry Pi 3**: HDMI standard  
  * **Raspberry Pi Zero 2W**: Mini HDMI 

  .. image:: img/need_hdmi.png
    :width: 400

* **Tastiera e Mouse**

  Molto utili durante la configurazione iniziale di Raspberry Pi OS. Successivamente potrai passare all’accesso remoto (SSH/VNC), ma per i principianti si consiglia di preparare un set USB o wireless di base.

  .. image:: img/need_keyboard_mouse.png
    :width: 500
  

**Suggerimenti per la preparazione**

* Se hai acquistato il **kit PiCar-X**, la maggior parte degli accessori è inclusa, ma dovrai comunque procurarti separatamente la scheda Raspberry Pi, la scheda Micro SD e l’alimentatore.  
* Non sai cosa comprare? 👉 La scelta più stabile e universale è:  
  **Raspberry Pi 4 (2GB) + Alimentatore ufficiale + Scheda Micro SD da 32GB**.
