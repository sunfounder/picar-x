.. note::

    Ciao, benvenuto nella Community di appassionati di Raspberry Pi & Arduino & ESP32 di SunFounder su Facebook! Esplora più a fondo Raspberry Pi, Arduino e ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto Esperto**: Risolvi i problemi post-vendita e affronta le sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e Condividi**: Scambia consigli e tutorial per migliorare le tue competenze.
    - **Anteprime Esclusive**: Ottieni accesso anticipato agli annunci di nuovi prodotti e anteprime riservate.
    - **Sconti Speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni Festive e Omaggi**: Partecipa a concorsi e promozioni durante le festività.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti subito!

Introduzione
====================


La Storia delle Auto a Guida Autonoma
----------------------------------------

Gli esperimenti sulle auto a guida autonoma risalgono almeno agli anni '20 
del Novecento. Prove promettenti si sono svolte negli anni '50, e da allora 
il lavoro è proseguito. Le prime auto completamente autonome e autosufficienti 
sono apparse negli anni '80, con i progetti Navlab e ALV della Carnegie Mellon 
University nel 1984, e il progetto Eureka Prometheus di Mercedes-Benz e Bundeswehr 
University Munich nel 1987. Dalla fine degli anni '80, numerose organizzazioni 
di ricerca e grandi case automobilistiche hanno sviluppato veicoli autonomi 
funzionanti, tra cui: Mercedes-Benz, General Motors, Continental Automotive Systems, 
Autoliv Inc., Bosch, Nissan, Toyota, Audi, Volvo, Vislab dell'Università di Parma, 
l'Università di Oxford e Google. Nel luglio 2013, Vislab ha dimostrato BRAiVE, un 
veicolo che si muove autonomamente su una rotta a traffico misto aperta al pubblico. 
A partire dal 2019, ventinove stati americani avevano già approvato leggi che 
consentono alle auto autonome di circolare su strade pubbliche.

Alcuni membri dell'UNECE e dell'UE, inclusi il Regno Unito, hanno emanato regolamenti 
relativi alle auto automatizzate e completamente automatizzate. In Europa, città in 
Belgio, Francia, Italia e Regno Unito hanno in programma di implementare sistemi di 
trasporto per auto senza conducente, e Germania, Paesi Bassi e Spagna hanno già 
consentito il collaudo di auto robotiche nel traffico pubblico. Nel 2020, Regno Unito, 
UE e Giappone erano già sulla buona strada per regolamentare le auto automatizzate.

* Riferimento: `History of self-driving cars - Wikipedia <https://en.wikipedia.org/wiki/History_of_self-driving_cars>`_

Oggi, le auto a guida autonoma sono la prossima rivoluzione tecnologica in arrivo. Alcuni esperti prevedono che entro il 2025 le auto di Livello 4 saranno probabilmente sul mercato. Le auto di Livello 4 consentiranno ai conducenti di dedicarsi completamente ad altro, eliminando la necessità di prestare attenzione alle condizioni del traffico, a condizione che il sistema funzioni correttamente.

Riferimento Livello 4:

* `SAE Levels of Driving Automation™ <https://www.sae.org/blog/sae-j3016-update>`_
* `ABI Research Forecasts 8 Million Vehicles to Ship with SAE Level 3, 4 and 5 Autonomous Technology in 2025 <https://www.abiresearch.com/press/abi-research-forecasts-8-million-vehicles-ship-sae-level-3-4-and-5-autonomous-technology-2025/>`_

.. image:: img/self_driving_car.jpeg

I recenti rapidi progressi nei software (Intelligenza Artificiale, Machine Learning), hardware (GPU, FPGA, accelerometri, ecc.) e nel cloud computing stanno spingendo avanti questa rivoluzione tecnologica.

* Nell'ottobre 2010, un camion senza conducente progettato dalla società tecnologica italiana **Vislab** ha impiegato tre mesi per `travel from Italy to China <http://edition.cnn.com/2010/TECH/innovation/10/27/driverless.car/>`_, coprendo una distanza totale di 8.077 miglia.
* Nell'aprile 2015, un'auto progettata da **Delphi Automotive** ha viaggiato da `San Francisco a New York <https://money.cnn.com/2015/04/03/autos/delphi-driverless-car-cross-country-trip/>`_, percorrendo 3.400 miglia, completando il 99% di quella distanza sotto controllo del computer.
* Nel dicembre 2018, **Waymo** di **Alphabet** ha lanciato un `level 4 self-driving taxi service in Arizona <https://www.reuters.com/article/us-waymo-selfdriving-focus/waymo-unveils-self-driving-taxi-service-in-arizona-for-paying-customers-idUSKBN1O41M2>`_, dove testavano già auto senza conducente dal 2008. Con nessuno al volante, i veicoli hanno operato per più di un anno percorrendo oltre 10 milioni di miglia.
* Nell'ottobre 2020, **Baidu** ha aperto completamente il suo `Apollo Robotaxi self-driving cab service <http://autonews.gasgoo.com/icv/70017615.html>`_, coprendo percorsi che attraversano aree residenziali, commerciali, di svago e parchi industriali locali, offrendo un sistema di guida completamente autonoma.

