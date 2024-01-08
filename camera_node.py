#!/usr/bin/env python3
import rclpy # Python Client Library for ROS 2
from rclpy.node import Node # Handles the creation of nodes
from sensor_msgs.msg import Image # Image is the message type
from cv_bridge import CvBridge # ROS2 package to convert between ROS and OpenCV Images
import cv2 # Python OpenCV library
import numpy as np
import math
from geometry_msgs.msg import Twist


class MinimalSubscriber(Node):
    def __init__(self):
        super().__init__('minimal_subscriber')
        self.window_name = "Sterownik"
        self.subscription = self.create_subscription(Image,'image_raw',self.listener_callback,10)
        self.subscription  # prevent unused variable warning
        self.point = None
        self.bridge = CvBridge()
        self.cmd_vel_publisher = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)

    def listener_callback(self, image_data):
        cv_image = np.zeros((512,700,3), np.uint8)
        if(self.point is not None):
            cv2.rectangle(cv_image,self.point,(self.point[0]+100,self.point[1]+100),(0,255,0),3)
            self.move_turtlesim(self.point, cv_image.shape[0])
        cv2.imshow(self.window_name, cv_image)
        cv2.waitKey(250)
        cv2.setMouseCallback(self.window_name, self.draw_rectangle)

    def draw_rectangle(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN: # check if mouse event is click
            self.point = (x,y)


    def move_turtlesim(self, point, image_height):
        twist_msg = Twist ()
        center_y = image_height // 2
        delta_y = center_y - point[1]
        twist_msg.linear.x = 1.0 if delta_y >= 0 else -1.0
        self.cmd_vel_publisher.publish(twist_msg)
        print(f"Moving:{twist_msg}")

def main(args=None):
    rclpy.init(args=args)
    minimal_subscriber = MinimalSubscriber()
    rclpy.spin(minimal_subscriber)
    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()