#! /usr/bin/env python3
import rospy
from std_msgs.msg import String

def talker():
    rospy.init_node("publish") # node name
    pub = rospy.Publisher("topic1", String, queue_size=10) # topic name
    rate = rospy.Rate(1) # message every 1 minute 

    while not rospy.is_shutdown():
        hello_msg = "Hello World"
        rospy.loginfo(hello_msg)
        pub.publish(hello_msg)
        rate.sleep()

if __name__ == "__main__":
    try:
        talker()
    except  rospy.ROSInitException:
        pass