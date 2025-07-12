#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class S1_signal(Node):
    def __init__(self):
        super().__init__('s1_signal')
        self.publisher_ = self.create_publisher(String, '/s1', 10)
        self.timer = self.create_timer(10, self.timer_callback)
        self.i = 0

'''This function publishes red and green alternately based on the property value of i which increments after every published message.'''   
    def timer_callback(self):
        msg = String()
        if self.i%2 == 0:
            msg.data = "red"
        else:
            msg.data = "green"
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.i += 1

def main(args=None):
    rclpy.init(args=args)
    minimal_publisher = S1_signal()
    rclpy.spin(minimal_publisher)
    minimal_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
