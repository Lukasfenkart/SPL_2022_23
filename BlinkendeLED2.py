from tkinter import E
import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT)

while True:
    eingabe = input("e = LED ein, a = LED aus" )
    if eingabe == "e":
        GPIO.output(3, True)
    elif eingabe == "a":
        GPIO.output(3, False)