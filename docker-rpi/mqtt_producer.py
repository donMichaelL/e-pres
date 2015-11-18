import time
import paho.mqtt.publish as publish


for i in range(0, 10):
        print i
        publish.single("airsoul", "%s This is a new Message" %(i), hostname="195.134.67.40",
        port=1883, client_id="", keepalive=60, will=None, auth=None, tls=None)
        time.sleep(1)


