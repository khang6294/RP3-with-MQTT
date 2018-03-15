import paho.mqtt.client as mqtt

def mqtt_connect(input1):
    def connect(client,userdata,rc):
        print("Connection returned result: "+ str(rc))
        client.publish("room/bed1")
        print("Successfully connected")

    def sendMessage(client,userdata,msg):
        client.publish("room/bed1",input1)
        client.disconnect()

    def disconnect(client,userdata,rc):
        print("Successfully disconnected")

    client = mqtt.Client()
    client.on_connect = connect
    client.on_publish = sendMessage
    client.on_disconnect = disconnect
    client.connect("192.168.1.116", 1883)
    client.loop_forever()