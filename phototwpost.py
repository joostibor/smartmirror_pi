import tweepy  
  
from twython import Twython
from keys import (
 consumer_key,
 consumer_secret,
 access_token,
 access_token_secret
)
 
import os
os.system('sh jpgmake.sh')
 
# Kulcsok és tokenek használata 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)  
auth.set_access_token(access_token, access_token_secret)  
 
api = tweepy.API(auth)  
  
# Kep feltoltese twitterre 
photo_path = '/home/pi/Documents/Projekt/tmp.jpg' 
status = 'Im happy, its working!!!' 
api.update_with_media(photo_path, status=status)

#tmp kep torlese
os.system('sh jpgremove.sh')
