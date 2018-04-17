#!/usr/bin/env python

from sardine.srv import *
import rospy
import numpy as np
from std_msgs.msg import String

# Thanks to https://stackoverflow.com/a/1969274
def translate(value, leftMin, leftMax, rightMin, rightMax):
    #FIgure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin

    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)

    # Convert the 0-1 range into a value in the right range
    return rightMin + (valueScaled * rightSpan)

def convert_gps_to_angles(gps):
    lat = gps.lat
    lon = gps.lon
    alt = gps.alt
    #print "Lat: %s, Lon: %s, Alt: %s"%(gps.lat, gps.lon, gps.alt)
    # Calculate angles
    r = np.sqrt((lat **2) + (lon ** 2))
    phi = np.arctan(alt/r)
    theta = np.arctan(lat/lon)

    # Map the values for use with the stepper motors
    mapped_phi = translate(phi, 0, 6.28318, 0, 800)
    if mapped_phi < 0:
        mapped_phi = mapped_phi + 800
    mapped_theta = translate(theta, 0, 6.28318, 0, 16980)
    if mapped_theta < 0:
        mapped_theta = mapped_theta + 16980
    
    # Make the response to send to the client
    return ConvertGPSToAnglesResponse(mapped_phi, mapped_theta)

def convert_gps_to_angles_server():
    rospy.init_node('convert_gps_to_angles_server')
    s = rospy.Service('convert_gps_to_angles', ConvertGPSToAngles, convert_gps_to_angles)
    print "Ready to convert GPS to angles."
    rospy.spin()

if __name__ == "__main__":
    convert_gps_to_angles_server()
