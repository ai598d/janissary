#!/usr/bin/env python

import rospy
import RPi.GPIO as GPIO
import time
from std_msgs.msg import Int32
from std_msgs.msg import String
from std_msgs.msg import Float32

# setup

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)


a = True;   # variable for while loop

def nemaR34():
    GPIO.output(22,True)
    GPIO.output(17, True)
    time.sleep(0.000010)
    GPIO.output(17, False)
    time.sleep(0.000010)
    

def callback(data):
    
    print("Too close %d" % data)
    
    
    



    
hellostr = "motor rotate"

def test_right_motor():
    
    pub = rospy.Publisher('Right_Motor',String, queue_size=10)
    
    rospy.Subscriber("measure_distance",Float32, callback) 
    
    rospy.init_node('talker', anonymous= True)
    
    
    rospy.spin()
    
    #while not rospy.is_shutdown():
        #nemaR34()
        #pub.Publish(hellostr)
   
    



    
    

'''        
def test_right_motor():
    rospy.init_node('test_right_motor', anonymous=True)

    pub  = rospy.Publisher('right_motor_rotate', Int32, queue_size=10)

    rate = rospy.Rate(2)
    
    

    #rospy.Subscriber("measure_distance",Int32, callback)
    
    rospy.spin()
'''
    

    

if __name__== '__main__':
    test_right_motor()







