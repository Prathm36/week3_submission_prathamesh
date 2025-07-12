#!/usr/bin/env python3
import time
import rclpy
from rclpy.action import ActionServer
from rclpy.node import Node

from kratos_prathamesh.action import Arm


class RotateActionServer(Node):

    def __init__(self):
        super().__init__('rotate_action_server')
        self._action_server = ActionServer(
            self,
            Arm,
            'rotate',
            self.execute_callback)

    def execute_callback(self, goal_handle):
        self.get_logger().info('Executing goal...')
        feedback_msg = Arm.Feedback()
        feedback_msg.curr_angle = 0

        angle = 0
        for i in range(goal_handle.request.target):
            angle = i
            feedback_msg.curr_angle = angle
            self.get_logger().info('Feedback: {0}'.format(feedback_msg.curr_angle))
            goal_handle.publish_feedback(feedback_msg)
            time.sleep(1)

        goal_handle.succeed()
        result = Arm.Result()
        result.succ = angle
        return result

        def feedback_callback(self, feedback_msg):
            feedback = feedback_msg.feedback
            self.get_logger().info('Received feedback: {0}'.format(feedback.curr_angle))


def main(args=None):
    rclpy.init(args=args)

    fibonacci_action_server = RotateActionServer()

    rclpy.spin(fibonacci_action_server)


if __name__ == '__main__':
    main()