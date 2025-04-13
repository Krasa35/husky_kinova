# kinova_gen3_control_interfaces
ROS2 interfaces package for PUTLunarTeam repository [kinova_gen3_control_cpp](https://github.com/ReQ1600/kinova_gen3_control_cpp)

Package created and tested on ROS2 Humble

### Dependencies
There are no packages needed to use this package only ROS2

### Installing
To install this package you need to clone it to the source of your workspace
~~~
  cd <your_workspace_name>/src
  git clone https://github.com/ReQ1600/kinova_gen3_control_interfaces.git
~~~

### Actions
#### MoveArmEffector.action interface
~~~
#Goal
geometry_msgs/Point goal_point
	float64 x
	float64 y
	float64 z
---
#Result
bool success
---
#Feedback
string error
geometry_msgs/Point current_effector_position
	float64 x
	float64 y
	float64 z
~~~
