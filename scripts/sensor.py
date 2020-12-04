#!/usr/bin/env python

# Libraries
import rospy
import RPi.GPIO as GPIO
import time
from std_msgs.msg import Int32

# GPIO mode
GPIO.setmode(GPIO.BCM)

# pins

GPIO_TRIGGER = 4
GPIO_ECHO    = 24

# GPIO in and out initialization

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)


rospy.init_node('sensor')

pub  = rospy.Publisher('measure_distance', Int32)

rate = rospy.Rate(2)

def distance ():
    # set trigger to HIGH
    
    GPIO.output(GPIO_TRIGGER, True)
    
    # set Trigger after 0.01ms to LOW
    
    time.sleep(.00001)
    GPIO.output(GPIO_TRIGGER, False)
    
    
    StartTime = time.time()
    StopTime  = time.time()
    
    # save start time
    
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
        
        
    # save time of arrival
    
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
        
        
    # time difference between start and arrival
    
    TimeElapsed = StopTime - StartTime
    
    # multiply with sonic speed
    # divide by 2 cuz of come and back
    
    distance = (TimeElapsed*34300)/2
    
    return distance


if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            print("measured distance = %.1f cm" % dist)
            time.sleep(1)
            
            # reset with CTRL+C
            
    except KeyboardInterrupt:
        print("MOTOR stopped by user")
        GPIO.cleanup()
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    