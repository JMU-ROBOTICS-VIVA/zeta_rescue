"""Launch the Zeta rescue system 

You can make any changes you want to this launch file, but it must
accept the time_limit command line argument.

"""

from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration


def generate_launch_description():

    return LaunchDescription([
        DeclareLaunchArgument('time_limit', default_value='360'),
        
        Node(
            package="zeta_rescue",
            executable="rescue_node",
            output="screen",
            parameters=[{'time_limit':  LaunchConfiguration('time_limit')}]
        )

    ])

if __name__ == "__main__":
    generate_launch_description()
