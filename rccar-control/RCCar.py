import RPi.GPIO as GPIO
import time

en_pin = 18

m2a_pin = 17
m2b_pin = 27

m1a_pin = 23
m1b_pin = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(en_pin, GPIO.OUT)

GPIO.setup(m1a_pin, GPIO.OUT)
GPIO.setup(m1b_pin, GPIO.OUT)
GPIO.setup(m2a_pin, GPIO.OUT)
GPIO.setup(m2b_pin, GPIO.OUT)

pwm = GPIO.PWM(en_pin, 500)
pwm.start(0)

speed=0
way=0

while True:
    cmd = raw_input("Command, f/b/l/r/s :")
    direction = cmd[0]
    if direction == "f":
        if speed<100:
            speed+=10
    elif direction == "b":
        if speed>-100:
            speed-=10
            
    elif direction == "r":
        if way<10:
            way+=10
    elif direction == "l":
        if way>-10:
            way-=10
    elif direction == "s":
        speed=0;
    else :
        print"error0"

        
    if speed>0:
        GPIO.output(m1a_pin, True)
        GPIO.output(m1b_pin, False)
    elif speed<0:
        GPIO.output(m1a_pin, False)
        GPIO.output(m1b_pin, True)
    elif speed==0:
        GPIO.output(m1a_pin, False)
        GPIO.output(m1b_pin, False)
    else :
        print"error1"

    if way>0:
        GPIO.output(m2a_pin, True)
        GPIO.output(m2b_pin, False)
    elif way<0:
        GPIO.output(m2a_pin, False)
        GPIO.output(m2b_pin, True)
    elif way==0:
        GPIO.output(m2a_pin, False)
        GPIO.output(m2b_pin, False)
    else :
        print"error2"


        

    print"speed=",speed
    print"way=",way
    pwm.ChangeDutyCycle(abs(speed))
    pwm.ChangeDutyCycle(abs(way))
    
        
        
    
