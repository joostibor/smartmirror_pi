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

def LED_Farbe(Red, Green, Blue, pause):
    RED.ChangeDutyCycle(red)
    GREEN.ChangeDutyCycle(green)
    BLUE.ChangeDutyCycle(blue)
    time.sleep(pause)
 
    RED.ChangeDutyCycle(0)
    GREEN.ChangeDutyCycle(0)
    BLUE.ChangeDutyCycle(0)
  
print "Sensor-Test"
  
# Jelerzekeles
def outFunction(null):
        print("Signal detected")
        LED_Farbe(1,0,0,.02)
        import time
        import os
        n = 10
        while n>0:
		if n>3:
                	LED_Farbe(0,1,0,.500)
                	print n
                if n<4:
                	LED_Farbe(1,0,0,.500)
                	print n
            time.sleep(1) # Varakozasi ido
            n = n-1
        # foto+twitter poszt
        import tweepy  
        from twython import Twython
        from keys import (
         consumer_key,
         consumer_secret,
         access_token,
         access_token_secret
        )
        os.system('sh jpgmake.sh')
         
        # Kulcsok es tokenek hasznalata 
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)  
        auth.set_access_token(access_token, access_token_secret)  
           
        api = tweepy.API(auth)  
          
        # Foto feltoltese 
        photo_path = '/home/pi/Documents/Projekt/tmp.jpg'
	# random szoveg a twitter poszthoz
        messages =  [
                     "Hogy vagytok?",
                     "Milyen a napotok?",
                     "It's me Mario!!!",
                     "Randomly access league control.",
                     "Be nice person!",
                     "Arccal a pacalba!",
                    ]
        import random
        message = random.choice(messages)
        status = message
        api.update_with_media(photo_path, status=status)
        print "Posztolva"
	
	# tmp kep torlese
        os.system('sh jpgremove.sh')
        print "Temp kep torolve"
 
GPIO.add_event_detect(GPIO_PIN, GPIO.FALLING, callback=outFunction, bouncetime=100) 
  
# main program
try:
        while True:
                time.sleep(1)
  
# Program vegen tisztitas
except KeyboardInterrupt:
        GPIO.cleanup()

import sys
sys.exit()
