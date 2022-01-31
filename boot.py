# # Complete project details at https://RandomNerdTutorials.com
#
try:
   import usocket as socket
except:
   import socket
#
from machine import Pin
#import network
from machine import Pin
from neopixel import NeoPixel
from time import sleep
import urequests
import json
import esp
# esp.osdebug(None)
#
# import gc
# import config
# gc.collect()
#
# ssid = 'FRITZ!Box 7590 YX'
# password = '81356826004780197398'
#
# station = network.WLAN(network.STA_IF)
#
# station.active(True)
# station.connect(ssid, password)
#
# while station.isconnected() == False:
#   pass
#
# print('Connection successful')
# print(station.ifconfig())

# Complete project details at https://RandomNerdTutorials.com

import network

ssid = 'FRITZ!Box 7590 YX'
password = '81356826004780197398'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
    pass

print('Connection successful')
print(station.ifconfig())



