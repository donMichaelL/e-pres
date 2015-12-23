import time
import timeit
import paho.mqtt.publish as publish

# selnei keraia 0
RFID_1 = ['0x30', '0x0', '0x3', '0x0', '0x12', '0x75', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x15', '0xdc', '0xad']
# selnei keraia 1
RFID_2 = ['0x40', '0x0', '0x3', '0x0', '0x12', '0x75', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x15', '0xdc', '0xad']
# selnei keraia 0
RFID_3 = ['0x50', '0x0', '0x3', '0x0', '0x12', '0x75', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x15', '0xdc', '0xad']
# selnei keraia 1
RFID_4 = ['0x60', '0x0', '0x3', '0x0', '0x12', '0x75', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x0', '0x15', '0xdc', '0xad']

TIMEOUT = 5
RFID = [RFID_1, RFID_2, RFID_3, RFID_4]
ANTENNA = [0, 1]
TOTAL_TAG_APPEARANCE_PER_CYCLE = 10


f = open('logs', 'w')

while 1:
    start = timeit.default_timer()
    f.write('------------------------------- STARTING A CYCLE---------------------- \n')
    for i in range(0,TOTAL_TAG_APPEARANCE_PER_CYCLE):
        for number in range(0, len(RFID)):
            tag = '-'.join(RFID[number])
            ant = str(ANTENNA[(number%2)])
            f.write('Tag: ' + tag + ' Antenna: ' + ant + '\n')
            publish.single(ant, tag, hostname="localhost", port=1883, client_id="new", keepalive=60, will=None, auth=None, tls=None)
    stop = timeit.default_timer()
    f.write('------------------------------- END CYCLE----------------------\n')
    f.write('Total Time: ' + str(stop-start) + 'sec'+ '\n')
    time.sleep(TIMEOUT)
