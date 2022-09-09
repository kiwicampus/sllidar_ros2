# SLAMTEC LIDAR ROS2 Package


ROS2 node for SLAMTEC LIDAR

Visit following Website for more details about SLAMTEC LIDAR:

SLAMTEC LIDAR roswiki: http://wiki.ros.org/sllidar， http://wiki.ros.org/rplidar

SLAMTEC LIDAR HomePage:   http://www.slamtec.com/en/Lidar

SLAMTEC LIDAR SDK: https://github.com/Slamtec/rplidar_sdk

SLAMTEC LIDAR Tutorial:  https://github.com/robopeak/rplidar_ros/wiki

---
```
File Tree
📦sllidar_ros2
 ┣ 📂launch
 ┃ ┣ 📜lidar_launch.py
 ┃ ┣ 📜sllidar_a3_launch.py
 ┃ ┣ 📜sllidar_launch.py
 ┃ ┣ 📜sllidar_s1_launch.py
 ┃ ┣ 📜sllidar_s1_tcp_launch.py
 ┃ ┣ 📜sllidar_s2_launch.py
 ┃ ┣ 📜sllidar_s2e_launch.py
 ┃ ┣ 📜sllidar_t1_launch.py
 ┃ ┣ 📜view_sllidar_a3_launch.py
 ┃ ┣ 📜view_sllidar_launch.py
 ┃ ┣ 📜view_sllidar_s1_launch.py
 ┃ ┣ 📜view_sllidar_s1_tcp_launch.py
 ┃ ┣ 📜view_sllidar_s2_launch.py
 ┃ ┣ 📜view_sllidar_s2e_launch.py
 ┃ ┗ 📜view_sllidar_t1_launch.py
 ┣ 📂rviz
 ┃ ┗ 📜sllidar_ros2.rviz
 ┣ 📂scripts
 ┃ ┣ 📜create_udev_rules.sh
 ┃ ┣ 📜delete_udev_rules.sh
 ┃ ┗ 📜rplidar.rules
 ┣ 📂sdk
 ┃ ┣ 📂include
 ┃ ┃ ┣ 📜rplidar.h
 ┃ ┃ ┣ 📜rplidar_cmd.h
 ┃ ┃ ┣ 📜rplidar_driver.h
 ┃ ┃ ┣ 📜rplidar_protocol.h
 ┃ ┃ ┣ 📜rptypes.h
 ┃ ┃ ┣ 📜sl_crc.h
 ┃ ┃ ┣ 📜sl_lidar.h
 ┃ ┃ ┣ 📜sl_lidar_cmd.h
 ┃ ┃ ┣ 📜sl_lidar_driver.h
 ┃ ┃ ┣ 📜sl_lidar_driver_impl.h
 ┃ ┃ ┣ 📜sl_lidar_protocol.h
 ┃ ┃ ┗ 📜sl_types.h
 ┃ ┣ 📂src
 ┃ ┃ ┣ 📂arch
 ┃ ┃ ┃ ┣ 📂linux
 ┃ ┃ ┃ ┃ ┣ 📜arch_linux.h
 ┃ ┃ ┃ ┃ ┣ 📜net_serial.cpp
 ┃ ┃ ┃ ┃ ┣ 📜net_serial.h
 ┃ ┃ ┃ ┃ ┣ 📜net_socket.cpp
 ┃ ┃ ┃ ┃ ┣ 📜thread.hpp
 ┃ ┃ ┃ ┃ ┣ 📜timer.cpp
 ┃ ┃ ┃ ┃ ┗ 📜timer.h
 ┃ ┃ ┃ ┣ 📂macOS
 ┃ ┃ ┃ ┃ ┣ 📜arch_macOS.h
 ┃ ┃ ┃ ┃ ┣ 📜net_serial.cpp
 ┃ ┃ ┃ ┃ ┣ 📜net_serial.h
 ┃ ┃ ┃ ┃ ┣ 📜net_socket.cpp
 ┃ ┃ ┃ ┃ ┣ 📜thread.hpp
 ┃ ┃ ┃ ┃ ┣ 📜timer.cpp
 ┃ ┃ ┃ ┃ ┗ 📜timer.h
 ┃ ┃ ┃ ┗ 📂win32
 ┃ ┃ ┃ ┃ ┣ 📜arch_win32.h
 ┃ ┃ ┃ ┃ ┣ 📜net_serial.cpp
 ┃ ┃ ┃ ┃ ┣ 📜net_serial.h
 ┃ ┃ ┃ ┃ ┣ 📜net_socket.cpp
 ┃ ┃ ┃ ┃ ┣ 📜timer.cpp
 ┃ ┃ ┃ ┃ ┣ 📜timer.h
 ┃ ┃ ┃ ┃ ┗ 📜winthread.hpp
 ┃ ┃ ┣ 📂hal
 ┃ ┃ ┃ ┣ 📜abs_rxtx.h
 ┃ ┃ ┃ ┣ 📜assert.h
 ┃ ┃ ┃ ┣ 📜byteops.h
 ┃ ┃ ┃ ┣ 📜event.h
 ┃ ┃ ┃ ┣ 📜locker.h
 ┃ ┃ ┃ ┣ 📜socket.h
 ┃ ┃ ┃ ┣ 📜thread.cpp
 ┃ ┃ ┃ ┣ 📜thread.h
 ┃ ┃ ┃ ┣ 📜types.h
 ┃ ┃ ┃ ┗ 📜util.h
 ┃ ┃ ┣ 📜rplidar_driver.cpp
 ┃ ┃ ┣ 📜rplidar_driver_TCP.h
 ┃ ┃ ┣ 📜rplidar_driver_impl.h
 ┃ ┃ ┣ 📜rplidar_driver_serial.h
 ┃ ┃ ┣ 📜sdkcommon.h
 ┃ ┃ ┣ 📜sl_crc.cpp
 ┃ ┃ ┣ 📜sl_lidar_driver.cpp
 ┃ ┃ ┣ 📜sl_serial_channel.cpp
 ┃ ┃ ┣ 📜sl_tcp_channel.cpp
 ┃ ┃ ┗ 📜sl_udp_channel.cpp
 ┃ ┣ 📜Makefile
 ┃ ┗ 📜README.txt
 ┣ 📂src
 ┃ ┣ 📜sllidar_client.cpp
 ┃ ┗ 📜sllidar_node.cpp
 ┣ 📜.git
 ┣ 📜CMakeLists.txt
 ┣ 📜LICENSE
 ┣ 📜README.md
 ┣ 📜package.xml
 ┣ 📜rplidar_A1.png
 ┗ 📜rplidar_A2.png
 ```
