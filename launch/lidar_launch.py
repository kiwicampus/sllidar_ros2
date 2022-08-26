#!/usr/bin/env python3
import os
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    # Lidar params
    # S1
    s1_params = {
        "serial_port": "/dev/ttyTHS0",
        "serial_baudrate": 256000,
        "frame_id": "laser_link",
        "inverted": False,
        "angle_compensate": True,
    }
    # S2
    s2_params = {
        "serial_port": "/dev/ttyTHS0",
        "serial_baudrate": 1000000,
        "frame_id": "laser_link",
        "inverted": False,
        "angle_compensate": True,
        "scan_mode": "DenseBoost",
    }

    lidar_params = (
        s2_params if bool(int(os.getenv(key="LIDAR_TYPE", default=1))) else s1_params
    )

    return LaunchDescription(
        [
            Node(
                package="sllidar_ros2",
                executable="sllidar_node",
                name="sllidar_node",
                parameters=[lidar_params],
                output="screen",
            ),
        ]
    )
