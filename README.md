
# MeArm Model: ROS1 → ROS2 Migration

Purpose
A functional URDF model of the MeArm robotic arm for ROS2 Humble, with RViz visualization and joint control via joint_state_publisher_gui.

The main goal was to simulate the MeArm in Gazebo but due to the URDF not having correct or unified code for gazebo it did not work but you can still use this to create nodes and send it a microcontroller.

(I will try to fix the Gazebo issue in my spare time).

Key Changes Made:

Build System

- Replaced catkin with ament_cmake in:
  - package.xml (updated format, ROS2 dependencies)
  - CMakeLists.txt (simplified, removed ROS1-specific code)

Launch Files
- Converted display.launch (XML) → display.launch.py (Python):
  - Uses IfCondition/UnlessCondition for GUI toggle
  - Fixed frame: world or base_link (user-configurable)

URDF/Meshes
 - Kept original structure but verified:
   - All mesh paths use package://mearm_model/meshes/...

RViz Setup
- Requires:
    - RobotModel display (topic: /robot_description)
    - Fixed Frame: base_link (or world if defined in URDF)

Dependencies
- xml
- Rviz
- robot_state_publisher
- joint_state_publisher_gui
- ROS2 Humble

How to Use
## Installation

Clone to your work_space

```bash
git clone https://github.com/Ashalen/mearm_ros2.git
cd mearm_ros2
colcon build
ros2 launch mearm_model gazebo_launch.py
```
(note that this part of the code: "ros2 launch mearm_model gazebo_launch.py", will launch it in Rviz with its joint state publisher so no need to have a split terminal, it does not however spawn in gazebo this will be fixed in future work or if you would like ot contibute to this problem I would appreaciate it)



## Credit
Forked from https://github.com/kubasikora/mearm_model.git with modifications for ROS2 compatibility done by myself as ROS1 is reaching EOL.


## License
License: Retained original MIT License.

[MIT](https://choosealicense.com/licenses/mit/)

