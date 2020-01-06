import RPi.GPIO as GPIO
import time
import os
import sqlite3
import random
from time import localtime, strftime

  
GPIO.setmode(GPIO.BCM)
  
# Pin deklaralas
LED_red = 17
LED_green = 27
LED_blue = 22
BUTTON_PIN = 24
MOTION_PIN = 25
# Pin setup
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(LED_red, GPIO.OUT) 
GPIO.setup(LED_green, GPIO.OUT)
GPIO.setup(LED_blue, GPIO.OUT)
GPIO.setup(MOTION_PIN, GPIO.IN) 
Freq = 100

# LED szinek default
RED = GPIO.PWM(LED_red, Freq) 
GREEN = GPIO.PWM(LED_green, Freq)
BLUE = GPIO.PWM(LED_blue, Freq)
RED.start(0)  
GREEN.start(0)
BLUE.start(0)

#segedvaltozo
phototweets = 0

def LED_Farbe(Red, Green, Blue, pause):
    RED.ChangeDutyCycle(Red)
    GREEN.ChangeDutyCycle(Green)
    BLUE.ChangeDutyCycle(Blue)
    time.sleep(pause)
 
    RED.ChangeDutyCycle(0)
    GREEN.ChangeDutyCycle(0)
    BLUE.ChangeDutyCycle(0)

# Gombnyomas erzekelese
def outFunction(null):
    print("Signal detected")
    LED_Farbe(0,0,1,.500)
    n = 10
    while n>0:
        if n>3:
            LED_Farbe(0,1,0,.500)
            print n
        if n<4:
            LED_Farbe(1,0,0,.500)
            print n
        time.sleep(1)
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
    message = random.choice(messages)
    status = message
    api.update_with_media(photo_path, status=status)
    print "Posztolva"
    global phototweets
    phototweets = phototweets + 1
                    
    # tmp kep torlese
    os.system('sh jpgremove.sh')
    print "Temp kep torolve"
GPIO.add_event_detect(BUTTON_PIN, GPIO.FALLING, callback=outFunction, bouncetime=100)

run = False # fut-e mar a MagicMirror
    
try:
    time.sleep(1)
    while True:
        if GPIO.input(MOTION_PIN) and run==False:
            print("Motion detected")
            # startdate lekerdezes
            startdate = strftime("%Y-%m-%d %H:%M:%S", localtime())
            print startdate
            # Okostukor program inditas
            os.system('sh smstart.sh')
            
            run = True
            time.sleep(3)
            # timer a MagicMirror kikapcsolasahoz 1 perc tetlenseg utan OFF
            x=0
            while x<61:
                if x%5==0:
                    print(x)
                if GPIO.input(MOTION_PIN) and run==True:
                    x=0
                if x==60:
                    #tukor mukodes vege, adatbazisba iras
                    os.system('./probakill.sh')
                    stopdate = strftime("%Y-%m-%d %H:%M:%S", localtime())
                    conn = sqlite3.connect('/home/pi/Documents/Projekt/mirrordb.sqlite')
                    cur = conn.cursor()                
                    cur.execute('INSERT INTO MirrorUsing (starttime, stoptime, phototweets) VALUES (?, ?, ?)', (startdate, stopdate, phototweets))
                    conn.commit()  
                    conn.close()
                    time.sleep(1)
                    run = False
                    phototweets = 0
                time.sleep(1) 
                x=x+1
            time.sleep(30) #fel percig nem kapcsol vissza a tukor

# Program vegen tisztitas
except KeyboardInterrupt:
        GPIO.cleanup()

import sys
sys.exit()
