### Under development

# Self Watering System (Raspberry Pi)
In this project we have planned to create a self watering system. The reason we want to create this is to find a solution on how we can go on vacation, and come home to plants that are still alive because of regular watering.

The idea is to measure the moisture in the soil to find out if the plant need more water. Based on how moist the soil is, a valve will open that water for x number of seconds before turning off again.

Thinking: If the moisture level is lower than X -> Open the water valve/run a water pump for X number of seconds.

Our team have never createt a project like this before, so we are looking forward to continue on the project.

## Goals of our project
- Setting up the raspberry and connect the soil moisture sensor 
- Get values from the soil moisture sensor through the raspberry 
- Create a source code that opens a valve/run a water pump based on the value from the soil moisture sensor

Blynk:
 - Implement the Blynk application into our code so that we could see the soil moisture levels on our phones
 - Implement a function that open the valve/run a water pump through the Blynk application
 - Implement a function that read temperature and display it on Blynk
 - Implement a function that check the battery status and display in on Blynk 
 - Check the amout water that is in the container (extra sensor, watersensor)

## Result

## Sources 

This is some of the sources that we have looked at before we have started our project.

- https://www.hackster.io/ben-eagan/raspberry-pi-automated-plant-watering-with-website-8af2dc?fbclid=IwAR2rEpD0V7SEx4g1vGgj0U8mOxeUxVy_Q9KWB-vI02odI4YQJSIKDzuGXjQ

- http://www.cyber-omelette.com/2017/09/automated-plant-watering.html

- https://www.youtube.com/watch?v=mQNJpWkdmbc&fbclid=IwAR2Lyb3M1nQq5Sxov5kAUKKsR2CUb9sm5UqoXmdDzFW9va9EiDJQGwjvSc0

- https://www.youtube.com/watch?v=9LxrX5Eeukg&fbclid=IwAR0FE4Wo4NlOYpyUm4fB3W9ZQpody4zdgLYMwzWjMiEy8pgzE_xLgZLLtiQ

- http://www.piddlerintheroot.com/soil-moisture-sensor/

## Requirements
Essensielt equipment:
- Raspberry Pi 3b +                              
- Jumper cables         
- Soil moisture sensor                            
- Valve/water pump                                
- Water container
- PVS Hose 
- Blynk Application

In addition to this equipment, we are going to use our own laptops (pc and mac) as well as our phones (IOS - iPhones)

## First meating with Blynk (Application)
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

## Developers
[Aas, Knut Andreas](https://github.com/nokaas) 

[Andreassen, Jarl](https://github.com/Genijarl)
 
[Mathisen, Vegard Saavesen](https://github.com/vegardmathisen)
  
[Pedersen, Eivind](https://github.com/eivped)
