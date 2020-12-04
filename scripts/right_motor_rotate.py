#!/usr/bin/env python

#----------------------------------- RIGHT NEMA 34 BACK(FOR ROTATE)---------------------------------
import rospy
import RPi.GPIO as GPIO
import time
from std_msgs.msg import Int32


rospy.init_node('right_motor_back_rotate')   # initialize ros node

pub  = rospy.Publisher('right_motor_rotate', Int32) # publisher






# setup

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)


#loop

def nema34():
    GPIO.output(22,False)
    GPIO.output(17, True)
    time.sleep(0.00010)
    GPIO.output(17, False)
    time.sleep(0.00010)

def motor():
    while not rospy.is_shutdown():
        
        nema34()
        
        


if __name__== "__main__":  # call the function
    rospy.init_node("right_motor_back_rotate")
    motor() 


