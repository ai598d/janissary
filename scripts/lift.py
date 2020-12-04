#!/usr/bin/env python

#----------------------------------- NEMA 23 CCW(FOR ROTATE)---------------------------------
import rospy
import RPi.GPIO as GPIO
import time
from std_msgs.msg import Int32


rospy.init_node('lift_up')   # initialize ros node

pub  = rospy.Publisher('lift_motor_rotate_CCW', Int32) # publisher






# setup

GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)


#loop

def nema23():
    GPIO.output(6,False)
    GPIO.output(5, True)
    time.sleep(0.0010)
    GPIO.output(5, False)
    time.sleep(0.0010)

def motor():
    while not rospy.is_shutdown():
        
        nema23()
        
        


if __name__== "__main__":  # call the function
    rospy.init_node("lift_up")
    motor() 



