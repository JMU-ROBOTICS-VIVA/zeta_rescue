"""

"""

import os
from launch import LaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node
from launch.substitutions import LaunchConfiguration



def generate_launch_description():
    # We need to get the path to the .rviz file...
    this_prefix = get_package_share_directory('zeta_rescue')
    rviz_path = os.path.join(this_prefix, 'rviz', 'aruco_foxy.rviz')
    use_sim_time = LaunchConfiguration('use_sim_time', default='true')

    return LaunchDescription([
        Node(
            package="rviz2",
            executable="rviz2",
            name="rviz2",
            output="screen",
            arguments=['-d', rviz_path],
            parameters=[{'use_sim_time': use_sim_time}],
        ),
        Node(
            package="ros2_aruco",
            executable="aruco_node",
            output="screen",
            parameters=[{'camera_frame': 'camera_rgb_optical_frame'}] ,
            arguments=['-d', rviz_path]
        )

    ])
