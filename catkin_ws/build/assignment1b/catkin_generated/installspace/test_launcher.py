#!/usr/bin/env python3

import roslaunch
import rospy
	
if __name__ == '__main__':
	try:
		node1 = roslaunch.core.Node("turtlesim","turtlesim_node")
		
		launch = roslaunch.scriptapi.ROSLaunch()
		launch.start()
		
		process = launch.launch(node1)

		#2. run this python script (already running so can skip)

		#3. make turtlebot move in a circle
		from geometry_msgs.msg import Twist #needed to send velocity messages to /turtle1/cmd_vel topic
		
		print("Imported Twist")

		#to move the turtle in a circle we need to change it's linear and angular velocity. We do this by publishing to the /turtle1/cmd_vel topic. So need to create a publisher
		publisher = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
		print("created publisher")
		#ROS makes us define a node. Even though I initialized a publisher, gotta make it a node
		rospy.init_node('turtlesim_controller',anonymous=True)
		print("initialized node")
		
		vel = Twist() #move forward at a velocity of 1 and rotate at 0.5 rad/s
		print("created Twist object with desired linear and angular velocities")
		
		rate = rospy.Rate(10)
		print("set rate to 10 Hz")
		
		print("starting while loop")
		
		#tried without loop since we only need to send command once to go in a circle but would not work. Node would not even initialize without loop even though I ran init_node
		while not rospy.is_shutdown():
			vel.linear.x = 1
			vel.linear.y = 0
			vel.linear.z = 0
			vel.angular.x = 0
			vel.angular.y = 0
			vel.angular.z = 0.5
			publisher.publish(vel)
			print("Sent Twist command to turtlesim")
			rate.sleep()
	except rospy.ROSInterruptException:
		pass
