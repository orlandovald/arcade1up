#!/usr/bin/python
import RPi.GPIO as GPIO
from time import sleep
from subprocess import call
import signal
import ConfigParser

config = ConfigParser.ConfigParser()
config.read("/home/pi/arcade1up/config.ini")
pinLow = config.get('volume', 'pinLow')
pinHigh = config.get('volume', 'pinHigh')

volLow = config.get('volume', 'volLow')
volMid = config.get('volume', 'volMid')
volHigh = config.get('volume', 'volHigh')


def cleanup(sig, frame):
    global loop
    loop = False
    GPIO.cleanup(pinLow)
    GPIO.cleanup(pinHigh)

print("Starting " + __file__)

signal.signal(signal.SIGTERM, cleanup)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pinLow, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(pinHigh, GPIO.IN, pull_up_down=GPIO.PUD_UP)

currentVolume = 0

loop = True
while loop:
    pinMinState = GPIO.input(pinLow)
    pinMaxState = GPIO.input(pinHigh)

    newVolume = currentVolume

    if pinMinState == False and pinMaxState == True and currentVolume != volLow:
        newVolume = volLow
    elif pinMinState == True and pinMaxState == False and currentVolume != volHigh:
        newVolume = volHigh
    elif pinMinState == True and pinMaxState == True and currentVolume != volMid:
        newVolume = volMid

    if currentVolume != newVolume:
        call(["amixer", "set", "PCM", str(newVolume) + "%"])
        currentVolume = newVolume
    sleep(1)

print("Finishing " + __file__)
