#!/usr/bin/python
import sys
import usb.core
import usb.util
import time
import commands
import response
# decimal vendor and product values
dev = usb.core.find(idVendor=0x24e9, idProduct=0x0861)
interface = 0
endpoint = dev[0][(0,0)][1]
cfg = dev.get_active_configuration()
intf = cfg[(0,0)]

ep = usb.util.find_descriptor(
    intf,
    # match the first OUT endpoint
    custom_match = \
    lambda e: \
        usb.util.endpoint_direction(e.bEndpointAddress) == \
        usb.util.ENDPOINT_OUT)

assert ep is not None

#------------------- Before Inventory ---------------------#
# cancel
ep.write(bytearray(commands.cancel_operation))
# get mac
for item in commands.read_mac:
    ep.write(bytearray(item))
    response.print_dictionary(response.read_antenna(dev))


# get firmware
ep.write(bytearray(commands.get_firmware))
response.print_dictionary(response.read_antenna(dev))


# get version
ep.write(bytearray(commands.get_version))
response.print_dictionary(response.read_antenna(dev))


# get update_number
ep.write(bytearray(commands.get_upd_num))
response.print_dictionary(response.read_antenna(dev))


# get update_number
ep.write(bytearray(commands.mac_registers))
response.print_dictionary(response.read_antenna(dev))

#------------------- Before Inventory ---------------------#

# set mode
ep.write(bytearray(commands.set_mode))
response.print_dictionary(response.read_antenna(dev))

# start inventory
ep.write(bytearray(commands.tag_inventory))
response.print_dictionary(response.read_antenna(dev))

response.print_dictionary(response.read_antenna(dev))

while 1:
    response.print_dictionary(response.read_antenna(dev))








# # release the device
# usb.util.release_interface(dev, interface)
# # reattach the device to the OS kernel
# dev.attach_kernel_driver(interface)
