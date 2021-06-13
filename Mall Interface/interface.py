def led(a):
    import time
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)

    GPIO.setup(3,GPIO.OUT) #Input
    GPIO.setup(12,GPIO.OUT) #Input
    GPIO.setup(5,GPIO.OUT) #Selection Pin 1
    GPIO.setup(7,GPIO.OUT) #Selection Pin 2
    GPIO.setup(8,GPIO.OUT) #Selection Pin 3
    GPIO.setup(10,GPIO.OUT) #Selection Pin 4
    if a==1:
        GPIO.output(3,GPIO.LOW)
        GPIO.output(12,GPIO.LOW)
        GPIO.output(5,GPIO.LOW)
        GPIO.output(7,GPIO.LOW)
        GPIO.output(8,GPIO.LOW)
        GPIO.output(10,GPIO.HIGH)
        #time.sleep(0.5)

    elif a==2:
        GPIO.output(3,GPIO.LOW)
        GPIO.output(12,GPIO.LOW)
        GPIO.output(5,GPIO.LOW)
        GPIO.output(7,GPIO.LOW)
        GPIO.output(8,GPIO.HIGH)
        GPIO.output(10,GPIO.LOW)
        #time.sleep(0.5)

    else:
        GPIO.output(3,GPIO.LOW)
        GPIO.output(12,GPIO.LOW)
        GPIO.output(5,GPIO.LOW)
        GPIO.output(7,GPIO.LOW)
        GPIO.output(8,GPIO.LOW)
        GPIO.output(10,GPIO.LOW)
        #time.sleep(0.5)
i=0
while(i!=-1):
    a=int(input())
    if a==[-1]:
        break
    led(a)

