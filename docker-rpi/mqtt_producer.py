import time
import paho.mqtt.publish as publish


print "That's one small step for man, one giant leap for mankind!!!!!"

# for i in range(0, 10):mport time
import random
import paho.mqtt.publish as publish


nodes = range(1, 11)
length = len(nodes)
propability = 1.25
weight = 10




def send_msg(tpc, number):
	publish.single(str(tpc), "%s This is a new Message" %(number), hostname="localhost",
    	port=1882, client_id="", keepalive=60, will=None, auth=None, tls=None)

while 1:
	max_idx = random.randint(0, length)
	idx = random.randint(0, length-max_idx)
	active_nodes = nodes[idx: idx+max_idx]
	for i in range(0,10):
		for node in nodes:
			if node in active_nodes:
				max_value = int(node*weight* propability)
				value = random.randint(0, max_value)
				print "Node %s Value %s MaxValue %s" %(node, value, max_value)
				send_msg(node, value)
			else:
				print "Node %s Value %s MaxValue %s" %(node, 0, 0)
				send_msg(node, 0)
		time.sleep(1)

