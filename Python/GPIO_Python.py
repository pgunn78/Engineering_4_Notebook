#Written by Paxton&Zane
import RPi.GPIO as GPIO
from time import sleep # all the librarys

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)# it likes to through warnings that mean jack didley
GPIO.setup(17,GPIO.OUT)
count = 0 

while count < 10: # self explanitory just writes on and off ten times 
    GPIO.output(17, GPIO.HIGH)
    sleep(1)
    GPIO.output(17, GPIO.LOW)
    sleep(1)
    count = count + 1
