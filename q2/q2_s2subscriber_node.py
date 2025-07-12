#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class S2_signal(Node):
    def __init__(self):
        super().__init__('s2_signal')
        self.subscription = self.create_subscription(String, '/s1', self.listener_callback, 10)
        self.publisher_ = self.create_publisher(String, '/s2', 10)

'''This function checks the published message on the topic /s1 and publishes red and green accordingly.'''
    def listener_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)
        if msg.data == "red":
            msg.data = "green"
        else:
            msg.data = "red"
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)

def main(args=None):
    rclpy.init(args=args)
    minimal_subscriber = S2_signal()
    rclpy.spin(minimal_subscriber)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()