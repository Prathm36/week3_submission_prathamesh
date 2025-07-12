#!/usr/bin/env python3
'''Over here inorder to store the clock values I have used Int32 datatype also.'''
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32
from std_msgs.msg import String

class Clock_publisher(Node):
    def __init__(self):
        super().__init__('clock_publisher')

'''I have different variables to store the values of the incoming messages from the topics.'''
        self.sec = Int32()
        self.min = Int32()
        self.hour = Int32()
        self.sec = 0
        self.min = 0
        self.hour = 0

'''I have 3 different callback functions which run whenever its needed and the values on the clock change accordingly.'''
        self.subscription = self.create_subscription(Int32, '/second', self.sec_callback, 10)
        self.subscription = self.create_subscription(Int32, '/minute', self.min_callback, 10)
        self.subscription = self.create_subscription(Int32, '/hour', self.hour_callback, 10)
        self.publisher_ = self.create_publisher(String, '/clock', 10)

    def sec_callback(self, msg):
        self.sec = msg.data
        self.publish_final()
    def min_callback(self, msg):
        self.min = msg.data
        self.publish_final()
    def hour_callback(self, msg):
        self.hour = msg.data
        self.publish_final()
'''This is the final function that retrieves the data from the previous functions and displays the time accrodingly.'''
    def publish_final(self):
        final_msg = String()
        final_msg.data = f"{self.hour}:{self.min}:{self.sec}"
        self.publisher_.publish(final_msg)
        self.get_logger().info(f"Publishing: {final_msg.data}")
        

def main(args=None):
    rclpy.init(args=args)
    minimal_subscriber = Clock_publisher()
    rclpy.spin(minimal_subscriber)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()