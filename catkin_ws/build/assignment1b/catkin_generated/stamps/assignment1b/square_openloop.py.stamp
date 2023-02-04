#!/usr/bin/env python3

import roslaunch
import rospy
from geometry_msgs.msg import Twist

def straight():

	counter = 0;
	
	#we know our loop runs 100 times every second, so to cover 2 units at 0.2 units/sec we need to go for 10 sec which is 1000 loops
	
	while not rospy.is_shutdown():
		if counter == 1000:
			break
		vel.linear.x = .2
		vel.linear.y = 0
		vel.linear.z = 0
		vel.angular.x = 0
		vel.angular.y = 0
		vel.angular.z = 0
		publisher.publish(vel)
		rate.sleep()
		counter += 1
		
def turn():
	#we want to make a 90 deg (pi/2 = 1.57079632679 rad) turn. We are gonna turn at 0.2 rad/s so we need to turn for 7.8539816 s. Our loops are 0.01s long so the best we can do is turn for 785 loops (truncate)
	
	counter = 0
	while not rospy.is_shutdown():
		if counter == 785:
			break
		vel.linear.x = 0
		vel.linear.y = 0
		vel.linear.z = 0
		vel.angular.x = 0
		vel.angular.y = 0
		vel.angular.z = 0.2
		publisher.publish(vel)
		rate.sleep()
		counter += 1

if __name__ == '__main__':
	try:
		node1 = roslaunch.core.Node("turtlesim","turtlesim_node")
		launch = roslaunch.scriptapi.ROSLaunch()
		launch.start()
		process = launch.launch(node1)

		publisher = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
		rospy.init_node('turtlesim_controller',anonymous=True)
		vel = Twist()
		rate = rospy.Rate(100)
		
		#keep making squares forever
		while True:
			straight()
			turn()
		
	except rospy.ROSInterruptException:
		pass
