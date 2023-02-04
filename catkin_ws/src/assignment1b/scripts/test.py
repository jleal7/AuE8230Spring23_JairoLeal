#!/usr/bin/env python3

#I don't want to use a launch file since I am not comfortable with the XML code launch files use. So I am gonna use roslaunch's python API

import roslaunch
import rospy

#need to use try and except structure so I can use ^C in terminal to quit
if __name__ == '__main__':
	try:
		node1 = roslaunch.core.Node("turtlesim","turtlesim_node")
		launch = roslaunch.scriptapi.ROSLaunch()
		launch.start()
		process = launch.launch(node1)

		from geometry_msgs.msg import Twist #needed to send velocity messages to /turtle1/cmd_vel topic

		#to move the turtle in a circle we need to change it's linear and angular velocity. We do this by publishing to the /turtle1/cmd_vel topic. So need to create a publisher
		publisher = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
		#ROS makes us define a node. Even though I initialized a publisher, gotta make it a node
		rospy.init_node('turtlesim_controller',anonymous=True)
		vel = Twist() #move forward at a velocity of 1 and rotate at 0.5 rad/s
		rate = rospy.Rate(10)
		#tried without loop since we only need to send command once to go in a circle but would not work. Node would not even initialize without loop even though I ran init_node
		while not rospy.is_shutdown():
			vel.linear.x = 1
			vel.linear.y = 0
			vel.linear.z = 0
			vel.angular.x = 0
			vel.angular.y = 0
			vel.angular.z = 0.5
			publisher.publish(vel)
			rate.sleep()
		
	except rospy.ROSInterruptException:
		print("FAILED: inside exception loop")
		pass
