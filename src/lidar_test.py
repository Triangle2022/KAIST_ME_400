#!/usr/bin/env python
import rospy
import cv2
import numpy as np
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan
import math

## image size setting
x_size = 720
y_size = 720 

standard_x = x_size/2
standard_y = y_size/2

## color configure
white = (255,255,255)
red = (0,0,255)

## other parameters
point_size = 2

black_img = np.zeros(shape=[720,720,3],dtype=np.uint8)

def cal_location(self,angle,range):
    

def draw_lidar_point(img,x,y):
    ## draw lidar point
    cv2.circle(img,(x+standard_x,-y+standard_y),point_size,(255,255,255),-1)

def draw_line(img,point1,point2):

    ## transform the point to the normal X_Y coordinate
    point1[0] = point1[0]+standard_x
    point1[1] = -point1[1]+standard_y
    point2[0] = point2[0]+standard_x
    point2[1] = -point2[1]+standard_y
    
    ## draw the line
    cv2.line(img,point1,point2,red,2)


def callback(data):
    angle =700
    range = data.ranges[angle]
    theta = angle*(math.pi/360)
    x = -(math.sin(theta) *range)
    y = math.cos(theta) *range
    print(x,y)

    cv2.imshow("black",black_img)

    #print(len(data.ranges))
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("scan", LaserScan, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
