#!/usr/bin/python
import RPi.GPIO as GPIO
import subprocess

THE_PIN = 5
ON_STATE = 0
OFF_STATE = 1

print("Starting " + __file__)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(THE_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

previousState = GPIO.input(THE_PIN)

loop = True
while loop:
    GPIO.wait_for_edge(THE_PIN, GPIO.BOTH)
    currentState = GPIO.input(THE_PIN)
    if previousState != currentState and currentState == OFF_STATE:
        subprocess.call(["bash", "/home/pi/arcade1up/scripts/shutdown.sh"], shell=True,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        loop = False
    else:
        previousState = currentState

GPIO.cleanup(THE_PIN)

print("Finishing " + __file__)
