.. note::

    Hola, bienvenido a la comunidad de entusiastas de SunFounder Raspberry Pi, Arduino y ESP32 en Facebook. Profundiza en Raspberry Pi, Arduino y ESP32 junto con otros entusiastas.

    **¿Por qué unirte?**

    - **Soporte experto**: Resuelve problemas postventa y desafíos técnicos con la ayuda de nuestra comunidad y equipo.
    - **Aprende y comparte**: Intercambia consejos y tutoriales para mejorar tus habilidades.
    - **Preestrenos exclusivos**: Obtén acceso anticipado a anuncios de nuevos productos y adelantos exclusivos.
    - **Descuentos especiales**: Disfruta de descuentos exclusivos en nuestros productos más recientes.
    - **Promociones festivas y sorteos**: Participa en sorteos y promociones especiales durante las festividades.

    👉 ¿Listo para explorar y crear con nosotros? Haz clic en [|link_sf_facebook|] y únete hoy mismo.

Introducción
====================


La historia de los coches autónomos
----------------------------------------

Se han realizado experimentos con coches autónomos desde al menos la década de 1920. 
Se llevaron a cabo pruebas prometedoras en la década de 1950, y desde entonces se ha 
seguido avanzando en esta tecnología. Los primeros coches verdaderamente autónomos y 
autosuficientes aparecieron en la década de 1980, con los proyectos Navlab y ALV de 
la Universidad Carnegie Mellon en 1984, y el Proyecto Eureka Prometheus de Mercedes-Benz 
y la Universidad de la Bundeswehr en Múnich en 1987. Desde finales de los años 80, 
diversas organizaciones de investigación y grandes fabricantes de automóviles han 
desarrollado vehículos autónomos en funcionamiento, incluidos: Mercedes-Benz, General 
Motors, Continental Automotive Systems, Autoliv Inc., Bosch, Nissan, Toyota, Audi, 
Volvo, Vislab de la Universidad de Parma, la Universidad de Oxford y Google. En julio 
de 2013, Vislab demostró BRAiVE, un vehículo que se desplazaba de manera autónoma en 
una ruta mixta de tráfico abierta al público. A partir de 2019, veintinueve estados 
de EE. UU. ya han aprobado leyes que permiten la circulación de coches autónomos en 
vías públicas.

Algunos miembros de la UNECE y miembros de la UE, incluido el Reino Unido, han 
promulgado normas y regulaciones relacionadas con los coches automatizados y 
completamente automatizados. En Europa, ciudades de Bélgica, Francia, Italia y 
el Reino Unido tienen planes para operar sistemas de transporte para coches sin 
conductor, y Alemania, los Países Bajos y España ya han permitido la prueba de 
coches robóticos en el tráfico público. En 2020, el Reino Unido, la UE y Japón 
ya estaban en camino de regular los coches automatizados.

* Reference: `History of self-driving cars - Wikipedia <https://en.wikipedia.org/wiki/History_of_self-driving_cars>`_

Hoy en día, los coches autónomos son la revolución tecnológica más cercana. Algunos expertos predicen que para el año 2025, es probable que los coches de Nivel 4 ingresen al mercado. Los coches de Nivel 4 permitirán a los conductores desviar su atención por completo hacia otras actividades, eliminando la necesidad de prestar atención a las condiciones del tráfico, siempre que el sistema funcione correctamente.

Referencia de Nivel 4:

* `SAE Levels of Driving Automation™  <https://www.sae.org/blog/sae-j3016-update>`_
* `ABI Research Forecasts 8 Million Vehicles to Ship with SAE Level 3, 4 and 5 Autonomous Technology in 2025 <https://www.abiresearch.com/press/abi-research-forecasts-8-million-vehicles-ship-sae-level-3-4-and-5-autonomous-technology-2025/>`_

.. image:: img/self_driving_car.jpeg

Los recientes avances rápidos en software (Inteligencia Artificial, Aprendizaje Automático), hardware (GPUs, FPGAs, acelerómetros, etc.) y computación en la nube están impulsando esta revolución tecnológica.

