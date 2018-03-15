import RPi.GPIO as GPIO
import time
import mqtt_receiver

LedPin = 11
def setup():
    GPIO.setmode(GPIO.BOARD) #Numbers GPIOs by physical location
    GPIO.setup(LedPin,GPIO.OUT) #Set LedPin's mode is output

def destroy():
    GPIO.output(LedPin,GPIO.LOW)
    GPIO.cleanup()

setup()
try:
    while True:
        output = mqtt_receiver.mqtt_connect()
except KeyboardInterrupt:
    destroy()