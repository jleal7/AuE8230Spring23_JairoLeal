#!/usr/bin/env python3

#basic script for creating a publisher node!

import rospy #always need
from std_msgs.msg import String

def talk_to_me():

	#create publisher node:
	publisher_node = rospy.Publisher('topic1',String,queue_size=10) #3 arguments: 1. topic we want to talk to. 2. type of message we are going to send. 3. Number of messages we can store before we start deleting.
	#now that we have created the publisher (talker) node, we need to initialize it using init_node() function
	
	#initialize node:
	rospy.init_node('publisher',anonymous=True)#2 arguments. 1. name of node (use name of variable for simplicity. 2. anonymous=True makes it so that if you have two instances of the same node it adds a number to the end. Ex: publisher1 and publisher2
	
	rate = rospy.Rate(10) #Creates a rate object! ODD. how often roscore needs to check this node in Hz. Sleeps between
	
	rospy.loginfo("Publisher node started and is publishing messages.")
	
	while not rospy.is_shutdown():#do this while the node is not shutdown (being accessed by roscore)
		msg = "Hello World! %s" % rospy.get_time()
		publisher_node.publish(msg) #[publisher node].publish(msg) sends msg to defined topic using publisher node
		rospy.loginfo(msg) #does 3 things. 1. Publishes the message that the node sent to topic to the Terminal. 2. Adds the message to the nodes log. 3. Message gets written to rosout which is a debugging tool.
		rate.sleep() #for remaining time of 10Hz loop sleep until we hit 10Hz again.COOL!

if __name__ == '__main__':
    try:
    	talk_to_me();
    except rospy.ROSInterruptException: #if we close or do ^C to end script
        pass
