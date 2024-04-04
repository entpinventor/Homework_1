#! /usr/bin/env python
# -*- coding: utf-8 -*-

######
# subscribe type -->  list
# 
#
#
######

import rospy
from std_msgs import String

class Listner():
    def __init__(self):
        self.sub_list = rospy.Subscriber('/homework/message', String, self.callback , queue_size = 1)
    
    def callback(self, msg)
        
        if msg.data = '100'
            
        
        
    def main(self):
        rospy.spin()

if __name__ == "__main__":
    rospy.init_node("listner_py")
    
    
