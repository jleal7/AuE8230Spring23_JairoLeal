#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import roslaunch

#save pose data from subscriber into pose and use as global var so I can access in any function
global pose #can't set on same line, have to do on next line!!!
pose = Pose(); #initialize pose to be of type Pose so if called to print b4 callback has set it, it won't error
#can't initialize to anything else like an int or else callback can't fill it in?

#just using callback to save pose data we got back from pose topic
def callback(data):
	pose = data #don't use data.data. Only need that we mssg you're recieving is String

if __name__ == '__main__':
	try:
		#launch turtlesim
		launch = roslaunch.scriptapi.ROSLaunch()
		launch.start()
		node1 = roslaunch.core.Node("turtlesim","turtlesim_node")
		process = launch.launch(node1)
		
		#create a node that is both a publisher and a listener!
		rospy.init_node('turtlebot_controller', anonymous=True)
		velocity_publisher = rospy.Publisher('/turtle1/cmd_vel',Twist, queue_size=10)
		pose_subscriber = rospy.Subscriber('/turtle1/pose',Pose,callback)
		#don't use rospy.spin() or rospy.sleep() let while not rospy.in_shutdown() and rate.sleep
		
		rate = rospy.Rate(10)
		
		while not rospy.is_shutdown():
			print(pose)
			rate.sleep()
		
		process.stop() #kill turtlesim_node
		print("Process stopped")
	except rospy.ROSInterruptException:
		pass
