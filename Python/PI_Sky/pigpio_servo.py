import pigpio
from time import sleep
pi = pigpio.pi()
pi.set_mode(17, pigpio.OUTPUT)
pi.set_PWM_frequency(17,50)
sleep(1)
print(pi.get_PWM_frequency(17))

while True:
    # pi.set_servo_pulsewidth(17,0)
    # sleep(1)
    pi.set_servo_pulsewidth(17,500)
    sleep(1)
    pi.set_servo_pulsewidth(17,1500)
    sleep(1)
    pi.set_servo_pulsewidth(17,2500)
    sleep(1)

    #0 = 500
    #180 = 2500
    #stay in this range