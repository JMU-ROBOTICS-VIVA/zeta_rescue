"""

"""

import os
from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node


def generate_launch_description():
    # We need to get the path to the .rviz file...
    this_prefix = get_package_share_directory('zeta_rescue')
    rviz_path = os.path.join(this_prefix, 'rviz', 'aruco.rviz')

    return LaunchDescription([
        Node(
            package="rviz2",
            node_executable="rviz2",
            node_name="rviz2",
            output="screen",
            arguments=['-d', rviz_path]
        ),
        Node(
            package="ros2_aruco",
            node_executable="aruco_node",
            output="screen",
            parameters=[{'camera_frame': 'camera_rgb_optical_frame'}] ,
            arguments=['-d', rviz_path]
        )

    ])
