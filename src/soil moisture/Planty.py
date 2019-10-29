# @author Knut Andreas Aas
# @version 0.1
# @last edited: 29.10.2019

import time
import RPi.GPIO as GPIO
from gpiozero import LED, Button

# Soil moisture sensor is connected to GPIO 14
soil = 14
# Pump is connected to GPIO 4
pump = LED(4)

# Setup the GPIO board
GPIO.setmode(GPIO.BCM)
GPIO.setup(soil, GPIO.IN)

# Starts the pump. The wiering is wrong so we had to invert this
pump.on()

# Main program
# Way of thinking: if water level is to low, start the water pump
def callback(soil):
    if GPIO.input(soil) == True:
        print("Water level to low")
        print("Watering...")
        time.sleep(2)
        pump.off()

# Way of thinking: if the water level is good, do not pump any more water         
    elif GPIO.input(soil) == False:
        print("Water detected")
        time.sleep(2)
        pump.on()
        
GPIO.add_event_detect(soil, GPIO.BOTH, bouncetime=300)
GPIO.add_event_callback(soil, callback)

#Cleans the GPIO after interrupt/reset
try:
    while True:
        pass
except:
    GPIO.cleanup()
