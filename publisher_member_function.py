# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from datetime import datetime
import time

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        
        self.subscription = self.create_subscription(
            String,
            'clock/setalarm',
            self.listener_callback,
            10)
        self.subscription  # prevent unused variable warning
        
        
    def listener_callback(self, msg):
        #self.get_logger().info('ALARM is set at : "%s"' % msg.data)
        self.j = datetime.now()
        current_time = '%s:%s:%s %s:%s:%s' %(self.j.year,self.j.month, self.j.day,self.j.hour,self.j.minute,self.j.second)
        #print(current_time)
        
        if current_time < msg.data:
        	self.get_logger().info('The system has set the ALARM at : "%s"' % msg.data)
        
        
        
        if current_time == msg.data:
        	self.publisher_ = self.create_publisher(String, 'clock/alarm', 10)
        	timer_period = 1
        	msg = String()
        	msg.data = '%s:%s:%s %s:%s:%s' %(self.j.year,self.j.month, self.j.day,self.j.hour,self.j.minute,self.j.second)
        	self.publisher_.publish(msg)
        	self.get_logger().info('The alarm is off')    
        	

def main(args=None):
    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
