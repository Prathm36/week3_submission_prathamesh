#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class Min_publisher(Node):
    def __init__(self):
        super().__init__('min_publisher')
        self.subscription = self.create_subscription(Int32, '/second', self.listener_callback, 10)
        self.publisher_ = self.create_publisher(Int32, '/minute', 10)
        self.i = 0

    def listener_callback(self, msg):
        min_msg = Int32()
        min_msg.data = self.i
        if msg.data == 0:
            self.publisher_.publish(min_msg)
            self.get_logger().info(f"Publishing: {min_msg.data}")
            self.i+=1
        

def main(args=None):
    rclpy.init(args=args)
    minimal_subscriber = Min_publisher()
    rclpy.spin(minimal_subscriber)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()