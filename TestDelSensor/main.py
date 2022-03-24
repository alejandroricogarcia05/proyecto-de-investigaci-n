#!/usr/bin/env pybricks-micropython
from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Color
from pybricks.robotics import DriveBase
from pybricks.hubs import EV3Brick

#from pybricks.media.ev3dev import Font
#from pybricks.tools import wait

ev3 = EV3Brick()


# Initialize the motors.
left_motor = Motor(Port.A)
right_motor = Motor(Port.B)

# Initialize the color sensor.
front_line_sensor = ColorSensor(Port.S1)

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

#Color identification loop.
while True:
    color_recognition = front_line_sensor.rgb()
    ev3.screen.print(color_recognition)

    #if front_line_sensor.color() == Color.BLACK:
      #  ev3.speaker.beep()
      #  robot.straight(-10)
      #  robot.turn

