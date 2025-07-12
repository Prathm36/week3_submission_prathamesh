cmake_minimum_required(VERSION 3.8)
project(kratos_prathamesh)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(rosidl_default_generators REQUIRED)

#------------------------------------------------------------------
# Install Python modules
# ament_python_install_package(${PROJECT_NAME})

# Install Python executables in the ros2_ws/install/cpp_py_pkg/lib/cpp_py_pkg/ folder
install(PROGRAMS
q1/__init__.py
q1/q1_publisher_member_function.py
q1/q1_subscriber_member_function.py
q2/q2_s1publisher_node.py
q2/q2_s2subscriber_node.py
q4/clock_publisher.py
q4/hour_publisher.py
q4/min_publisher.py
q4/sec_publisher.py
bonus_q/bonus_actionclient.py
bonus_q/bonus_actionserver.py
DESTINATION lib/${PROJECT_NAME}
)
#------------------------------------------------------------------

#------------------------------------------------------------------
rosidl_generate_interfaces(${PROJECT_NAME}
  "q3/msgs/RoverStatus.msg"
  "action/Arm.action"
  DEPENDENCIES builtin_interfaces geometry_msgs # Add packages that above messages depend on, in this case geometry_msgs for Sphere.msg
)
#------------------------------------------------------------------

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
