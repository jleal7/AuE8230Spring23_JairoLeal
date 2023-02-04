#!/usr/bin/env python3


import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

if __name__ == '__main__':
	try:
		rospy.init_node('turtlebot_controller', anonymous=True)

        	# Publisher which will publish to the topic '/turtle1/cmd_vel'.
        	self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel',Twist, queue_size=10)

        	# A subscriber to the topic '/turtle1/pose'. self.update_pose is called
        	# when a message of type Pose is received.
        	self.pose_subscriber = rospy.Subscriber('/turtle1/pose',Pose, self.update_pose)

		
	except rospy.ROSInterruptException:
		pass
