#!/usr/bin/python
import RPi.GPIO as GPIO
from time import sleep
from subprocess import call
import signal

PIN_MIN = 18
PIN_MAX = 16

VOL_LOW = 70
VOL_MEDIUM = 85
VOL_HIGH = 100


def cleanup(sig, frame):
    global loop
    loop = False
    GPIO.cleanup(PIN_MIN)
    GPIO.cleanup(PIN_MAX)

print("Starting " + __file__)

signal.signal(signal.SIGTERM, cleanup)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN_MIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(PIN_MAX, GPIO.IN, pull_up_down=GPIO.PUD_UP)

currentVolume = 0

loop = True
while loop:
    pinMinState = GPIO.input(PIN_MIN)
    pinMaxState = GPIO.input(PIN_MAX)

    newVolume = currentVolume

    if pinMinState == False and pinMaxState == True and currentVolume != VOL_LOW:
        newVolume = VOL_LOW
    elif pinMinState == True and pinMaxState == False and currentVolume != VOL_HIGH:
        newVolume = VOL_HIGH
    elif pinMinState == True and pinMaxState == True and currentVolume != VOL_MEDIUM:
        newVolume = VOL_MEDIUM

    if currentVolume != newVolume:
        call(["amixer", "set", "PCM", str(newVolume) + "%"])
        currentVolume = newVolume
    sleep(1)

print("Finishing " + __file__)
