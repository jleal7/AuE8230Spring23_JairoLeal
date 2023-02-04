Videos of each code runnign available in the videos folder.

<ins>circle.py</ins>:

What it is:
Code to make turtlebot move in a circle of any size.

Instruction to launch: 
1. Open a Terminal window and run roscore.
2. Ctrl+Shift+T and cd into catkin_ws/src/assignment1b/scripts.
3. run python3 circle.py
4. To end, close turtlesim window and ^C in terminal.

Trajectory:
![Alt text](screenshots/circle.png?raw=true "")


<ins>square_openloop</ins>:

What it is:
Given a linear speed of 0.2 units/s and angular speed of 0.2 rad/s, make the turtlebot move in a 2x2 unit circle.

Instruction to launch: 
1. Open a Terminal window and run roscore.
2. Ctrl+Shift+T and cd into catkin_ws/src/assignment1b/scripts.
3. run python3 square_openloop.py
4. To end, close turtlesim window and ^C in terminal.

Trajectory:
![Alt text](screenshots/square_openloop.png?raw=true "")


<ins>square_closedloop</ins>:

What it is:
Code that uses velocity proportional control to make the turtlebot trace a square.

Instruction to launch: 
1. Open a Terminal window and run roscore.
2. Ctrl+Shift+T and cd into catkin_ws/src/assignment1b/scripts.
3. run python3 square_closedloop.py
4. To end, close turtlesim window and ^C in terminal.

Trajectory:
![Alt text](screenshots/square_closedloop.png?raw=true "")

I think something is wrong with the steering_angle function. I thought it would be atan2 not letting it turn left but it makes the first 3 left turns just fine, so I don't know.
