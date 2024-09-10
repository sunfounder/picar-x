.. note::

    Ciao, benvenuto nella Community di appassionati di Raspberry Pi & Arduino & ESP32 di SunFounder su Facebook! Esplora più a fondo Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi i problemi post-vendita e affronta le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e anteprime riservate.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Omaggi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti subito!

FAQ
===========================

Q1: Dopo aver installato Ezblock OS, il servo non riesce a raggiungere i 0°?
---------------------------------------------------------------------------------

1) Controlla se il cavo del servo è correttamente collegato e se l'alimentazione del Robot HAT è accesa.
2) Premi il pulsante di Reset.
3) Se hai già eseguito un programma in Ezblock Studio, il programma personalizzato per P11 non sarà più disponibile. Puoi fare riferimento all'immagine qui sotto per scrivere manualmente un programma in Ezblock Studio per impostare l'angolo del servo a 0°.

.. image:: img/faq_servo.png

Q2: Utilizzando VNC, ricevo un messaggio che il desktop non può essere visualizzato al momento?
-----------------------------------------------------------------------------------------------------

Nel Terminale, digita ``sudo raspi-config`` per modificare la risoluzione.

Q3: Perché il servo a volte torna alla posizione centrale senza motivo?
------------------------------------------------------------------------------------

Quando il servo viene bloccato da una struttura o da un oggetto e non può raggiungere la posizione prevista, entra in modalità di protezione da spegnimento per evitare il surriscaldamento dovuto a un eccesso di corrente.

Dopo un periodo di interruzione di corrente, se il servo non riceve alcun segnale PWM, tornerà automaticamente alla sua posizione originale.

Q4: Dove posso trovare un tutorial dettagliato sul Robot HAT?
--------------------------------------------------------------------

Puoi trovare un tutorial completo sul Robot HAT qui, inclusi dettagli sull'hardware e sull'API.

* |link_robot_hat|
