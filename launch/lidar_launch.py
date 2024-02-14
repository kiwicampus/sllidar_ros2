#!/usr/bin/env python3
import os
from launch import LaunchDescription
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    # Lidar params
    # S1
    s1_params = {
        "serial_port": os.getenv(key="LIDAR_PORT", default="/dev/ttyTHS0"),
        "serial_baudrate": int(os.getenv(key="LIDAR_BAUD_RATE", default=256000)),
        "frame_id": "laser_link",
        "inverted": False,
        "angle_compensate": True,
    }
    # S2
    s2_params = {
        "serial_port": os.getenv(key="LIDAR_PORT", default="/dev/ttyUSB0"),
        "serial_baudrate": int(os.getenv(key="LIDAR_BAUD_RATE", default=1000000)),
        "frame_id": "laser_link",
        "inverted": False,
        "angle_compensate": True,
        "scan_mode": "DenseBoost",
    }

    lidar_params = (
        s2_params if bool(int(os.getenv(key="LIDAR_TYPE", default=1))) else s1_params
    )

    # Lidar 2D filter Params
    lidar2d_filter_params_file = None
    try:
        lidar2d_filter_params_file = os.path.join(
            get_package_share_directory("navigation"),
            "config",
            "lidar_filter_0deg.yaml",
        )
    except Exception as e:
        print(f"Collision monitor failed reading params file. Got: {e}")

    return LaunchDescription(
        [
            Node(
                package="sllidar_ros2",
                executable="sllidar_node",
                name="sllidar_node",
                parameters=[lidar_params],
                output="screen",
                respawn=True,
                respawn_delay=5.0,
            ),
            Node(
                executable="scan_to_scan_filter_chain",
                package="laser_filters",
                exec_name="scan_filter",
                parameters=[lidar2d_filter_params_file],
                output="screen",
                respawn=True,
                respawn_delay=5.0,
            ),
        ]
    )