---


Supported SLAMTEC LIDAR
-------------------
| Lidar Model    | 
| ---------------------- | 
|RPLIDAR A1              | 
|RPLIDAR A2              | 
|RPLIDAR A3              | 
|RPLIDAR S1              |
|RPLIDAR S2              | 
|SLAMTEC LPX T1          | 


## How to [install ROS2](https://index.ros.org/doc/ros2/Installation)
[foxy](https://docs.ros.org/en/foxy/Installation.html),
[dashing](https://docs.ros.org/en/dashing/Installation.html),
[rolling](https://docs.ros.org/en/rolling/Installation.html)

## How to configuring your ROS 2 environment
[Configuring your ROS 2 environment](https://docs.ros.org/en/foxy/Tutorials/Configuring-ROS2-Environment.html)

## How to Create a ROS2 workspace
[Create a workspace](https://docs.ros.org/en/foxy/Tutorials/Workspace/Creating-A-Workspace.html)

## Compile & Install sllidar_ros2 package

1. Clone sllidar_ros2 package from github : 

   ```bash
   git clone https://github.com/Slamtec/sllidar_ros2.git
   ``` 

2. Build sllidar_ros2 package :

   ```bash
   cd <your_own_ros2_ws>
   colcon build --symlink-install
   ```
   if you find output like "colcon:command not found",you need separate [install colcon](https://docs.ros.org/en/foxy/Tutorials/Colcon-Tutorial.html#install-colcon) build tools. 

  
3. Package environment setup :
    ```bash
    source ./install/setup.bash
    ```

    Note: Add permanent workspace environment variables.
    It's convenientif the ROS2 environment variables are automatically added to your bash session every time a new shell is launched:
    ```bash
    $echo "source <your_own_ros2_ws>/install/setup.bash" >> ~/.bashrc
    $source ~/.bashrc
    ```

## Run sllidar_ros2
 

```bash
ros2 launch sllidar_ros2 lidar_launch.py
```

## sllidar frame
sllidar frame must be broadcasted according to picture shown in sllidar-frame.png


## Environment Variables
**LIDAR_TYPE** Set in 0 to use S1 model or 1 to use S2 model.