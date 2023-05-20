#! /usr/bin/env python3
import rospy
from std_msgs.msg import String

def Listener():
    rospy.init_node("subscribe")
    rospy.Subscriber("topic1", String, callback)
    rospy.spin()

def callback(data):
    rospy.loginfo('Herad a message %s'% data.data)

if __name__ == '__main__':
    Listener()    