import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO
import time

def mqtt_connect():
    def connect(client,userdata,rc,cc):
        client.subscribe('room/bed1')
        print('Successfully connected!')

    def receiveMessage(client,userdata,rc,cc):
        print('Start receiving message..')

    def on_message(client,userdata,msg):
        LedPin = 11
        mess = msg.payload
        print(mess.decode('utf-8'))
        if mess.decode('utf-8') == 'on':
            GPIO.output(LedPin, GPIO.HIGH)
        elif mess.decode('utf-8') == 'off':
            GPIO.output(LedPin, GPIO.LOW)
        elif mess.decode('utf-8') == 'increase_speed':
            time.sleep(1)
            GPIO.output(LedPin,GPIO.LOW)
            time.sleep(1)
            GPIO.output(LedPin,GPIO.HIGH)
            time.sleep(1)
            GPIO.output(LedPin,GPIO.LOW)
            time.sleep(1)
        client.disconnect()

    client = mqtt.Client()
    client.connect('192.168.1.116',1883)
    client.on_connect = connect
    client.on_subscribe = receiveMessage
    client.on_message = on_message

    client.loop_forever()