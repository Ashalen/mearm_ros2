import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription, ExecuteProcess
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import Command

def generate_launch_description():
    # Path to URDF (update if using xacro)
    urdf_path = os.path.join(
        get_package_share_directory('mearm_model'),
        'urdf',
        'robot.urdf'  # or 'mearm.xacro' if using xacro
    )
    
    # Load URDF (use Command if using xacro)
    robot_description = {'robot_description': open(urdf_path).read()}
    # If using xacro:
    # robot_description = {'robot_description': Command(['xacro ', urdf_path])}

    # Launch Ignition Gazebo
    ign_gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            [os.path.join(get_package_share_directory('ros_gz_sim'), 'launch', 'gz_sim.launch.py')]
        ),
        launch_arguments={
            'gz_args': '-r empty.sdf'  # or your custom world
        }.items()
    )

    # Spawn robot
    spawn_robot = Node(
        package='ros_gz_sim',
        executable='create',
        arguments=[
            '-name', 'mearm',
            '-topic', 'robot_description',
            '-x', '0.0',
            '-y', '0.0',
            '-z', '0.1',
        ],
        output='screen'
    )

    return LaunchDescription([
        ign_gazebo,
        spawn_robot
    ])