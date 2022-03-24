#!/usr/bin/env pybricks-micropython

"""
Example LEGO® MINDSTORMS® EV3 Robot Educator Driving Base Program
-----------------------------------------------------------------

This program requires LEGO® EV3 MicroPython v2.0.
Download: https://education.lego.com/en-us/support/mindstorms-ev3/python-for-ev3

Building instructions can be found at:
https://education.lego.com/en-us/support/mindstorms-ev3/building-instructions#robot
"""

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase

# Initialize the EV3 Brick.
ev3 = EV3Brick()

# Initialize the motors.
left_motor = Motor(Port.A)
right_motor = Motor(Port.B)

def MoveAndRotate(Distance,Degrees):
    robot.straight(Distance)

    ev3.speaker.beep()

    robot.straight(-Distance)
    ev3.speaker.beep()

    # Turn clockwise by 360 degrees and back again.
    robot.turn(Degrees)
    ev3.speaker.beep()

    robot.turn(-Degrees)
    ev3.speaker.beep()


def f(x):
    resultado = 2 * x - 4
    print(resultado)

f(2) # 0
f(3) # 2
f(4) # 4

def g(x):
    resultado = 2 / x

f(0) # Daría error de división de cero


# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

MoveAndRotate(1000,360)
MoveAndRotate(100,90)
MoveAndRotate(2000,45)


