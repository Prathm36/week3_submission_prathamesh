#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class Sec_publisher(Node):
    def __init__(self):
        super().__init__('sec_publisher')
        self.publisher_ = self.create_publisher(Int32, '/second', 10)
        self.timer = self.create_timer(1, self.timer_callback)
        self.i = 0
    
    def timer_callback(self):
        msg = Int32()
        
        if self.i == 61:
            self.i = 0
        msg.data = self.i
        self.publisher_.publish(msg)
        self.get_logger().info(f"Publishing: {msg.data}")
        self.i += 1

def main(args=None):
    rclpy.init(args=args)
    minimal_publisher = Sec_publisher()
    rclpy.spin(minimal_publisher)
    minimal_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
