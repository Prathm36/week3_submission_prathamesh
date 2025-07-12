#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

'''I sourced a skeleton of the code from the documentation'''
'''This class created below is inherited from Node class which is imported above, it basically has all the properties of Node class and more.'''
class MinimalPublisher(Node):

    def __init__(self):
        '''Names the node minimal_publisher'''
        super().__init__('minimal_publisher')
        '''Names the topic /new publishing type of String'''
        self.publisher_ = self.create_publisher(String, '/new', 10)
        timer_period = (1.0 / 15)
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0
'''The callback function defined almost in all the codes for nodes and actions is basically a function that is executed periodically by ros2 acc to the parameters provided by user.'''
    def timer_callback(self):
        msg = String()
        msg.data = 'Hello World: %d' % self.i
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        '''This property value of i keeps incrememnting once a Hello world is published.'''
        self.i += 1

'''This part of code is staple in all the codes for the proper running of the package in the terminal.'''
def main(args=None):
    rclpy.init(args=args)
    minimal_publisher = MinimalPublisher()
    rclpy.spin(minimal_publisher)
    minimal_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
