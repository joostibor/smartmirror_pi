# needed modules will be imported
import RPi.GPIO as GPIO
import time
  
GPIO.setmode(GPIO.BCM)
  
# The input pin of the Sensor will be declared. Additional to that the pullup resistor will be activated.
LED_Rot = 17
LED_Gruen = 27
LED_Blau = 22
GPIO_PIN = 24
GPIO.setup(GPIO_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(LED_Rot, GPIO.OUT) 
GPIO.setup(LED_Gruen, GPIO.OUT)
GPIO.setup(LED_Blau, GPIO.OUT)
Freq = 100

ROT = GPIO.PWM(LED_Rot, Freq) 
GRUEN = GPIO.PWM(LED_Gruen, Freq)
BLAU = GPIO.PWM(LED_Blau, Freq)
ROT.start(0)  
GRUEN.start(0)
BLAU.start(0)

def LED_Farbe(Rot, Gruen,Blau, pause):
    ROT.ChangeDutyCycle(Rot)
    GRUEN.ChangeDutyCycle(Gruen)
    BLAU.ChangeDutyCycle(Blau)
    time.sleep(pause)
 
    ROT.ChangeDutyCycle(0)
    GRUEN.ChangeDutyCycle(0)
  
print "Sensor-Test [press ctrl+c to end it]"
  
# This output function will be started at signal detection
def outFunction(null):
        print("Signal detected")
        LED_Farbe(1,0,0,.02)
        import time
        import os
        n = 10
        while n>0: #enter your value here
            print(n)
            time.sleep(1) #to wait a second
            n = n-1
        os.system('sh jpgmake.sh')
  
# At the moment of detecting a Signal ( falling signal edge ) the output function will be activated.
GPIO.add_event_detect(GPIO_PIN, GPIO.FALLING, callback=outFunction, bouncetime=100) 
  
# main program loop
try:
        while True:
                time.sleep(1)
  
# Scavenging work after the end of the program
except KeyboardInterrupt:
        GPIO.cleanup()

import sys
sys.exit()
