from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='ros_gz_bridge',
            executable='parameter_bridge',
            name='bridge_joint0',
            arguments=['/sat_model/joint0@std_msgs/msg/Float64@gz.msgs.Double'],
            output='screen'
        ),
        Node(
            package='ros_gz_bridge',
            executable='parameter_bridge',
            name='bridge_joint1',
            arguments=['/sat_model/joint1@std_msgs/msg/Float64@gz.msgs.Double'],
            output='screen'
        ),
        Node(
            package='joint_pub',
            executable='sine_pub',
            name='sine_pub',
            output='screen'
        ),
    ])