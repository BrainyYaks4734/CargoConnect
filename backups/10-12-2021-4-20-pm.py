from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

hub = PrimeHub()
motors = MotorPair('A', 'B')
motorLeft = Motor('A')
motorRight = Motor('B')
lift = Motor ('E')
twist = Motor ('F')
motors.set_default_speed(50)

# startfile libs/gyro.py
def gyroTurn(degrees, speed):
    if (degrees < 0):
        hub.motion_sensor.reset_yaw_angle()
        angle = hub.motion_sensor.get_yaw_angle()
        motors.start(-100,speed)
        while angle>degrees:
            angle = hub.motion_sensor.get_yaw_angle()
        motors.stop()
    else:
        hub.motion_sensor.reset_yaw_angle()
        angle = hub.motion_sensor.get_yaw_angle()
        motors.start(100, speed)
        while angle<degrees:
            angle = hub.motion_sensor.get_yaw_angle()
        motors.stop()
# endfile libs/gyro.py

# startfile libs/arm.py
#def gyroStraight(distance, speed=20):
#    ADJ_SPEED = 10
#    distance_traveled = 0
#    error = 0
#    hub.motion_sensor.reset_yaw_angle()
#    motorLeft.set_degrees_counted(0)
#    motorRight.set_degrees_counted(0)
#    motorLeft.start(speed)
#    motorRight.start(speed)
#
#    while distance_traveled <= distance:
#        distance_traveled = (motorLeft.get_degrees_counted() + motorRight.get_degrees_counted()) / 2
#        error = 0-hub.motion_sensor.get_yaw_angle()
#        if error > 0:
#            motorRight.start(speed)
#            motorLeft.start(speed+ADJ_SPEED)
#        elif error < 0:
#            motorLeft.start(speed)
#            motorRight.start(speed+ADJ_SPEED)
#        else:
#            motorLeft.start(speed)
#            motorRight.start(speed)
#        motorLeft.stop()
#        motorRight.stop()

# first mission: M02 Unused Capacity
motors.move(17) # Moving the robot into position to knock the cargo container into base
twist.run_for_degrees(360) # Move our top arm to the left in order to knock the cargo container over
# second mission: M05 Switch Engine
pass
# third mission: M03 Unload Cargo Plane
pass
