#!/usr/bin/env python

#----------------------------------- RIGHT NEMA 34 FORWARD---------------------------------
import rospy
import RPi.GPIO as GPIO
import time
from std_msgs.msg import Int32


rospy.init_node('right_motor_forward')   # initialize ros node

pub  = rospy.Publisher('right_motor_rotate', Int32) # publisher






# setup

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)


#loop

def nema34():
    GPIO.output(22,False)
    GPIO.output(17, True)
    time.sleep(0.000010)
    GPIO.output(17, False)
    time.sleep(0.000010)

def motor():
    while not rospy.is_shutdown():
        
        nema34()
        
        


if __name__== "__main__":  # call the function
    rospy.init_node("right_motor_forward")
    motor() 