#!/usr/bin/env python


#----------------------------------- LEFT NEMA 34 FORWARD(FOR ROTATE)---------------------------------

import rospy
import RPi.GPIO as GPIO
import time
from std_msgs.msg import Int32


rospy.init_node('left_motor_forward_rotate')    # initialize node

pub  = rospy.Publisher('left_motor_rotate', Int32)  # publisher







# setup

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)


#loop

def nema34():
    GPIO.output(23,False)
    GPIO.output(18, True)
    time.sleep(0.00010)
    GPIO.output(18, False)
    time.sleep(0.00010)
    
    
    
    
    
def motor():
    while not rospy.is_shutdown():
        
        nema34()
        
        
if __name__== "__main__":  # call the function
    rospy.init_node("left_motor_forward_rotate")
    motor()         
        
