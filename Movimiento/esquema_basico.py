#!/usr/bin/env pybricks-micropython

"""
Example LEGO® MINDSTORMS® EV3 Robot Educator Driving Base Program
-----------------------------------------------------------------

This program requires LEGO® EV3 MicroPython v2.0.
Download: https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3

Building instructions can be found at:
https://education.lego.com/en-us/support/mindstorms-ev3/building-instructions#robot
"""

from pybricks.ev3devices import *
from pybricks.parameters import *
from pybricks.robotics import *
from pybricks.tools import wait
from pybricks.hubs import EV3Brick

# Initialize the EV3 Brick.
ev3 = EV3Brick()

#PortsLocation
#Motors
left_motor = Motor(Port.A)
right_motor = Motor(Port.B)

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=152)
robot.settings(straight_speed = 200, straight_acceleration = 100, turn_rate=100)

fcolor_sensor_in1 = ColorSensor(Port.S1)

#MovementStraigt
robot.straight(1000)
robot.turn(360)
robot.turn(-360)
