#!/usr/bin/env python3

#I don't want to use a launch file since I am not comfortable with the XML code launch files use. So I got two options, run roscore manually then use rosrun to call this script, or, use roslaunch to call this script and it will automatically run roscore if needed. Option 2 won't work since roslaunch only accepts launch files and I am trying to avoid them. So I am gonna have to run roscore in a terminal window, open another window then run "rosrun assignment1b test.py"

def run():
#need to use try and except structure so I can use ^C in terminal to quit

	import rospy
	import subprocess
	import os #so we can send terminal commands from inside the Python script

	#just need to copy in Python what gotogoal.launch file does:
	#1. open turtle sim
	os.system("rosrun turtlesim turtlesim_node") #execute this command in Terminal
	
	subprocess.call(['gnome-terminal'])
	print("started a new terminal")

	#2. run this python script (already running so can skip)

	#3. make turtlebot move in a circle
	from geometry_msgs.msg import Twist #needed to send velocity messages to /turtle1/cmd_vel topic
	import sys

	#to move the turtle in a circle we need to change it's linear and angular velocity. We do this by publishing to the /turtle1/cmd_vel topic. So need to create a publisher
	publisher = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
	#ROS makes us define a node. Even though I initialized a publisher, gotta make it a node
	rospy.init_node('turtlesim_controller',anonymous=True)
		
	vel = Twist([1,0,0],[0,0,.5]) #move forward at a velocity of 1 and rotate at 0.5 rad/s
		
	rate = rospy.Rate(10)
		
	#tried without loop since we only need to send command once to go in a circle but would not work. Node would not even initialize without loop even though I ran init_node
	while not rospy.is_shutdown():
		publisher.publish(vel)
		rospy.loginfo("Sent Twist command to turtlesim")
		rate.sleep()
if __name__ == '__main__':
	try:
		#tried putting all my code here instead of calling a function that runs my code but would not start transmitting until I git ^C (shut down turtlesim) so gonna try the normal way
		run();
	except rospy.ROSInterruptException:
		pass
