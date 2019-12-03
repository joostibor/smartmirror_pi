#!/bin/bash

DATE=$(date +"%Y-%m-%d_%H%M")

raspistill -t 1 -o /home/pi/Documents/Projekt/Pictures/$DATE.jpg
