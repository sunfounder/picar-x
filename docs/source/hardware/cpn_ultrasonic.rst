.. note::

    Ciao, benvenuto nella Community di appassionati di Raspberry Pi & Arduino & ESP32 di SunFounder su Facebook! Esplora più a fondo Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi i problemi post-vendita e affronta le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e anteprime riservate.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Omaggi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti subito!

Modulo Ultrasuoni
================================

.. image:: img/ultrasonic_pic.png
    :width: 400
    :align: center

* **TRIG**: Ingresso impulso di trigger
* **ECHO**: Uscita impulso di eco
* **GND**: Massa
* **VCC**: Alimentazione 5V

Questo è il sensore di distanza ultrasonico HC-SR04, che fornisce una misurazione senza contatto da 2 cm a 400 cm con una precisione di portata fino a 3 mm. Il modulo include un trasmettitore ultrasonico, un ricevitore e un circuito di controllo.

È sufficiente collegare 4 pin: VCC (alimentazione), Trig (trigger), Echo (ricezione) e GND (massa) per renderlo facile da usare nei tuoi progetti di misurazione.

**Caratteristiche**

* Tensione di funzionamento: DC5V
* Corrente di funzionamento: 16mA
* Frequenza di lavoro: 40Hz
* Gamma massima: 500cm
* Gamma minima: 2cm
* Segnale di ingresso di trigger: impulso TTL di 10uS
* Segnale di uscita di eco: segnale di livello TTL di ingresso e gamma proporzionale
* Connettore: XH2.54-4P
* Dimensioni: 46x20.5x15 mm

**Principio**

I principi di base sono i seguenti:

* Utilizzare il trigger IO per un segnale alto di almeno 10us.
* Il modulo invia una raffica di 8 cicli di ultrasuoni a 40 kHz e rileva se viene ricevuto un segnale di impulso.
* L'eco emetterà un livello alto se viene restituito un segnale; la durata del livello alto è il tempo dall'emissione al ritorno.
* Distanza = (tempo del livello alto x velocità del suono (340M/S)) / 2

    .. image:: img/ultrasonic_prin.jpg
        :width: 800

Formula:

* us / 58 = distanza in centimetri
* us / 148 = distanza in pollici
* distanza = tempo del livello alto x velocità (340M/S) / 2


**Note Applicative**

* Questo modulo non deve essere collegato sotto tensione; se necessario, collegare prima il GND del modulo. Altrimenti, influenzerà il funzionamento del modulo.
* L'area dell'oggetto da misurare deve essere di almeno 0,5 metri quadrati e il più piatta possibile. Altrimenti, i risultati saranno influenzati.
