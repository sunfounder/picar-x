Introduction 
====================


The History of Self-driving Cars
----------------------------------------

Experiments have been conducted on self-driving cars since at least the 1920’s. 
Promising trials took place in the 1950’s, and work has proceeded forward ever since. 
The first self-sufficient and truly autonomous cars appeared in the 1980’s, 
with Carnegie Mellon University’s Navlab and ALV projects in 1984, 
and Mercedes-Benz and Bundeswehr University Munich’s Eureka Prometheus Project in 1987. Since the late 1980’s, 
numerous research organizations and major automakers have developed working autonomous vehicles, 
including: Mercedes-Benz, General Motors, Continental Automotive Systems, Autoliv Inc., Bosch, Nissan, Toyota, 
Audi, Volvo, Vislab from University of Parma, Oxford University, and Google. 
In July 2013, Vislab demonstrated BRAiVE, a vehicle that moved autonomously on a mixed traffic route open to the public. 
As of 2019, twenty-nine U.S. states have already passed laws permitting autonomous cars on public roadways.

Some UNECE members and EU members, including the UK, 
have enacted rules and regulations related to automated and fully automated cars. 
In Europe, cities in Belgium, France, Italy, and the UK have plans in place to operate transport systems for driverless cars, 
and Germany, the Netherlands, and Spain have already allowed the testing of robotic cars in public traffic. 
In 2020, the UK, the EU, and Japan are already on track to regulate automated cars.

* Reference: `History of self-driving cars - Wikipedia <https://en.wikipedia.org/wiki/History_of_self-driving_cars>`_


Today, self-driving cars are the closest technological revolution at hand. Some experts predict that by 2025, Level 4 cars are likely to enter the market. The Level 4 cars will allow drivers to divert their attention to something else entirely, eliminating the need to pay attention to traffic conditions as long as the system is functioning properly.

Level 4 reference:

* `SAE Levels of Driving Automation™  <https://www.sae.org/blog/sae-j3016-update>`_
* `ABI Research Forecasts 8 Million Vehicles to Ship with SAE Level 3, 4 and 5 Autonomous Technology in 2025 <https://www.abiresearch.com/press/abi-research-forecasts-8-million-vehicles-ship-sae-level-3-4-and-5-autonomous-technology-2025/>`_

.. image:: img/self_driving_car.jpeg

Recent rapid advances in software (Artificial Intelligence, Machine Learning), hardware (GPUs, FPGAs, accelerometers, etc.), and cloud computing are driving this technological revolution forward.

* In October 2010, a driverless truck designed by the Italian technology company **Vislab** took three months to `travel from Italy to China <http://edition.cnn.com/2010/TECH/innovation/10/27/driverless.car/>`_, with a total distance of 8, 077 miles.
* In April 2015, a car designed by **Delphi Automotive** traveled from `San Francisco to New York <https://money.cnn.com/2015/04/03/autos/delphi-driverless-car-cross-country- trip/>`_ , traversing 3,400 miles, completing 99 percent of that distance under computer control. 
* In December 2018, **Alphabet**'s **Waymo** launched a `level 4 self-driving taxi service in Arizona <https://www.reuters.com/article/us-waymo-selfdriving-focus/waymo-unveils-self- driving-taxi-service-in-arizona-for-paying-customers-idUSKBN1O41M2>`_ , where they had already been testing driverless cars since 2008. With no one in the driver's seat, the vehicles operated for more than a year and traveled over 10 million miles.
* In October 2020, **Baidu** fully opened its `Apollo Robotaxi self-driving cab service <http://autonews.gasgoo.com/icv/70017615.html>`_ in Beijing. The driving routes cover local residential, commercial, leisure, and industrial parks areas, and offer a fully autonomous driving system.

However, despite the massive amounts of data collected every day, including training data from real driving records and simulated scenarios, the complexity of AI models for self-driving cars has not been fully met.

According to `RAND's report <https://www.rand.org/pubs/research_reports/RR1478.html>`_ , reaching the appropriate level of autonomous learning requires training data from hundreds of millions, or even hundreds of billions of miles to establish a level of reliability.

So, while the future of self-driving cars is promising and exciting, there are still many more years of development to go before the technology has matured enough to become fully accessible to the self-driving car market.

The proven way to allow an emerging technology to quickly mature is to make it easily accessible to everyone by minimizing the market-entry requirements. 
This is SunFounders motivation for launching PiCar-X.

SunFounders goal is to help beginners, novices, and those who simply just want to learn about autonomous driving, to understand the development process, the technology, and the latest innovations in self-driving vehicles.


About PiCar-X
-------------------

.. image:: img/picar-x.jpg

The PiCar-X is an AI-controlled self-driving robot car for the Raspberry Pi platform, upon which the Raspberry Pi acts as the control center. The PiCar-X’s 2-axis camera module, ultrasonic module, and line tracking modules can provide the functions of color/face/traffic signs detection, automatic obstacle avoidance, automatic line tracking, etc.

With the SunFounder-designed Robot HAT board, the PiCar-X integrates left/right driving motors, servo motors for steering and the camera’s pan/tilt functions, and pre-sets the Robot HAT’s ADC, PWM, and Digital I2C pins to allow for extensions to the standard functionality of the Raspberry Pi. Both a speaker and a bluetooth chip have been engineered into the Robot HAT for remote control of Text-to-Speech, sound effects, or even background music functionality.

All of the PiCar-X functions, including GPIO control, computer vision, and deep learning, are implemented through the open sourced Python programming language, OpenCV’s Computer Vision Library software, and Google’s TensorFlow for deep learning frameworks. Other software has been included to optimize the PiCar-X capabilities, allowing the user a near-limitless learning environment.


Deep Learning and Neural Networks
-------------------------------------------------
To learn more about deep learning and Neural Networks, SunFounder recommends the following resources:

`Machine Learning - Andrew Ng <https://www.coursera.org/learn/machine-learning>`_ : This course provides a broad introduction to machine learning, datamining, and statistical pattern recognition. 

`Neural Networks and Deep Learning <http://neuralnetworksanddeeplearning.com/>`_ : This E-book covers both Neural Networks, a biologically-inspired programming paradigm that enables a computer to learn from observational data, and Deep learning, a powerful set of techniques for machine learning in neural networks.

`Rethinking the Inception Architecture for Computer Vision <https://arxiv.org/abs/1512.00567>`_ : This high-level white-paper explores the methods users can scale up networks by utilizing added computations as efficiently as possible through factorized convolutions and aggressive regularization.