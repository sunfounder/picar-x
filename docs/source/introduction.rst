Introduction 
====================

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


At present, automatic driving is the technological revolution closest at hand. Some experts predict that around 2025, four-class cars may appear on the market, allowing drivers to entirely shift their attention to other things, and the driver no longer needs to pay attention to traffic conditions so long as the system works normally.

* `SAE Levels of Driving Automation™  <https://www.sae.org/blog/sae-j3016-update>`_
* `ABI Research Forecasts 8 Million Vehicles to Ship with SAE Level 3, 4 and 5 Autonomous Technology in 2025 <https://www.abiresearch.com/press/abi-research-forecasts-8-million-vehicles-ship-sae-level-3-4-and-5-autonomous-technology-2025/>`_

Recently, the vigorous development of software (artificial intelligence), hardware (GPUs, FPGAs, etc.) and cloud computing is advancing this technological revolution.

* In October 2010, the unmanned truck designed by Vislab, an Italian technological company,  lasted for three months, 'from Italy to China <http://edition.cnn.com/2010/TECH/innovation/10/27/driverless.car/>'_ , with a total mileage of 8,077 miles.
* In April, 2015, a car designed by Delphi Automotive crossed 34,000 miles from 'San Francisco to New York <https://money.cnn.com/2015/04/03/autos/delphi-driverless-car-cross-country-trip/>'_ , finishing 99% of the distance under computer control. 
* In December 2018, Alphabet's Waymo launched 'Class-4 self-driving taxi service <https://www.reuters.com/article/us-waymo-selfdriving-focus/waymo-unveils-self-driving-taxi-service-in-arizona-for-paying-customers-idUSKBN1O41M2>'_ , and prior to that, they had already tested driverless cars - without safety drivers in their seats - for more than one year, with more than 10 million miles.
* In October, 2020, Baidu fully opened the 'Apollo Robotax self-driving taxi service <http://autonews.gasgoo.com/icv/70017615.html>'_ . The driving route will cover local residential areas, commercial leisure areas and industrial parks as well as other multi-dimensional practical life scenes.

However, despite that a large amount of data (including real driving records and training data of simulation scenes) can be collected on a daily basis, it cannot fully satisfy the increasing complexity of AI models for autonomous vehicles.
Based on 'RAND's report <https://www.rand.org/pubs/research_reports/RR1478.html>'_ , to achieve this level of autonomous learning, hundreds of millions of miles or even hundreds of billions of miles of training data await to be trained, so as to prove its reliability.

Thus, despite that the future of autonomous vehicles is filled with hope and highly exciting, there is still a few years away from the maturity and comprehensive popularization of technology.

In an attempt to make a kind of technology become mature quickly, the best way is to make it easy for everyone to get and use it, and to lower the entry threshold as much as possible, which is precisely our chief motive of launching Picar-X.
We aim to help beginners and students who wish to know about automatic driving as well as its development history, technical introduction as well as the latest development trends.


About PiCar-X
-------------------

PiCar-X is an AI self-driving robot car for Raspberry Pi, on which RPi works as the control center. 
The mounted camera module, ultrasonic module, line tracking module can separately realize the functions of color detection, 
face detection, automatic obstacle avoidance, automatic line tracking, etc.

All its functions (including GPIO control, computer vision and deep learning) are implemented by Python (actual programming language), OpenCV (powerful computer vision software package), Tensorflow (Google's popular deep learning framework) and other software.


Think Further
---------------------
Here is optional reading part. If you wish to study in greater depth, some other resources are available for your reference.

`Machine Learning - Andrew Ng <https://www.coursera.org/learn/machine-learning>`_ : This course provides a broad introduction to machine learning, datamining, and statistical pattern recognition. 

`Neural Networks and Deep Learning <http://neuralnetworksanddeeplearning.com/>`_ : This book will teach you about: Neural networks, a beautiful biologically-inspired programming paradigm which enables a computer to learn from observational data. Deep learning, a powerful set of techniques for learning in neural networks

`Rethinking the Inception Architecture for Computer Vision <https://arxiv.org/abs/1512.00567>`_ : Exploring ways to scale up networks in ways that aim at utilizing the added computation as efficiently as possible by suitably factorized convolutions and aggressive regularization.