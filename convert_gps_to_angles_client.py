#!/usr/bin/env python

import sys
import rospy
from sardine.srv import *
#from sardine.msg import *

def convert_gps_to_angles_client(lat, lon, alt):
    # Block until service "convert_gps_to_angles" is available
    rospy.wait_for_service('convert_gps_to_angles')
    try:
        # Create handle for calling conversion service
        convert_gps_to_angles = rospy.ServiceProxy('convert_gps_to_angles', ConvertGPSToAngles)

        # Generate a response object (end of ConvertGPSToAngles.srv file), return response
        response = convert_gps_to_angles(lat, lon, alt)
        return response
    except rospy.ServiceException, e:
        # Print out the error message, if there is one
        print "Service call failed: %s"%e

# Print out how to use the client
def usage():
    return "%s [latitude longitude altitude]"%sys.argv[0]

if __name__ == "__main__":
    if len(sys.argv) == 4:
        lat = float(sys.argv[1])
        lon = float(sys.argv[2])
        alt = float(sys.argv[3])
    else:
        print usage()
        sys.exit(1)
    print "Requesting lat: %s, lon: %s, alt: %s"%(lat, lon, alt)
    print "%s"%(convert_gps_to_angles_client(lat, lon, alt))
