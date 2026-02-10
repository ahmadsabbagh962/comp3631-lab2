from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        # Launch the numeric talker node
        Node(
            package='lab2',
            executable='numeric_talker',
            name='numeric_talker'
        ),
        # Launch the numeric listener node
        Node(
            package='lab2',
            executable='numeric_listener',
            name='numeric_listener'
        ),
    ])
