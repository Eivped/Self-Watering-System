### Current project status: Under development

# Self Watering System (Raspberry Pi)
In this project we have planned to create a self watering system. The reason we want to create this is to find a solution on how we can go on vacation, and come home to plants that are still alive because of regular watering.

The idea is to measure the moisture in the soil to find out if the plant need more water. Based on how moist the soil is, a valve will open that water for x number of seconds before turning off again.

Thinking: If the moisture level is lower than X -> Open the water valve/run a water pump for X number of seconds.

Our team have never create a project like this before, so we are looking forward to continue on the project.

## Goals of our project
- Setting up the raspberry and connect the soil moisture sensor 
- Get values from the soil moisture sensor through the raspberry 
- Create a source code that opens a valve/run a water pump based on the value from the soil moisture sensor 

## Goals related to Blynk
 - Implement the Blynk application into our code so that we could see the soil moisture levels on our phones
 - Implement a function that open the valve/run a water pump through the Blynk application
 - Implement a function that read temperature and display it on Blynk
 - Implement a function that check the battery status and display in on Blynk 
 - Check the amout water that is in the container (extra sensor, watersensor)

## Quality assurance
The way that our team has decited to assure the quality of our product is by doing a form of TDD (Test-driven development). Wikipedia definds test-driven development as a "software development process that depends on the repetition of a very short development cycle: requirements are transformed into very specific test cases, then the software is improved so that the tests run"([Wikipedia, 2019](https://en.wikipedia.org/wiki/Test-driven_development)). 

While developing our product, we focus on one task at the time and test if it works proparly before we move further on to impementing more functionalities. The reason why we use this method of quality assurance is because our team have previous experience with this way of workning. It is also an agile way of working. From previous courses, we have gains positive relations to working with Scrum which also is an agile process framwork. Based on frequently testing during the development process will hopefully lead to a product with solid quality.  


## UN sustainable development goals (This topic is under development)
Our project in relation with UN sustainable development goals. These are the sustainable development goals that we expect to have in mind while developing this project. 
- 7 Afortable and clean energy
- 9 Industry, innovation and infrastructure 
- 11 Sustainable cities and communities 
- 12 Responsible consumption and production
- 15 Life on land
- 17 Partnership for the goals 
![All-SDGs](https://user-images.githubusercontent.com/35767860/68113261-ab8a8200-fef3-11e9-836e-1df7e036fd24.png)
 
## Result
- Comming soon

## Sources 
This is some of the sources that we have looked at before we have started our project.

- [Raspberry Pi Automated Plant Watering with Website](https://www.hackster.io/ben-eagan/raspberry-pi-automated-plant-watering-with-website-8af2dc?fbclid=IwAR2rEpD0V7SEx4g1vGgj0U8mOxeUxVy_Q9KWB-vI02odI4YQJSIKDzuGXjQ)
- [Raspberry Pi Automated Plant Watering with Website Video](https://www.youtube.com/watch?v=mQNJpWkdmbc&fbclid=IwAR2Lyb3M1nQq5Sxov5kAUKKsR2CUb9sm5UqoXmdDzFW9va9EiDJQGwjvSc0)
- [Automated Plant Watering with a Raspberry Pi](http://www.cyber-omelette.com/2017/09/automated-plant-watering.html)
- [Soil Moisture Sensor (Raspberry Pi) Video](https://www.youtube.com/watch?v=9LxrX5Eeukg&fbclid=IwAR0FE4Wo4NlOYpyUm4fB3W9ZQpody4zdgLYMwzWjMiEy8pgzE_xLgZLLtiQ)
- [Soil Moisture Sensor](http://www.piddlerintheroot.com/soil-moisture-sensor/)

## Equipment
- Raspberry Pi 3b +                              
- Jumper cables
- Soil moisture sensor
- Water pump
- Water container                                                         
- PVC tube
- Blynk Application

In addition to this equipment, we are going to use our own laptops (pc and mac) as well as our phones (IOS - iPhones). 
We also had a monitor, keyboard and mouse to work directly on the Pi.

## General information 
- This is a school project created by students 
- The programming language that are used in this project is Python
- We use the knowledge that we have gatherd through the our study program at IT and Informations Systems, Bachelor

## First meeting with Blynk (Application)
Through the study we are taking, IT and information systems, we have a subject called Internet Technologies. In this subject we have covered everything from IoT, AI, machine learning and more. In addition to this, we have this project that we are working on during our 5th semester at Universitetet i Agder, Kristiansand.

One of the tasks we have done is to create an iRAT (Individual Readiness Assurance Test), tRAT (Team Readiness Assurance Test) and an ICA (In Class Activity) which is a form of Team-based learning. We chose to focus on IoT, and generated a test that later was used in class. The questions we created were based on the IoT and the syllabus we went through in class. 
After we had gathered the results we saw that there were generally good results. This may indicate that we may made too simple questions, poorly formulated alternatives, or that the class is incredibly skilled within IoT (something we obviously believe).

For our ICA (In Class Activity) we chose to give our class the following task: 
- Connect the Raspberry Pi to a network
- Build a circuit that uses an LED bulb
- Set up Blink (App) and control the LED bulb over Wi-Fi

This should basically be pretty straight forward, and it is not very complicated. We thought this might be too easy, but we had limited time on our ICA. If someone had finished quickly, we made an extra assignment:
- Imagine that the LED bulb poses a fire hazard. Set up a sensor that can measure temperature and alert Blynk in case of temperature increase

Most of the groups managed the first part of the task, but had too little time to start on task two. Our group that was responsible for creating the ICA chose to do the same project with the other students. This was a success and we managed to create the first part of the project. We got started on part two of the task, but had some trouble connecting the temperature sensor to the Raspberry Pi we used.

Souces that we used to do the first part of our ICA:
- [Blynk help](http://help.blynk.cc/en/articles/583104-how-to-install-node-js-library-on-linux)
- [Blynk YouTube video](https://www.youtube.com/watch?v=LJ3ic8C8CcA)

One problem that occured during the process of creating this project where that we had problems with installing Node.js NPM package. 
After some research, we found that there have been several who have come across the same problem. This led us to help.
- [Problems with installing Node.js NPM package](https://raspberrypi.stackexchange.com/questions/27333/problems-with-installing-node-js-npm-package)

After some Googling and reading, we finally managed to get it to work. 
This was our first meeting with the application Blynk and we see this as a good experience that we will take with us in the development of our self-watering system.

## Instructions 

### Attempts
## Attempt 1:
Building the circuit is the first thing we did to connect sensor to the Raspberry Pi. Since we bought the sensor without doing enough research, we found out that we needed an ADC (Analog-Digital Converter). This meant that we had to create a circuit that was able to receive the signals we received from the sensor and translate it so the Pi understood the information it received. With the help of the internet we came across a useful explanation of how we could solve this problem. The source is linked below. 

- [Measuring soil moisture with raspberry pi](https://tutorials-raspberrypi.com/measuring-soil-moisture-with-raspberry-pi/)

After spending some time connecting everything, we were quite happy with the result. Here are some pictures of how it all look at this point. 

### Everything hooked up and runs as it should
![1](https://user-images.githubusercontent.com/35767860/66339658-df4da880-e943-11e9-9e9f-60511cfd9bb2.jpg)

### The soil moisture sensor has power and collects data
The rope around the cables is mostly for the look, but works as cable management
![2](https://user-images.githubusercontent.com/35767860/66339813-33588d00-e944-11e9-8ee8-c550af5abdad.jpg)

### Overview of how we connected the wires to the Rasperry's GPIO pins
We also used electric tape for cable management
![3](https://user-images.githubusercontent.com/35767860/66339837-3fdce580-e944-11e9-8510-849f2a4e23ab.jpg)

### The connections that we used to connect the ADC to the sensor and raspberry pi
We had too few jumber cables so we had to be creative and make more of the ones we already had.
![4](https://user-images.githubusercontent.com/35767860/66339854-4a977a80-e944-11e9-957f-acd7c3a49f7d.jpg)

### This is how we connected everything
Collected from Raspberry Pi Tutorials. Link bellow the picture.
![Koblingsforklaring (Pi)](https://user-images.githubusercontent.com/35767860/66340818-52f0b500-e946-11e9-8501-14c8385cb66b.png)
- [Raspberry Pi Tutorials](https://tutorials-raspberrypi.com/measuring-soil-moisture-with-raspberry-pi/)

### Conclusion for attempt 1 
- We managed to get some data from the soil moisture sensor. The values that we were introduced to was repeatedly: 35, 255, 550, 860. The highest values was collected when we tested the sensor in water. 35 & 255 is the values that we got when the sensor was dry and not in any soil. 
- A problem that occured is that we did not get a reliable frequence of measurements. The values varied from 35 to 255 without doing anything with the sensor (not in any soil or water).
- Anoter problem that occured is that the source code that we used did not always run as it should.
- We have tried to update Raspbian, as well as every source that we use. Some of the cabeling that we used was not that good and we tried some other cables. This did not work as well as we thought.

## Attempt 2
To start of this attempt, we chose to reinstall the raspbian operating system to start off with a clean Raspberry Pi. 
After a period of time we finally got the new parts to continue with testing and attempt to create the a good solution for our project.
We have now got a new soil moisture sensor that we beliveve is going to make our project much easier to implement in addition to some other parts as well. The team decided to do even more reaseach on how to create this project. So we looked up on the following links:
- [Build a Smart, Automated IoT Plant Irrigation System with Raspberry Pi and PubNub](https://www.pubnub.com/blog/smart-automated-iot-plant-irrigation-system-raspberry-pi-pubnub/)
- [Soil Moisture Sensor](https://www.piddlerintheroot.com/soil-moisture-sensor/)

### Introduction to our new parts

### New soil moisture sensor
We had some problems with the other sensor that we tried out, so we ordered this one. We have seen other simular projects that are using this sensor which was a good step, hopefully,  in the right direction. 
![73262276_2456809481309334_1278103038027890688_n](https://user-images.githubusercontent.com/35767860/67786444-2aed0100-fa6f-11e9-9705-84fa6e3f0b60.jpg)
[Buy here](https://www.ebay.co.uk/itm/302930866767)

### Relay
A relay is used to control a circuit by an independent low-power signal. By using a relay we can turn on and off a swich that have more power than directry from the Raspberry Pi - without hurting the Pi it self.
![75450112_721594501666644_5189100094556733440_n](https://user-images.githubusercontent.com/35767860/67786439-27f21080-fa6f-11e9-861a-7867165858c8.jpg)
[Buy here](https://www.ebay.co.uk/itm/4-Channel-5V-Relay-Module-for-Arduino-TTL-Logik-G2U5-EL/223146727140?epid=1481516985&_trkparms=ispr%3D1&hash=item33f494d6e4:g:VbwAAOSwqmdbnRGt&enc=AQAEAAACQBPxNw%2BVj6nta7CKEs3N0qXk1uYxqGBo%2BoER1o2752CPU6%2BCp2Wz4gkT%2B1d11B8ELcwFyGtt7%2Fmc75DN8rDqh%2F9cxWPNDKRIPU%2B4YcVnwI1M9WrTiYypY8LXHI9BuVfcHjKxag%2BvJuYA19KxMRHtKpaTDqoYxyl26kYY1wGXtRly1KxBrCG3wgQgzNOCJ4BXWHL1YAXusGJGh5S%2FAzF8SPPwjz%2BDMSOqNHo3EhzCWJeL5ACYpcIVt7zovpYZdJ6TfLtSAajgOzheV2nIyhf9P1Of5ba6EjXl13vpyccN7PEKuBUvP0lOnTPfDIiGJD4xVV8te8cSlCEyL0QcmGnJm6%2BER%2BDqWknJ6y%2F1AQZS8WmaQY0unpve0M1GTcdN%2B%2BBBPGF6JbF2QcQe6o0m5fMQ4IGD5J5f6vLRAwHctII8EfK9srP0XqePtp%2B3kQgUQDBg0SFLD7fnYST3tDH0%2BIR0FMIwl9PFKFZ6juStMfZQIoSbzYnpji4i6d1EpdnKuAeWd7cOa3H3E8A5RRnAMYyn%2FaNaHHwxOpjpLHsdOaPIhL1hyKKuFSg952qp8vxE%2BoQjKaFfdKS4CyVAiFmpucGfwaq1S8ZLr%2FMSxXA9YHl2Zy3bAtUpY6Ac%2BCSV5I%2FBE2ciOxWt3u3fMBOL%2FY72FGvXEdd7Ttrg6RCv9laORTp%2FecamXX3Q3pVWaspZp6FEAZddSMLZxn0F9K4WyBM4fwIxo6G9lqHLRCCgwdDJucvwNDbc%2FucoFO%2F0jL33TgA%2B8OLlWA%3D%3D&checksum=223146727140033b4e9c8dbc4f3eb9b33540bff49a47&enc=AQAEAAACQBPxNw%2BVj6nta7CKEs3N0qXk1uYxqGBo%2BoER1o2752CPU6%2BCp2Wz4gkT%2B1d11B8ELcwFyGtt7%2Fmc75DN8rDqh%2F9cxWPNDKRIPU%2B4YcVnwI1M9WrTiYypY8LXHI9BuVfcHjKxag%2BvJuYA19KxMRHtKpaTDqoYxyl26kYY1wGXtRly1KxBrCG3wgQgzNOCJ4BXWHL1YAXusGJGh5S%2FAzF8SPPwjz%2BDMSOqNHo3EhzCWJeL5ACYpcIVt7zovpYZdJ6TfLtSAajgOzheV2nIyhf9P1Of5ba6EjXl13vpyccN7PEKuBUvP0lOnTPfDIiGJD4xVV8te8cSlCEyL0QcmGnJm6%2BER%2BDqWknJ6y%2F1AQZS8WmaQY0unpve0M1GTcdN%2B%2BBBPGF6JbF2QcQe6o0m5fMQ4IGD5J5f6vLRAwHctII8EfK9srP0XqePtp%2B3kQgUQDBg0SFLD7fnYST3tDH0%2BIR0FMIwl9PFKFZ6juStMfZQIoSbzYnpji4i6d1EpdnKuAeWd7cOa3H3E8A5RRnAMYyn%2FaNaHHwxOpjpLHsdOaPIhL1hyKKuFSg952qp8vxE%2BoQjKaFfdKS4CyVAiFmpucGfwaq1S8ZLr%2FMSxXA9YHl2Zy3bAtUpY6Ac%2BCSV5I%2FBE2ciOxWt3u3fMBOL%2FY72FGvXEdd7Ttrg6RCv9laORTp%2FecamXX3Q3pVWaspZp6FEAZddSMLZxn0F9K4WyBM4fwIxo6G9lqHLRCCgwdDJucvwNDbc%2FucoFO%2F0jL33TgA%2B8OLlWA%3D%3D&checksum=223146727140033b4e9c8dbc4f3eb9b33540bff49a47)

### Water pump
The pump that we are using is a sbmersible pump that works very well. Here is a picture of how it looks.
![76702307_499330190651998_7707215458578989056_n](https://user-images.githubusercontent.com/35767860/67786427-2294c600-fa6f-11e9-8961-7ae303157a3c.jpg)
[Buy here](https://www.ebay.co.uk/itm/DC-3V-5V-Micro-Submersible-Pump-Water-Mute-Pump-Low-Noise-DIY-Fish-Tank-Aquarium/283657475848?hash=item420b4d9708:g:zi0AAOSw5r9drV5l)

### AA-Battery holder
To deliver more power to the water pump we had to get an additional power source. This is the one we got.
![75271420_399871984300678_8619613030763724800_n](https://user-images.githubusercontent.com/35767860/67786421-1f013f00-fa6f-11e9-88d7-df6d1cff349a.jpg)
[Buy here](https://www.ebay.com/itm/2-x-AA-3V-Battery-Holder-Connector-Storage-Case-Box-ON-OFF-Switch-With-Lead-Wire/112855488640?hash=item1a46b61880:g:6GIAAOSw01dZnWnZ)

### Building the circuit
Before we assembled all the parts togehter, we did test them individualy to know they worked. We did this by adding power to the motor and see that everything worked as it should. As in the first attempt, we chose to start with building the circuit. This time with the new parts. After connecting everything, we looked over everything to check that the connections were correct - before powering up the Pi. Here are a picture of how it looks at his point.

![73349276_556064008268810_6843775801989529600_n](https://user-images.githubusercontent.com/35767860/67786434-258fb680-fa6f-11e9-8bdd-03c0d6d4b553.jpg)

### This is how we connected everything at attempt number 2
![Attempt22](https://user-images.githubusercontent.com/35767860/67791761-4f011000-fa78-11e9-8109-9c9f839a6f58.jpg)


### Conclution for attempt 2 
- This time we managed to get information from the sensor so that it controlled the water pump.
- The cable management were much easier and it was quite fast to setup.
- As a team, we see that this is a step closer to a more finished product.

### Programming Planty.py
To get this project to work we had to do some programming. We did this by using the Python IDLE that comes with the Raspberry Pi. To start off this process, we did reasearch on how simular projects had been completed. The code that we generated is based on some of the projects that we found online, and the links for the inspiration are below: 
- [IoT Plant](https://github.com/Cakhavan/IoT_Plant/blob/master/Planty.py)
- [Turning on an LED with your Raspberry Pi](https://thepihut.com/blogs/raspberry-pi-tutorials/27968772-turning-on-an-led-with-your-raspberry-pis-gpio-pins)

Our source code is created by testing and trying different things, in the spirit of the term "learning by doing". We think it worked quite well. Take a look at the source code here:
- [Planty.py - source code](https://github.com/nokaas/Self-Watering-System/blob/master/src/soil%20moisture/Planty.py)

## Developers
[Aas, Knut Andreas](https://github.com/nokaas) 

[Andreassen, Jarl](https://github.com/Genijarl)
 
[Mathisen, Vegard Saavesen](https://github.com/vegardmathisen)
  
[Pedersen, Eivind](https://github.com/eivped)
