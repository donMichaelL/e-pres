import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("airsoul")
	# Subscribing in on_connect() means that if we lose the connection and
	# reconnect then subscriptions will be renewed.
	

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
	print(str(msg.payload)+"-->topic: "+ msg.topic)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

try:
	client.connect("localhost", 1882, 60)
except:
	print 'No Connection'
	exit()

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()