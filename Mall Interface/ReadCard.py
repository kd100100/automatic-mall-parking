import RPi.GPIO as gpio
from mfrc522 import SimpleMFRC522
def readRFID():
    cardRead = SimpleMFRC522()

    print("Scanning...")
    print("to cancel press ctrl+c")
    try:
        id, text = cardRead.read()
        print("ID: %s\nText: %s" % (id,text))
        return text
    finally:
        gpio.cleanup()