Tuttavia, nonostante l'enorme quantità di dati raccolti ogni giorno, compresi i dati di addestramento da registrazioni di guida reali e scenari simulati, la complessità dei modelli di AI per le auto a guida autonoma non è stata ancora pienamente affrontata.

Secondo il `RAND's report <https://www.rand.org/pubs/research_reports/RR1478.html>`_, per raggiungere un livello adeguato di apprendimento autonomo sono necessari dati di addestramento provenienti da centinaia di milioni, o addirittura centinaia di miliardi di miglia, per stabilire un livello di affidabilità.

Quindi, sebbene il futuro delle auto a guida autonoma sia promettente e affascinante, ci vorranno ancora molti anni di sviluppo prima che la tecnologia sia abbastanza matura per diventare completamente accessibile al mercato delle auto a guida autonoma.

Il modo comprovato per consentire a una tecnologia emergente di maturare rapidamente è renderla facilmente accessibile a tutti, riducendo al minimo i requisiti di ingresso sul mercato. 
Questo è il motivo per cui SunFounder ha lanciato PiCar-X.

L'obiettivo di SunFounder è aiutare principianti, neofiti e chiunque desideri semplicemente imparare a conoscere la guida autonoma, a comprendere il processo di sviluppo, la tecnologia e le ultime innovazioni nei veicoli a guida autonoma.


Informazioni su PiCar-X
-------------------------------

.. .. image:: img/picar-x.jpg

Il PiCar-X è un'auto robotica a guida autonoma controllata da AI per la piattaforma Raspberry Pi, in cui il Raspberry Pi funge da centro di controllo. Il modulo fotocamera a 2 assi, il modulo ultrasonico e i moduli di rilevamento della linea del PiCar-X consentono funzioni come il riconoscimento di colori/volti/segnali stradali, l'evitamento automatico degli ostacoli, il tracciamento automatico della linea, ecc.

Con la scheda Robot HAT progettata da SunFounder, il PiCar-X integra motori di guida sinistra/destra, servomotori per lo sterzo e le funzioni di pan/tilt della fotocamera, e preimposta i pin ADC, PWM e Digital I2C del Robot HAT per consentire estensioni alle funzionalità standard del Raspberry Pi. Sono stati progettati anche un altoparlante e un chip bluetooth nel Robot HAT per il controllo remoto della sintesi vocale, degli effetti sonori o persino della funzionalità di musica di sottofondo.

Tutte le funzioni del PiCar-X, inclusi il controllo GPIO, la visione artificiale e il deep learning, vengono implementate tramite il linguaggio di programmazione Python open source, la libreria OpenCV per la visione artificiale e TensorFlow di Google per i framework di deep learning. Altri software sono stati inclusi per ottimizzare le capacità del PiCar-X, offrendo all'utente un ambiente di apprendimento praticamente illimitato.

Deep Learning e Reti Neurali
-------------------------------------------------
Per saperne di più su Deep Learning e Reti Neurali, SunFounder consiglia le seguenti risorse:

`Machine Learning - Andrew Ng <https://www.coursera.org/learn/machine-learning>`_ : Questo corso fornisce un'ampia introduzione al machine learning, al datamining e al riconoscimento statistico dei modelli.

`Neural Networks and Deep Learning <http://neuralnetworksanddeeplearning.com/>`_ : Questo E-book copre sia le reti neurali, un paradigma di programmazione ispirato biologicamente che consente a un computer di apprendere dai dati osservativi, sia il deep learning, un potente insieme di tecniche per l'apprendimento automatico nelle reti neurali.

`Rethinking the Inception Architecture for Computer Vision <https://arxiv.org/abs/1512.00567>`_ : Questo white-paper di alto livello esplora i metodi per scalare le reti utilizzando computazioni aggiuntive nel modo più efficiente possibile, attraverso convoluzioni fattorizzate e regolarizzazione aggressiva.
