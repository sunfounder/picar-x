Introduction 
====================


The History of Self-driving Car
----------------------------------------

Experiments have been conducted on self-driving cars since at least the 1920s; promising trials took place in the 1950s and work has proceeded since then. 
The first self-sufficient and truly autonomous cars appeared in the 1980s, 
with Carnegie Mellon University's Navlab and ALV projects in 1984 and Mercedes-Benz and Bundeswehr University Munich's Eureka Prometheus Project in 1987. 
Since then, numerous major companies and research organizations have developed working autonomous vehicles including Mercedes-Benz, General Motors, 
Continental Automotive Systems, Autoliv Inc., Bosch, Nissan, Toyota, Audi, Volvo, Vislab from University of Parma, Oxford University and Google. 
In July 2013, Vislab demonstrated BRAiVE, a vehicle that moved autonomously on a mixed traffic route open to public traffic.
As of 2019, twenty-nine U.S. states have passed laws permitting autonomous cars.

Some UNECE members and EU members and the UK have some rules and regulations related to automated and fully automated cars: 
In Europe, cities in Belgium, France, Italy and the UK are planning to operate transport systems for driverless cars, and Germany, 
the Netherlands, and Spain have allowed testing robotic cars in traffic.
In 2020, the UK, the EU and Japan are also on track to regulate automated cars.

* REF: `History of self-driving cars - Wikipedia <https://en.wikipedia.org/wiki/History_of_self-driving_cars>`_


Today, self-driving is the closest technological revolution at hand. Some experts predict that around 2025, Level 4 car are likely to enter the market. Allowing drivers to divert their attention to something else entirely, and eliminating the need to pay attention to traffic conditions as long as the system is functioning properly.

* `SAE Levels of Driving Automation™  <https://www.sae.org/blog/sae-j3016-update>`_
* `ABI Research Forecasts 8 Million Vehicles to Ship with SAE Level 3, 4 and 5 Autonomous Technology in 2025 <https://www.abiresearch.com/press/abi-research-forecasts-8-million-vehicles-ship-sae-level-3-4-and-5-autonomous-technology-2025/>`_

.. image:: img/self_driving_car.jpeg

Recent rapid advances in software (AI), hardware (GPUs, FPGAs, etc.) and cloud computing are driving this technological revolution.

* In October 2010, a driverless truck designed by the Italian technology company **Vislab** took three months to `start in Italy and reach China <http://edition.cnn.com/2010/TECH/innovation/10/27/driverless.car/>`_, with a total distance of 8, 077 miles.
* In April 2015, a car designed by Delphi Automotive traveled from `San Francisco to New York <https://money.cnn.com/2015/04/03/autos/delphi-driverless-car-cross-country- trip/>`_ , traversing 3,400 miles, completing 99 percent of that distance under computer control. 
* In December 2018, **Alphabet**'s **Waymo** launched a `level 4 self-driving taxi service in Arizona <https://www.reuters.com/article/us-waymo-selfdriving-focus/waymo-unveils-self- driving-taxi-service-in-arizona-for-paying-customers-idUSKBN1O41M2>`_ , where they had been testing driverless cars - with no safety driver in the seat - for more than a year and over 10 million miles before.
* In October 2020, **Baidu** fully opened its `Apollo Robotaxi self-driving cab service <http://autonews.gasgoo.com/icv/70017615.html>`_ in Beijing. The driving routes will cover local residential areas, commercial and leisure areas and industrial parks, and other multi-dimensional practical life scenarios.

Yet despite the large amount of data collected every day (including training data from real driving records and simulated scenarios), the growing complexity of AI models for self-driving car has not been fully met.

According to `RAND's report <https://www.rand.org/pubs/research_reports/RR1478.html>`_ , reaching this level of autonomous learning requires training hundreds of millions or even hundreds of billions of miles of training data to prove reliability.

So while the future of self-driving cars is promising and exciting, there are still a few years to go before the technology matures and becomes fully accessible.

The best way to make a technology mature quickly is to make it easily accessible to everyone and to minimize the entry requirements. This is our main motivation for launching PiCar-X.

Our goal is to help beginners and those who want to learn about autonomous driving to understand its development, technology overview and the latest developments.


About PiCar-X
-------------------

.. image:: img/picar-x.jpg

PiCar-X is an AI self-driving robot car for Raspberry Pi, on which RPi works as the control center. 
The mounted camera module, ultrasonic module, line tracking module can separately realize the functions of color/face/traffic signs detection, automatic obstacle avoidance, automatic line tracking, etc.

Taking the SunFounder-designed Robot HAT as the driving module, PiCar-X integrates the motor driving, servo driving and presets ADC, PWM, Digital pins for your function extension. 
A speaker has already been inserted in the Robot HAT to realize TTS (Text-to-Speech), sound effect, background music, etc.

All its functions (including GPIO control, computer vision and deep learning) are implemented by Python (actual programming language), OpenCV (powerful computer vision software package), Tensorflow (Google's popular deep learning framework) and other software.


Think Further
---------------------
This is optional reading. If you want to learn more about deep learning, here are some other resources for you.

`Machine Learning - Andrew Ng <https://www.coursera.org/learn/machine-learning>`_ : This course provides a broad introduction to machine learning, datamining, and statistical pattern recognition. 

`Neural Networks and Deep Learning <http://neuralnetworksanddeeplearning.com/>`_ : This book will teach you about: Neural networks, a beautiful biologically-inspired programming paradigm which enables a computer to learn from observational data. Deep learning, a powerful set of techniques for learning in neural networks

`Rethinking the Inception Architecture for Computer Vision <https://arxiv.org/abs/1512.00567>`_ : Exploring ways to scale up networks in ways that aim at utilizing the added computation as efficiently as possible by suitably factorized convolutions and aggressive regularization.