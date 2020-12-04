#!/usr/bin/env python

# Libraries
import rospy
import RPi.GPIO as GPIO
import time
from std_msgs.msg import Int32
from std_msgs.msg import Float32


   

# GPIO mode
GPIO.setmode(GPIO.BCM)

# pins

GPIO_TRIGGER = 4
GPIO_ECHO    = 24

# GPIO in and out initialization

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

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



def distpub():
    
    pub = rospy.Publisher('distance',Float32,queue_size=10)
        # rospy.Publisher('Topic Name', data type, buffer size)
    
    rate = rospy.Rate(4)  # hz
    
    msg_to_publish = Float32()  # type of the published msg
    
    
    
    
    
    while not rospy.is_shutdown():
        
        msg_to_publish.data = distance()
        
        
        if msg_to_publish.data<10:
            pub.publish(msg_to_publish)
            rospy.loginfo(msg_to_publish)
            rate.sleep()
                
    
   
    
         
            
                         
            
            
if __name__== "__main__":  # call the function
    rospy.init_node("distance_measure")
    distpub()            
            
