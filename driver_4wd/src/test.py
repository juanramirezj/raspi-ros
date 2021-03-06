#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist
import serial
import time

ser = serial.Serial('/dev/ttyUSB0', 115200)
message =  "{},{},{},{}*".format(200,200,200,200)
print(message)
ser.write(message)

messagein = ser.readline()
print("> {}".format(messagein))


