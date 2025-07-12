#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class Hour_publisher(Node):
    def __init__(self):
        super().__init__('hour_publisher')
        self.subscription = self.create_subscription(Int32, '/minute', self.listener_callback, 10)
        self.publisher_ = self.create_publisher(Int32, '/hour', 10)
        self.i = 0

    def listener_callback(self, msg):
        hour_msg = Int32()
        hour_msg.data = self.i
'''This if statement in this function checks if the incoming min data is 60 because that is when the hour increments.'''
        if msg.data == 0:
            self.publisher_.publish(hour_msg)
            self.get_logger().info(f"Publishing: {hour_msg.data}")
            self.i+=1
        

def main(args=None):
    rclpy.init(args=args)
    minimal_subscriber = Hour_publisher()
    rclpy.spin(minimal_subscriber)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()