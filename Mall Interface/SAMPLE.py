import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

GPIO.setup(3,GPIO.OUT) #Selection Pin 4
GPIO.output(3,GPIO.LOW)
GPIO.setup(5,GPIO.OUT)
GPIO.output(5,GPIO.LOW)
