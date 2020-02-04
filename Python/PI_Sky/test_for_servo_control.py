import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
p = GPIO.PWM(17, 50)
p.start(7.5)

while True:
    '''
    for dutycycle in range(0, 125, 1):
        p.ChangeDutyCycle(dutycycle/10)
        print(dutycycle)
        time.sleep(.1)
    '''
    p.ChangeDutyCycle(7.5)
    time.sleep(1)
    '''
    p.ChangeDutyCycle(2.5)
    time.sleep(1)
    p.ChangeDutyCycle(12.5)
    time.sleep(1)'''