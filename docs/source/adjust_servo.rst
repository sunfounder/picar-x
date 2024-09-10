.. note::

    Ciao, benvenuto nella Community di appassionati di Raspberry Pi & Arduino & ESP32 di SunFounder su Facebook! Esplora più a fondo Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi i problemi post-vendita e affronta le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e anteprime riservate.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Omaggi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti subito!

Regolazione del Servo per l'Assemblaggio
===========================================

Prima di assemblare il servo, 
è necessario impostare l'angolo a zero gradi. 
Questo perché il motore del servo ha un range di movimento limitato, 
impostare l'angolo a zero gradi garantisce che il servo sia nella sua 
posizione iniziale e non superi il suo range di movimento quando viene alimentato. 
Se il servo non è impostato a zero gradi prima dell'assemblaggio, 
potrebbe tentare di superare il suo range di movimento quando alimentato, 
rischiando di danneggiare il servo o il sistema meccanico a cui è collegato. 
Pertanto, impostare l'angolo a zero è un passaggio importante per garantire il 
funzionamento sicuro e corretto del motore del servo.

.. image:: img/IMG_9897.png


**Per Utenti Python**

Si prega di fare riferimento a :ref:`quick_guide_python` per completare l'installazione 
del sistema operativo Raspberry Pi e regolare l'angolo dei servomotori.


**Per Utenti Ezblock**

.. note::

    Se stai utilizzando un Raspberry Pi 5, non potrai utilizzare il nostro software di programmazione grafica, EzBlock, per programmare il PiCrawler.

Dopo aver installato il sistema Ezblock, 
è possibile utilizzare il pin P11 per regolare il servo. 
Si prega di fare riferimento a :ref:`ezb_servo_adjust` per ulteriori dettagli.
