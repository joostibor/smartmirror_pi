#!/bin/bash

DATE=$(date +"%Y-%m-%d_%H%M")

raspistill -t 3000  -rot 270 -st -br 50 -n -o /home/pi/Documents/Projekt/Pictures/$DATE.jpg
raspistill -t 3000  -rot 270 -st -br 50 -n -o /home/pi/Documents/Projekt/tmp.jpg
