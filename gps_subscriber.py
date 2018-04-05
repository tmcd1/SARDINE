#!/usr/bin/env python

# Subscribe to gps coordinates

import rospy
from sardine.msg import GpsCoord

def callback(data):
    rospy.loginfo("Lat: %s, Lon: %s, Alt: %s"%(data.lat, data.lon, data.alt))

def gps_subscriber():
    rospy.init_node('gps_subscriber', anonymous=True)
    rospy.Subscriber('gps_coordinate_topic', GpsCoord, callback)
    rospy.spin()

if __name__ == '__main__':
    gps_subscriber()
