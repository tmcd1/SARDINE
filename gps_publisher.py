#!/usr/bin/env python

import rospy
from sardine.msg import GpsCoord

def gps_publisher():
    pub = rospy.Publisher('gps_coordinate_topic', GpsCoord, queue_size=10)
    rospy.init_node('gps_publisher', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown(): # is rospy still running?
        cord = GpsCoord()
        cord.lat = input("Latitude? ")
        cord.lon = input("Longitude? ")
        cord.alt = input("Altitude? ")
#        rospy.loginfo(cord) # Write to rosout, screen, and Node log file
        pub.publish(cord) # publish GPS Coordinate to 'gps_coordinate_topic'
    rate.sleep()

if __name__ == '__main__':
    try:
        gps_publisher()
    except rospy.ROSInterruptException:
        pass
