#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist #pre-defined message type
from turtlesim.msg import Pose #pre-defined message type
from math import pow, atan2, sqrt
import roslaunch


class TurtleBot:
    def __init__(self):
        # Creates a node with name 'turtlebot_controller' and make sure it is a
        # unique node (using anonymous=True).
        rospy.init_node('turtlebot_controller', anonymous=True)

        # Publisher which will publish to the topic '/turtle1/cmd_vel'.
        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel',
                                                  Twist, queue_size=10)

        # A subscriber to the topic '/turtle1/pose'. self.update_pose is called
        # when a message of type Pose is received.
        self.pose_subscriber = rospy.Subscriber('/turtle1/pose',
                                                Pose, self.update_pose)

        self.pose = Pose()
        self.rate = rospy.Rate(10)

    def update_pose(self, data):
        """Callback function which is called when a new message of type Pose is
        received by the subscriber."""
        self.pose = data
        self.pose.x = round(self.pose.x, 4)
        self.pose.y = round(self.pose.y, 4)

    def euclidean_distance(self, goal_pose):
        """Euclidean distance between current pose and the goal."""
        return sqrt(pow((goal_pose.x - self.pose.x), 2) +
                    pow((goal_pose.y - self.pose.y), 2))

    def linear_vel(self, goal_pose, constant=1.5):
        """See video: https://www.youtube.com/watch?v=Qh15Nol5htM."""
        return constant * self.euclidean_distance(goal_pose)

    def steering_angle(self, goal_pose):
        """See video: https://www.youtube.com/watch?v=Qh15Nol5htM."""
        return atan2(goal_pose.y - self.pose.y, goal_pose.x - self.pose.x)
        #return atan((goal_pose.x - self.pose.x)/(goal_pose.y - self.pose.y))

    def angular_vel(self, goal_pose, constant=6):
        """See video: https://www.youtube.com/watch?v=Qh15Nol5htM."""
        return constant * (self.steering_angle(goal_pose) - self.pose.theta)
        
    #def setDesiredOrientation(self):
    	#self.pose = Pose() #get the current x,y,theta info
    	#print("Theta = %.2f" % self.pose.theta)
    	
    def move2goal(self, x_coord, y_coord):
        """Moves the turtle to the goal."""
        goal_pose = Pose() #initialize goal_pose to Pose mssg type

        goal_pose.x = x_coord
        goal_pose.y = y_coord

        # Please, insert a number slightly greater than 0 (e.g. 0.01).
        distance_tolerance = 0.1

        vel_msg = Twist() #initialize velocity message to Twist mssg type

        while self.euclidean_distance(goal_pose) > distance_tolerance:

            # Porportional controller.
            # https://en.wikipedia.org/wiki/Proportional_control

            # Linear velocity in the x-axis.
            vel_msg.linear.x = self.linear_vel(goal_pose)
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0

            # Angular velocity in the z-axis.
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = self.angular_vel(goal_pose)

            # Publishing our vel_msg
            self.velocity_publisher.publish(vel_msg)

            # Publish at the desired rate.
            self.rate.sleep()

        # Stopping our robot after the movement is over.
        vel_msg.linear.x = 0
        vel_msg.angular.z = 0
        self.velocity_publisher.publish(vel_msg)
        
        print("Reached goal: (%d,%d)"% (x_coord,y_coord))
        
        #self.setDesiredOrientation()
        
        return #exit function once we have reached coordinates so we can continue to next ones
        
        # If we press control + C, the node will stop.
        #rospy.spin()

if __name__ == '__main__':
    try:
    	#use roslaunch python api to launch turtlesim from python script
    	node1 = roslaunch.core.Node("turtlesim","turtlesim_node")
    	launch = roslaunch.scriptapi.ROSLaunch()
    	launch.start()
    	process = launch.launch(node1)
    	
    	x = TurtleBot() #creates a turtlebotcontroller node which publishes to /turtle1/cmd_vel and subscribes (reads from) to /turtle1/pose
    	
    	
    	x.move2goal(5,5) #runs our move2goal function defined above
    	x.move2goal(8,5)
    	x.move2goal(8,8)
    	x.move2goal(5,8)
    	x.move2goal(5,5)
     
    except rospy.ROSInterruptException: #if we close or do ^C to end script
        pass