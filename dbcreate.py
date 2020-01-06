import sqlite3

connection = sqlite3.connect('/home/pi/Documents/Projekt/mirrordb.sqlite')

current = connection.cursor()
current.execute('CREATE TABLE MirrorUsing (starttime VARCHAR PRIMARY KEY, stoptime VARCHAR, phototweets INTEGER)')

connection.commit()
connection.close()
