import sqlite3

conn = sqlite3.connect('/home/pi/Documents/Projekt/mirrordb.sqlite')
cur = conn.cursor()

cur.execute('SELECT * FROM MirrorUsing')
records = cur.fetchall()
conn.close()

print('Starttime           | Stoptime            | Phototweets\n')
 
for row in records:
    print(str(row[0]) + ' | ' + str(row[1]) + ' | ' + str(row[2]) + '\n')
