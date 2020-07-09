#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import ConfigParser

print("Starting " + __file__)

config = ConfigParser.ConfigParser()
config.read("/home/pi/arcade1up/config/config.ini")
pinRelay = config.getint('power-relay', 'pinRelay')

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pinRelay, GPIO.OUT)
GPIO.output(pinRelay, GPIO.HIGH)

print("Finishing " + __file__)

