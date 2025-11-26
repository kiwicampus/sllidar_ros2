################################################################################
# Set minimum required version of cmake, project name and compile options
################################################################################
cmake_minimum_required(VERSION 3.5)
project(sllidar_ros2)

if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

if(MSVC)
  add_compile_definitions(
    _USE_MATH_DEFINES
  )
endif()

set(SLLIDAR_SDK_PATH "./sdk/")

FILE(GLOB SLLIDAR_SDK_SRC 
  "${SLLIDAR_SDK_PATH}/src/arch/linux/*.cpp"
  "${SLLIDAR_SDK_PATH}/src/hal/*.cpp"
  "${SLLIDAR_SDK_PATH}/src/*.cpp"
  "${SLLIDAR_SDK_PATH}/src/dataunpacker/*.cpp"
  "${SLLIDAR_SDK_PATH}/src/dataunpacker/unpacker/*.cpp"
)

################################################################################
# Find ament packages and libraries for ament and system dependencies
################################################################################
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(sensor_msgs REQUIRED)
find_package(std_srvs REQUIRED)
find_package(rclcpp_components REQUIRED)

################################################################################
# Build
################################################################################
include_directories(
  ${SLLIDAR_SDK_PATH}/include
  ${SLLIDAR_SDK_PATH}/src
  ${Boost_INCLUDE_DIRS}
)

add_library(sllidar_node_component SHARED src/sllidar_node.cpp ${SLLIDAR_SDK_SRC})
ament_target_dependencies(sllidar_node_component
  rclcpp_components
  rclcpp
  std_srvs
  sensor_msgs
)

rclcpp_components_register_node(
  sllidar_node_component
  PLUGIN "sl::SLlidarNode"
  EXECUTABLE sllidar
)
ament_export_targets(export_sllidar_node_component)
install(TARGETS sllidar_node_component
  EXPORT export_sllidar_node_component
  ARCHIVE DESTINATION lib
  LIBRARY DESTINATION lib
  RUNTIME DESTINATION bin
)


add_executable(sllidar_client src/sllidar_client.cpp)
ament_target_dependencies(sllidar_client
  rclcpp
  std_srvs
  sensor_msgs
)
################################################################################
# Install
################################################################################
install(DIRECTORY launch rviz
  DESTINATION share/${PROJECT_NAME}
)

install(
  TARGETS sllidar_client
  RUNTIME DESTINATION lib/${PROJECT_NAME}
)

################################################################################
# Macro for ament package
################################################################################
ament_export_dependencies(rclcpp)
ament_export_dependencies(std_msgs)
ament_export_dependencies(sensor_msgs)
ament_export_include_directories(include)
ament_package()
