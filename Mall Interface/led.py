def led_on(red,green,blue):
    # LED Interfacing

    # Raspberry Pi Setup
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)

    # RFID Pins - 1,9,19,21,22,23,24
    # POWER 3.3 - 1,17
    # POWER 5V= 2,4
    # GND- 6,9,14,20,25,30,34,39
    # 27,28 EXTENDER FOR EPROM
    # GPIO Left - (3,5,7,8,10),11,(12,13,15,16,17),18,26,29,(31,32,33,35,37),38,40

    # Red Color
    GPIO.setup(3,GPIO.OUT) #Input
    GPIO.setup(5,GPIO.OUT) #Selection Pin 1
    GPIO.setup(7,GPIO.OUT) #Selection Pin 2
    GPIO.setup(8,GPIO.OUT) #Selection Pin 3
    GPIO.setup(10,GPIO.OUT) #Selection Pin 4

    # Green Color
    GPIO.setup(12,GPIO.OUT) #Input
    GPIO.setup(13,GPIO.OUT) #Selection Pin 1
    GPIO.setup(15,GPIO.OUT) #Selection Pin 2
    GPIO.setup(16,GPIO.OUT) #Selection Pin 3
    GPIO.setup(18,GPIO.OUT) #Selection Pin 4

    # Blue Color
    GPIO.setup(31,GPIO.OUT) #Input
    GPIO.setup(32,GPIO.OUT) #Selection Pin 1
    GPIO.setup(33,GPIO.OUT) #Selection Pin 2
    GPIO.setup(35,GPIO.OUT) #Selection Pin 3
    GPIO.setup(37,GPIO.OUT) #Selection Pin 4

    GPIO.output(3,GPIO.LOW)
    GPIO.output(12,GPIO.LOW)
    GPIO.output(31,GPIO.LOW)

    # Red LED Demux
    if (red["wing"]=='A' and red["slot"]==1):
        GPIO.output(5,GPIO.LOW)
        GPIO.output(7,GPIO.LOW)
        GPIO.output(8,GPIO.LOW)
        GPIO.output(10,GPIO.HIGH)
    elif (red["wing"]=='A' and red["slot"]==2):
        GPIO.output(5,GPIO.LOW)
        GPIO.output(7,GPIO.LOW)
        GPIO.output(8,GPIO.HIGH)
        GPIO.output(10,GPIO.LOW)
    elif (red["wing"]=='A' and red["slot"]==3):
        GPIO.output(5,GPIO.LOW)
        GPIO.output(7,GPIO.LOW)
        GPIO.output(8,GPIO.HIGH)
        GPIO.output(10,GPIO.HIGH)
    elif (red["wing"]=='A' and red["slot"]==4):
        GPIO.output(5,GPIO.LOW)
        GPIO.output(7,GPIO.HIGH)
        GPIO.output(8,GPIO.LOW)
        GPIO.output(10,GPIO.LOW)
    elif (red["wing"]=='A' and red["slot"]==5):
        GPIO.output(5,GPIO.LOW)
        GPIO.output(7,GPIO.HIGH)
        GPIO.output(8,GPIO.LOW)
        GPIO.output(10,GPIO.HIGH)
    elif (red["wing"]=='A' and red["slot"]==6):
        GPIO.output(5,GPIO.LOW)
        GPIO.output(7,GPIO.HIGH)
        GPIO.output(8,GPIO.HIGH)
        GPIO.output(10,GPIO.LOW)
    elif (red["wing"]=='B' and red["slot"]==1):
        GPIO.output(5,GPIO.HIGH)
        GPIO.output(7,GPIO.LOW)
        GPIO.output(8,GPIO.HIGH)
        GPIO.output(10,GPIO.LOW)
    elif (red["wing"]=='B' and red["slot"]==2):
        GPIO.output(5,GPIO.HIGH)
        GPIO.output(7,GPIO.LOW)
        GPIO.output(8,GPIO.HIGH)
        GPIO.output(10,GPIO.HIGH)
    elif (red["wing"]=='B' and red["slot"]==3):
        GPIO.output(5,GPIO.HIGH)
        GPIO.output(7,GPIO.HIGH)
        GPIO.output(8,GPIO.LOW)
        GPIO.output(10,GPIO.LOW)
    elif (red["wing"]=='B' and red["slot"]==4):
        GPIO.output(5,GPIO.HIGH)
        GPIO.output(7,GPIO.HIGH)
        GPIO.output(8,GPIO.LOW)
        GPIO.output(10,GPIO.HIGH)
    elif (red["wing"]=='B' and red["slot"]==5):
        GPIO.output(5,GPIO.HIGH)
        GPIO.output(7,GPIO.HIGH)
        GPIO.output(8,GPIO.HIGH)
        GPIO.output(10,GPIO.LOW)
    elif (red["wing"]=='B' and red["slot"]==6):
        GPIO.output(5,GPIO.HIGH)
        GPIO.output(7,GPIO.HIGH)
        GPIO.output(8,GPIO.HIGH)
        GPIO.output(10,GPIO.HIGH)

    # Green LED Demux
    if (green["wing"]=='A' and green["slot"]==1):
        GPIO.output(13,GPIO.LOW)
        GPIO.output(15,GPIO.LOW)
        GPIO.output(16,GPIO.LOW)
        GPIO.output(18,GPIO.HIGH)
    elif (green["wing"]=='A' and green["slot"]==2):
        GPIO.output(13,GPIO.LOW)
        GPIO.output(15,GPIO.LOW)
        GPIO.output(16,GPIO.HIGH)
        GPIO.output(18,GPIO.LOW)
    elif (green["wing"]=='A' and green["slot"]==3):
        GPIO.output(13,GPIO.LOW)
        GPIO.output(15,GPIO.LOW)
        GPIO.output(16,GPIO.HIGH)
        GPIO.output(18,GPIO.HIGH)
    elif (green["wing"]=='A' and green["slot"]==4):
        GPIO.output(13,GPIO.LOW)
        GPIO.output(15,GPIO.HIGH)
        GPIO.output(16,GPIO.LOW)
        GPIO.output(18,GPIO.LOW)
    elif (green["wing"]=='A' and green["slot"]==5):
        GPIO.output(13,GPIO.LOW)
        GPIO.output(15,GPIO.HIGH)
        GPIO.output(16,GPIO.LOW)
        GPIO.output(18,GPIO.HIGH)
    elif (green["wing"]=='A' and green["slot"]==6):
        GPIO.output(13,GPIO.LOW)
        GPIO.output(15,GPIO.HIGH)
        GPIO.output(16,GPIO.HIGH)
        GPIO.output(18,GPIO.LOW)
    elif (green["wing"]=='B' and green["slot"]==1):
        GPIO.output(13,GPIO.HIGH)
        GPIO.output(15,GPIO.LOW)
        GPIO.output(16,GPIO.HIGH)
        GPIO.output(18,GPIO.LOW)
    elif (green["wing"]=='B' and green["slot"]==2):
        GPIO.output(13,GPIO.HIGH)
        GPIO.output(15,GPIO.LOW)
        GPIO.output(16,GPIO.HIGH)
        GPIO.output(18,GPIO.HIGH)
    elif (green["wing"]=='B' and green["slot"]==3):
        GPIO.output(13,GPIO.HIGH)
        GPIO.output(15,GPIO.HIGH)
        GPIO.output(16,GPIO.LOW)
        GPIO.output(18,GPIO.LOW)
    elif (green["wing"]=='B' and green["slot"]==4):
        GPIO.output(13,GPIO.HIGH)
        GPIO.output(15,GPIO.HIGH)
        GPIO.output(16,GPIO.LOW)
        GPIO.output(18,GPIO.HIGH)
    elif (green["wing"]=='B' and green["slot"]==5):
        GPIO.output(13,GPIO.HIGH)
        GPIO.output(15,GPIO.HIGH)
        GPIO.output(16,GPIO.HIGH)
        GPIO.output(18,GPIO.LOW)
    elif (green["wing"]=='B' and green["slot"]==6):
        GPIO.output(13,GPIO.HIGH)
        GPIO.output(15,GPIO.HIGH)
        GPIO.output(16,GPIO.HIGH)
        GPIO.output(18,GPIO.HIGH)

    # Blue LED Demux
    if (blue["wing"]=='A' and blue["slot"]==1):
        GPIO.output(32,GPIO.LOW)
        GPIO.output(33,GPIO.LOW)
        GPIO.output(35,GPIO.LOW)
        GPIO.output(37,GPIO.HIGH)
    elif (blue["wing"]=='A' and blue["slot"]==2):
        GPIO.output(32,GPIO.LOW)
        GPIO.output(33,GPIO.LOW)
        GPIO.output(35,GPIO.HIGH)
        GPIO.output(37,GPIO.LOW)
    elif (blue["wing"]=='A' and blue["slot"]==3):
        GPIO.output(32,GPIO.LOW)
        GPIO.output(33,GPIO.LOW)
        GPIO.output(35,GPIO.HIGH)
        GPIO.output(37,GPIO.HIGH)
    elif (blue["wing"]=='A' and blue["slot"]==4):
        GPIO.output(32,GPIO.LOW)
        GPIO.output(33,GPIO.HIGH)
        GPIO.output(35,GPIO.LOW)
        GPIO.output(37,GPIO.LOW)
    elif (blue["wing"]=='A' and blue["slot"]==5):
        GPIO.output(32,GPIO.LOW)
        GPIO.output(33,GPIO.HIGH)
        GPIO.output(35,GPIO.LOW)
        GPIO.output(37,GPIO.HIGH)
    elif (blue["wing"]=='A' and blue["slot"]==6):
        GPIO.output(32,GPIO.LOW)
        GPIO.output(33,GPIO.HIGH)
        GPIO.output(35,GPIO.HIGH)
        GPIO.output(37,GPIO.LOW)
    elif (blue["wing"]=='B' and blue["slot"]==1):
        GPIO.output(32,GPIO.HIGH)
        GPIO.output(33,GPIO.LOW)
        GPIO.output(35,GPIO.HIGH)
        GPIO.output(37,GPIO.LOW)
    elif (blue["wing"]=='B' and blue["slot"]==2):
        GPIO.output(32,GPIO.HIGH)
        GPIO.output(33,GPIO.LOW)
        GPIO.output(35,GPIO.HIGH)
        GPIO.output(37,GPIO.HIGH)
    elif (blue["wing"]=='B' and blue["slot"]==3):
        GPIO.output(32,GPIO.HIGH)
        GPIO.output(33,GPIO.HIGH)
        GPIO.output(35,GPIO.LOW)
        GPIO.output(37,GPIO.LOW)
    elif (blue["wing"]=='B' and blue["slot"]==4):
        GPIO.output(32,GPIO.HIGH)
        GPIO.output(33,GPIO.HIGH)
        GPIO.output(35,GPIO.LOW)
        GPIO.output(37,GPIO.HIGH)
    elif (blue["wing"]=='B' and blue["slot"]==5):
        GPIO.output(32,GPIO.HIGH)
        GPIO.output(33,GPIO.HIGH)
        GPIO.output(35,GPIO.HIGH)
        GPIO.output(37,GPIO.LOW)
    elif (blue["wing"]=='B' and blue["slot"]==6):
        GPIO.output(32,GPIO.HIGH)
        GPIO.output(33,GPIO.HIGH)
        GPIO.output(35,GPIO.HIGH)
        GPIO.output(37,GPIO.HIGH)
