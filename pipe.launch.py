from launch import LaunchDescription
from launch_ros.actions import Node

node_list = [
    Node(
        package='joint_pub',
        executable='sine_pub',
        name='sine_pub',
        output='screen'
    ),
]

for i in range(6):
    node_list.append(
        Node(
            package='ros_gz_bridge',
            executable='parameter_bridge',
            name='bridge_joint' + str(i),
            arguments=['/floating_manipulator/joint' + str(i) + '@std_msgs/msg/Float64@gz.msgs.Double'],
            output='screen'
        ),
    )

def generate_launch_description():
    return LaunchDescription(node_list)