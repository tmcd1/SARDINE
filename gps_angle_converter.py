#!/usr/bin/env python

# Get GPS coordinates from gps_coordinate_topic, then
# publish angles to angles topic

import rospy
from sardine.msg import *

def sub_callback(data):
    