#!/usr/bin/python
import RPi.GPIO as GPIO
from time import sleep
from subprocess import call
from subprocess import check_output
import signal
import ConfigParser

config = ConfigParser.ConfigParser()
config.read("/home/pi/arcade1up/config/config.ini")
pinLow = config.getint('volume', 'pinLow')
pinHigh = config.getint('volume', 'pinHigh')

volLow = config.getint('volume', 'volLow')
volMid = config.getint('volume', 'volMid')
volHigh = config.getint('volume', 'volHigh')


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

device = 'PCM'
controls = check_output(["amixer", "scontrols"])
if 'HDMI' in controls:
    device = 'HDMI'
elif 'Master' in controls:
    device = 'Master'

print("Using device = " + device)

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
        call(["amixer", "set", device, str(newVolume) + "%"])
        currentVolume = newVolume
    sleep(1)

print("Finishing " + __file__)
