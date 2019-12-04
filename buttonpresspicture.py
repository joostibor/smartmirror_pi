import RPi.GPIO as GPIO
import time
  
GPIO.setmode(GPIO.BCM)
  
# Pin deklaralas
LED_red = 17
LED_green = 27
LED_blue = 22
GPIO_PIN = 24
GPIO.setup(GPIO_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(LED_red, GPIO.OUT) 
GPIO.setup(LED_green, GPIO.OUT)
GPIO.setup(LED_blue, GPIO.OUT)
Freq = 100

RED = GPIO.PWM(LED_red, Freq) 
GREEN = GPIO.PWM(LED_green, Freq)
BLUE = GPIO.PWM(LED_blue, Freq)
RED.start(0)  
GREEN.start(0)
BLUE.start(0)

def LED_Color(Red, Green,Blue, pause):
    RED.ChangeDutyCycle(Red)
    GREEN.ChangeDutyCycle(Green)
    BLUE.ChangeDutyCycle(Blue)
    time.sleep(pause)
 
    RED.ChangeDutyCycle(0)
    GREEN.ChangeDutyCycle(0)
  
print "Sensor-Test"
  
# Jelerzekeles es kepkeszites
def outFunction(null):
        print("Signal detected")
        LED_Color(1,0,0,.02)
        import time
        import os
        n = 10
        while n>0:
            print(n)
            time.sleep(1) #1 sec varakozas
            n = n-1
        os.system('sh jpgmake.sh')
  
GPIO.add_event_detect(GPIO_PIN, GPIO.FALLING, callback=outFunction, bouncetime=100) 
  
# main program
try:
        while True:
                time.sleep(1)
  
# Program végén tisztítás
except KeyboardInterrupt:
        GPIO.cleanup()

import sys
sys.exit()