* En octubre de 2010, un camión autónomo diseñado por la empresa tecnológica italiana **Vislab** tardó tres meses en `viajar desde Italia hasta China <http://edition.cnn.com/2010/TECH/innovation/10/27/driverless.car/>`_, cubriendo una distancia total de 8,077 millas.
* En abril de 2015, un coche diseñado por **Delphi Automotive** viajó desde `San Francisco to New York <https://money.cnn.com/2015/04/03/autos/delphi-driverless-car-cross-country- trip/>`_, recorriendo 3,400 millas y completando el 99 % de esa distancia bajo control computarizado.
* En diciembre de 2018, **Waymo** de **Alphabet** lanzó un `level 4 self-driving taxi service in Arizona <https://www.reuters.com/article/us-waymo-selfdriving-focus/waymo-unveils-self- driving-taxi-service-in-arizona-for-paying-customers-idUSKBN1O41M2>`_, donde ya habían estado probando coches sin conductor desde 2008. Sin nadie en el asiento del conductor, los vehículos operaron durante más de un año y recorrieron más de 10 millones de millas.
* En octubre de 2020, **Baidu** inauguró por completo su servicio de taxi autónomo `Apollo Robotaxi <http://autonews.gasgoo.com/icv/70017615.html>`_ en Pekín. Las rutas cubren áreas residenciales, comerciales, de ocio y parques industriales locales, y ofrecen un sistema de conducción completamente autónomo.

Sin embargo, a pesar de la enorme cantidad de datos recopilados a diario, incluidos los datos de entrenamiento de registros de conducción reales y escenarios simulados, la complejidad de los modelos de IA para los coches autónomos aún no se ha resuelto por completo.

Según el `RAND's report <https://www.rand.org/pubs/research_reports/RR1478.html>`_, alcanzar el nivel adecuado de aprendizaje autónomo requiere datos de entrenamiento de cientos de millones o incluso miles de millones de millas para establecer un nivel de fiabilidad.

Por lo tanto, aunque el futuro de los coches autónomos es prometedor y emocionante, aún quedan muchos años de desarrollo antes de que la tecnología madure lo suficiente como para ser completamente accesible en el mercado de coches autónomos.

La forma comprobada de permitir que una tecnología emergente madure rápidamente es hacerla fácilmente accesible para todos, minimizando los requisitos de entrada al mercado. Esta es la motivación de SunFounder para lanzar PiCar-X.

El objetivo de SunFounder es ayudar a principiantes, novatos y a aquellos que simplemente desean aprender sobre conducción autónoma, a comprender el proceso de desarrollo, la tecnología y las últimas innovaciones en vehículos autónomos.

Sobre el PiCar-X
-------------------

.. .. image:: img/picar-x.jpg

El PiCar-X es un coche robot autónomo controlado por IA para la plataforma Raspberry Pi, en la que la Raspberry Pi actúa como el centro de control. El módulo de cámara de 2 ejes, el módulo ultrasónico y los módulos de seguimiento de líneas del PiCar-X proporcionan funciones como la detección de colores, caras y señales de tráfico, la evitación automática de obstáculos, el seguimiento automático de líneas, entre otros.

Con la placa Robot HAT diseñada por SunFounder, el PiCar-X integra motores de conducción izquierda/derecha, motores servo para la dirección y las funciones de paneo/inclinación de la cámara, y preconfigura los pines ADC, PWM y Digital I2C del Robot HAT para permitir extensiones de la funcionalidad estándar de la Raspberry Pi. Tanto un altavoz como un chip Bluetooth han sido integrados en el Robot HAT para el control remoto de texto a voz, efectos de sonido o incluso funciones de música de fondo.

Todas las funciones del PiCar-X, incluido el control GPIO, la visión por computadora y el aprendizaje profundo, se implementan a través del lenguaje de programación de código abierto Python, la biblioteca de visión por computadora OpenCV y TensorFlow de Google para los marcos de aprendizaje profundo. Se ha incluido otro software para optimizar las capacidades del PiCar-X, permitiendo al usuario un entorno de aprendizaje casi ilimitado.


Aprendizaje profundo y redes neuronales
-------------------------------------------------
Para aprender más sobre aprendizaje profundo y redes neuronales, SunFounder recomienda los siguientes recursos:

`Machine Learning - Andrew Ng <https://www.coursera.org/learn/machine-learning>`_ : Este curso proporciona una introducción amplia al aprendizaje automático, la minería de datos y el reconocimiento estadístico de patrones.

`Neural Networks and Deep Learning <http://neuralnetworksanddeeplearning.com/>`_ : Este libro electrónico cubre tanto las redes neuronales, un paradigma de programación inspirado biológicamente que permite a una computadora aprender a partir de datos observacionales, como el aprendizaje profundo, un poderoso conjunto de técnicas para el aprendizaje automático en redes neuronales.

`Repensando la Arquitectura Inception para la Visión por Computadora <https://arxiv.org/abs/1512.00567>`_ : Este documento técnico de alto nivel explora los métodos que los usuarios pueden utilizar para escalar redes mediante el uso de cálculos adicionales de manera eficiente a través de convoluciones factorizadas y regularización agresiva.
