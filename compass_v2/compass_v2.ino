/*
 * rosserial Publisher Example
 * Prints "hello world!"
 */

#include <ros.h>
#include <std_msgs/String.h>
#include <std_msgs/Int32.h>
#include <std_msgs/Float32.h>

#include <Adafruit_LSM303DLH_Mag.h>
#include <Adafruit_Sensor.h>
#include <Wire.h>

ros::NodeHandle  nh;
Adafruit_LSM303DLH_Mag_Unified mag = Adafruit_LSM303DLH_Mag_Unified(12345);

std_msgs::String str_msg;
std_msgs::Float32 dir;
ros::Publisher compass("compass", &dir);


void setup()
{
  nh.initNode();
  nh.advertise(compass);
  mag.begin();  
}

void loop()
{
  sensors_event_t event;
  mag.getEvent(&event);

  float Pi = 3.141592;

  // Calculate the angle of the vector y,x
  float heading = (atan2(event.magnetic.y, event.magnetic.x) * 180) / Pi;

  // Normalize to 0-360
  if (heading < 0) {
    heading = 360 + heading;
  }
  
  dir.data = heading;
  compass.publish(&dir);
  nh.spinOnce();
  delay(1);
}
